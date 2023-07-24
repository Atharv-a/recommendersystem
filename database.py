import psycopg2
import pickle
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()
connection=psycopg2.connect(host=os.getenv('hostname'),
                            database=os.getenv('database'),
                            user=os.getenv('user'),
                            password=os.getenv('password'),
                            cursor_factory=RealDictCursor)


cursor=connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS movie_data(
                        id  INTEGER NOT NULL PRIMARY KEY,
                        dis REAL[] NOT NULL
)''') 

dis=pickle.load(open(r'C:\Users\Ayush\projects\recommendersystem\dis.pkl','rb'))

for i in range(len(dis)):
    cursor.execute("INSERT INTO movie_data(id,dis) VALUES(%s,%s)",(i,list(dis[i])))

connection.commit()
cursor.close()
connection.close()

