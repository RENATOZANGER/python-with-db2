import pyodbc


def connect():
    with pyodbc.connect('DSN=DB2DES;UID=db2inst1;PWD=123456;') as conn:
        print('Drivers:', pyodbc.drivers())
        print("Decimal separator", pyodbc.getDecimalSeparator())
        print("Available data sources"), pyodbc.dataSources()
        
        driver_name = conn.getinfo(pyodbc.SQL_DRIVER_NAME)
        print("Driver name:", driver_name)
        
        query = "SELECT * FROM TEST"
        
        with conn.cursor() as cursor:
            results = cursor.execute(query).fetchall()
            print(results)


connect()
