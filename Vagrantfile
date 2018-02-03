# -*- mode: ruby -*-
# vi: set ft=ruby :

puts ENV["AZURE_TENANT_ID"]
puts ENV["AZURE_CLIENT_ID"]
puts ENV["AZURE_CLIENT_SECRET"]
puts ENV["AZURE_SUBSCRIPTION_ID"]

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    config.ssh.private_key_path = '~/.ssh/id_rsa'
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    azure.vm_size = 'Basic_A0'
    azure.location = 'southcentralus'
    azure.tcp_endpoints = '80'
    azure.vm_name = "jaochaosbot"
    azure.resource_group_name= "JaoChaosBot"
    azure.tenant_id = 'b6f2d7ef-0bce-4820-b6e8-fee39045f175'
    azure.client_id = '0f7e34be-21f9-4786-aa70-089d1758a25c'
    azure.client_secret = '4qpjKyOumaasy438Gq6nKp6JzVqE2DeIphvGO+cfXHc='
    azure.subscription_id = '34352f6b-1f92-464a-94c9-88d482cce75a'

  end

  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "./provision/playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end

end
