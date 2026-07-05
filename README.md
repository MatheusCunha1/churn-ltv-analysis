# Churn & LTV Analysis

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-1.5-FFF000?logoColor=black)
![dbt](https://img.shields.io/badge/dbt-Core-FF694B?logo=dbt&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

Pipeline de dados end-to-end construído como projeto de estudo de Analytics Engineering, usando dados reais de transações de cartão de crédito.

## Sobre

Projeto de aprendizado prático para construir um pipeline completo com arquitetura Medalhão — desde a ingestão dos dados brutos até a visualização em um dashboard de BI.

O dataset contém dados de clientes, cartões, transações (~13 milhões de registros) e categorias de estabelecimentos (MCC codes), totalizando 1.17GB. A exploração dos dados guiará as perguntas de negócio que serão respondidas na camada Gold, como padrões de churn e lifetime value de clientes.

O foco do projeto é aprender na prática as ferramentas da stack moderna de dados: MinIO, Pandas, DuckDB, dbt, Airflow e Metabase.

## Arquitetura

```
Bronze (CSV → MinIO)
    ↓ Pandas — limpeza e conversão para Parquet
Silver (Parquet → MinIO)
    ↓ DuckDB + dbt — modelagem dimensional
Gold (PostgreSQL)
    ↓
Metabase (BI)
```

## Stack

| Camada | Tecnologia |
|---|---|
| Storage | MinIO (S3 compatível) |
| Exploração | DuckDB |
| Transformação | Pandas |
| Modelagem | dbt |
| Orquestração | Apache Airflow |
| Data Warehouse | PostgreSQL |
| BI | Metabase |
| Infraestrutura | Docker + Docker Compose |

## Dataset

Dataset de transações de cartão de crédito com ~13 milhões de registros (1.17GB).

| Arquivo | Descrição |
|---|---|
| `cards_data.csv` | Dados dos cartões (6.146 registros) |
| `transactions_data.csv` | Transações (~13M registros) |
| `users_data.csv` | Dados demográficos e financeiros dos clientes |
| `online_data.csv` | Dados de transações online |
| `mcc_codes.json` | Categorias de estabelecimentos (Merchant Category Codes) |

## Estrutura do Projeto

```
churn-ltv-analysis/
├── src/
│   ├── configs/        # Conexões e configurações (MinIO)
│   └── scripts/        # Scripts de execução (buckets, upload)
├── notebooks/
│   └── bronze/         # Exploração exploratória dos dados brutos
├── docs/
│   ├── aprendizado.md                  # Diário de aprendizagem
│   ├── checklist_atividades_feitas.md  # Rastreador de progresso
│   └── memory.md                       # Referência consolidada
├── docker-compose.yml  # MinIO + serviços
├── Dockerfile
└── requirements.txt
```

## Como rodar

### Pré-requisitos
- Docker e Docker Compose instalados
- Python 3.12+

### Subir o MinIO

```bash
docker-compose up -d
```

Acesse o console em: http://localhost:9001
Credenciais padrão: `minioadmin` / `minioadmin`

### Instalar dependências

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### Criar buckets

```bash
python src/scripts/create_buckets.py
```

## Status do Projeto

- [x] Fase 1 — Setup MinIO + estrutura do projeto
- [ ] Fase 2 — Exploração Bronze + script Silver (Pandas)
- [ ] Fase 3 — Modelagem Gold (dbt)
- [ ] Fase 4 — Orquestração (Airflow)
- [ ] Fase 5 — BI (Metabase)
