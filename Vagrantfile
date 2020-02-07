Vagrant.configure(2) do |config|
  # Como base de la máquina vamos a utilizar ubuntu 16.04 LTS
  config.vm.box = "ubuntu/xenial64"

  # Configuración de reenvío de puertos
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.provider "virtualbox" do |vb|
    # Asignamos 1GB de RAM a la máquina
    vb.memory = "1024"
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'provision/playbook.yml'
    ansible.verbose = 'v'
  end
end