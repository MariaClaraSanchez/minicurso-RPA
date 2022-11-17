# RPA Preencher Formulário - Minicurso

Essa solução foi desenvolvida utilizando puramente a linguagem de programação Python com algumas bibliotecas. Essa automação foi feita durante o minicurso de Python, que eu mistrei no Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas - Campus Poços de Caldas, no dia 09/11/2023. 

O formulário utilizado nesse robô para ser preenchido foi : [Formulário](https://forms.gle/WSQJXD2ohBWtnyLC7)
  
# Configurações
## Máquina Virtual
Caso queira executar o projeto separadamente da onde fica seus documentos python é preciso cria uma máquina virtual e para isso precisa da os seguintes passos:
<br>
1º Instalar o env em sua máquina para isso utilize o comando :
```
pip install venv
```
2º Criar sua máquina virtual:
```
python -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Antes de iniciar o projeto é necessário instalar as configurações de ambiente de um modo mais fácil e prático é só usar o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

# Inicializando

Para executar a automação basta entrar na pasta scr executar o comando :

```
pyhton main.py
```
