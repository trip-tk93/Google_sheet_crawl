The Code helps to crawl through google sheets, it captures data from google sheets by replacing "edit#gid" part of url to 
"export?format=csv&gid". 
It then traverse through each url and stores each url data into "new_cols" dataframe. 
And concat this new fetched data with 'gsheet_data' dataframe. 
It also creates "url_column_map" dataframe which stores mapping of urls and their corresponding column names.

Then, using sqlalchemy "gsheet_data" and  "url_column_map" tables are created in SQL. 
CODE using either in-memory SQLite database or SQL Server is given.

"url_column_map" has mapping of urls and corresponding column names for that URL. This can help in identifying which columns of table "gsheet_data" comes from which url.

To change the initial URL in code, update "given_url" variable in the code.

To provides credentials for MS SQL, update "conn_str" in the code.



