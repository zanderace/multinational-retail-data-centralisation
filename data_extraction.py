import database_utils as dbu
import pandas as pd

class DataExtractor():
    
    @classmethod
    def read_dbs_table(self):
        dbs_dic = {}
        for item in dbu.DatabaseConnector.list_db_tables():    
            dbs_dic[item] = pd.read_sql_table(item, dbu.DatabaseConnector.init_db_engine())

        return(dbs_dic)
        
DataExtractor.read_dbs_table()