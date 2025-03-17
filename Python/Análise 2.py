## Evolução das Avaliações IMDb
## Este gráfico de linha mostra como as avaliações dos filmes (imdb_score) mudaram ao longo dos anos.

import pandas as pd
import matplotlib.pyplot as plt


# Ordenar os dados por ano
df_sorted = df.sort_values(by='Year')

# Criar o gráfico de linha
plt.figure(figsize=(8, 5))
plt.plot(df_sorted['Year'], df_sorted['imdb_score'], marker='o', linestyle='-', color='red')

# Configuração do gráfico
plt.xlabel('Ano de Lançamento')
plt.ylabel('IMDb Score')
plt.title('Evolução das Avaliações IMDb dos Filmes da Pixar')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir gráfico
plt.show()
