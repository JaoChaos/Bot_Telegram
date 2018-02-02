vagrantup --provider=azure

fab -f ./deployment/fabfile.py -H vagrant@jaochaosbot.southcentralus.cloudapp.azure.com InstallApp
fab -f ./deployment/fabfile.py -H vagrant@jaochaosbot.southcentralus.cloudapp.azure.com StartApp
