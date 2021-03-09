import streamlit as st
from main import palabras_1
import random
from main import df_imdb



titulo = []
n = random.randint(2,6)

for i in range(n):
    i = random.choice(palabras_1)
    titulo.append(i)

titulo_str = " ".join(titulo)

#LISTAS TOP10 GÉNEROS, ACTORES Y DIRECTORES

top_generos = ['Action', 'Drama', 'Animation', 'Adventure', 'Biography',
                   'Comedy', 'Crime', 'Horror', 'Family', 'Mystery']
top_star1 = ['Tom Hanks', 'Joe Russo', 'Leonardo DiCaprio', 'Daniel Radcliffe', 'Christian Bale',
                 'Robert Downey Jr.', 'Elijah Wood', 'Daisy Ridley', 'Mark Hamill', 'Craig T. Nelson']
top_star2 = ['Emma Watson', 'Robert Downey Jr.', 'Chirs Evans', 'Ian McKellen', 'Zoe Saldana',
                 'Tim Allen', 'Jhon Boyega', 'Harrison Ford', 'Kate Winslet', 'Tom Hardy']
top_star3 = ['Rupert Grint', 'Carrie Fiesher', 'Sigourney Weaver', 'Oscar Isaac', 'Chris Evans',
                 'Scarlett Johanson', 'Chris Hemswort', 'Billy Zane', 'Orlando Bloom', 'Sarah Vowell']
top_star4 = ['Mark Ruffalo', 'Domhnall Gleeson', 'Michelle Rodriguez', 'Michael Caine',
                 'Orlando Bloom', 'Michael Gambon', 'Scarlett Johansson', 'Kathy Bates', 'Jeremy Renner', 'Huck Milner']
top_dir = ['Steven Spielberg', 'Anthony Russo', 'Christopher Nolan', 'James Cameron', 'Peter Jackson',
               'J.J. Abrams', 'Brad Bird', 'Robert Zemeckis', 'David Yates', 'Pete Docter']


#CREAR CRÉDITOS

import random

for i in range(1):
    genero = random.choice(top_generos)


for i in range(1):
    star1 = random.choice(top_star1)


for i in range(1):
     star2 = random.choice(top_star2)


for i in range(1):
    star3 = random.choice(top_star3)


for i in range(1):
     star4 = random.choice(top_star4)


for i in range(1):
     director = random.choice(top_dir)


st.set_page_config(page_title='MOVIE CREATOR', page_icon = ':cinema:', layout = 'wide',)

menu = st.sidebar.selectbox('Seleccionar menu:', ('MOVIE CREATOR', 'DATOS POR GÉNERO'))

if menu == 'MOVIE CREATOR':

    st.markdown('<style>body{background-color: grey ;}</style>',unsafe_allow_html=True)

    st.sidebar.markdown("<h1 style='text-align: center; color: black; '> MOVIE CREATOR </h1>", unsafe_allow_html= True)

    st.sidebar.write('')
    st.sidebar.write('')

    st.sidebar.button('Crea tu película')

    st.markdown("<h1 style='text-align: center; color: white; '> GÉNERO </h1>", unsafe_allow_html= True)

    st.markdown("<h2 style='text-align: center; color: white; '>" + genero + "</h1>", unsafe_allow_html= True)

    st.markdown("<h1 style='text-align: center; color: white; '> TÍTULO </h1>", unsafe_allow_html= True)

    st.markdown("<h2 style='text-align: center; color: white; '>" + titulo_str + "</h1>", unsafe_allow_html= True)

    st.markdown("<h1 style='text-align: center; color: white; '> PROTAGONIZADA POR </h1>", unsafe_allow_html= True)

    st.markdown("<h2 style='text-align: center; color: white; '>" + star1 + " & " + star2 + "</h1>", unsafe_allow_html= True)

    st.markdown("<h1 style='text-align: center; color: white; '> CO PROTAGONIZADA POR </h1>", unsafe_allow_html= True)

    st.markdown("<h2 style='text-align: center; color: white; '>" + star3 + " & " + star4 + "</h1>", unsafe_allow_html= True)

    st.markdown("<h1 style='text-align: center; color: white; '> DIRIGIDA POR </h1>", unsafe_allow_html= True)

    st.markdown("<h2 style='text-align: center; color: white; '>" + director + "</h1>", unsafe_allow_html= True)

elif menu == 'DATOS POR GÉNERO':

    st.write('Recaudación media por género')

    recaudacion_genero = df_imdb.groupby('genero_ok')['recaudacion'].mean()

    st.bar_chart(recaudacion_genero)

    st.write('Puntuación media por género')

    puntuacion_genero = df_imdb.groupby('genero_ok')['rating'].mean()

    st.bar_chart(puntuacion_genero)

    st.write('Media metascore por género')

    metascore_genero = df_imdb.groupby('genero_ok')['metascore'].mean()

    st.bar_chart(metascore_genero)

    st.write('Media duración por género')

    duracion_genero = df_imdb.groupby('genero_ok')['duracion'].mean()

    st.bar_chart(duracion_genero)





