import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv('data.csv')

# Calcular o CVR (Conversion Rate) e NRPS (Net Revenue per Session) por plataforma
platforms = data['platform'].unique()
cvr_by_platform = [
    data[(data['platform'] == platform) & (data['event_name'] == 'purchase')]['sessions'].sum() /
    data[data['platform'] == platform]['sessions'].sum() for platform in platforms
]

nrps_by_platform = [
    data[data['platform'] == platform]['revenue'].sum() /
    data[data['platform'] == platform]['sessions'].sum() for platform in platforms
]

# Criar gráficos de barras para CVR e NRPS
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Definir paleta de tons de cinza
colors = ['#A9A9A9', '#696969']  # Cinza claro e escuro

# Gráfico de CVR por plataforma
ax[0].bar(platforms, cvr_by_platform, color=colors)
ax[0].set_title('Conversion Rate (CVR) by Platform', fontsize=16)
ax[0].set_ylabel('CVR (%)', fontsize=12)
ax[0].set_ylim(0, 1)  # Limite de 0 a 100%
ax[0].set_xticks(range(len(platforms)))
ax[0].set_xticklabels(platforms, fontsize=12)

# Adicionar rótulos com os valores nas barras do gráfico de CVR
for i, v in enumerate(cvr_by_platform):
    ax[0].text(i, v + 0.03, f"{v:.2%}", ha='center', fontsize=10, color='black')

# Gráfico de NRPS por plataforma
ax[1].bar(platforms, nrps_by_platform, color=colors)
ax[1].set_title('Net Revenue per Session (NRPS) by Platform', fontsize=16)
ax[1].set_ylabel('NRPS ($)', fontsize=12)
ax[1].set_xticks(range(len(platforms)))
ax[1].set_xticklabels(platforms, fontsize=12)

# Ajustar a posição dos rótulos para evitar sobreposição
for i, v in enumerate(nrps_by_platform):
    ax[1].text(i, v + 0.02 if v < 0.5 else v - 0.05, f"${v:.2f}", ha='center', fontsize=10, color='black')

# Ajustar espaçamento e exibir o dashboard
plt.tight_layout()
plt.show()