# Google cloud plattform
## Consola
- Obviamente lo primero seria isntalar en CLI
- `gcloud init` es como un git init, inicializamos el gcp
- `gcloud config lsit` nos muestra la configuración pero no sé si del proyecto actual, o en general
- `gcloud projects list` vemos la lista de proyectos
- `gcloud config set project <project-id>` para cambiar de proyecto
- `gcloud auth list` para ver con que estamos logeados, la del "***" es con la que estamos trabajando
- `gcloud auth login` para cambiar de cuenta

## IAM
- En general es para gestionar los permisos y roles

## Google cloud storage
- ``Bucket``, unidad organizativa o contenedor de objetos.
- ``Objeto``, el dato no estructurado a subir.
### Crear un bucket desde la interfaz gráfica
- En la partde de bucket le damos a create, y en Name your bucket ponemos el nombre (Debe ser único, será algo asi como un dominio).
- La parte de región es donde se almacenará los datos, cualquier cosa de la [doc](https://cloud.google.com/storage/docs/locations?hl=es-419).
- Tipos de almacenamiento, , cualquier cosa ver la [doc](https://cloud.google.com/storage/docs/storage-classes?hl=es-419).
- Para escoger el control de acceso a objetos, es un tema mas complejo, lo normal seria quitar el checkbox que dice ***Enforce public access prevention on this bucket*** esto es para que no sea accesible al público, y abajo dice ***uniform*** y ***granular***, que es que los permisos del bucket se apliquen a sus objetos y que cada objeto tenga permiso diferente.
- Para cambiar permisos en uniforme vamos a la parte de permisos, porque si cambiamos el principal se cambia todo, y en granular tocaria archivo por archivo.

### GCS por consola
- `gcloud storage buckets create gs://<nombre-unico-del-bucket> --location=us-central1 --default-storage-class=NEARLINE` para crear el bucket usamos `gcloud`, y hacemos lo mismo, escogemos la región y el tipo de almacenamiento.
- `gcloud storage buckest list --format="value(name)"` para ver los buckets. Lo de los guiones es para ver únicamente el nombre de los buckets.
- `gcloud storage buckets delete gs://<nombre-del-bucket>`  para eliminar el bucket.
- `gcloud storage cp "imagen.png" gs://<nombre-del-bucket>` cargar información.
- `gcloud storage ls gs://<nombre-del-bucket>` para listar lo del bucket.
- `gcloud storage rm "gs://<nombre-del-bucket>/imagen.png"` eliminar el objeto.
- `gcloud storage cp gs://[bucket-name]/[file-name] [destination]` descarga un archivo desde el bucket a tu sistema local.
- ``gcloud storage mv [source] gs://[bucket-name]/[destination]`` Mueve o renombra un archivo dentro de GCS o desde el sistema local.
- ``gcloud storage buckets describe gs://[bucket-name]`` Muestra la configuración detallada de un bucket.`
- ``gcloud storage buckets update gs://[bucket-name] --location=[location] --retention-period=[time]`` Actualiza la configuración de un bucket, como la ubicación o el período de retención.
- ``gcloud storage buckets add-iam-policy-binding gs://[bucket-name] --member=[member] --role=[role]`` Añade una política IAM para un bucket (permiso específico para un usuario o grupo).
- ``gcloud storage buckets remove-iam-policy-binding gs://[bucket-name] --member=[member] --role=[role]`` Elimina una política IAM de un bucket.
- ``gcloud storage buckets get-iam-policy gs://[bucket-name]`` Obtiene la política de IAM actual para un bucket.
- ``gcloud storage buckets set-labels gs://[bucket-name] --labels=[KEY=VALUE,...]`` Asigna etiquetas a un bucket.
- ``gcloud storage notifications create --topic=[topic] --payload-format=json gs://[bucket-name]`` Crea una notificación de eventos para un bucket que envía mensajes a un tema de Pub/Sub.

### Encripción de datos (para el bucket)
Buscamos security, luego en el menú vamos a Key Management.
- Le podemos dar en ***create key ring***, la región debe ser la misma de donde están los datos, los nombres pues ya sabemos.
- Generar o importar la llave, normalmente se genera.
- Purpose and algorithm, el algoritmo normalmente usado es el simetrico que se usa para encriptar y decriptar.
- En Versions es para ir rotando la clave.
- Ahora al crear un bucket (con la misma región), en ***Data encryption*** damos en Cloud KMS, entramos manualmente la llave (la llave está creada donde la creamos, le damos en los puntos y ***copy resource name***), eso se pega ahí.
- Desde donde creamos la clave también se puede desactivar, en caso de que se requiera, pero al desactivar por ejemplo el archivo quedaria encriptado.

### Soft deleted policy (para el bucket)
En la parte de ***Chooose how to protect object data*** por defecto está habilitado el qeu si eliminamos algo se guarda por 7 dias por defecto, en caso de querer recuperarlo, la duración también puede ser modificada. Para recuperar los datos toca por consola.
- `gcloud storage ls gs://bucket --soft-deleted --recursive` nos sirve para listar los objetos eliminados
- `gcloud storage restore gs://bucket/archivo#generation_number` es para recuperar el archivo, la ruta no hay que ponerla como tal, al listar aparecerá y se puede copiar y pegar para ahorrarnos tiempo.

### Object versioning
Dentro del bucket no se sobreescribe archivos asi tengan el mismo nombre, crea un versionamineto. Esto también se encuentra en ***Data protection***, solo activamos el ***Object versioning***, se puede poner un máximo, por ejemplo 3 versiones, y en cuantos días expira. No hay que abusar de esta opción porque come almacenamiento. Cualquier cosa la [documentación](https://cloud.google.com/storage/docs/using-versioned-objects?hl=es-419).
- `gcloud storage ls --all-versions gs://bucket` en la consola de google puede ejecutarse este código, es para ver las versiones de los archivos del bucket.
- `gcloud storage cat gs://bucket/documento#numero` para ver el contenido, es mejor copiar lo que sale al listar en el código anterior, en lugar de escribir todo.
- `gcloud storage cp gs://bucket/version_a_restaurar#numero gs://bucket/nuevo_nombre_del_archivo_restaurado` copiamos el archivo que salió en el listado, el que queremos restaurar, lo recomendable seria copiarlo con otro nombre.

### Object retention policy
Al crear el bucket también se encuentra en ***Data protection***, donde dice ***Retention(For compliance)***, esto me garantiza que el objeto no sea eliminado o modificado donde cierto tiempo. Esto se puede hacer a nivel de bucket, o por objeto. Al activar se puede elegir el tiempo de retención.

## OLTP (Online Transaction Processing) vs OLAP (Online analytical processing)
- OLTP, Se enfoca en la gestión de transacciones operativas en tiempo real. Es el sistema que alimenta las aplicaciones del día a día, como los sistemas bancarios, los puntos de venta en tiendas, etc. Sus caracteristicas principales son:
    - ***Alta concurrencia:*** puede manejar muchos usuarios simultaneamente, por ejemplo, compras o transacciones bancarias.
    - ***Operaciones rápidas y pequeñas:*** Insert, delete y update, por ejemplo, agregar productos, transferir dinero.
    - ***Datos normalizados:*** Evita duplicidad y mantiene consistencia, por ejemplo, tablas separadas para clientes, productos y órdenes.
    - ***Consultas simples y rápidas:*** buscar clientes o productos por ejemplo.
    - ***Orientado a escritura:*** su principal objetivo es registrar transacciones en tiempo real.
- OLAP, Diseñado para el análisis y la generación de reportes. Se utiliza para comprender tendencias y patrones a gran escala. Sus caracteristicas principales son:
    - ***Optimizado para lectura y análisis:*** se priorizan consultas grandes y complejas, como analizar ventas anuales por región o patrones de compra.
    - ***Datos no normalizados:*** utiliza esquemas como el modelo estrella o copo de nieve para agilizar consultas analíticas.
    - ***Consultas complejas:*** como por ejemplo, cual fue el producto mas vendido el ultimo año en cada región.
    - ***Grandes volúmenes de datos:*** trabaja con millones de registros, ya que suele integrar datos históricos.
    - ***no en tiempo real:*** los datos suelen cargarse en lotes de sistemas OLTP u otras fuentes.

## BigQuery (OLAP)
La estructura que usa Bigquery para almacenar los datos es ***FROM proyecto.dataset.tabla***, ``SELECT tripduration FROM `bigquery-public-data`.new_york_citibike.citibike_trips``. Hay que tener cuidado en cuanta información proceso, porque google cobra por eso. El `limit 10` por ejemplo, no va a funcionar, porque igual procesa todas y luego si le saca las 10 primeras, igual a la derecha dice el peso de la consulta.

### Ejemplos sencillos en sql
> En el select voy a poner siempre la misma tabla, para que gc no me consuma muchos recursos, lo ideal seria seleccionar todas o ciertas tablas.
1. Query de un tripduration menor a 600 seg
```sql
SELECT tripduration FROM `bigquery-public-data`.new_york_citibike.citibike_trips
WHERE tripduration<600
```
2. Query donde end_station_name tenga la palabra Ave, par eso se usan los ``%``
```sql
SELECT end_station_name FROM `bigquery-public-data`.new_york_citibike.citibike_trips
WHERE end_station_name LIKE '%Ave%'
```
3. Query donde start_station_name esté en X lista
```sql
SELECT start_station_name FROM `bigquery-public-data`.new_york_citibike.citibike_trips
WHERE start_station_name IN ('W 52 St & 5 Ave','Liberty St & Broadway')
```
4. Query de todas las columnas, excepto customer_plan. Como dato el `EXCEPT` es único de BigQuery
```sql
SELECT * EXCEPT(customer_plan) FROM `bigquery-public-data`.new_york_citibike.citibike_trips
```
5. Query de todas las columnas, donde tripduration se pase de seg a min.
```sql
SELECT * REPLACE(tripduration/60 AS tripduration) FROM `bigquery-public-data`.new_york_citibike.citibike_trips
```
6. Query sobre start_station_name, que me muestre las estaciones visitadas entre cierta fecha y ordenado de manera ascendente.
```sql
SELECT DISTINCT start_station_name FROM `bigquery-public-data`.new_york_citibike.citibike_trips WHERE starttime BETWEEN '2016-07-01' and '2016-07-05' ORDER BY start_station_name ASC
```
7. Tema ***funciones de agregación***. Query del número de filas en la tabla. 
```sql
SELECT COUNT(*) AS Total_filas FROM `bigquery-public-data`.new_york_citibike.citibike_trips
```
8. Número de viajes por género.
```sql
SELECT gender, COUNT(*) AS Total_gender FROM `bigquery-public-data`.new_york_citibike.citibike_trips GROUP BY gender
```
9. Tiempo de duración de los viajes promedio por tipo de usuario.
```sql
SELECT usertype, AVG(tripduration) AS tripduration_avg FROM `bigquery-public-data`.new_york_citibike.citibike_trips GROUP BY usertype
```
10. Tema ***subquerys***. Obtener todos los viajes cuya duración es mayor a la promedio de todos los viajes. Lo mejor seria primero hacer el subquery, luego si intentar el otro y ponerlo en parentesis.
```sql
SELECT tripduration FROM `bigquery-public-data`.new_york_citibike.citibike_trips
WHERE tripduration > (SELECT AVG(tripduration) AS tripduration_avg FROM `bigquery-public-data`.new_york_citibike.citibike_trips)
```
11. Obtener las estaciones que tengan más de 10_000 viajes. Acá se pasó la subquery en el from porque como tal la data era de una tabla, no de un valor como avg.
```sql
SELECT start_station_name, total_trips FROM (
    SELECT start_station_name,
    COUNT(*) AS total_trips
    FROM `bigquery-public-data`.new_york_citibike.citibike_trips
    GROUP BY start_station_name)WHERE total_trips>10000
```
12. Tema ***having***. El mismo ejercicio anterior pero con having. El having funciona como un where pero para los datos ya procesados.
```sql
SELECT start_station_name,
COUNT(*) AS total_trips
FROM `bigquery-public-data`.new_york_citibike.citibike_trips
GROUP BY start_station_name
HAVING total_trips>10000
```
13. Tema ***WITH***. Identificar las bicicletas que han sido usadas en más de 500 viajes y luego seleccionar todos los detalles de esos viajes. Para esto se pueden usar los CTE que son tablas temporales, que se pueden reusar, también  se pueden crear más de uno.
```sql
WITH bike_500 AS (
  SELECT bikeid FROM `bigquery-public-data`.new_york_citibike.citibike_trips
  GROUP BY bikeid
  HAVING count(bikeid) > 500
)

SELECT *
FROM `bigquery-public-data`.new_york_citibike.citibike_trips
WHERE bikeid IN (select bikeid from bike_500)
```

14. Tema ***INNER JOIN***. Este es un poco complejo, la idea es ver si la lluvia afecta a las rentas de bicicletas, con el código también se puede jugar con las fechas, para ver entre ciero mes por ejemplo. la función `EXTRACT` es de bigquery.
```sql
WITH bicycle_rentals AS(
   SELECT EXTRACT(DATE from starttime) AS trip_date, COUNT(*) AS num_trips
   FROM `bigquery-public-data`.new_york_citibike.citibike_trips
   GROUP BY trip_date
),
rainy_days AS (
   SELECT date, 
   (MAX(prcp)>5) AS rainy
   FROM(
      SELECT wx.date as date,
         IF (wx.element='PRCP', wx.value/10, NULL) AS prcp
      FROM `bigquery-public-data`.ghcn_d.ghcnd_2016 as wx
      WHERE wx.id = 'USW00094728'
   )
   GROUP BY date
)

SELECT ROUND(AVG(br.num_trips)) AS NUM_TRIPS_AVG, rd.rainy
FROM bicycle_rentals as br
INNER JOIN rainy_days as rd
ON br.trip_date = rd.date
GROUP BY rd.rainy
```
> ***Explicación del código.***
> Comenzamos con dos tablas temporales, `bicycle_rentals` que nos cuenta los viajes que se hicieron en X fecha, extraigo la fecha sin hora con la función de bq `EXTRACT`, esto para poder agruparlo y tener el numero total de viajes por dia.<br>
>Luego `rainy_days`, empezando por la subconsulta que me imprime las fechas agrupadas en dias en donde hubo precipitaciones, el ``IF`` es para decir, que si es ***PRCP***(Precipitación) lo divida en 10 para pasarlo a mm, y lo devuelva, si no, devuelve null, el ``WHERE`` nos iguala el id al del centro metereológico de NY. Ya teniendo los dias con precipitaciones la consulta grande lo que hace es teniendo en cuenta la tabla de la consulta anterior, agrupar por dias y mostrar si la precipitación max era mayor a 5, o sea, hubo mal clima, y que quede en booleano.<br>
>***La consulta final***, me saca el promedio de los numeros de viajes, y agrupa por rainy, es decir nos daria un promedio de las rentas de las bicicletas si hubo mal clima o no. el código consiste en hacer un inner join con la fecha (por dias), y un group by si hubo mal clima.




## Usando python
> En el archivo ``main.py`` va a estar lo que haga.

Siguiendo el tutorial... me voy a IAM/Service Accounts, creo el nuevo servicio con el nombre que quiera, luego le doy permisos de solo cargar cosas, entonces en select role, el que tenemos es ***Storage Object Creator***, entro en la cuenta y en keys, la generamos y descargamos el json.