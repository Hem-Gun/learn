print 'Hello'.count('e') # counts the number of e's in the word

text = 'Happy Birthday'
print text.count('a')
print text.count('day')
print text
print text.lower() # converts to lower case
print text.upper() # converts to upper case
print text.title() # converts to title case

text = text.lower() # overrides the variable
print text

print text.capitalize() # makes first letter to upper case

print text.isupper() # true/false is the word upper case
print text.islower() # true/false is the word lower case
print text.istitle() # true/false is the word title case
print text.isalpha() # true/false only letters
print text.isdigit() # true/false only digits
print text.isalnum() # true/false only alphabets and numbers

print text.index('birthday') # where the string starts in the main string
# print text.index('sdvjkdkj') # where the string starts in the main string; throws an error and breaks the script if not found

print text.find('birthday') # where the string starts in the main string
print text.find('sdhjvbhjdfv') # where the string starts in the main string; returns -1 if not found

new_text = '   777777777Happy Birthday77777777   '

print new_text
print new_text.strip('7') # strips the main string of the mentioned string
print new_text.lstrip('7') # strips the main string of the mentioned string on the left 
print new_text.rstrip('7') # strips the main string of the mentioned string on the right
print new_text.strip() # strips the main string of the mentioned string; in this case trailing spaces
print len(new_text) # number of characters including leading and trailing spaces
print len(new_text.strip()) # number of characters including leading and trailing spaces