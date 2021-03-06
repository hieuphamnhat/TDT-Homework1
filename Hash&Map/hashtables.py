hash_table = [[] for _ in range(10)]
print (hash_table)
def hashing_func(key):
    return hash(key) % len(hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    key_exists = False
    bucket = hash_table[hash_key]    
    for i, record in enumerate(bucket):
        k, v = record
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    key_exists = False
    bucket = hash_table[hash_key]
    for i, record in enumerate(bucket):
        k, v = record 
        if key == k:
            key_exists = True
            print(k, v) 
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))
insert(hash_table, 10, 'One')
print (hash_table)
insert(hash_table, 2, 'Two')
insert(hash_table, 20, 'Zero')
print (hash_table)
delete(hash_table, 10)
print (hash_table)
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    bucket = hash_table[hash_key]
    for i, record in enumerate(bucket):
        k, v = record
        if key == k:
            return v