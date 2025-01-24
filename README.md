# Python with DB2

Este projeto apresenta exemplos de como conectar uma aplicacao Python(3.12) ao banco de dados DB2 utilizando diferentes bibliotecas. Ele inclui três tipos de arquivos de exemplo:

- **`python_with_jaydebeapi.py`**: Conexão com o DB2 usando `jaydebeapi`.
- **`python_with_pyodbc.py`**: Conexão com o DB2 usando `pyodbc`.
- **`main.py`**: Pesquisa pela string `'123456'` em todas as tabelas do DB2 e exibe os resultados no console.

---

## Pré-requisitos

### Ambiente com Podman

Este projeto utiliza o [Podman](https://podman.io/) para gerenciar a imagem do DB2. Siga os passos abaixo para configurar o ambiente:

1. **Baixar a imagem DB2:**
   ```bash
   podman pull ibmcom/db2
   ```

2. Executar o contêiner com o DB2:
    ```bash
   podman run -d \
    --name db2_container \
    --privileged \
    -e LICENSE=accept \
    -e DB2INST1_PASSWORD=123456 \
    -e DBNAME=DB2DES \
    -p 50000:50000 \
    ibmcom/db2
    ```

3. Verificar se o contêiner está em execução
   ```bash
   podman ps


### Configurar o DBeaver

Após configurar e executar o `Podman`, é possível conectar ao DB2 através do DBeaver:


1. Baixe e instale o DBeaver: [Download DBeaver](https://dbeaver.io/download/)

2. Configuração de conexão no DBeaver:
   - host:localhost
   - port:50000
   - Database: DB2DES
   - usuario:db2inst1
   - senha:123456


### Scripts SQL

#### O arquivo `script.sql` contém exemplos para:
- Criação de tabelas.
- Inserção de registros.
- Consultas com SELECT.
- Carregue e execute o script no DBeaver para testar as configurações.


### Dependências do Projeto

As bibliotecas necessárias para executar os scripts em Python estão listadas no arquivo requirements.txt. 

Instale-as com o comando:
```bash
  pip install -r requirements.txt
```

## Exemplos de Conexão com Python

1. Usando JayDeBeApi
- Observação: Não é necessário configurar ODBC para usar o jaydebeapi.
- Passo adicional: Baixe o driver JDBC db2jcc4.jar através do link: [IBM DB2 JDBC Driver Downloads](https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads)
- Nesse exemplo estou usando o [jdk-21](https://www.oracle.com/br/java/technologies/downloads/)

2. Usando PyODBC

- Instalar o Driver ODBC para o DB2

  - Baixe e instale o IBM Data Server Driver Package (DS Driver): [IBM Client and Driver Downloads](https://www.ibm.com/support/pages/download-initial-version-115-clients-and-drivers).
    - Determine a arquitetura do seu Python:

      ```bash
        python -c "import platform; print(platform.architecture()[0])"
        ```
    - Se o resultado for 64bit, instale o ODBC de 64 bits.
    - Caso contrário, use o ODBC de 32 bits.

### Configurar o DSN no ODBC:

No exemplo estou usando o `DSN=DB2DES`

1. Abra o "Administrador de Fonte de Dados ODBC".
2. Adicione uma nova fonte de dados e selecione o driver IBM DB2 ODBC DRIVER - IBMDBCLI1.
3. Configure os seguintes campos:
   - Data source name:DB2DES
   - DATABASE Alias: Clique em ADD e configure:
     - Data Source
        - user ID: db2inst1
        - Password: 123456
     - TCP/IP:
       - Database name:DB2DES
       - host name: localhost
       - Port number:50000

## Comandos Úteis do Podman

### Gerenciamento do Contêiner
- Baixar a imagem DB2:
    ```bash
    podman pull ibmcom/db2
    ```
  - Executar o contêiner:
  ```bash
      podman run -d \
    --name db2_container \
    --privileged \
    -e LICENSE=accept \
    -e DB2INST1_PASSWORD=123456 \
    -e DBNAME=DB2DES \
    -p 50000:50000 \
    ibmcom/db2
    ```


- Abrir uma sessao iterativa no container db2: 
    ```bash
    podman exec -it db2_container bash
    ```

## Comandos DB2
1. Mudar para o usuário padrão:
    ```bash
     su - db2inst1
    ```

2. Executar o cliente DB2:
    ```bash
    db2
    ```

3. Conectar no DB2DES: 
    ```bash
     connect to DB2DES
    ```

4. listar tabelas:
    ```bash
     list tables
    ```
