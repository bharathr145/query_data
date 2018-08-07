import unittest
import mysql.connector
import json

from unittest import TestCase
#from mock import patch, Mock

READER_CONFIG = json.loads(open('readers/database_connection.json').read())

class Mysqldatabase(object):

    def __init__(self, host, port, user, password, dbname,
                 tablename=None, query=None):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.tablename = tablename

        self.query = query

        self.conn = None
        self.cursor = None


    def validate_tests(self, tests_config=None, table_config=None):
        """
        """
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.dbname
        )

        #self.query = "SELECT * FROM bharath"
        self.cursor = self.conn.cursor()

        self.cursor.execute(self.query)

        return self.cursor



class MysqldatabaseTest(unittest.TestCase):

    def setUp(self):

        self.data = Mysqldatabase(**READER_CONFIG['green'])

    def test_validate_tests(self):
        
        expected_results = [(1, u'cs'), (2, u'eee'), (3, u'ece'), (4, u'civil'), (5, u'bpharma')]

        var = self.data.validate_tests()
        
        results = var.fetchall()

        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()

