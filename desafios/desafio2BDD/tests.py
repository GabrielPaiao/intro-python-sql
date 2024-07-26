import unittest
from init_db import get_connection
from add import add_people
from delete import delete_people
from add1 import insert_one

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.cursor.execute("TRUNCATE TABLE pessoas")  # Limpa a tabela para testes

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_add_people(self):
        add_people()
        self.cursor.execute("SELECT COUNT(*) FROM pessoas")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 100)  # 100 inseridos

    def test_delete_people(self):
        add_people()
        delete_people()
        self.cursor.execute("SELECT COUNT(*) FROM pessoas")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 90)  # 10 excluídos

    def test_insert_one(self):
        add_people()
        delete_people()
        insert_one()
        self.cursor.execute("SELECT COUNT(*) FROM pessoas")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 91)  # 90 restantes mais 1 inserido

if __name__ == "__main__":
    unittest.main()