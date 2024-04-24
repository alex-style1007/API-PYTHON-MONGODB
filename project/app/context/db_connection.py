from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

class Session:
    session = None

    def __init__(self):
        url = URL.create(
            drivername='postgresql',
            username=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME']
        )
        self.session = self._create_session(url)

    def _create_session(self, url):
        engine = create_engine(url, poolclass=NullPool)
        metadata = MetaData()
        metadata.reflect(bind=engine, schema='testRepository')
        session = sessionmaker(bind=engine)
        return session()

    def __del__(self):
        if self.session:
            self.session.close()