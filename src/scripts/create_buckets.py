import boto3
import os 
from botocore.client import ClientError
from src.configs.minio_config import get_minio_client

client = get_minio_client()

def create_buckets(): 
    lista_buckets = ["bronze", "silver", "gold"] 
    for bucket_name in lista_buckets: 
        try:
            client.head_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' já existente!")
        except ClientError:
            client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' criado!")
        

def upload_buckets(directory, bucket_name):
    for arquivo in os.listdir(directory):
        try:
            caminho = os.path.join(directory, arquivo)
            client.upload_file(caminho, bucket_name, arquivo)
            print(f"Arquivo '{arquivo}' importado!")
        except Exception as e:
            print(f"Arquivo '{arquivo}' com erro! {e}")

if __name__ == "__main__":

    directory = "data/bronze"
    bucket_name = "bronze"
    create_buckets()
    upload_buckets(directory, bucket_name)
