## Code Challenge Data Engineer

## Purpose
This coding test is designed to know your understanding about databases and data processing, together with your aptitude in a programming language of your choice.

There are two stages to this code test:

1.	Preparing code ahead of your interview.
2.	Pairing with us at the videocall, making additions to your code.

The pairing phase is to give us an indication of what it will be like to work together, and should be regarded as a collaborative effort.
Prerequisites:


- Knowledge of IDE, you could use whatever you feel comfortable, normally in our team we use VSCode, Pycharm or Azure Data Studio. 

- Knowledge of relational databases, including how to create tables, insert data, and query data. For the purpose of this test, we are using MSSQL.

Database Server: SQL-DE-TEST-D
        * Database Name: CodeChallenge
        * User Name: candidate
        * pass: c4nd1d4t3

- Knowledge of a programming language, including how to read and write files, process data, and access a MSSQL database. In our environment we use Python3, however, feel free to choose any of them. 

- Familiarity with Git for source control, branching strategy and a gitlab accounts which will be used for sharing your code.

We have included example data and programme code. The example schema creates a simple table, with example code in several common programming languages to load data from a CSV file and output to a JSON file.

## Background

We have provided an internal Gitlab repo containing:

1. An example_table.sql file containing a table schema used by the example scripts.

2. A "/data" folder containing four files:
    * example.csv: A tiny dataset, used by the example script.

    * places.csv: 113 rows, where each row has a city, county, and country name.

    * people.csv: 10,000 rows, where each row has a first name, last name, date of birth, and city of birth.

    * sample_output.json: Sample output file, to show what your output should look like.


## Problem

There are a sequence of steps that we would like you to complete. We hope this won't take more than a couple of hours of your time.

1.	Clone the git repo to your local computer and createa new branch with your name.

2.	Devise a database schema to hold the data in the people and places CSV files, and apply it to the MSSQL database. You may apply this schema via a script, via the MSSQL command-line client, or via a GUI client SSMS.

        * Database Server: SQL-DE-TEST-D
        * Database Name: CodeChallenge
        * User Name: candidate
        * pass: c4nd1d4t3

3.	Create a simple script for loading the CSV files, places.csv and people.csv, into the tables you have created in the database. Your data ingest process can be implemented in any way that you like. You may implement this via programme code in a language of your choice, or via the use of ETL tools.

4.	Create a second script for outputting a summary of content in the database. You may implement this using a programming language of your choice. The output must be in JSON format, and be written to a file in the data folder called data/summary_output.json. It should consist of a list of the countries, and a count of how many people were born in that country. We have supplied a sample output data/sample_output.json to compare your file against.

5.	Once data be ingested build follow SQL query’s: 
    1.	List of cities by country 
    2.	Count of persons by country birth 
    3.	Count of city by country 
    4.	Age by each person and order by lowest 
    6.	Share a link to your cloned github repo with us so we can review your code ahead of your interview.

We have provided an example schema and code that shows how to handle a simple data ingest and output.

Details of how to run and connect to the database are below, together with how to use the example schema and code.

6. Commit and push your local changes to remote repository

## Notes on completing these tasks

- There is no right way to do this. We are interested in the choices that you make, how you justify them, and your development process.

- Consider how normalized your schema should be, and whether or not you should be using foreign keys to join tables.

- Make sure that your code is executable, and if you are working in a scripting language, make sure that your script has an appropriate “hash-bang” line (as featured in our example scripts).

- Most of the example code uses ORM libraries to connect to the database. This is not essential for the purpose of this test: your code should connect to the database and your queries should be implemented in whatever way you are most comfortable with.

- Consider what kind of error handling and testing is appropriate.

- All data input, storage, and output should be in UTF-8. Expect multi-byte characters in the data.

- You may find it easier to work with a subset of the data when developing your ingest.

## Pairing activity at your Videocall 

We will spend 40 minutes at your interview pairing with you. This will include:

- Looking at your current code and solution.

- Modifying your output code, to add several new output files containing different subsets of the data. Be prepared to make different queries of the database, to manipulate data in your programme code, and to output data to disk as JSON and CSV files.

## Note 

By security reasons, our infraestructure use a proxy server, so if you choose Python as programming language you should use this way to install new packages: 

pip install -r ./requirements/requirements_local.txt \
                    --proxy http://proxy:8080 \
                    --trusted-host=pypi.org \ 
                    --trusted-host=files.pythonhosted.org 
                    --no-cache-dir --index-url https://artifactory.controlexpert.com/artifactory/api/pypi/pypi-all/simple
