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

df = pd.read_csv('MICRODADOS_ENEM_2013.csv', parse_dates=True,encoding='latin-1',sep=';',nrows=CHUNKSIZE)
df = df[['ID_DEPENDENCIA_ADM_ESC','NOTA_CN','NOTA_CH','NOTA_LC','NOTA_MT','NU_NOTA_REDACAO','UF_ESC']]
df.dropna()
print(df)

"""
df['TP_DEPENDENCIA_ADM_ESC'] = df['TP_DEPENDENCIA_ADM_ESC'].map({['MA','PI','CE','RN','PB','PE','AL','SE','BA']:'Nordeste',
	['MG','ES','RJ','SP']:'Sudeste',['PR','SC','RS']:'Sul',['MT','MS','GO','DF']:'Centro Oeste',
	['AC','RO','AM','RR','PA','AP','TO']:'Norte'})
	"""
df_nordeste = df[df.UF_ESC.isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])]
df_sudeste = df[df.UF_ESC.isin(['MG','ES','RJ','SP'])]
df_sul = df[df.UF_ESC.isin(['PR','SC','RS'])]
df_centro_oeste = df[df.UF_ESC.isin(['MT','MS','GO','DF'])]
df_norte = df[df.UF_ESC.isin(['AC','RO','AM','RR','PA','AP','TO'])]


df_nordeste['ID_DEPENDENCIA_ADM_ESC'] = df_nordeste['ID_DEPENDENCIA_ADM_ESC'].map({1:'Publica',2:'Publica',3:'Publica',4:'Privada'})
df_sudeste['ID_DEPENDENCIA_ADM_ESC'] = df_sudeste['ID_DEPENDENCIA_ADM_ESC'].map({1:'Publica',2:'Publica',3:'Publica',4:'Privada'})
df_sul['ID_DEPENDENCIA_ADM_ESC'] = df_sul['ID_DEPENDENCIA_ADM_ESC'].map({1:'Publica',2:'Publica',3:'Publica',4:'Privada'})
df_centro_oeste['ID_DEPENDENCIA_ADM_ESC'] = df_centro_oeste['ID_DEPENDENCIA_ADM_ESC'].map({1:'Publica',2:'Publica',3:'Publica',4:'Privada'})
df_norte['ID_DEPENDENCIA_ADM_ESC'] = df_norte['ID_DEPENDENCIA_ADM_ESC'].map({1:'Publica',2:'Publica',3:'Publica',4:'Privada'})

df_nordeste['Media'] = (df_nordeste['NOTA_CN'] + df_nordeste['NOTA_CH'] + df_nordeste['NOTA_LC'] + df_nordeste['NOTA_MT'] + df_nordeste['NU_NOTA_REDACAO']) / 5
df_sudeste['Media'] = (df_sudeste['NOTA_CN'] + df_sudeste['NOTA_CH'] + df_sudeste['NOTA_LC'] + df_sudeste['NOTA_MT'] + df_sudeste['NU_NOTA_REDACAO']) / 5
df_sul['Media'] = (df_sul['NOTA_CN'] + df_sul['NOTA_CH'] + df_sul['NOTA_LC'] + df_sul['NOTA_MT'] + df_sul['NU_NOTA_REDACAO']) / 5
df_centro_oeste['Media'] = (df_centro_oeste['NOTA_CN'] + df_centro_oeste['NOTA_CH'] + df_centro_oeste['NOTA_LC'] + df_centro_oeste['NOTA_MT'] + df_centro_oeste['NU_NOTA_REDACAO']) / 5
df_norte['Media'] = (df_norte['NOTA_CN'] + df_norte['NOTA_CH'] + df_norte['NOTA_LC'] + df_norte['NOTA_MT'] + df_norte['NU_NOTA_REDACAO']) / 5

df_nordeste = df_nordeste.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sudeste = df_sudeste.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sul = df_sul.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_centro_oeste = df_centro_oeste.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_norte = df_norte.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()



dateindex=df_nordeste['ID_DEPENDENCIA_ADM_ESC']

aa=dict(zip(df_nordeste['ID_DEPENDENCIA_ADM_ESC'],df_nordeste['Media']))
bb=dict(zip(df_norte['ID_DEPENDENCIA_ADM_ESC'],df_norte['Media']))
cc=dict(zip(df_centro_oeste['ID_DEPENDENCIA_ADM_ESC'],df_centro_oeste['Media']))
dd=dict(zip(df_sul['ID_DEPENDENCIA_ADM_ESC'],df_sul['Media']))
ee=dict(zip(df_sudeste['ID_DEPENDENCIA_ADM_ESC'],df_sudeste['Media']))


dfbar = pd.DataFrame({'Nordeste': aa, 'Norte': bb, 'Centro Oeste': cc,'Sul': dd, 'Sudeste': ee},index = dateindex)

