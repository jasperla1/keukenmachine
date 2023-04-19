import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

#render
DATABASE_URL = "postgresql://myuser:Y5kPvilP6mjggpGVLVh4SxxOCQHu6LIn@dpg-cgvs259euhlhlbhj4efg-a.oregon-postgres.render.com/keukenmachines_database"

#local
#DATABASE_URL = "postgresql://myuser:password@localhost/keukenmachines_database"

engine = sql.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()

