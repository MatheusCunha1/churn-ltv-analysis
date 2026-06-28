# Churn & LTV Analysis

Pipeline de dados end-to-end para análise de churn e lifetime value de clientes de cartão de crédito.

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

Arquivos:
- `cards_data.csv` — dados dos cartões (6.146 registros)
- `transactions_data.csv` — transações (~13M registros)
- `online_data.csv` — dados de transações online

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
