# -- coding: utf-8 --
"""

@author: victor
"""

from matplotlib.pyplot import figure
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

CHUNKSIZE=10000

df = pd.read_csv('MICRODADOS_ENEM_2015.csv', parse_dates=True,encoding='latin-1',sep=',',nrows=CHUNKSIZE)
df = df[['TP_DEPENDENCIA_ADM_ESC','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']]
df = df.dropna()

df['TP_DEPENDENCIA_ADM_ESC'] = df['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
#Média de cada coluna baseado no valor de TP_DEPENCENCIA_ADM_ESC .e.g Média para Federal, Média para Estadual...
df = df.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']].mean()



fig, axs = plt.subplots(1,5)

#criar gráficos de barra lado a lado
for ax,col in zip(axs,["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"]):
	ax.set_xticks([])
	ax.set_xlabel([])

	sns.barplot(x = "TP_DEPENDENCIA_ADM_ESC", y = col,ci = None,
		hue = "TP_DEPENDENCIA_ADM_ESC", data = df, ax=ax,capsize=.8)

i=0
for ax in axs:
	ax.set_ylabel('')
	ax.set_xlabel('')
	ax.set_xticks([])

	if i == 0:	
		ax.set_ylabel('Média Nota',fontsize = 13)
		ax.legend_.remove()
		ax.set_xlabel('Ciências da Natureza',fontsize = 11)
	if i == 1:
		ax.set_xlabel("Ciências Humanas",fontsize = 11)
		ax.legend_.remove()
	if i == 2:
		ax.set_xlabel("Linguagens e Códigos",fontsize = 11)
		ax.legend_.remove()
	if i ==3:
		ax.set_xlabel("Matemática",fontsize = 11)
		leg = plt.legend(loc = 'upper right')
		bb = leg.get_bbox_to_anchor().inverse_transformed(ax.transAxes)
		bb.x0 += 0.5
		bb.x1 += 0.5
		leg.set_bbox_to_anchor(bb,transform=ax.transAxes)
		ax.legend_.remove()
	if i == 4:
		ax.set_xlabel("Redação",fontsize = 11)

	i = i+1

plt.title('Desempenho em cada prova do ENEM 2015 para cada tipo de Escola', loc = 'right',x=-0.55,y=1.04, fontsize = 15)
f = plt.figure(1)
plt.show()



##############################################################################################################################
"""



df1 = pd.read_csv('MICRODADOS_ENEM_2017.csv', parse_dates=True,encoding='latin-1',sep=';',nrows=CHUNKSIZE)
df1 = df1[['TP_DEPENDENCIA_ADM_ESC','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']]
df1 = df1.dropna()


df1['TP_DEPENDENCIA_ADM_ESC'] = df1['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
#Média de cada coluna baseado no valor de TP_DEPENCENCIA_ADM_ESC .e.g Média para Federal, Média para Estadual...
df1 = df1.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']].mean()

fig1, axs1 = plt.subplots(1,5)


#criar gráficos de barra lado a lado
for ax1,col1 in zip(axs1,["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"]):
	ax1.set_xticks([])
	ax1.set_xlabel([])

	sns.barplot(x = "TP_DEPENDENCIA_ADM_ESC", y = col1,ci = None,
		hue = "TP_DEPENDENCIA_ADM_ESC", data = df1, ax=ax1,capsize=.8)


#Configurações dos gráficos
i=0
for ax1 in axs1:
	ax1.set_ylabel('')
	ax1.set_xlabel('')
	ax1.set_xticks([])

	if i == 0:	
		ax1.set_ylabel('Média Nota',fontsize = 13)
		ax1.legend_.remove()
		ax1.set_xlabel('Ciências da Natureza',fontsize = 11)
	if i == 1:
		ax1.set_xlabel("Ciências Humanas",fontsize = 11)
		ax1.legend_.remove()
	if i == 2:
		ax1.set_xlabel("Linguagens e Códigos",fontsize = 11)
		ax1.legend_.remove()
	if i ==3:
		ax1.set_xlabel("Matemática",fontsize = 11)
		leg1 = plt.legend(loc = 'upper right')
		bb1 = leg1.get_bbox_to_anchor().inverse_transformed(ax1.transAxes)
		bb1.x0 += 0.5
		bb1.x1 += 0.5
		leg1.set_bbox_to_anchor(bb1,transform=ax1.transAxes)
		ax1.legend_.remove()
	if i == 4:
		ax1.set_xlabel("Redação",fontsize = 11)

	i = i+1
plt.title('Desempenho em cada prova do ENEM 2017 para cada tipo de Escola', loc = 'right',x=-0.55,y=1.04, fontsize = 15)
f1 = plt.figure(2)
print(df1)
print(df)
plt.show()
"""