users = (1,2,3,'a','b', 'c') # [] is a list; () is a tuple; tuples works similar to lists, but cannot be changed; used when you don't want the data to change

print users

print type(users)

user_list = [4, 5, 6]

print user_list

user_tuple = tuple(user_list) # convert list to tuple

print user_tuple

(a, b, c) = 1,2,3
print a
print b
print c

users = users + ('4') # throws an error

print users