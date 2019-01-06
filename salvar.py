import pandas as pd


df_2013 = pd.read_csv('MICRODADOS_ENEM_2013.csv', parse_dates=True,encoding='latin-1',sep=';',nrows=1000000)
df_2013 = df_2013[['ID_DEPENDENCIA_ADM_ESC','NOTA_CN','NOTA_CH','NOTA_LC','NOTA_MT','NU_NOTA_REDACAO','UF_ESC']]
df_2013.dropna()

df_2013.to_csv('ENEM_2013.csv',index=False)