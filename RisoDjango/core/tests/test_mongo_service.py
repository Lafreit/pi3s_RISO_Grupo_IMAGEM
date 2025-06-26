import unittest
from core import service

class MongoServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.collection = "mongoTest"
        service.mongoDelete(self.collection, {})

    def tearDown(self):
        service.mongoDelete(self.collection, {})

    def test_insert_and_findOne_nome(self):
        doc = {"nome": "Teste"}
        inserted_id = service.mongoInsert(self.collection, doc)
        found = service.mongoFindOne(self.collection, {"_id": inserted_id})
        self.assertIsNotNone(found)
        self.assertEqual(found["nome"], "Teste")

    def test_find_varios_documentos(self):
        doc1 = {"nome": "Teste"}
        doc2 = {"nome": "Teste2"}
        service.mongoInsert(self.collection, doc1)
        service.mongoInsert(self.collection, doc2)
        results = list(service.mongoFind(self.collection, {}))
        nomes = [r["nome"] for r in results]
        self.assertIn("Teste", nomes)
        self.assertIn("Teste2", nomes)

    def test_update_nome(self):
        doc = {"nome": "Teste"}
        inserted_id = service.mongoInsert(self.collection, doc)
        count = service.mongoUpdate(self.collection, {"_id": inserted_id}, {"$set": {"nome": "TesteUpdate", "descricao": "Depois do update"}})
        self.assertEqual(count, 1)
        updated = service.mongoFindOne(self.collection, {"_id": inserted_id})
        self.assertEqual(updated["nome"], "TesteUpdate")

    def test_delete_documento(self):
        doc = {"nome": "TesteDelete", "descricao": "Pra deletar"}
        inserted_id = service.mongoInsert(self.collection, doc)
        count = service.mongoDelete(self.collection, {"_id": inserted_id})
        self.assertEqual(count, 1)
        found = service.mongoFindOne(self.collection, {"_id": inserted_id})
        self.assertIsNone(found)

    def test_findAll(self):
        service.mongoInsert(self.collection, {"nome": "teste"})
        service.mongoInsert(self.collection, {"nome": "teste2"})
        results = list(service.mongoFindAll(self.collection))
        nomes = []
        for r in results:
            nomes.append(r.get("nome"))
        self.assertIn("teste", nomes)
        self.assertIn("teste2", nomes)

    def test_count_nome(self):
        service.mongoInsert(self.collection, {"nome": "bla"})
        service.mongoInsert(self.collection, {"nome": "bla"})
        count = service.mongoCount(self.collection, {"nome": "bla"})
        self.assertEqual(count, 2)

    def test_aggregate_group_nome(self):
        service.mongoInsert(self.collection, {"tipo": "a"})
        service.mongoInsert(self.collection, {"tipo": "b"})
        service.mongoInsert(self.collection, {"tipo": "a"})
        pipeline = [{"$group": {"_id": "$tipo", "total": {"$sum": 1}}}]
        results = list(service.mongoAggregate(self.collection, pipeline))
        tipos = {r["_id"]: r["total"] for r in results}
        self.assertEqual(tipos["a"], 2)
        self.assertEqual(tipos["b"], 1)

    def test_distinct_nome(self):
        service.mongoInsert(self.collection, {"categoria": "a"})
        service.mongoInsert(self.collection, {"categoria": "b"})
        service.mongoInsert(self.collection, {"categoria": "c"})
        distinct = service.mongoDistinct(self.collection, "categoria")
        self.assertIn("a", distinct)
        self.assertIn("b", distinct)

if __name__ == "__main__":
    unittest.main()
