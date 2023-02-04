#!/usr/bin/env python
import os
import csv
import json
import pymssql

# connect to the database
connection = pymssql.connect(server='MyDatabaseServer', user='myDatabaseUser',
                             password='my5tr0n6pw4', database='MyDatabaseName')

cursor = connection.cursor()

# read the CSV data file into the table
with open(f'{os.getcwd()}/data/example.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        cursor.execute(f"INSERT INTO dbo.example (name) values ('{row[0]}');")
        print(f"Inserted: {row[0]}")
        connection.commit()
connection.close()


# connect to the database
connection = pymssql.connect(server='MyDatabaseServer', user='myDatabaseUser',
                             password='my5tr0n6pw4', database='MyDatabaseName')

cursor = connection.cursor()

# output the table to a JSON file
with open(f'{os.getcwd()}/data/sample_output.json', 'w') as json_file:
    cursor.execute("select * from [dbo].[example];")
    rows = cursor.fetchall()
    rows = [{'id': row[0], 'name': row[1]} for row in rows]
    json.dump(rows, json_file, separators=(',', ':'))
