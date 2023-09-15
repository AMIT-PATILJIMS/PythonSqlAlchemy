import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.sql.operators import ilike_op,like_op


url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="xyz@123",
    host="localhost",
    database="SQLAlchemyPractice",
)

engine = create_engine(url_object)

metadata_obj = db.MetaData()

db.Table(
    'Movies',                                        
    metadata_obj,                                    
    db.Column('id', db.Integer, primary_key=True),  
    db.Column('Movietitle', db.String(50)),                    
    db.Column('genre', db.String(15))         
)

        
MOVIES = metadata_obj.tables['Movies']

query  = db.select(MOVIES).filter(like_op(MOVIES.c.Movietitle, f'h%'))

#query  = db.select(MOVIES).filter(ilike_op(MOVIES.c.Movietitle, 'h%'))


result = engine.connect().execute(query).fetchall()

for record in result:
    print("\n", record)