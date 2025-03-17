# Análise dos Filmes da Pixar (1995 - 2021)

**📌Introdução**
A Pixar é um dos estúdios de animação mais icônicos do cinema, responsável por sucessos como Toy Story, Procurando Nemo e Divertida Mente. Desde o lançamento do primeiro filme em 1995, a empresa revolucionou o mercado de animação com histórias cativantes e avanços tecnológicos.

Neste trabalho, exploramos um conjunto de dados que contém informações sobre os filmes da Pixar lançados entre 1995 e 2021. O objetivo é realizar análises exploratórias para entender tendências, padrões e insights sobre a evolução do estúdio ao longo dos anos.

Entre os aspectos analisados, destacamos:

O número de filmes lançados por década; A evolução das avaliações no IMDb ao longo dos anos; A média de duração dos filmes por década; A distribuição de gêneros dentro do catálogo da Pixar. Utilizando bibliotecas como pandas e matplotlib, buscamos apresentar uma visão geral dos dados e suas principais características. Este estudo pode ser útil para fãs do estúdio, pesquisadores de cinema e profissionais de análise de dados interessados na evolução da indústria de animação.

**📊 Aspectos Analisados**

O número de filmes lançados por década.

A evolução das avaliações no IMDb ao longo dos anos.

A média de duração dos filmes por década.

A distribuição de gêneros dentro do catálogo da Pixar.

Utilizando bibliotecas como pandas e matplotlib, buscamos apresentar uma visão geral dos dados e suas principais características. Este estudo pode ser útil para fãs do estúdio, pesquisadores de cinema e profissionais de análise de dados interessados na evolução da indústria de animação.

**📂 Estrutura do Repositório**

notebook_pixar_analysis.ipynb → Notebook principal contendo as análises exploratórias.

data/pixar_films.csv → Conjunto de dados utilizado na análise.

README.md → Documentação do projeto.

images/ → Pasta contendo os gráficos gerados na análise.

**🛠 Tecnologias Utilizadas**

Python 3

Pandas (para manipulação de dados)

Matplotlib e Seaborn (para visualização de dados)

NumPy (para operações matemáticas)


**📈 Exemplos de Visualização**

1️⃣ Número de Filmes por Década

Mostra quantos filmes a Pixar lançou em cada década:
    
    import matplotlib.pyplot as plt
    
    df['Decada'] = (df['release_date'].dt.year // 10) * 10
    df_decada = df['Decada'].value_counts().sort_index()
    
    plt.figure(figsize=(8, 5))
    df_decada.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('Década')
    plt.ylabel('Número de Filmes')
    plt.title('Número de Filmes da Pixar por Década')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

**2️⃣ Evolução das Avaliações IMDb**

Mostra a tendência das avaliações dos filmes ao longo dos anos:

    plt.figure(figsize=(8, 5))
    plt.plot(df_sorted['Year'], df_sorted['imdb_score'], marker='o', linestyle='-', color='red')
    plt.xlabel('Ano de Lançamento')
    plt.ylabel('IMDb Score')
    plt.title('Evolução das Avaliações IMDb dos Filmes da Pixar')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()




## 📧 Contact
For questions or collaborations, feel free to reach out via:

🔗 LinkedIn: [(https://www.linkedin.com/in/belcruz/)]

📧 Email: [isabel.gon.adm@gmail.com]

📌 Author: Bel – Technical Data Analyst, Government of São Paulo, Brazil
