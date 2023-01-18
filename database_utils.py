import yaml
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import pandas as pd

class DatabaseConnector():

    @classmethod
    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as f:
            creds_dict = yaml.load(f, Loader=yaml.FullLoader)
        return creds_dict 

    @classmethod
    def init_db_engine(self):
        db_credentials = self.read_db_creds()
        RDS_USER = db_credentials["RDS_USER"]
        RDS_PASSWORD = db_credentials["RDS_PASSWORD"]
        RDS_HOST = db_credentials["RDS_HOST"]
        RDS_PORT = db_credentials["RDS_PORT"]
        RDS_DATABASE = db_credentials["RDS_DATABASE"]

        connection_string = f"postgresql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}"

        engine = create_engine(connection_string)

        return engine

    @classmethod
    def list_db_tables(self):
        tables = self.init_db_engine().table_names()
        return tables

