import unittest
import importlib


class TestUMMiniMart(unittest.TestCase):
    def setUp(self):
        # reload module to start fresh for each test
        self.module = importlib.reload(__import__('ummart'))
        # reset inventory to a known state
        self.module.inventory.clear()
        self.module.inventory.extend([
            {"code": "P001", "name": "Notebook", "price": 25.0, "stock": 10},
            {"code": "P002", "name": "Ballpen", "price": 10.0, "stock": 20},
        ])
        self.module.transactions.clear()

    def test_add_and_find(self):
        prod = self.module.add_product('P003', 'Eraser', 5.5, 4)
        self.assertEqual(prod['code'], 'P003')
        # ensure product exists in inventory
        exists = any(p['code'] == 'P003' for p in self.module.inventory)
        self.assertTrue(exists)

    def test_update_stock(self):
        self.module.update_stock('P001', 5)
        p = next(p for p in self.module.inventory if p['code'] == 'P001')
        self.assertEqual(p['stock'], 15)

    def test_purchase(self):
        txn = self.module.purchase_product('P002', 2)
        self.assertEqual(txn['qty'], 2)
        p = next(p for p in self.module.inventory if p['code'] == 'P002')
        self.assertEqual(p['stock'], 18)

    def test_search(self):
        res = self.module.search_products('note')
        self.assertTrue(len(res) >= 1)

    def test_delete(self):
        removed = self.module.delete_product('P001')
        self.assertEqual(removed['code'], 'P001')


if __name__ == '__main__':
    unittest.main()
