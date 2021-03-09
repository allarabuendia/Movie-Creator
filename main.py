#Importo librerías


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_rows", 500)
sns.set(color_codes=True)
import random
from plotly.offline import init_notebook_mode, iplot, plot
init_notebook_mode(connected=True)
from wordcloud import WordCloud
import squarify
from tkinter import *
from tkinter import ttk

#Importo dataset

data_imdb = pd.read_csv("imdb_top_1000.csv", error_bad_lines=False)


#Creo dataframe

df_imdb = pd.DataFrame(data_imdb)


#Cambio nombre de las columnas

df_imdb.columns = ['Link', 'Titulo', 'year', 'certificado', 'duracion', 'genero', 'rating', 'sinopsis',
                   'metascore', 'director', 'star1', 'star2', 'star3', 'star4','votos','recaudacion']



#Elimino columnas que no me sirven para el análisis

df_imdb.drop(columns = ['Link', 'sinopsis'], inplace = True)

#Reseteo el indice para seguir limpiando
df_imdb.reset_index()

#Tengo una fila con datos incorrectos en 'YEAR', aplico una máscara para saber su índice y eliminarla del dataframe.

mask = df_imdb['year'] == 'PG'
df_imdb[mask].index

df_imdb.drop([966], inplace = True)

#Elimino filas con Nans

df_imdb = df_imdb.dropna()

# Limpio la columna 'duración' y paso los datos a float.

limpiar= lambda x: x.replace("min", "").replace(" ", "")

df_imdb['duracion'] = df_imdb['duracion'].apply(limpiar)

df_imdb['duracion'] = df_imdb['duracion'].astype("float64")


# Limpio la columna 'recaudación' y paso los datos a float.

limpiar= lambda x: x.replace(",", "").replace(" ", "")

df_imdb['recaudacion'] = df_imdb['recaudacion'].apply(limpiar)

df_imdb['recaudacion'] = df_imdb['recaudacion'].astype("float64")

#Vemos que la columna 'genero' nos puede devolver hasta 2 subgeneros.

df_imdb['genero']

#Limpio los subgeneros y dejo la columna con un solo string como género principal.

separado = df_imdb["genero"].str.split(",", n=1, expand=True)

df_imdb["genero_ok"]= separado[0]

df_imdb.drop(columns =["genero"], inplace = True)


"""
Empezamos el análisis
"""

#sacamos los primeros datos

df_imdb.describe()

#Busco correlaciones entre los numéricos, parece que no hay nada especialmente relevante.

df_imdb.corr()

"""
#Correlación nº de votos / recuadación

x = df_imdb['votos']
y = df_imdb['recaudacion']

plt.plot(x, y, 'o')
plt.title('Correlación nº de votos / recaudación.')
plt.xlabel('nº de votos')
plt.ylabel('Recaudación')

plt.show()
"""

"""
No hay correlación, las películas que más recaudan no tienen más votos de los usuarios.
"""

"""
#Correlación rating / recaudación

x = df_imdb['rating']
y = df_imdb['recaudacion']

plt.plot(x, y,'o')
plt.title('Correlación rating/recaudación.')
plt.xlabel('rating')
plt.ylabel('recaudacion')

plt.show()
"""

"""
Que tengas un buen rating no significa que vayas a recaudar más, vemos que las mejores películas
no tienen una recaudación abundante.
"""

"""
#Correlación duración / recaudación

x = df_imdb['duracion']
y = df_imdb['recaudacion']

plt.plot(x, y,'o')
plt.title('Correlación duración/recaudación.')
plt.xlabel('duracion')
plt.ylabel('recaudacion')

plt.show()
"""

"""
La duración tampoco influye para hacer una película taquillera.
"""

"""
#Correlación nº votos / rating

x = df_imdb['votos']
y = df_imdb['rating']

plt.plot(x, y,'o')
plt.title('Correlación votos/rating.')
plt.xlabel('votos')
plt.ylabel('rating')

plt.show()
"""

"""
Esto es interesante, por varianza debería ser complicado tener un buen rating medio
cuanto más numero de votos tengas, sin embargo, hay cierta correlación positiva, lo cual
indica que más cantidad de usuarios votan a las primeras peliculas en el ranking. 
Es por cómo está estructurada la web??
"""

"""
#Veamos ahora como se distribuyen los votos de usuarios vs metascore

g = sns.JointGrid(data=df_imdb, x="rating", y="metascore")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)
"""

"""
Vemos que hay  muchas peliculas con muy buena nota en metascore donde los usuarios no la han valorado tambien.
Es interesante ver como en IMDB los usuarios son más exigentes que los críticos
"""

