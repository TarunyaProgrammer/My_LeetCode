class MyHashMap:

    def __init__(self):
        self.size = 10007
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hv = self._hash(key)
        for item in self.table[hv]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hv].append([key, value])

    def get(self, key: int) -> int:
        hv = self._hash(key)
        for item in self.table[hv]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hv = self._hash(key)
        for i, item in enumerate(self.table[hv]):
            if item[0] == key:
                del self.table[hv][i]
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)