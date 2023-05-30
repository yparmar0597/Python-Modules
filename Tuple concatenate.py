### Tuple concatenate

t1 = (1,2,3)
t2 = (6,7,8)

print(t1, id(t1))
print(t2, id(t2))

t1=t1+t2
print(t1, id(t1))  #### id is getting modified


### List concatenate

t1 = [1,2,3]
t2 = [6,7,8]

print(t1, id(t1))
print(t2, id(t2))

t1.extend(t2)
print(t1, id(t1))  #### id is getting modified