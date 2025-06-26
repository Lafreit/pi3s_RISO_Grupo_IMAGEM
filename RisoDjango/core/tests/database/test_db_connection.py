import unittest
import os
from core.services.db_connection import MongoDBConnection

class MongoDBConnectionTestCase(unittest.TestCase):
    def setUp(self):
        self.testdb = "testMongo"
        self.conn = MongoDBConnection(db_name=self.testdb)
        self.db = self.conn.get_db()
        self.db[self.testdb].delete_many({})

    def tearDown(self):
        self.db[self.testdb].delete_many({})

    def test_init_default(self):
        conn = MongoDBConnection()
        self.assertEqual(conn.db.name, "riso")

    def test_init_custom_db(self):
        self.assertEqual(self.conn.db.name, self.testdb)

    def test_get_db(self):
        db = self.conn.get_db()
        self.assertEqual(db.name, self.testdb)

if __name__ == "__main__":
    unittest.main()
