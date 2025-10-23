# 🚀 Mini Pipeline de ETL com Python, MinIO e POO
O objetivo é implementar uma **pipeline de ETL (Extract, Transform, Load)** local, simulando a interação com a AWS S3 através do **MinIO**, aplicando **boas práticas de engenharia de software**, **POO**, **testes unitários** e **automação de execução**.

---

## ✅ Critérios de Aceite e Evidências

| Área | Critério de Aceite | Evidência / Forma de Validação |
|------|--------------------|-------------------------------|
| **1. Organização e Estrutura de Projeto** | Projeto organizado em módulos (`src/`, `tests/`, `utils/`, etc.). Uso de `__init__.py` para pacotes. | Estrutura de pastas criada e navegável. Importações funcionam corretamente. |
| **2. Programação Orientada a Objetos (POO)** | Pelo menos 1 classe criada (ex: `DataPipeline`, `DataExtractor`, `LoggerConfig`). | Classe implementada e instanciada em `main.py`. |
| **3. Manipulação de Arquivos** | Ler e escrever arquivos CSV, JSON e Parquet do MinIO local. | Scripts `extract.py` e `load.py` testados com `boto3` + MinIO. |
| **4. Logging e Exceções** | Configuração de logs via módulo `logging`, salvando em `logs/app.log` e exibindo no console. | Execução do pipeline gera logs legíveis com timestamps e níveis (`INFO`, `ERROR`). |
| **5. Tipagem (Typing)** | Funções principais anotadas com tipos (`def func(x: str) -> int:`). | Execução do `mypy` sem erros críticos de tipagem. |
| **6. Testes Unitários** | Criar testes com `pytest` ou `unittest` cobrindo pelo menos 3 módulos. Uso de `unittest.mock` para simular S3. | Execução `pytest` → cobertura ≥ **80%**, sem falhas. |
| **7. Mini Pipeline de ETL** | Pipeline completo: lê de `raw/`, transforma, grava em `processed/`. | Rodar `python src/main.py` executa o fluxo end-to-end com logs. |
| **8. Automação (Agendamento)** | Script `.sh` ou `.py` para execução agendada (ex: `crontab` ou `schedule`). | Execução simulada dispara pipeline em horário determinado. |
| **9. Documentação** | README.md explicando propósito, dependências, execução e exemplos. | Leitura do README permite rodar o projeto sem ajuda externa. |
| **10. Boas Práticas de Engenharia** | Código limpo (PEP8), docstrings, tratamento de erros, versionamento via Git. | `flake8`/`ruff` sem erros críticos; commits organizados. |

---

## 🧠 Tecnologias Utilizadas

- **Python 3.10+**
- **boto3** – integração com MinIO (S3 local)
- **pytest / unittest** – testes unitários
- **mypy** – checagem de tipos
- **flake8 / ruff** – linting e boas práticas
- **logging** – logs estruturados
- **schedule / crontab** – automação de execução
- **pandas / pyarrow** – manipulação de dados e arquivos

---

## 📂 Resumo dos arquivos - Raw
**Orders.csv** — dados de pedidos com datas em formatos variados, valores (incluindo alguns negativos para simular retornos), ship_date faltando em alguns registros e notas com caracteres especiais. Ótimo para praticar parsing de datas, limpeza e detecção de anomalias.

**Customers.csv** — cadastro de clientes com variações de casing, e-mails faltando/malformados, telefones, endereços e pontuações de fidelidade com alguns null. Bom para normalização, validação e enriquecimento.

**events.jsonl** — newline-delimited JSON com eventos de produto/usuário, propriedades aninhadas e algumas linhas intencionalmente malformadas para que você pratique tolerância a erros e parsing robusto.

## ⚙️ Instalação e Execução - (Em Construção)

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/etl-minio-pipeline.git
cd etl-minio-pipeline
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o MinIO local
Para iniciar:
```bash
minio server ~/minio-data
```
Acesse a interface web em: 👉 http://localhost:9001

Configure suas credenciais no arquivo: *src/config/settings.py*\
Exemplo:
```python
MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password"
RAW_BUCKET = "raw-data"
PROCESSED_BUCKET = "processed-data"
```

### 5. Executar o pipeline ETL
```bash
python src/main.py
```

### 6. Rodar os testes
```bash
pytest --cov=src
```

### 7. Os logs são gerados em:
```text
logs/app.log
```