# log_analysis
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
1. The 3 most popular articles of all time.
2. The most popular authors ranked by article views.
3. Dates on which more than 1% of requests led to errors.

## Install
- [Python2.7](https://www.python.org/download/releases/2.7/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [psycopg2 2.7 - Python-PostgreSQL Database Adapter](https://pypi.python.org/pypi/psycopg2)                        

## Set-up Instructions
1. Create the news database in PostgreSQL
- From the command line, launch the psql console by typing: `psql`
- Check to see if a _news_ database already exists by listing all databases with the command: `\l`
- If a _news_ database already exists, drop it with the command: `DROP DATABASE news;`
- Create the _news_ database with the command: `CREATE DATABASE news;`
- Exit the console by typing: `\q`
2. Download the schema and data for the _news_ database:
- [Click here to download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. Unzip the downloaded file. `unzip newsdata.zip`. 
- You should now have an sql script called _newsdata.sql_.
4. From the command line, navigate to the directory containing _newsdata.sql_.
5. Import the schema and data in _newsdata.sql_ to the _news_ database by typing: `psql -d news -f newsdata.sql`
## How to run
1. Once the _news_ database has been set up, from the command line navigate to the directory containing _log_analysis.py_.
2. Run the script by typing: `python log_analysis.py`

Refer to the file _log_analysis_output.txt_ for the expected output.

## License
This software is licensed under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/3.0/us/).
# serverloganalysis
