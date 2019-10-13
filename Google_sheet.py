""" Code to crawl through google sheets, it captures data from google sheets by replacing "edit#gid" part of url to 
"export?format=csv&gid". It then traverse through each url and stores each url data into "new_cols" dataframe. 
And concat this new fetched data with 'gsheet_data' dataframe. 

It also creates "url_column_map" dataframe which stores mapping of urls and their corresponding column names.

Then, using sqlalchemy "gsheet_data" and  "url_column_map" tables are created in SQL. 
CODE using either in-memory SQLite database or SQL Server is geiven
""" 

import pandas as pd

# given_url contains the main URL where url for all sheets are given
given_url = "https://docs.google.com/spreadsheets/d/199haoLuNdcyaMdPcpVHWbcqPlLwYUA4XXHc0ExDS_9E/edit#gid=0"
updated_url = given_url.replace("edit#gid", "export?format=csv&gid")
url_df = pd.read_csv(updated_url)

gsheet_data = pd.DataFrame()
url_column_map = pd.DataFrame(columns = ['url', 'column'])


for myurl in url_df.Urls:
    new_url = myurl.replace("edit#gid", "export?format=csv&gid")
    new_data = pd.read_csv(new_url) 
    # adding column-url mapping
    col_data = {'url': myurl, 'column': new_data.columns.values.tolist()} 
    new_cols = pd.DataFrame(col_data, columns = ['url', 'column'])
    url_column_map = pd.concat([url_column_map, new_cols])
    # adding sheets data to dataframe  
    gsheet_data = pd.concat([gsheet_data, new_data], axis=1, sort=False)
    # print(url_column_map)

# using in-memory SQLite database

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
gsheet_data.to_sql("gsheet_data", engine)
url_column_map.to_sql("url_column_map", engine)


# #using SQL Server
# import sqlalchemy
# import pyodbc
# import urllib
# #engine = sqlalchemy.create_engine("mssql+pyodbc://product:product@<dsnname>")
# conn_str = "DRIVER=SQL Server Native Client 11.0;SERVER=<server>;DATABASE=<database>;UID=<user id>;PWD=<password>"
# params = urllib.parse.quote_plus(conn_str)
# engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params), echo=True, isolation_level = "AUTOCOMMIT")
# # write the DataFrame to a table in the sql database
# gsheet_data.to_sql("gsheet_data", engine)
# url_column_map.to_sql("url_column_map", engine)

