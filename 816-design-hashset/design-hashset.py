# class MyHashSet:

#     # def __init__(self):
#     #     self.hash_list = []

#     # def add(self, key: int) -> None:
#     #     if key not in self.hash_list:
#     #         self.hash_list.append(key)

#     # def remove(self, key: int) -> None:
#     #     if key in self.hash_list:
#     #         self.hash_list.remove(key)

#     # def contains(self, key: int) -> bool:
#     #     return key in self.hash_list

# #APP 2
#     def __init__(self):
#         self.hash_list = [0]*(10**6+10)

#     def add(self, key: int) -> None:
#         self.hash_list[key] = 1

#     def remove(self, key: int) -> None:
#         self.hash_list[key] = 0

#     def contains(self, key: int) -> bool:
#         return self.hash_list[key] == 1


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)




## APP 3
class MyHashSet:

    def __init__(self):
        
        self.size = 10000
        self.table = [None] * self.size
    
    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        
        if self.table[hv] is None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        
        if self.table[hv] is not None:
            while key in self.table[hv]: 
                self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        
        hv = self.calculate_hash_value(key)
        
        if self.table[hv] is not None:
            return key in self.table[hv]
        return False