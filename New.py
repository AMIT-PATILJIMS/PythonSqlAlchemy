import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.engine import result
from sqlalchemy.sql.operators import ilike_op,like_op


metadata_obj = db.MetaData()

url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="Laddu@123",
    host="localhost",
    database="SQLAlchemyPractice",
)

engine = create_engine(url_object)


profile = db.Table(
    'Movies',                                        
    metadata_obj,                                    
    db.Column('id', db.Integer, primary_key=True),  
    db.Column('Movietitle', db.String(50)),                    
    db.Column('genre', db.String(15))         
)
        
metadata_obj.create_all(engine)

MOVIES = metadata_obj.tables['Movies']

x = [
    (1,'Harry Potter and the Philosophers Stone','genre'),
    (2,'Harry Potter and the Chamber of Secrets','genre'),
    (3,'harry Potter and the Prisoner of Azkaban','genre'),
    (4,'Harry Potter and the Goblet of Fire','genre'),
    (5,'harry Potter and the Order of the Phoenix','genre'),
    (6,'harry Potter and the Half-Blood Prince','genre'),
    (7,'Harry Potter and the Deathly Hallows','genre')
]

#statement = db.insert(MOVIES).values([{'id': ID, 'Movietitle' : Movietitle, 'genre' : genre} for ID, Movietitle, genre in x])


query  = db.select(MOVIES).where(ilike_op(MOVIES.c.Movietitle, f'h%'))

result = engine.connect().execute(query).fetchall()

for record in result:
    print("\n", record)




