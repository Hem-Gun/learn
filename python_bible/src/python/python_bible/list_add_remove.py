users = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print users

users = users+[10, 11, 12]

print users

users = users+['A','B']

print users

users = users+list('CDE') # adds everything in () as individual items even spaces, commas, etc. Does not work with int because int are not iterable

print users

users = users + list(str(131415)) # can add numbers as strings, but each number will be an independent addition

print users

users = users + [[13, 14, 15]] # can add numbers as strings, but each number will be an independent addition

print users

print users[-1] # fetch last item

users.append([16, 17, 18]) # appends item to the list; only 1 item at a time.

print users

users.append(['F', 'G'])

print users

users.insert(2, 369) # index, what to insert; inserts 369 at index 2

print users

users.insert(3, ['H', 'I', 100])

print users

users[0]=9 # replace with the specified number; starts with index 0; here the first element is replaced with 9

print users

users.remove(369) # works the same as add

print users

users = users.append(19) # deletes all the data because of the = operator; lists are mutable unlike variables which are immutable

print users