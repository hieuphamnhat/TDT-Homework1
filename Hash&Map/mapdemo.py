class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [[] for _ in range(self.size)]
  
    # Insert values into hash map
    def insert(self, keys, val):
        for key in keys:
            hashed_key = hash(key) % self.size
            bucket = self.hash_table[hashed_key]
    
            key_exists = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    key_exists = True
                    break
            if key_exists:
                bucket[index] = (key, val)
            else:
                bucket.append((key, val))
    def search(self, key):
        
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        key_exists = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                key_exists = True
                break
        if key_exists:
            return record_val
        else:
            return "No record found"
    def delete(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        key_exists = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                key_exists = True
                break
        if key_exists:
            bucket.pop(index)
        return
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
#Map<Key, Value>
hash_table = HashMap(50)
hash_table.insert('key1', 'some value')
print(hash_table)
print("---------------------")
hash_table.insert('key2', 'some other value')
print(hash_table)
print("---------------------")
print(hash_table.search('key2'))
print("---------------------")
hash_table.delete('key1')
print(hash_table)

#create Object
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_val(self):
        print(self.name, ";", self.age)

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
man = Person(10, "Nam")
man.get_val()
woman = Person(12, "Nga")
list_person = [man, woman]
list_key = []
for index, p in enumerate(list_person):
    list_key.append(index)
    print(p.get_age())
#Map<Key, List(Object)>
hash_table.insert('key3', list_person)
print(hash_table)
#Map<List(Key), List(Object)>
hash_table.insert(list_key, list_person)
print(hash_table)

