#!/bin/bash

# Script de gerenciamento de configurações usando o Ansible

echo "Iniciando o gerenciamento de configurações..."

# Comandos para executar playbooks do Ansible para configurar servidores
ansible-playbook -i inventory.ini playbook.yml

echo "Gerenciamento de configurações concluído com sucesso!"
