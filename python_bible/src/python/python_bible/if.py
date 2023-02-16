if 2 != 3:
    print 'true'
else:
    print 'false'

if True:
    print 'It worked'


print 'Enter the 1st number: \n'
num1 = float(raw_input())

print 'Enter the 2nd number: \n'
num2 = float (raw_input())

if num1 > num2:
    print 'Number 1 is greater than number 2.'
elif num1 < num2:
    print 'Number 1 is smaller than number2.'
elif num1 == num2:
    print 'Number 1 is equal to number 2.'