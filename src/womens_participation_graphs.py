import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from data_cleaner import *
from womens_participation import *


df_olymp, df_olymp_countries, df_paralymp, df_paralymp_countries, df2_olymp, df2_olymp_bra, df2_paralymp, df2_paralymp_bra = create_dataframes()

def plot_scatter_graph(df, x, y1, y2, title, score_or_amount):
    # Criando o gráfico de dispersão
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=x, y=y1, data=df, label='Women', color='purple', s=70)
    sns.scatterplot(x=x, y=y2, data=df, label='Men', color='blue', s=70)

    # Ajustando o gráfico
    plt.xlabel('Year')
    plt.ylabel(score_or_amount)
    plt.title(title)
    plt.legend(loc='upper left')
    plt.show()
    
    
df_analisys_aux = df_olymp
#plot_scatter_graph(df_analisys_aux, 'Year', 'F_Athletes', 'M_Athletes', 'Scatter Plot: Male Athletes X Female Athletes (Global)', 'Amount')
df_analisys_aux = df_analisys_aux[(df_analisys_aux['M_Score'] > 0) | (df_analisys_aux['F_Score'] > 0)]
#plot_scatter_graph(df_analisys_aux, 'Year', 'F_Medal', 'M_Medal', 'Scatter Plot: Men\'s Score X Women\'s Score (Global)', 'Score')

df_analisys_aux = df_olymp_countries[df_olymp_countries['NOC']=='BRA']
#lot_scatter_graph(df_analisys_aux, 'Year', 'F_Athletes', 'M_Athletes', 'Scatter Plot: Male Athletes X Female Athletes (Brazil)', 'Amount')
df_analisys_aux = df_analisys_aux[(df_analisys_aux['M_Score'] > 0) | (df_analisys_aux['F_Score'] > 0)]
#plot_scatter_graph(df_analisys_aux, 'Year', 'F_Medal', 'M_Medal', 'Scatter Plot: Men\'s Score X Women\'s Score (Brazil)', 'Score')

