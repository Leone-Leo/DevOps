#!/bin/bash

# Script de provisionamento de infraestrutura usando o Terraform

echo "Iniciando o provisionamento da infraestrutura..."

# Comandos para inicializar o diretório do projeto Terraform
terraform init

# Comandos para planejar as alterações de infraestrutura
terraform plan

# Comandos para aplicar as alterações de infraestrutura
terraform apply -auto-approve

echo "Provisionamento da infraestrutura concluído com sucesso!"
