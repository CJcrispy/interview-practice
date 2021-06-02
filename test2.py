# for i in range(97,123):
#     print(chr(i), end=" ")

# for i in range(65,91):
#     print(chr(i), end=" ")

def hash_test(keyvalue):
	try:
		if type(keyvalue) is int:
			return keyvalue  % 2069
		elif type(keyvalue) is str:
			lst = []
			for i in keyvalue:
				lst.append(ord(i))
			return sum(lst) % 2069
		else:
			print("keyvalue is not a str or int")			
	except NameError:
		raise NameError
	
# print(ord("h"))
# for i in "hi":
# 	print(ord(i))
print(hash_test("hi"))
print(hash_test("21"))
print(hash_test(10))
print(hash_test(5.5))