import pandas as pd
from sqlalchemy import create_engine

# Define the path to your CSV file
csv_file = r'D:\python\alex\covid_analysis\dataset\covid.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Define the database connection string
db_connection_string = 'sqlite:///covid.db'

# Create a database engine
engine = create_engine(db_connection_string)

# Define the table name for the SQL table
table_name = 'covid'

# Write the DataFrame to an SQL table
df.to_sql(table_name, engine, if_exists='replace', index=False)
