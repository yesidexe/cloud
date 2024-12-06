# Azure
## Crear espacio de trabajo
Es para crear un entorno básico de ml.
- Removemos ciertas extensiones o versiones antiguas para que no cuase conflicto.
- Agregamos la extesión ml, ``-y`` evita la confimación
- Creo el grupo de recursos, que es similar a crear un proyecto en gcp, con la ubicación en "east us"
- creo un workspace de ml donde puedo desarrollar, entrenar y desplegar modelos de ml que permite az.
```shell
az extension remove -n azure-cli-ml
az extension remove -n ml
az extension add -n ml -y
az group create --name "bootcamp-dp100" --location "eastus"
az ml workspace create --name "mlw-dp100-cli" -g "bootcamp-dp100"
```

