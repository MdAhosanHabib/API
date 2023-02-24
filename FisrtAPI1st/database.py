from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://etl_test:etl_test@ahosan1/etl_test",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
