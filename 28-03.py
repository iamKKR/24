key = [x for x in range(1,100)]
value = [chr(y) for y in range(ord('a'),ord('z')+1)]
# print(list1)
print(value)


diction1 = { k:v for k,v in zip(key,value)}
print(diction1)



