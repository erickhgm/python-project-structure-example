# Exemplo de estrutura de pacotes para um projeto Python
Exemplo de estrutura de projeto com possibilidade de ter varios pacotes e modulos com seus respectivos testes.

## Pré-requisitos
Ter o Python 3.8.2+ instalado

## Passos para executar
### Criar um ambiente virtual
```
python -m vevn venv
venv\Scripts\activate.bat
```

### Instalar bibliotecas
```
pip install -r requirements.txt
```

### Executar
```
python src\main.py
```

### Executar testes
```
coverage run --source=src -m pytest -o junit_family=xunit2 --junitxml=xunit.xml
```

### Gerar arquivo de cobertura (SonarQube)
```
coverage xml
```

### Gerar relatório HTML de cobertura
```
coverage html
```

### Gerar arquivo com pylint (SonarQube)
```
pylint src -r n --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.txt
```