## Número de Filmes por Década
## Este gráfico de barras mostra quantos filmes a Pixar lançou em cada década, usando a coluna release_date.

import pandas as pd
import matplotlib.pyplot as plt

# Converter release_date para datetime e extrair o ano
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['Year'] = df['release_date'].dt.year

# Criar uma nova coluna para a década
df['Decada'] = (df['Year'] // 10) * 10

# Contagem de filmes por década
df_decada = df['Decada'].value_counts().sort_index()

# Plotar gráfico de barras
plt.figure(figsize=(8, 5))
df_decada.plot(kind='bar', color='skyblue', edgecolor='black')

# Configuração do gráfico
plt.xlabel('Década')
plt.ylabel('Número de Filmes')
plt.title('Número de Filmes da Pixar por Década')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir gráfico
plt.show()
