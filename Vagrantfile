# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

require 'rbconfig'



Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.forward_agent = true
  config.vm.box_check_update = true
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "10.1.2.200"
  config.vm.network :forwarded_port, host: 8000, guest: 8000

  config.vm.synced_folder ".", "/home/vagrant", :id => "vagrant-root", :nfs => true
  config.vm.synced_folder ".", "/vagrant", disabled: true


  config.vm.provider "virtualbox" do |vb|
  vb.gui = true
  end

end
