import boto3 

def get_minio_client():
      """
      Retorna cliente conectado no MinIO.
      Centralizado: mudanças de credencial só aqui.
      """
      return boto3.client(
          's3',
          endpoint_url='http://minio:9000',
          aws_access_key_id='minioadmin',
          aws_secret_access_key='minioadmin'
      )