dfbar.plot.bar(figsize=(20, 8))
plt.title("Média de notas do ENEM 2013 Publico Privado")
plt.legend(title="Região", fontsize = 13)
plt.xticks(rotation=0)
ax = plt.subplot(111)
ax.set_xlabel('')
ax.legend(loc = 'upper left', bbox_to_anchor=(0.77, 1.15),  shadow=True, ncol=2)
ax.set_ylabel('Nota',fontsize = 13)
plt.xticks(rotation=0)

plt.show()
"""

df = pd.read_csv('MICRODADOS_ENEM_2013.csv', parse_dates=True,encoding='latin-1',sep=',',nrows=CHUNKSIZE)
df = df[['TP_DEPENDENCIA_ADM_ESC','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO','SG_UF_ESC']]
df.dropna()

df_nordeste = df[df.SG_UF_ESC.isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])]
df_sudeste = df[df.SG_UF_ESC.isin(['MG','ES','RJ','SP'])]
df_sul = df[df.SG_UF_ESC.isin(['PR','SC','RS'])]
df_centro_oeste = df[df.SG_UF_ESC.isin(['MT','MS','GO','DF'])]
df_norte = df[df.SG_UF_ESC.isin(['AC','RO','AM','RR','PA','AP','TO'])]


df_nordeste['TP_DEPENDENCIA_ADM_ESC'] = df_nordeste['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sudeste['TP_DEPENDENCIA_ADM_ESC'] = df_sudeste['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sul['TP_DEPENDENCIA_ADM_ESC'] = df_sul['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_centro_oeste['TP_DEPENDENCIA_ADM_ESC'] = df_centro_oeste['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_norte['TP_DEPENDENCIA_ADM_ESC'] = df_norte['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})

df_nordeste['Media'] = (df_nordeste['NU_NOTA_CN'] + df_nordeste['NU_NOTA_CH'] + df_nordeste['NU_NOTA_LC'] + df_nordeste['NU_NOTA_MT'] + df_nordeste['NU_NOTA_REDACAO']) / 5
df_sudeste['Media'] = (df_sudeste['NU_NOTA_CN'] + df_sudeste['NU_NOTA_CH'] + df_sudeste['NU_NOTA_LC'] + df_sudeste['NU_NOTA_MT'] + df_sudeste['NU_NOTA_REDACAO']) / 5
df_sul['Media'] = (df_sul['NU_NOTA_CN'] + df_sul['NU_NOTA_CH'] + df_sul['NU_NOTA_LC'] + df_sul['NU_NOTA_MT'] + df_sul['NU_NOTA_REDACAO']) / 5
df_centro_oeste['Media'] = (df_centro_oeste['NU_NOTA_CN'] + df_centro_oeste['NU_NOTA_CH'] + df_centro_oeste['NU_NOTA_LC'] + df_centro_oeste['NU_NOTA_MT'] + df_centro_oeste['NU_NOTA_REDACAO']) / 5
df_norte['Media'] = (df_norte['NU_NOTA_CN'] + df_norte['NU_NOTA_CH'] + df_norte['NU_NOTA_LC'] + df_norte['NU_NOTA_MT'] + df_norte['NU_NOTA_REDACAO']) / 5

df_nordeste = df_nordeste.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sudeste = df_sudeste.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sul = df_sul.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_centro_oeste = df_centro_oeste.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_norte = df_norte.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()



dateindex=df_nordeste['TP_DEPENDENCIA_ADM_ESC']

aa=dict(zip(df_nordeste['TP_DEPENDENCIA_ADM_ESC'],df_nordeste['Media']))
bb=dict(zip(df_norte['TP_DEPENDENCIA_ADM_ESC'],df_norte['Media']))
cc=dict(zip(df_centro_oeste['TP_DEPENDENCIA_ADM_ESC'],df_centro_oeste['Media']))
dd=dict(zip(df_sul['TP_DEPENDENCIA_ADM_ESC'],df_sul['Media']))
ee=dict(zip(df_sudeste['TP_DEPENDENCIA_ADM_ESC'],df_sudeste['Media']))


dfbar = pd.DataFrame({'Nordeste': aa, 'Norte': bb, 'Centro Oeste': cc,'Sul': dd, 'Sudeste': ee},index = dateindex)

dfbar.plot.bar(figsize=(20, 8))
plt.title("Média de notas do ENEM 2017 para cada tipo de colégio por região")
plt.legend(title="Região", fontsize = 13)
plt.xticks(rotation=0)
ax = plt.subplot(111)
ax.set_xlabel('')
ax.legend(loc = 'upper left', bbox_to_anchor=(0.77, 1.15),  shadow=True, ncol=2)
ax.set_ylabel('Nota',fontsize = 13)
plt.xticks(rotation=0)

plt.show()
"""