"""
#Recaudación

plt.figure(figsize=(20,10))
sns.distplot(df_imdb['recaudacion'], kde = False, color = 'g', bins=20)
plt.title('Recaudación en USD')

plt.figure(figsize=(20,7))
sns.boxplot(df_imdb['recaudacion'], color = 'g')
ax = sns.swarmplot(x=df_imdb['recaudacion'], data=df_imdb, color=".25")
"""

"""
La media de recaudacion es de 79 millones de USD. Al rededor de esta cifra en adelante,
estamos hablando de un blockbuster.
"""

"""
#En qué época se situan más películas?

plt.figure(figsize=(10,5))
sns.distplot(df_imdb['year'], kde = False, color = 'b', x=df_imdb['year'])
plt.title('Densidad de películas por año')

plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
ax = sns.countplot(y="year", data=df_imdb, palette="Set2", order=df_imdb['year'].value_counts().index[0:15])
plt.title('Películas por año')
"""

"""
Un crecimiento en el tiempo muy obvio, cada año se hace más cine, asique es lógico ver más peliculas en el ranking 
segun pasa el tiempo. Vemos una pequeña caida a inicios de los 2000.
"""

"""
#Duración de las películas
plt.figure(figsize=(12,8))
sns.kdeplot(data=df_imdb[df_imdb.columns[0:4]],
           shade = True)
plt.title('Duración de las películas')


plt.figure(figsize=(20,7))
sns.boxplot(df_imdb['duracion'], color = 'g')
plt.title('DURACIÓN')
"""

"""
Como vimos antes, la media de la duración de las peliculas es muy regular. Esta claro que está estudiado cuanto 
debe durar una pelicula para que sea un éxito. La media es 123min
"""

"""
#Cual es el género más habitual?

fig, ax = plt.subplots(figsize=(18,7))
fig = sns.countplot(x = df_imdb['genero_ok'], ax=ax, order = df_imdb['genero_ok'].value_counts().index)
plt.title('Géneros que más aparecen')
"""

"""
Los dramas son las películas que mas aparecen en el top 1000. Significa esto que es el género que más recauda?
"""

"""
#Recaudacion por los 3 generos más importantes

df_imdb2 = df_imdb[df_imdb['genero_ok'].isin(['Drama', 'Action', 'Comedy'])]
df_imdb2 = df_imdb2.groupby(['genero_ok', 'year']).sum()
df_imdb2.reset_index(inplace=True)
df_imdb2 = df_imdb2.sort_values(by='year', ascending=True)

df_imdb2 = df_imdb2.iloc[-60:]
plt.figure(figsize=(15,10))
sns.lineplot(data = df_imdb2,
            x ='year',
            y = 'recaudacion',
            hue = 'genero_ok',
            linewidth = 3,
            size_order= 10)

plt.title('RECAUDACIÓN DE LOS GÉNEROS QUE MÁS APARECEN')
"""

"""
De los géneros que más aparecen en la lista, vemos que la recaudación que predomina es del género Acción.
"""

"""
#Top géneros rating

df_imdb2 = df_imdb.groupby(['genero_ok', 'rating']).sum()
df_imdb2.reset_index(inplace=True)

plt.figure(figsize=(15,10))
sns.boxplot(data = df_imdb2[:50],
            x ='rating',
            y = 'genero_ok',
            hue = 'genero_ok',
            linewidth = 1)

plt.title('RATING TOP GÉNEROS')
"""

"""
Y en cuanto a rating, drama ni si quiera aparece, en el top 5. 
Esto significa que, en este género, hay muchas películas de puntuacion media en el ranking
pero no tienen la pegada suficiente para aparecer en el top 5. Sorprendente
"""


"""
A continuación haremos squarifys de géneros y casting
"""



#GÉNERO POR RECAUDACIÓN

data_gnr = df_imdb.groupby("genero_ok").sum()['recaudacion'].sort_values(ascending=False)[:10]

plt.figure(figsize=(15,10))

squarify.plot(sizes = data_gnr.values,
            label =  data_gnr.index,
             alpha = 0.7,
             )

plt.axis('off')

plt.title('TOP 10 RECAUDACIÓN POR GÉNERO')

#ACTOR PRINCIPAL1 POR RECAUDACIÓN

data_str1 = df_imdb.groupby("star1").sum()['recaudacion'].sort_values(ascending=False)[:10]

plt.figure(figsize=(15,10))

