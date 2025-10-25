from utils.functions import spark_session, retorna_dataframe

spark = spark_session()

pedidos = retorna_dataframe(
    spark, 
    bucket="data-engineering-projects", 
    key="fundamentals/raw/customers.csv", 
    tipo_arquivo="csv"
)

clientes = retorna_dataframe(
    spark, 
    bucket="data-engineering-projects", 
    key="fundamentals/raw/orders.csv", 
    tipo_arquivo="csv"
)

eventos = retorna_dataframe(
    spark, 
    bucket="data-engineering-projects", 
    key="fundamentals/raw/events.jsonl", 
    tipo_arquivo="jsonl"
)

pedidos.show(3, False)
clientes.show(3, False)
eventos.show(3, False)