import streamlit as st
import pandas as pd
import pickle
import requests
from dotenv import load_dotenv
import psycopg2,os
from psycopg2.extras import RealDictCursor

load_dotenv()

connection=psycopg2.connect(host=os.getenv('hostname'),
                            database=os.getenv('database'),
                            user=os.getenv('user'),
                            password=os.getenv('password'),
                            cursor_factory=RealDictCursor)

cursor=connection.cursor()

def recommend(movie):
    index=int(movies[movies['title']==movie].index[0])
    cursor.execute('SELECT dis FROM movie_data Where id=%s',(index,))
    distances=cursor.fetchone()['dis']
    m_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_m=[]
    recommend_m_p=[]
    for i in m_list:

        recommend_m.append(movies.iloc[i[0]].title)
        recommend_m_p.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommend_m,recommend_m_p


def fetch_poster(m_i):
    data=requests.get(f'https://api.themoviedb.org/3/movie/{m_i}?api_key=325afcbd5a670e1d1fdc99f18580f564&language=en-US')
    data=data.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

st.set_page_config(layout="wide")

movies_list=pickle.load(open('movies.pkl','rb'))
movies= pd.DataFrame(movies_list)

movies_l=movies['title'].values
st.title('Movie Recommender System') 

selected_name = st.selectbox('Enter a movie',movies_l)

if st.button('Recommend'):
    names,posters=recommend(selected_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
    
