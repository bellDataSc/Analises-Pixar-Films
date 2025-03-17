## Duração Média dos Filmes por Década
## Mostra como a duração média dos filmes variou ao longo das décadas.

import pandas as pd
import matplotlib.pyplot as plt

# Média de duração por década
df_runtime = df.groupby('Decada')['run_time'].mean()

# Gráfico de barras
plt.figure(figsize=(8, 5))
df_runtime.plot(kind='bar', color='lightcoral', edgecolor='black')

# Configuração do gráfico
plt.xlabel('Década')
plt.ylabel('Duração Média (min)')
plt.title('Duração Média dos Filmes da Pixar por Década')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir gráfico
plt.show()
