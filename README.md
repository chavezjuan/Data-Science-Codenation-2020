# AceleraDev Data Science Codenation 2020
*Repositório para os desafios semanais e projeto final do programa Aceleradev Data Science da Codenation*

## Getting Started
Cada projeto semanal se encontra na pasta correspondente na estrutura do repositório. Em cada pasta há um arquivo requirements.txt que já apresenta todas as dependências necessárias para rodar o projeto. 
Recomendo fortemente que utilize um ambiente virtual de sua preferência. No meu caso escolhi o virtualenv.

## Instalação

#### Criando um ambiente virtual com o virtualenv
Dentro da pasta do projeto desejado, proceder da seguinte forma para instalação:
```bash
pip3 install virtualenv
virtualenv venv -p python3
```
Para ativar o seu ambiente virtual criado:
```bash
source venv/bin/activate
```

#### Instalando dependências
Com o ambiente ativado, executar o arquivo requirements.txt:
```bash
pip install -r requirements.txt
```

#### Executando o notebook pelo Jupyter Notebook
Para acessaar a solução do desafio basta entrar na pasta correspondente, ativar o ambiente virtual e executar:
```bash
jupyter notebook
```
Uma nova tela será aberta no seu navegador o o diretório da pasta. Basta clicar no notebook para executar.

## Contribuição
Fique a vontade para sugerir melhorias no código. Estou em constante aprendizado.

