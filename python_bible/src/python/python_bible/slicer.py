word = 'supercalifragilisticexpialidocious'

print word
print word[0] # returns the letter in the word. starts at 0
print word[2]

print word [0:5:1] # returns letters from and till in steps; the letter you want to end at +1

print word [5:9:1]

print word [5::1]

print word [5::2] # returns from the 6th letter onwards in steps of 2

print word [0:7] # returns 1st to 7th letter

print word [:5:1] # returns till the 5th letter

print word [::-1] # reverses the word

print word[-2] # returns the value counting backwards

print word[-1] # returns the last letter

print word [word.index('cali'):word.index('fragi'):1]
