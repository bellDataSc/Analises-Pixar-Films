## Correlação entre Orçamento e Bilheteria Mundial
## Visualiza a relação entre orçamento (budget) e arrecadação global (box_office_worldwide).

import pandas as pd
import matplotlib.pyplot as plt

# Gráfico de dispersão
plt.figure(figsize=(8, 5))
plt.scatter(df['budget'], df['box_office_worldwide'], color='blue', alpha=0.5)

# Configuração do gráfico
plt.xlabel('Orçamento (USD)')
plt.ylabel('Bilheteria Mundial (USD)')
plt.title('Relação entre Orçamento e Bilheteria Mundial')
plt.grid(True, linestyle='--', alpha=0.7)

# Exibir gráfico
plt.show()
