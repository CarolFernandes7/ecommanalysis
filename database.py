import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv('data.csv')

# Configurar o tamanho da figura
fig, ax = plt.subplots(figsize=(10, 2.5))  # Ajuste o tamanho conforme necessário

# Remover as bordas do gráfico
ax.axis('off')

# Criar uma tabela com os dados do DataFrame
table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center')

# Ajustar a escala da tabela
table.scale(1.2, 1.5)  # Aumentar a largura e a altura das células

# Ajustar o layout da tabela
table.auto_set_font_size(False)
table.set_fontsize(14)  # Aumentar o tamanho da fonte para melhor visibilidade

# Salvar a tabela como uma imagem PNG
plt.savefig('adjusted_database_table.png', bbox_inches='tight', dpi=300)

# Exibir a tabela
plt.show()