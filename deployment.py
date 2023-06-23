import subprocess

def deploy_app():
    # Passos de implantação do aplicativo
    print("Iniciando implantação do aplicativo...")
    
    # Passo 1: Obter a última versão do código-fonte do repositório Git
    subprocess.run(["git", "pull"])
    
    # Passo 2: Executar testes automatizados
    subprocess.run(["pytest"])
    
    # Passo 3: Construir o pacote de implantação (por exemplo, um arquivo tar ou um contêiner Docker)
    subprocess.run(["docker", "build", "-t", "myapp:latest", "."])
    
    # Passo 4: Implantar o aplicativo em um ambiente de produção
    subprocess.run(["kubectl", "apply", "-f", "kubernetes-deployment.yaml"])
    
    print("Implantação concluída com sucesso!")

# Chamada da função para implantação
deploy_app()
