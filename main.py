import pyodbc
import re

try:
    with pyodbc.connect('DSN=DB2DES;UID=db2inst1;PWD=123456;') as conn:
        with conn.cursor() as cursor:
            sql = "SELECT NAME FROM SYSIBM.SYSTABLES WHERE CREATOR = 'DB2INST1'"
            cursor.execute(sql)
            tables = [row.NAME for row in cursor.fetchall()]
            
            caracteres_especiais = re.compile(r'[^a-zA-Z0-9_]')
            contador = 0
            
            for table in tables:
                contador += 1
                if caracteres_especiais.search(table):
                    print(f"Igonorar a tabela: {table}")
                    continue
                print(f"Tabela {contador}: {table}")
                
                try:
                    sql = f"SELECT NAME,COLTYPE, LENGTH FROM SYSIBM.SYSCOLUMNS WHERE TBNAME = '{table}'"
                    cursor.execute(sql)
                    columns = cursor.fetchall()
                    
                    for column in columns:
                        sql = ''
                        column_name = column.NAME.strip()
                        column_type = column.COLTYPE.strip()
                        column_length = column.LENGTH
                        
                        # verifcar se o tipo da coluna CHAR, VARCHAR e se o tamanho e menor que 200
                        if column_type in ('CHAR', 'VARCHAR') and column_length < 200:
                            sql = f"SELECT COUNT(*) AS COUNT FROM {table} WHERE RTRIM({column_name}) like '123456'"
                        # verifcar se o tipo da coluna DECIMAL, INTEGER e se o tamanho e menor que 200
                        elif column_type in ('DECIMAL', 'INTEGER') and column_length < 200:
                            sql = f"SELECT COUNT(*) AS COUNT FROM {table} WHERE {column_name} = 123456"
                        
                        if sql:
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            if result and result.COUNT > 0:
                                print(f"valor encontrado na tabela {table}, coluna{column}")
                except Exception as ex:
                    print(f"erro ao processar a tabela: {table}, {ex} ")

except Exception as ex:
    print("Connection error: {}".format(ex))
