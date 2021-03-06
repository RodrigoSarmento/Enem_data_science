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

df_2013 = pd.read_csv('MICRODADOS_ENEM_2013.csv', parse_dates=True,encoding='latin-1',sep=';',nrows=CHUNKSIZE)
df_2013 = df_2013[['ID_DEPENDENCIA_ADM_ESC','NOTA_CN','NOTA_CH','NOTA_LC','NOTA_MT','NU_NOTA_REDACAO','UF_ESC']]
df_2013.dropna()

df_2015 = pd.read_csv('MICRODADOS_ENEM_2015.csv', parse_dates=True,encoding='latin-1',sep=',',nrows=CHUNKSIZE)
df_2015 = df_2015[['TP_DEPENDENCIA_ADM_ESC','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO','SG_UF_ESC']]
df_2015.dropna()

df_2017 = pd.read_csv('MICRODADOS_ENEM_2017.csv', parse_dates=True,encoding='latin-1',sep=';',nrows=CHUNKSIZE)
df_2017 = df_2017[['TP_DEPENDENCIA_ADM_ESC','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO','SG_UF_ESC']]
df_2017.dropna()


df_nordeste_2013 = df_2013[df_2013.UF_ESC.isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])]
df_sudeste_2013 = df_2013[df_2013.UF_ESC.isin(['MG','ES','RJ','SP'])]
df_sul_2013 = df_2013[df_2013.UF_ESC.isin(['PR','SC','RS'])]
df_centro_oeste_2013 = df_2013[df_2013.UF_ESC.isin(['MT','MS','GO','DF'])]
df_norte_2013 = df_2013[df_2013.UF_ESC.isin(['AC','RO','AM','RR','PA','AP','TO'])]

df_nordeste_2015 = df_2015[df_2015.SG_UF_ESC.isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])]
df_sudeste_2015 = df_2015[df_2015.SG_UF_ESC.isin(['MG','ES','RJ','SP'])]
df_sul_2015 = df_2015[df_2015.SG_UF_ESC.isin(['PR','SC','RS'])]
df_centro_oeste_2015 = df_2015[df_2015.SG_UF_ESC.isin(['MT','MS','GO','DF'])]
df_norte_2015 = df_2015[df_2015.SG_UF_ESC.isin(['AC','RO','AM','RR','PA','AP','TO'])]

df_nordeste_2017 = df_2017[df_2017.SG_UF_ESC.isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])]
df_sudeste_2017 = df_2017[df_2017.SG_UF_ESC.isin(['MG','ES','RJ','SP'])]
df_sul_2017 = df_2017[df_2017.SG_UF_ESC.isin(['PR','SC','RS'])]
df_centro_oeste_2017 = df_2017[df_2017.SG_UF_ESC.isin(['MT','MS','GO','DF'])]
df_norte_2017 = df_2017[df_2017.SG_UF_ESC.isin(['AC','RO','AM','RR','PA','AP','TO'])]


