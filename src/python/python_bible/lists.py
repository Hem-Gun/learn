a = [1, 2, 3, 4, 5]

b = ['A', 'B', 'C', 'D', 'E']

print type (a)

print a

print b[-1] # fetch an element of a list

c = b[0: 3: 1] # a list can be cut and used to create a new list
print c

[x,y,z] = 1,2,3
print x
print y
print z

d = [1, 2, 3, ['A', 'B', 'C'], 4, 'D']

print d
print d[5]
print d[3]
print d[3][1]

print d[3][0:2:1]