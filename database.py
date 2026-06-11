from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "mysql+pymysql://root:root@192.168.150.3:3306/learn_hibernate"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)