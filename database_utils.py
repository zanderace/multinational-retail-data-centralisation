import yaml
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import pandas as pd

class DatabaseConnector:
    def __init__(self, file):
        self.file = file


    def read_db_creds(self):
        with open(self.file, 'r') as f:
            creds_dict = yaml.load(f, Loader=yaml.FullLoader)
        return creds_dict 

    def init_db_engine(self):
        db_credentials = self.read_db_creds()
        RDS_USER = db_credentials["RDS_USER"]
        RDS_PASSWORD = db_credentials["RDS_PASSWORD"]
        RDS_HOST = db_credentials["RDS_HOST"]
        RDS_PORT = db_credentials["RDS_PORT"]
        RDS_DATABASE = db_credentials["RDS_DATABASE"]

        connection_string = f"postgresql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}"

        engine = create_engine(connection_string)

    #def list_db_tables(self, engine):


DatabaseConnector('db_creds.yaml').init_db_engine()