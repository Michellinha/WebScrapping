# Ajustando Ambiente Virtual Python

### Instalando nosso novo gerenciados de pacotes

### Estrutura basica do projeto:

A pasta **app** contem as pastas **src** e **test**. A pasta src são onde ficam os códigos(programas) e a pasta **test** é para a realização de testes dos códigos(programas). O arquivo **Pipfile** é onde ficam todas as informações de dependências do projeto. O arquivo **Pipfile.lock** é um arquivo para guardar informações de especificações das versões. Esse arquivo não é utilizado pelos humanos e sim pelas maquinas. O arquivo **README.md** tem todas as informações para a execuções do projeto no ambiente virtual python.

```
.
├── app
│   ├── src
│   │   └── webscrapping.py
│   └── test
│       └── web_test.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

Os diretórios (.venv) e (.vscode) são arquivos de configurações e do ambiente virtual. O ambiente virtual deste projeto fica na pasta (.venv) e as configurações da IDE ficam na pasta (.vscode).

#### Linux Ubuntu

Adicione a seguinte sentença no arquivo .profile em /home/.profile

Isso é realizado apenas uma vez.

```
export PIPENV_VENV_IN_PROJECT=1 
```

Após adicinar a variável (PIPENV_VENV_IN_PROJECT) acima no arquivo .profile, reiniciar o computador.

Essa variável de ambiente é utilizada para criar o ambiente virtual do python por projeto, sendo assim, será criada um diretório (.venv) na raiz do projeto.

Esse diretório (.venv) é o seu ambiente virtual python. As dependências instaladas nesse ambiente virtual, no caso o projeto, não afetará outros ambientes virtuais(outros projetos). Sendo assim, não teremos conflitos de versões de módulos.

#### Utilizando o pipenv ao invés do pip

```
pip install --user pipenv
```

# Todos os pacotes utilizados

## Inicializando um projeto

Se o projeto já estiver um arquivo com o nome Pipfile, não é necessário rodar o comando abaixo.

O comando abaixo inicializa um novo projeto python.

```
pipenv --three --python 3.11
```

Caso o projeto já possua o arquvio (Pipfile) rode o comando abaixo:

```
pipenv shell
```
Ao executar o comando acima, você entrará no ambiente virtual do seu projeto, nesse caso, (WebScrapping). Aparecerá no seu terminal, o nome do projeto, indicando que você está no ambiente virtual.

E posteriormente rode o comando abaixo, para installar todas as dependências(módulos) necessário para a execução do projeto.

```
pipenv install
```


### Instalação dos pacotes(módulos) utilizados nesse projeto.

Caso você precise installar um novo pacote que não está no seu Pipfile. Entre no terminal e digite  o seguinte comando:

```
pipenv install nome_pacote
```

Estas são as dependências específicas deste projeto.

```
pipenv install pandas

pipenv install selenium

pipenv install webdriver_manager

pipenv install Beautifulsoup4

pipenv install requests

pipenv install python_time

pipenv install openpyxl
```

Se você verificar o arquivo Pipfile, verá que existe todas as dependencias instaladas na tag [packages].

Isso facilita quando um novo desenvolvedor entra no projeto, com apenas um comando (pipenv install) já instala todas as dependências deste projeto.