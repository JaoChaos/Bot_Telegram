//Fichero de despliegue con fabric

vagrantup --provider=azure

fab -f ./despliegue/fabfile.py -H vagrant@jaochaosbot.southcentralus.cloudapp.azure.com InstallApp
fab -f ./despliegue/fabfile.py -H vagrant@jaochaosbot.southcentralus.cloudapp.azure.com StartApp