df_nordeste_2013['ID_DEPENDENCIA_ADM_ESC'] = df_nordeste_2013['ID_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sudeste_2013['ID_DEPENDENCIA_ADM_ESC'] = df_sudeste_2013['ID_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sul_2013['ID_DEPENDENCIA_ADM_ESC'] = df_sul_2013['ID_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_centro_oeste_2013['ID_DEPENDENCIA_ADM_ESC'] = df_centro_oeste_2013['ID_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_norte_2013['ID_DEPENDENCIA_ADM_ESC'] = df_norte_2013['ID_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})

df_nordeste_2013['Media'] = (df_nordeste_2013['NOTA_CN'] + df_nordeste_2013['NOTA_CH'] + df_nordeste_2013['NOTA_LC'] + df_nordeste_2013['NOTA_MT'] + df_nordeste_2013['NU_NOTA_REDACAO']) / 5
df_sudeste_2013['Media'] = (df_sudeste_2013['NOTA_CN'] + df_sudeste_2013['NOTA_CH'] + df_sudeste_2013['NOTA_LC'] + df_sudeste_2013['NOTA_MT'] + df_sudeste_2013['NU_NOTA_REDACAO']) / 5
df_sul_2013['Media'] = (df_sul_2013['NOTA_CN'] + df_sul_2013['NOTA_CH'] + df_sul_2013['NOTA_LC'] + df_sul_2013['NOTA_MT'] + df_sul_2013['NU_NOTA_REDACAO']) / 5
df_centro_oeste_2013['Media'] = (df_centro_oeste_2013['NOTA_CN'] + df_centro_oeste_2013['NOTA_CH'] + df_centro_oeste_2013['NOTA_LC'] + df_centro_oeste_2013['NOTA_MT'] + df_centro_oeste_2013['NU_NOTA_REDACAO']) / 5
df_norte_2013['Media'] = (df_norte_2013['NOTA_CN'] + df_norte_2013['NOTA_CH'] + df_norte_2013['NOTA_LC'] + df_norte_2013['NOTA_MT'] + df_norte_2013['NU_NOTA_REDACAO']) / 5

df_nordeste_2013 = df_nordeste_2013.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sudeste_2013 = df_sudeste_2013.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sul_2013 = df_sul_2013.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_centro_oeste_2013 = df_centro_oeste_2013.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_norte_2013 = df_norte_2013.groupby('ID_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()

##########################################################################################


df_nordeste_2015['TP_DEPENDENCIA_ADM_ESC'] = df_nordeste_2015['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sudeste_2015['TP_DEPENDENCIA_ADM_ESC'] = df_sudeste_2015['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sul_2015['TP_DEPENDENCIA_ADM_ESC'] = df_sul_2015['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_centro_oeste_2015['TP_DEPENDENCIA_ADM_ESC'] = df_centro_oeste_2015['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_norte_2015['TP_DEPENDENCIA_ADM_ESC'] = df_norte_2015['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})

df_nordeste_2015['Media'] = (df_nordeste_2015['NU_NOTA_CN'] + df_nordeste_2015['NU_NOTA_CH'] + df_nordeste_2015['NU_NOTA_LC'] + df_nordeste_2015['NU_NOTA_MT'] + df_nordeste_2015['NU_NOTA_REDACAO']) / 5
df_sudeste_2015['Media'] = (df_sudeste_2015['NU_NOTA_CN'] + df_sudeste_2015['NU_NOTA_CH'] + df_sudeste_2015['NU_NOTA_LC'] + df_sudeste_2015['NU_NOTA_MT'] + df_sudeste_2015['NU_NOTA_REDACAO']) / 5
df_sul_2015['Media'] = (df_sul_2015['NU_NOTA_CN'] + df_sul_2015['NU_NOTA_CH'] + df_sul_2015['NU_NOTA_LC'] + df_sul_2015['NU_NOTA_MT'] + df_sul_2015['NU_NOTA_REDACAO']) / 5
df_centro_oeste_2015['Media'] = (df_centro_oeste_2015['NU_NOTA_CN'] + df_centro_oeste_2015['NU_NOTA_CH'] + df_centro_oeste_2015['NU_NOTA_LC'] + df_centro_oeste_2015['NU_NOTA_MT'] + df_centro_oeste_2015['NU_NOTA_REDACAO']) / 5
df_norte_2015['Media'] = (df_norte_2015['NU_NOTA_CN'] + df_norte_2015['NU_NOTA_CH'] + df_norte_2015['NU_NOTA_LC'] + df_norte_2015['NU_NOTA_MT'] + df_norte_2015['NU_NOTA_REDACAO']) / 5

df_nordeste_2015 = df_nordeste_2015.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sudeste_2015 = df_sudeste_2015.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sul_2015 = df_sul_2015.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_centro_oeste_2015 = df_centro_oeste_2015.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_norte_2015 = df_norte_2015.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()

####################################################################################################

df_nordeste_2017['TP_DEPENDENCIA_ADM_ESC'] = df_nordeste_2017['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sudeste_2017['TP_DEPENDENCIA_ADM_ESC'] = df_sudeste_2017['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_sul_2017['TP_DEPENDENCIA_ADM_ESC'] = df_sul_2017['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_centro_oeste_2017['TP_DEPENDENCIA_ADM_ESC'] = df_centro_oeste_2017['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})
df_norte_2017['TP_DEPENDENCIA_ADM_ESC'] = df_norte_2017['TP_DEPENDENCIA_ADM_ESC'].map({1:'Federal',2:'Estadual',3:'Municipal',4:'Privada'})

df_nordeste_2017['Media'] = (df_nordeste_2017['NU_NOTA_CN'] + df_nordeste_2017['NU_NOTA_CH'] + df_nordeste_2017['NU_NOTA_LC'] + df_nordeste_2017['NU_NOTA_MT'] + df_nordeste_2017['NU_NOTA_REDACAO']) / 5
df_sudeste_2017['Media'] = (df_sudeste_2017['NU_NOTA_CN'] + df_sudeste_2017['NU_NOTA_CH'] + df_sudeste_2017['NU_NOTA_LC'] + df_sudeste_2017['NU_NOTA_MT'] + df_sudeste_2017['NU_NOTA_REDACAO']) / 5
df_sul_2017['Media'] = (df_sul_2017['NU_NOTA_CN'] + df_sul_2017['NU_NOTA_CH'] + df_sul_2017['NU_NOTA_LC'] + df_sul_2017['NU_NOTA_MT'] + df_sul_2017['NU_NOTA_REDACAO']) / 5
df_centro_oeste_2017['Media'] = (df_centro_oeste_2017['NU_NOTA_CN'] + df_centro_oeste_2017['NU_NOTA_CH'] + df_centro_oeste_2017['NU_NOTA_LC'] + df_centro_oeste_2017['NU_NOTA_MT'] + df_centro_oeste_2017['NU_NOTA_REDACAO']) / 5
df_norte_2017['Media'] = (df_norte_2017['NU_NOTA_CN'] + df_norte_2017['NU_NOTA_CH'] + df_norte_2017['NU_NOTA_LC'] + df_norte_2017['NU_NOTA_MT'] + df_norte_2017['NU_NOTA_REDACAO']) / 5

df_nordeste_2017 = df_nordeste_2017.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sudeste_2017 = df_sudeste_2017.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_sul_2017 = df_sul_2017.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_centro_oeste_2017 = df_centro_oeste_2017.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()
df_norte_2017 = df_norte_2017.groupby('TP_DEPENDENCIA_ADM_ESC', as_index = False)[['Media']].mean()

df_nordeste = pd.DataFrame({'Escola': ['Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada'],
	'Ano':[2013,2013,2013,2013,2015,2015,2015,2015,2017,2017,2017,2017]})
df_nordeste.set_index('Escola')
df_nordeste['Media'] = df_nordeste_2013['Media']

df_nordeste.iloc[4:8, 2] = df_nordeste_2015['Media'].tolist()
df_nordeste.iloc[8:12, 2] = df_nordeste_2017['Media'].tolist()
sns.set_style('darkgrid')

sns.factorplot(data = df_nordeste,
	x = 'Ano',
	y = 'Media',
	hue = 'Escola')

df_sul = pd.DataFrame({'Escola': ['Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada'],
	'Ano':[2013,2013,2013,2013,2015,2015,2015,2015,2017,2017,2017,2017]})
df_sul.set_index('Escola')
df_sul['Media'] = df_sul_2013['Media']

df_sul.iloc[4:8, 2] = df_sul_2015['Media'].tolist()
df_sul.iloc[8:12, 2] = df_sul_2017['Media'].tolist()

sns.factorplot(data = df_sul,
	x = 'Ano',
	y = 'Media',
	hue = 'Escola')

df_sudeste = pd.DataFrame({'Escola': ['Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada'],
	'Ano':[2013,2013,2013,2013,2015,2015,2015,2015,2017,2017,2017,2017]})
df_sudeste.set_index('Escola')
df_sudeste['Media'] = df_sudeste_2013['Media']

df_sudeste.iloc[4:8, 2] = df_sudeste_2015['Media'].tolist()
df_sudeste.iloc[8:12, 2] = df_sudeste_2017['Media'].tolist()

sns.factorplot(data = df_sudeste,
	x = 'Ano',
	y = 'Media',
	hue = 'Escola')

df_norte = pd.DataFrame({'Escola': ['Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada'],
	'Ano':[2013,2013,2013,2013,2015,2015,2015,2015,2017,2017,2017,2017]})
df_norte.set_index('Escola')
df_norte['Media'] = df_norte_2013['Media']

df_norte.iloc[4:8, 2] = df_norte_2015['Media'].tolist()
df_norte.iloc[8:12, 2] = df_norte_2017['Media'].tolist()

sns.factorplot(data = df_norte,
	x = 'Ano',
	y = 'Media',
	hue = 'Escola')

df_centro_oeste = pd.DataFrame({'Escola': ['Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada','Estadual','Federal','Municipal','Privada'],
	'Ano':[2013,2013,2013,2013,2015,2015,2015,2015,2017,2017,2017,2017]})
df_centro_oeste.set_index('Escola')
df_centro_oeste['Media'] = df_centro_oeste_2013['Media']

df_centro_oeste.iloc[4:8, 2] = df_centro_oeste_2015['Media'].tolist()
df_centro_oeste.iloc[8:12, 2] = df_centro_oeste_2017['Media'].tolist()

sns.factorplot(data = df_centro_oeste,
	x = 'Ano',
	y = 'Media',
	hue = 'Escola')




plt.show()







