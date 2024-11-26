from google.cloud import storage

def cargar_objetos_gcs(bucket_name, file_name, object_name):
    # storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json('credenciales.json')
    
    bucket = storage_client.bucket(bucket_name)
    
    blob = bucket.blob(object_name)
    blob.upload_from_filename(file_name)
    
cargar_objetos_gcs('bucket-name','nombre_archivo_a_cargar','nombre_final')

# Si ejecutamos hasta acá me carga el archivo, no lo hago porque no tengo el gcp premium o la prueba gratuita, pero si funciona.

