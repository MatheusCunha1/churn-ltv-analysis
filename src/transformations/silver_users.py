"""
users_data.csv
--------------
- Renomear colunas para português (ver tabela de tradução no notebook 03_users_data.ipynb)
- Separar endereco em duas colunas: numero_endereco (parte numérica) + logradouro (parte textual)
- Remover cifrão ($) e converter para DOUBLE: renda_per_capita, renda_anual, divida_total
- Unificar birth_year + birth_month em uma coluna data_nascimento no formato MM/YYYY
- Converter 0 → NULL em renda_per_capita, renda_anual e divida_total
  → Decisão: 113 de 2000 registros (5,6%) com valor 0 — improvável que seja real em dados de cartão de crédito
  → Motivo: manter 0 distorceria médias e agregações na Gold

"""

