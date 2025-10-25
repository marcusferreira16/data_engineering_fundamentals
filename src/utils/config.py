import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(".env.txt")

# Configurações do MinIO
MINIO_CONFIG = {
    "endpoint_url": os.getenv("MINIO_ENDPOINT"),
    "access_key": os.getenv("MINIO_ACCESS_KEY"),
    "secret_key": os.getenv("MINIO_SECRET_KEY"),
    "region_name": os.getenv("REGION_NAME"),
    "bucket_name": os.getenv("MINIO_BUCKET")
}