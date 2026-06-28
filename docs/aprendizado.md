# 🎓 Aprendizado - Documentar Progressão para LinkedIn

## Objetivo
Registrar progressão no projeto **churn-ltv-analysis** para futuro portfólio profissional.

---

## 📅 Sessão 1 (2026-06-12)

### O que aprendi
- ✅ MinIO com Docker (S3 compatível local)
- ✅ Arquitetura Medalhão (Bronze → Silver → Gold)
- ✅ Padrão DRY (Don't Repeat Yourself)
- ✅ Boto3 (SDK AWS/MinIO)
- ✅ Separação de responsabilidades em projeto Python

### O que fiz
- Criou `docker-compose.yml` com MinIO
- Criou `src/config/minio_config.py` com função `get_minio_client()`
- Implementou padrão de conexão reutilizável

### Conceitos-chave consolidados
- **MinIO**: S3 compatível rodando localmente, Porto 9000 (API) + 9001 (Console)
- **Boto3**: SDK para comunicar com AWS/MinIO
- **DRY**: Centralizar credenciais, não repetir código

---

## 📅 Sessão 2 (2026-06-14)

### O que aprendi
- ✅ Python Recapitulado: variáveis, funções, loops, condicionais, try/except
- ✅ Boto3 avançado: `head_bucket()` e `make_bucket()`
- ✅ Tratamento de erros com `ClientError`
- ✅ Idempotência em scripts (rodar 1x ou 100x, resultado é o mesmo)
- ✅ Integração com docker-compose

### O que fiz
- Criou script `src/scripts/create_buckets.py` que:
  - Conecta no MinIO via Boto3
  - Verifica se buckets existem com `head_bucket()`
  - Cria buckets faltantes com `make_bucket()`
  - Lida com erros profissionalmente (try/except)

### Conceitos-chave consolidados
- **Try/Except**: Tentar algo, capturar erro se falhar
- **Idempotência**: Script seguro para rodar múltiplas vezes
- **Boto3 Avançado**: Métodos específicos para verificação e criação
- **Estrutura Profissional**: `if __name__ == "__main__"` (padrão Python)

---

## 📅 Sessão 3 (2026-06-20)

### O que aprendi
- ✅ Dockerfile — receita do container (FROM, WORKDIR, COPY, RUN)
- ✅ `requirements.txt` — lista de dependências Python
- ✅ `image:` vs `build:` no docker-compose
- ✅ Rede Docker — containers se comunicam pelo nome do serviço, não localhost
- ✅ Volumes Docker — como montar pastas da máquina no container
- ✅ `os.listdir()` e `os.path.join()` para percorrer pastas
- ✅ `upload_file()` do boto3
- ✅ História: Hadoop → Spark → Data Lake → lakehouse
- ✅ Data Swamp — o que acontece sem organização de camadas
- ✅ Agentes customizados no Claude Code

### O que fiz
- Criou `Dockerfile` e `requirements.txt`
- Corrigiu docker-compose para usar `build: .` e `PYTHONPATH`
- Criou função `upload_buckets()` com loop, try/except e os.path.join
- Montou volume para o container enxergar `data/bronze/`
- Subiu os dados CSV para o bucket bronze no MinIO ✅
- Criou dois agentes de mentoria no projeto

### Conceitos-chave consolidados
- **Dockerfile**: receita para construir o container
- **`build: .`**: usa o Dockerfile local em vez de imagem pronta
- **Rede Docker**: containers usam nome do serviço como host
- **Volume**: `./data:/app/data` mapeia pasta local para dentro do container
- **Data Swamp**: Data Lake sem organização de camadas vira caos

---

## 📅 Sessão 4 (2026-06-27)

### O que aprendi
- ✅ DuckDB — banco analítico embarcado, lê CSV/Parquet direto sem carregar tudo na RAM
- ✅ Paradigmas declarativo (SQL/dbt) vs imperativo (Python/Pandas)
- ✅ Parâmetros do `read_csv_auto`: `strict_mode`, `null_padding`, `ignore_errors`, `quote`
- ✅ Diferença entre coluna faltando (`null_padding`) vs coluna sobrando (`strict_mode=false`)
- ✅ Jupyter Notebook no VS Code — exploração célula por célula
- ✅ Organização de projeto: `notebooks/` para exploração, `src/` para produção
- ✅ Aspas triplas `"""` para SQL multilinha no Python
- ✅ Análise exploratória categórica com DuckDB

### O que fiz
- Instalou DuckDB e adicionou ao `requirements.txt`
- Criou `src/scripts/explore_bronze.py` para primeiros testes
- Migrou exploração para `notebooks/bronze/01_cards_data.ipynb`
- Rodou análise exploratória no `cards_data.csv` (6.146 linhas) — dataset limpo ✅
- Descobriu problema no `transactions_data.csv` — 941 linhas com vírgula dentro do valor
- Confirmou que `quote='"'` resolve o parsing corretamente (13.305.915 linhas)
- Verificou ausência de duplicatas no `CARD_NUMBER`

### Conceitos-chave consolidados
- **DuckDB**: motor SQL embarcado, coluna por coluna, sem carregar tudo na RAM
- **`strict_mode=false`**: tolera linhas com colunas extras (vírgula dentro do valor)
- **`null_padding=true`**: preenche com NULL quando falta coluna na linha
- **`quote='"'`**: reconhece aspas como delimitador de texto no CSV
- **Notebook vs Script**: notebook para exploração interativa, script para produção
- **Dado sujo encontrado**: `transactions_data.csv` — campo `errors` com vírgula interna

---

## 🎯 Habilidades Desenvolvidas

### Python (em progresso)
- [x] Variáveis e tipos básicos
- [x] Funções
- [x] Loops (for)
- [x] Condicionais (if/else)
- [x] Try/Except
- [ ] Classes e OOP
- [ ] Decorators
- [ ] Context Managers

### Data Engineering
- [x] MinIO/S3 (boto3)
- [x] Arquitetura Medalhão
- [ ] MongoDB (conexão, consulta)
- [ ] Pandas (transformação)
- [ ] SQL (avançado)
- [ ] Airflow DAGs
- [ ] dbt

### Padrões & Boas Práticas
- [x] DRY (Don't Repeat Yourself)
- [x] Separação de responsabilidades
- [x] Idempotência
- [x] Tratamento de erros
- [ ] Factory Pattern
- [ ] Strategy Pattern
- [ ] Logging profissional

---

## 📊 Progressão do Projeto

### Fase 1: Setup MinIO ✅ CONCLUÍDO
- [x] Docker-compose com MinIO
- [x] Função de conexão (Boto3)
- [x] Script de criação de buckets
- [x] Estrutura de pastas profissional

### Fase 2: Upload de Dados ⏳ PRÓXIMA
- [ ] Script para fazer upload do CSV (1.17GB)
- [ ] Validação de dados no bronze
- [ ] Testes unitários

### Fase 3: Transformação Silver ⏳ FUTURA
- [ ] Script silver.py para limpeza
- [ ] Pandas para transformação
- [ ] Validação de dados

### Fase 4: Orquestração ⏳ FUTURA
- [ ] DAG Airflow básica
- [ ] Agendamento de pipeline
- [ ] Logging profissional

### Fase 5: Modelagem Gold ⏳ FUTURA
- [ ] dbt para transformações
- [ ] Star schema (dimensional)
- [ ] Dashboard Power BI

---

## 💡 Insights & Decisões Arquiteturais

### Por que MinIO localmente?
- Ambiente de desenvolvimento igual produção (S3 compatível)
- Sem custo AWS durante desenvolvimento
- Fácil iterar e testar

### Por que separar scripts de config?
- **DRY**: não repetir credenciais
- **Segurança**: centralizar secrets
- **Testabilidade**: mockar conexão em testes
- **Profissionalismo**: qualquer dev entende arquitetura

### Por que try/except em create_buckets?
- **Robusto**: não trava se bucket já existe
- **Idempotente**: rodar múltiplas vezes é seguro
- **Production-ready**: comportamento previsível

---

## 🔗 Próximos Focos de Aprendizado

1. **Python Intermediário**
   - Classes e OOP
   - Context Managers (`with`)
   - Decorators

2. **Testes Unitários**
   - pytest
   - Mocking Boto3
   - Fixtures

3. **Transformação de Dados**
   - Pandas na prática
   - SQL avançado
   - PySpark (futuro)

4. **Airflow & Orquestração**
   - Estrutura de DAGs
   - Agendamento
   - Monitoramento

---

## 📝 Reflexão Pessoal

### O que funcionou bem
- Aprender conceito → ver exemplo real → codificar funcionou muito bem
- Entender POR QUÊ cada padrão existe ajudou a reter conhecimento
- Lógica forte em programação facilitou mapear Python

### Desafios
- Sintaxe Python ainda precisa praticar mais
- Explorar documentação de Boto3 foi helpful

### Taxa de Aprendizado
- ✅ 6 conceitos Python consolidados
- ✅ 5 padrões Data Engineering aprendidos
- ✅ 1 script profissional implementado
- ✅ Estrutura robusta pronta para próxima fase

---

**Última atualização**: 2026-06-14 — Sessão 2 concluída com sucesso 🎉
