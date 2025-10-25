from pyspark.sql import SparkSession
import boto3
from dotenv import load_dotenv
import os
import tempfile

def inicia_minio_client():
    load_dotenv(dotenv_path=".env.txt")
    minio_client = boto3.client(
        "s3",
        endpoint_url=os.environ["MINIO_ENDPOINT"],
        aws_access_key_id=os.environ["MINIO_ACCESS_KEY"],
        aws_secret_access_key=os.environ["MINIO_SECRET_KEY"],
        region_name=os.environ["REGION_NAME"],
    )
    return minio_client

def spark_session():

    spark = (
        SparkSession.builder
        .appName("data_engineering_fundamentals")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider",
                "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    return spark

def retorna_dataframe(spark, bucket: str, key: str, tipo_arquivo: str):

    # Cria o cliente boto3 apontando para o MinIO
    s3 = inicia_minio_client()

    # Faz o download do objeto do MinIO
    obj = s3.get_object(Bucket=bucket, Key=key)
    conteudo = obj['Body'].read().decode('utf-8')

    # Salva temporariamente para Spark ler (Spark lê melhor do arquivo do que da string)
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write(conteudo)
        tmp_path = tmp.name

    tipo_arquivo = tipo_arquivo.lower()
    if tipo_arquivo == "csv":
        df = spark.read.option("header", "true").option("inferSchema", "true").csv(tmp_path)
    elif tipo_arquivo in ("json", "jsonl"):
        df = spark.read.option("multiline", "true").json(tmp_path)
    else:
        raise ValueError("Tipo de arquivo não suportado. Use 'csv' ou 'json'.")

    return df