squarify.plot(sizes = data_str1.values,
             label =  data_str1.index,
             alpha = .7)

plt.axis('off')

plt.title('TOP 10 RECAUDACIÓN POR ACTOR/ACTRIZ PRINCIPAL')

#ACTOR PRINCIPAL2 POR RECAUDACIÓN

data_str2 = df_imdb.groupby("star2").sum()['recaudacion'].sort_values(ascending=False)[:10]

plt.figure(figsize=(15,10))

squarify.plot(sizes = data_str2.values,
             label =  data_str2.index,
             alpha = .7)

plt.axis('off')

plt.title('TOP 10 RECAUDACIÓN POR ACTOR/ACTRIZ PRINCIPAL II')

#ACTOR SECUNDARIO1 POR RECAUDACIÓN


data_str3 = df_imdb.groupby("star3").sum()['recaudacion'].sort_values(ascending=False)[:10]

plt.figure(figsize=(15,10))

squarify.plot(sizes = data_str3.values,
             label =  data_str3.index,
             alpha = .7)

plt.axis('off')

plt.title('TOP 10 RECAUDACIÓN POR ACTOR/ACTRIZ DE REPARTO')



#ACTOR SECUNDARIO2 POR RECAUDACIÓN


data_str4 = df_imdb.groupby("star4").sum()['recaudacion'].sort_values(ascending=False)[:10]

plt.figure(figsize=(15,10))

squarify.plot(sizes = data_str4.values,
             label =  data_str4.index,
             alpha = .7)

plt.axis('off')

plt.title('TOP 10 RECAUDACIÓN POR ACTOR/ACTRIZ DE REPARTO II')



#DIRECTOR POR RECAUDACIÓN



data_dir = df_imdb.groupby("director").sum()['recaudacion'].sort_values(ascending=False)[:10]

plt.figure(figsize=(15,10))

squarify.plot(sizes = data_dir.values,
             label =  data_dir.index,
             alpha = .7)

plt.axis('off')

plt.title('TOP 10 RECAUDACIÓN POR DIRECTOR')


#Tratamiento de texto


df_imdb["Titulo"].str.split(expand=True)
Titulo = df_imdb["Titulo"].str.split(expand=True)
Titulo.columns = ['1', '2','3','4','5','6','7','8','9','10','11','12','13']
df_imdb = pd.concat([df_imdb, Titulo], axis=1)

data_palabras = df_imdb.iloc[:, 14:27]

limpiar = lambda x: x.replace(".", None).replace("&", None) \
    .replace(" ", None).replace(":", None).replace("-", None) \
    .replace("Vol", None).replace(",", None).replace("V", None) \
    .replace("II", None).replace("X", None).replace("2", None) \
    .replace("Capharnaüm", None).replace("Shichinin", None).replace("Gisaengchung", None) \
    .replace("buono", None).replace("brutto", None).replace("cattivo", None) \
    .replace("no", None).replace("il", None).replace("nuovo", None) \
    .replace("La", None).replace("Le", None).replace("Das", None) \
    .replace("la", None).replace("Trois", None).replace("di", None) \
    .replace("les", None).replace("Serbuan", None).replace("de", None) \
    .replace("Der", None)

data_palabras = data_palabras.apply(limpiar)

palabras_1 = list(pd.value_counts(data_palabras['1']).index)
palabras_2 = list(pd.value_counts(data_palabras['2']).index)
palabras_3 = list(pd.value_counts(data_palabras['3']).index)
palabras_4 = list(pd.value_counts(data_palabras['4']).index)
palabras_5 = list(pd.value_counts(data_palabras['5']).index)
palabras_6 = list(pd.value_counts(data_palabras['6']).index)

metapalabras = palabras_1+palabras_2+palabras_3+palabras_4+palabras_5+palabras_6

def juntar_palabras(x, y):
    x.extend([element for element in y if element not in x])


    return x

juntar_palabras(palabras_1, palabras_2)
juntar_palabras(palabras_1, palabras_3)
juntar_palabras(palabras_1, palabras_4)
juntar_palabras(palabras_1, palabras_5)
juntar_palabras(palabras_1, palabras_6)

# DESPUÉS DEL TRATADO DE TEXTO GRAFICAMOS LAS PALABRAS QUE MÁS APARECEN


graficapalabras = metapalabras
plt.subplots(figsize=(8,8))
wordcloud = WordCloud(
                          background_color='white',
                          width=512,
                          height=384
                         ).generate(" ".join(metapalabras))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('graph.png')

plt.show()


df_imdb.to_csv('IMDB_clean.csv')