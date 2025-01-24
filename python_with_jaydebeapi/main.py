import os
import jaydebeapi


def configurar_ambiente(java_home, driver_path):
    """
    Configura as variáveis de ambiente necessárias para o driver JDBC.
    """
    os.environ['JAVA_HOME'] = java_home
    os.environ['PATH'] = f"{java_home}/bin;{os.environ.get('PATH')}"
    os.environ['CLASSPATH'] = driver_path


def executar_consulta(jdbc_url, username, password, driver_class, query):
    """
    Conecta ao banco de dados usando o driver JDBC e executa uma consulta SQL.
    """
    try:
        with jaydebeapi.connect(driver_class, jdbc_url, [username, password], driver_class) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None


def main():
    # Configurações do ambiente
    JAVA_HOME = r"C:\Program Files\Java\jdk-21\bin"
    DRIVER_PATH = "C:/Users/079568631/DRIVER_JDBC/db2jcc4.jar"
    
    configurar_ambiente(JAVA_HOME, DRIVER_PATH)
    
    # Configurações do banco de dados
    JDBC_URL = "jdbc:db2://localhost:50000/DB2DES"
    USERNAME = 'db2inst1'
    PASSWORD = '123456'
    DRIVER_CLASS = "com.ibm.db2.jcc.DB2Driver"
    QUERY = "SELECT * FROM TEST"
    
    resultados = executar_consulta(JDBC_URL, USERNAME, PASSWORD, DRIVER_CLASS, QUERY)
    
    if resultados:
        print("Resultados da consulta:")
        for linha in resultados:
            print(linha)
    else:
        print("Nenhum resultado encontrado ou erro na execução da consulta.")


if __name__ == "__main__":
    main()
