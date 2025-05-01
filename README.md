```
Olá mundo! 😉

Prazer meu nome é Fernando, sou "minêro" e estou aprendendo python para me tornar um engenheiro de dados!
```


# Inicio do projeto do workshop de Estruturação de projeto

## Utilização do [Pyenv](https://github.com/pyenv/pyenv)

```
Para ver as versões do python instaladas: 

pyenv versions

Para Instalar uma nova versão:

pyenv install 3.11.5
```

## Ambiente venv

```
Para controle do ambiente preciso criar o ambiente através do:
python -m venv .venv

Para ativar:
linux: source .vent/bin/activate
windows: souce .venv/Scripts/activate

Para desativar:
deactivate
```

Primeiramente inicio com o poetry para fazer o controle do meu ambiente


## Poetry

```
    para configurar o ambiente
 - poetry init 
    para entrar no ambiente virtual
 - poetry shell 
```

## git
```
para inicializar o git:
 - git init
para adicionar um ou mais arquivos
 - git add .
iniciando o versionamento do codigo 
 - git commit -m "first commit"
definindo a branch 
 - git branch -M main
definido o meu ambiente remoto
 - git remote add origin https://github.com/#
Imputando o arquivo no github
 - git push -u origin main

```
# Plugins

```
 - materials icon
```

# Testes unitarios

Primeiramente, o teste unitário é um teste feito basicamente para validar e certificar que o nosso código está rodando e funcional.

A biblioteca utilizada vai ser o **pytest**, utilizando o padrão de testes [Automation Panda](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)

O teste unitário é feito literalmente testando e forçando erros no código ex: validando se um dataframe do pandas é do tipo pd.DataFrame:

def test_minha_funcao():
   df = pd.DataFrame
   dataframe = meudf
   assert df == meudf

```
para rodar o teste:
 - pytest -v
```

# Bibliotecas auxiliares

Existem PEP's que seguem "regras" para que o código fique pythonico... 

Destas bibliotecas:

```
   Para seguir a PEP8
 - black .
 - blue .
 - isort .

   Uma opção de variação do blue ou black é o flake8 mas vai de gosto, o flake pega toda a pep8 e analisa o código

obs: é importante o "gerogero" no pyproject para que um não sobrescreva o outro quando se tem blue ou black e isort por exemplo

[tool.isort]
profile = "black"
known_third_party = []

   O taskipy é uma ferramenta poderosa que "automatiza" a ordem e necessidades do código
 - taskipy

no pyproject
[tool.taskipy.tasks]
format = "isort . && black ."
run ""

Para rodar> - task format

Este comando roda oque foi colocado no pyproject

```

# CI/CD

Basicamente é um "pre-merge" se é que posso dizer assim... para que possamos validar se o código está rodando e validado com base em critérios postos no yaml
[Documentação](https://docs.github.com/pt/actions/writing-workflows/quickstart)