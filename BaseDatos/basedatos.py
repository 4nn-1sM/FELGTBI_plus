import psycopg2

# Configura los parámetros de la conexión
db_host="felgtbiplus.ctkyu2ec8xfz.eu-west-1.rds.amazonaws.com"  
db_name="FELGTBIplus"  
db_user="your_database_user"  
db_password="d3sAf10_7riPulAc10n3s!"  
db_port =5432


# Establecer la conexión
try:
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port,
        sslmode='disable'
    )
    print("Conexión exitosa a la base de datos PostgreSQL con SSL")

    # Crear un cursor para interactuar con la base de datos
    cursor = connection.cursor()

    # Ejecutar una consulta de ejemplo
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Versión de PostgreSQL:", record)

    # Cerrar cursor y conexión
    cursor.close()
    connection.close()

except psycopg2.OperationalError as e:
    print("Error de conexión:", e)
except Exception as error:
    print("Error desconocido:", error)
