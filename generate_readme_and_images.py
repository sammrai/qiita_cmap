import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# 利用可能なカラーマップを取得
cmaps = plt.colormaps()

# データの生成
xs = np.arange(1, 10)
ys = np.arange(1, 10).reshape(9, 1)
m = xs * ys
df = pd.DataFrame(m)

# テンプレートの読み込み
def load_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# テンプレートを読み込む
header_template = load_template('templates/header_template.txt')
section_template = load_template('templates/section_template.txt')

# README.mdを作成
with open('README.md', 'w') as readme:
    readme.write(header_template)
    
    for cmap in cmaps:
        # ヒートマップを生成し、画像として保存
        plt.figure(figsize=(5, 3))
        ax = sns.heatmap(df, cmap=cmap)
        ax.tick_params(axis='both', which='both', length=0)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlabel('')
        ax.set_ylabel('')
        plt.tight_layout(pad=0.1)
        plt.savefig(f'images/{cmap}.png',transparent=True)
        plt.close()

        # READMEにセクションを追加
        section_content = section_template.format(cmap_name=cmap)
        readme.write(section_content)
