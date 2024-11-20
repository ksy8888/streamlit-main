import psycopg2
import streamlit as st
from driver.preprocessor import preprocess

class call_db:
    def __init__(self, database ,host, dbname, id, pwd, port):
        self.fetch = None
        if database == 'Postgresql':
            self.__connection = psycopg2.connect(host=host
                                              , dbname=dbname
                                              , user=id
                                              , password=pwd
                                              , port=port)
            self.cursor = self.__connection.cursor()
            st.session_state['database_connection'] = True

    def __call__(self,sql):
        self.cursor.execute(sql)
        self.fetch = self.cursor.fetchall()
        return self.fetch

    def is_connect(self):
        return st.success("DB connect"), st.rerun()
