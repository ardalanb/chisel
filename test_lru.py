import unittest
import LRUCache
class testTest(unittest.TestCase):

    def test_putAndGet(self):
        cache = LRUCache.LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        self.assertEqual(cache.get(1) , 1)

    def test_overLimit(self):
        cache = LRUCache.LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        cache.put(3,3)
        self.assertEqual(cache.get(1) , -1)

    def test_LastRecentUsed(self):
        cache = LRUCache.LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        cache.get(1)
        cache.put(3,3)
        self.assertEqual(cache.get(1) , 1)
        self.assertEqual(cache.get(2) , -1)

    def test_delete(self):
        cache = LRUCache.LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        cache.delete(2)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.delete(2),-1)

    def test_reset(self):
        cache = LRUCache.LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        cache.reset()
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.delete(2),-1)

    def test_overWrite(self):
        cache = LRUCache.LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        cache.put(2,3)
        self.assertEqual(cache.get(2) , 3)
        




if __name__ == "__main__":

    unittest.main()
