import boto3 
import duckdb

def get_minio_client():

      return boto3.client(
          's3',
          endpoint_url='http://minio:9000',
          aws_access_key_id='minioadmin',
          aws_secret_access_key='minioadmin'
      )


def get_duckdb_connection():

    con =duckdb.connect()
    con.sql("""
        INSTALL httpfs;
        LOAD httpfs;
        SET s3_endpoint='localhost:9000';
        SET s3_access_key_id='minioadmin';
        SET s3_secret_access_key='minioadmin';
        SET s3_use_ssl=false;
        SET s3_url_style='path';
    """)
    
    return con
