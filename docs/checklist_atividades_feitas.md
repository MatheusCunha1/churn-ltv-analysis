# ✅ Checklist de Atividades Realizadas

## Objetivo
Rastrear atividades concluídas do projeto churn-ltv-analysis.

---

## 📆 Dias de Estudo

| Data       | Estudou? |
|------------|----------|
| 2026-06-12 | ✅ |
| 2026-06-14 | ✅ |
| 2026-06-20 | ✅ |
| 2026-06-21 | ✅ |
| 2026-06-27 | ✅ | DuckDB + exploração Bronze |

---

## 📅 Sessão 1 (2026-06-12) - Setup MinIO

### Planejamento & Conceitos
- [x] Entender por que MinIO (S3 compatível local)
- [x] Estudar arquitetura Medalhão (Bronze/Silver/Gold)
- [x] Aprender padrão DRY (Don't Repeat Yourself)
- [x] Compreender separação de responsabilidades

### Implementação
- [x] Criar arquivo `docker-compose.yml` com MinIO
- [x] Configurar volume persistente
- [x] Subir container MinIO (porta 9000 API, 9001 console)
- [x] Acessar console web (http://localhost:9001)
- [x] Criar arquivo `src/config/minio_config.py`
- [x] Implementar função `get_minio_client()` com Boto3
- [x] Criar script para gerar buckets (bronze, silver, gold)
- [x] Testar conexão MinIO com Python

### Documentação
- [x] Criar `CLAUDE.md` com instruções do projeto
- [x] Documentar padrões de arquitetura

---

## 📅 Sessão 2 (2026-06-14) - Script de Buckets & Python Recapitulação

### Planejamento & Conceitos
- [x] Entender diferença entre `src/` e `config/`
- [x] Aprender quando rodar scripts (setup vs execução)
- [x] Recapitular Python: variáveis, funções, loops, condicionais
- [x] Aprender try/except (tratamento de erros)
- [x] Entender botocore e ClientError
- [x] Estudar `head_bucket()` e `make_bucket()` (Boto3)

### Implementação
- [x] Pesquisar solução Stack Overflow (boto3 bucket validation)
- [x] Criar script `src/scripts/create_buckets.py`
- [x] Implementar verificação com `head_bucket()`
- [x] Implementar criação com `make_bucket()`
- [x] Adicionar try/except para tratamento de erros
- [x] Adicionar prints informativos
- [x] Usar padrão `if __name__ == "__main__"`
- [x] Estruturar código de forma profissional

### Aprendizado & Consolidação
- [x] Mapear lógica pura → sintaxe Python
- [x] Entender por quê try/except é importante
- [x] Entender idempotência em scripts
- [x] Recapitular 5 conceitos Python fundamentais
- [x] Aprender 2 métodos Boto3 novos

### Documentação
- [x] Atualizar `CLAUDE.md` com framework de mentoria completo
- [x] Criar `memory.md` com conceitos para estudar
- [x] Criar `aprendizado.md` para LinkedIn/portfólio
- [x] Criar `checklist_atividades_feitas.md` (este arquivo)
- [x] Salvar instruções de mentoria em memória

---

## 📅 Sessão 3 (2026-06-20) - Docker, Upload Bronze & Agentes

### Planejamento & Conceitos
- [x] Entender por que a pasta se chama `src`
- [x] Entender Dockerfile — receita do container
- [x] Entender `requirements.txt` — lista de dependências
- [x] Diferença entre `image:` e `build:` no docker-compose
- [x] Entender por que `localhost` não funciona entre containers
- [x] Entender volumes Docker (`./data:/app/data`)
- [x] História do Data Lake: Hadoop → Spark → lakehouse
- [x] Diferença boto3 vs MinIO SDK (`create_bucket` vs `make_bucket`)
- [x] Conceito de Data Swamp (falta de organização no Data Lake)

### Implementação
- [x] Criar `Dockerfile` na raiz do projeto
- [x] Criar `requirements.txt` com boto3
- [x] Corrigir docker-compose: `image:` → `build: .`
- [x] Adicionar `PYTHONPATH: /app` no docker-compose
- [x] Criar `__init__.py` em `src/` e `src/configs/`
- [x] Corrigir endpoint: `localhost:9000` → `minio:9000`
- [x] Criar função `upload_buckets()` com `os.listdir` + `upload_file`
- [x] Adicionar `try/except` no upload com `Exception as e`
- [x] Montar volume `./data:/app/data` no docker-compose
- [x] Upload dos dados CSV para o bucket bronze ✅

### Agentes criados
- [x] `python-mentor` — especialista Python/boto3
- [x] `data-engineering-mentor` — mentor progressivo de arquitetura

### Documentação
- [x] Atualizar `CLAUDE.md` com estado atual do projeto
- [x] Atualizar `docs/memory.md` com armadilha boto3 vs MinIO SDK
- [x] Adicionar seção de docs no `CLAUDE.md`

---

## 📅 Sessão 4 (2026-06-27) - DuckDB + Exploração Bronze

### Conceitos
- [x] DuckDB — o que é, por que usar na exploração
- [x] Paradigmas declarativo vs imperativo
- [x] Parâmetros read_csv_auto: strict_mode, null_padding, ignore_errors, quote
- [x] Diferença coluna faltando vs sobrando
- [x] Jupyter Notebook no VS Code
- [x] Organização: notebooks/ vs src/
- [x] Aspas triplas para SQL multilinha no Python

### Implementação
- [x] Instalou DuckDB (`duckdb-1.5.4`) e adicionou ao requirements.txt
- [x] Criou `src/scripts/explore_bronze.py` (testes iniciais)
- [x] Criou `notebooks/bronze/01_cards_data.ipynb`
- [x] Rodou COUNT no cards_data.csv → 6.146 linhas
- [x] Rodou DESC para ver colunas e tipos
- [x] Descobriu 941 linhas problemáticas no transactions_data.csv
- [x] Confirmou `quote='"'` como solução correta → 13.305.915 linhas
- [x] Verificou duplicatas em CARD_NUMBER → sem duplicatas ✅
- [x] Análise categórica: CARD_BRAND (Mastercard, Visa, Amex, Discover)

### Findings Bronze
- [x] `cards_data.csv` → dataset limpo, sem problemas aparentes
- [x] `transactions_data.csv` → campo `errors` com vírgula interna (941 linhas afetadas)

---

## 🎯 Próximas Atividades (Sessão 5 — próximo estudo)

### Fase 2 — Continuar Exploração Bronze + Bronze → Silver
- [ ] Continuar exploração do `transactions_data.csv` e `online_data.csv` no notebook
- [ ] Abrir Jupyter Notebook com Pandas
- [ ] Ler CSV do Bronze e explorar: nulos, tipos, duplicatas, colunas sujas
- [ ] Anotar o que precisa ser limpo
- [ ] Escrever script de limpeza (Pandas)
- [ ] Converter CSV → Parquet
- [ ] Subir Parquet limpo para MinIO Silver
- [ ] Configurar DuckDB para ler Parquet da Silver
- [ ] Setup dbt Core no projeto
- [ ] Criar primeiro model dbt (stg_transactions)
- [ ] Adicionar PostgreSQL no docker-compose.yml
- [ ] Adicionar Metabase no docker-compose.yml

---

## 🎯 Atividades Futuras (Sessão 5+)

### Upload de Dados
- [ ] Testar script `create_buckets.py` rodando manualmente
- [ ] Integrar `create_buckets.py` no `docker-compose.yml`
- [ ] Criar script `src/scripts/upload_data.py`
- [ ] Implementar upload do CSV (1.17GB) para bucket bronze
- [ ] Validar se dados estão no MinIO (console web)
- [ ] Testar leitura de dados do MinIO

### Testes Unitários
- [ ] Criar pasta `tests/unit/`
- [ ] Escrever testes para `minio_config.py`
- [ ] Escrever testes para `create_buckets.py`
- [ ] Usar pytest e mocking Boto3
- [ ] Rodar testes localmente

### Transformação Silver
- [ ] Criar `src/transformations/silver.py`
- [ ] Ler dados do bucket bronze
- [ ] Aplicar transformações (limpeza, padronização)
- [ ] Salvar em bucket silver
- [ ] Documentar transformações aplicadas

### Orquestração
- [ ] Estudar Airflow (básico)
- [ ] Criar DAG inicial
- [ ] Integrar scripts existentes
- [ ] Agendamento da pipeline

### Modelagem Gold
- [ ] Estudar star schema
- [ ] Criar modelagem dimensional
- [ ] Usar dbt para transformações
- [ ] Testes de modelagem

---

## 📊 Progresso Geral

### Concluído (2 sessões)
```
████████░░ 80% de Fase 1
```

**Sessão 1**: 7 atividades
**Sessão 2**: 8 atividades
**Total**: 15 atividades ✅

### Métrica de Qualidade
- ✅ Código profissional (padrões, estrutura)
- ✅ Conceitos aprendidos (entender POR QUÊ)
- ✅ Documentação atualizada
- ✅ Erros tratados corretamente

---

## 💾 Arquivos Criados/Modificados

### Sessão 1
- `docker-compose.yml` ✅
- `src/config/minio_config.py` ✅
- `CLAUDE.md` ✅

### Sessão 2
- `src/scripts/create_buckets.py` ✅
- `CLAUDE.md` (atualizado com framework) ✅
- `docs/memory.md` ✅
- `docs/aprendizado.md` ✅
- `docs/checklist_atividades_feitas.md` ✅

---

## 🎓 Habilidades Consolidadas por Sessão

### Sessão 1
- MinIO + Docker ✅
- Arquitetura Medalhão ✅
- Boto3 básico ✅
- DRY Pattern ✅

### Sessão 2
- Python (5 conceitos) ✅
- Try/Except ✅
- Boto3 avançado (head_bucket, make_bucket) ✅
- Idempotência ✅
- Padrão profissional (if __name__) ✅

---

## 🚀 Métricas de Progresso

| Métrica | Valor |
|---------|-------|
| Sessões Completas | 2 |
| Atividades Realizadas | 15 |
| Conceitos Aprendidos | 11 |
| Scripts Criados | 2 |
| Padrões Implementados | 4 |
| Taxa de Retenção | 80%+ |

---

**Última atualização**: 2026-06-14 — Sessão 2
