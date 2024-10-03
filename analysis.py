import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')


platforms = data['platform'].unique()
cvr_by_platform = [
    data[(data['platform'] == platform) & (data['event_name'] == 'purchase')]['sessions'].sum() /
    data[data['platform'] == platform]['sessions'].sum() for platform in platforms
]

nrps_by_platform = [
    data[data['platform'] == platform]['revenue'].sum() /
    data[data['platform'] == platform]['sessions'].sum() for platform in platforms
]

fig, ax = plt.subplots(1, 2, figsize=(14, 6))


colors = ['#A9A9A9', '#696969']  


ax[0].bar(platforms, cvr_by_platform, color=colors)
ax[0].set_title('Conversion Rate (CVR) by Platform', fontsize=16)
ax[0].set_ylabel('CVR (%)', fontsize=12)
ax[0].set_ylim(0, 1)  
ax[0].set_xticks(range(len(platforms)))
ax[0].set_xticklabels(platforms, fontsize=12)


for i, v in enumerate(cvr_by_platform):
    ax[0].text(i, v + 0.03, f"{v:.2%}", ha='center', fontsize=10, color='black')


ax[1].bar(platforms, nrps_by_platform, color=colors)
ax[1].set_title('Net Revenue per Session (NRPS) by Platform', fontsize=16)
ax[1].set_ylabel('NRPS ($)', fontsize=12)
ax[1].set_xticks(range(len(platforms)))
ax[1].set_xticklabels(platforms, fontsize=12)


for i, v in enumerate(nrps_by_platform):
    ax[1].text(i, v + 0.02 if v < 0.5 else v - 0.05, f"${v:.2f}", ha='center', fontsize=10, color='black')


plt.tight_layout()
plt.show()
