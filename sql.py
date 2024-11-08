import pandas as pd
import sqlite3

# Load your DataFrame (assuming you've already loaded it as 'df')
df = pd.read_csv(r"data/sales_sample.csv")

# Step 1: Remove rows with any null or missing values
df = df.dropna()

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Connect to SQLite database (this will create the db file if it doesn't exist)
conn = sqlite3.connect('sqlite.db')

# Step 4: Write the DataFrame to a new SQLite table
df.to_sql('sales_data', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

#########################################################################

# check if really create 
import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r"sqlite.db")

# Read data from a specific table (replace 'your_table_name' with the actual table name)
df = pd.read_sql("SELECT * FROM sales_data", conn)

# Close the connection
conn.close()

# Print column names
print(df.info())