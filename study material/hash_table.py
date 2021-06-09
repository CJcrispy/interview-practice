# Function to display hashtable
def display_hash(hashTable):
	
	for i in range(len(hashTable)):
		print(i, end = " ")
		
		for j in hashTable[i]:
			print("-->", end = " ")
			print(j, end = " ")
			
		print()

# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(20)]

# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
	if type(keyvalue) is int:
		return keyvalue  % 13
	elif type(keyvalue) is str:
		lst = []
		for i in keyvalue:
			lst.append(ord(i))
		return sum(lst) % 13
	else:
		print("keyvalue is not a str or int")	


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].append(value)

def search(Hashtable, keyvalue):
	hash_key = Hashing(keyvalue)
	print(Hashtable[hash_key])

def delete(Hashtable, keyvalue):
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].pop()

# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Punjab')
insert(HashTable, 21, 'Noida')
insert(HashTable, "test", 'Chris')

display_hash (HashTable)

search(HashTable, "test")
search(HashTable, 9)

delete(HashTable, "test")
delete(HashTable, 20)

display_hash (HashTable)