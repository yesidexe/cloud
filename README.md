# Cloud

## Introducción
### Modelos de servicio en la nube
- **IaaS (Infrastructure as a Service)**: El proveedor te da servidores, redes, almacenamiento, etc. Tú gestionas el sistema operativo, las aplicaciones, los datos. (Por ejemplo: *Amazon EC2*, *Google Compute Engine*, *Microsoft Azure VM*).     
Ideal para: equipos técnicos que quieren control total del entorno.
- **PaaS (Platform as a Service)**: El proveedor te da la infraestructura + el sistema operativo + entornos de desarrollo. Tú solo te encargas del código y los datos. (Por ejemplo: *Google App Engine*, *Azure App Service*, *Heroku*).        
Ideal para: desarrolladores que quieren enfocarse en construir apps sin gestionar servidores.
- **SaaS (Software as a Service)**: El proveedor te da todo listo: infraestructura + plataforma + aplicación. Tú solo lo usas por medio de un navegador o app. (Por ejemplo: *Gmail*,*Google Docs*,*Zoom*)      
Ideal para: usuarios finales que solo necesitan usar el software.

## NOTAS PARA REVISAR
- Google storage con buckets, UNNEST, ARRAY y STRUCT
- Estudiar particiíón y clustering en sql para bigquery
- Automatización y Orquestación con Cloud Composer (Apache Airflow gestionado), conceptos básicos de Airflow: DAG (Grafo Acrílico Dirigido), Operadores y Tareas.
- Que es BigQueryOperator?
- Cloud functions, por ejemplo, crear una Cloud Function que se active cada vez que un nuevo archivo CSV se sube a un bucket de GCS y, automáticamente, lo cargue en una tabla de BigQuery. Este es un patrón de ingesta de datos muy común.


## Cuando sirva gemini
- Preguntarle por dataform
- Preguntar por Cloud schedule
- Pub/Sub
- Por trigger y sus usos en gcp
- Que es Cloud Logging
- Que es terraform y dbt