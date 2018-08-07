import unittest
import mysql.connector
import json

from unittest import TestCase
#from mock import patch, Mock

READER_CONFIG = json.loads(open('readers/database_connection.json').read()) # connection to database config  
READER_CONFIG1 = json.loads(open('readers/config_tests.json').read())   # config of config_tests.json


test_column = None

class Mysqldatabase(object):

    def __init__(self, host, port, user, password, dbname,
                 tablename=None, query=None, test_column=None):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.tablename = tablename

        self.query = query

        self.conn = None
        self.cursor = None

        self.test_column = test_column


        


    def validate_tests(self, test_column=None, tablename=None):
        """
        """
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.dbname
        )
        self.test_column = test_column
        
        self.query = "select " + "count( " + test_column +  ") , count(distinct "+ test_column + ") from " + tablename + " "


        self.cursor = self.conn.cursor()

        self.cursor.execute(self.query)

        return self.cursor



class MysqldatabaseTest(unittest.TestCase):

    def setUp(self):

        self.data = Mysqldatabase(**READER_CONFIG['green'])

    def test_validate_tests(self):
        
        expected_results = [(5,5)]       # count(distinct id) and count(id ) from table = bharath 
 
        var = self.data.validate_tests(**READER_CONFIG1['column_unique_tests'])
        
        results = var.fetchall()

        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()

