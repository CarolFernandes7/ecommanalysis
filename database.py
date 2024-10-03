import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv('data.csv')

# Configurar o tamanho da figura
fig, ax = plt.subplots(figsize=(10, 2.5))  


ax.axis('off')


table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center')


table.scale(1.2, 1.5)  


table.auto_set_font_size(False)
table.set_fontsize(14)  


plt.savefig('adjusted_database_table.png', bbox_inches='tight', dpi=300)


plt.show()
