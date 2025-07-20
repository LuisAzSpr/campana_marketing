import boto3

BUCKET = "campana-bucket"
s3 = boto3.client('s3')

def descargar_archivo(archivo_s3, archivo_local):
    s3.download_file(BUCKET, archivo_s3, archivo_local)
