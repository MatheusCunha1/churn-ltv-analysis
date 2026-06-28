# 📚 Memory.md - Conceitos de Python & Data Engineering

## Objetivo
Centralizar conceitos aprendidos para estudar fora e consolidar conhecimento.

---

## 🐍 Python Fundamentals (Recapitulados)

### 1. Variáveis
**Conceito**: Guardar dados
```python
lista_buckets = ["bronze", "silver", "gold"]  # lista de strings
```
**Por quê**: Reutilizar valores sem repetir código (DRY)

---

### 2. Funções
**Conceito**: Bloco de código reutilizável
```python
def create_buckets():
    # código aqui
```
**Por quê**: Não repetir a mesma lógica em vários lugares

---

### 3. Loop (For)
**Conceito**: Repetir algo para cada item de uma lista
```python
for bucket_name in lista_buckets:
    # faz algo com cada bucket_name
```
**Lógica**: "para cada bucket na minha lista, execute isso"

---

### 4. Condicional (If/Else)
**Conceito**: Fazer coisas diferentes baseado em uma condição
```python
if bucket_existe:
    print("já existe")
else:
    print("criar novo")
```
**Lógica**: "se X é verdadeiro, faça Y, senão faça Z"

---

### 5. Try/Except (Tratamento de Erros)
**Conceito**: Tentar fazer algo, mas se der erro, fazer outra coisa
```python
try:
    client.head_bucket(Bucket=bucket_name)  # TENTA
except ClientError:
    client.create_bucket(Bucket=bucket_name)  # SE DER ERRO, FAZ ISSO
```
**Lógica**: "tenta isso, MAS se falhar, faz aquilo"

**Por quê**: Programa não trava quando algo dá errado

---

## 🏗️ Arquitetura de Dados

### Medalhão (3 camadas)
- **Bronze**: dados brutos, sem transformação
- **Silver**: dados limpos, estruturados
- **Gold**: dados agregados, prontos para análise

**Buckets MinIO**: bronze, silver, gold (correspondem às camadas)

---

## ☁️ MinIO & Boto3

### O que é MinIO?
S3 compatível rodando localmente em Docker. Permite testar sem AWS.

### O que é Boto3?
SDK Python para comunicar com AWS/MinIO.

### Métodos Boto3 aprendidos
- **`head_bucket(Bucket=name)`**: Verifica se bucket existe
  - Retorna sucesso se existe
  - Lança `ClientError` se não existe
  
- **`create_bucket(Bucket=name)`**: Cria novo bucket
  - Cria o bucket no MinIO
  - Usa `try/except` pra capturar se já existe

### ClientError
Exceção (erro) lançada por Boto3 quando algo dá errado.

---

### ⚠️ Armadilha: boto3 vs MinIO SDK

Existem dois SDKs diferentes para usar o MinIO com Python:

| SDK | Lib | Método para criar bucket |
|---|---|---|
| **boto3** (AWS) | `import boto3` | `create_bucket()` |
| **MinIO SDK** | `from minio import Minio` | `make_bucket()` |

**Este projeto usa boto3.** Nunca usar `make_bucket()` aqui — vai dar `AttributeError`.

---

## 🎯 Padrões Aprendidos

### DRY (Don't Repeat Yourself)
**Conceito**: Não repetir código
- ✅ Centralizar conexão em `src/config/minio_config.py`
- ✅ Usar funções reutilizáveis
- ❌ Hardcoded credenciais

### Separação de Responsabilidades
**Conceito**: Cada arquivo/função tem UM propósito
- `config/` = configuração (credenciais, conexões)
- `scripts/` = execução (scripts rodáveis)
- `transformations/` = lógica de negócio

### Idempotência
**Conceito**: Rodar 1x ou 100x, resultado é o mesmo
- Exemplo: criar buckets que já existem não dá erro, ignora

---

## 📁 Estrutura de Projeto

```
src/
├── config/              # Configuração (credenciais, conexões)
│   └── minio_config.py  # Função get_minio_client()
├── scripts/             # Scripts executáveis
│   └── create_buckets.py  # Criar buckets MinIO
└── transformations/     # Lógica de transformação

tests/                   # Testes unitários
```

**Por quê cada pasta?**
- Separação clara de responsabilidades
- Fácil de navegar e manter
- Padrão profissional

---

## 🔗 Links Úteis

- [Boto3 Documentação](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [MinIO Python SDK](https://docs.min.io/docs/python-client-quickstart-guide.html)
- Stack Overflow: buscar "boto3 [operação]"

---

## 📝 Exercícios para Praticar

1. **Variáveis**: Crie uma lista de 5 nomes e printe cada um com loop
2. **Funções**: Crie uma função que recebe um número e retorna ele × 2
3. **Try/Except**: Tente abrir um arquivo que não existe, capture o erro
4. **Boto3**: Crie um script que lista todos os buckets do MinIO

---

**Última atualização**: 2026-06-14
