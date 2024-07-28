from sqlalchemy import create_engine

# Define the connection string
connection_string = (
    'mssql+pyodbc://aldo:Bpa12345@DESKTOP-5EI239P\MSSQLSERVER01/aldo'
    '?driver=ODBC+Driver+17+for+SQL+Server'
)

# Create the engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
