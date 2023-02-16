a = 10
b= 5

if a > 10 and b > 1:
    print 'true'
else:
    print 'false'

if a > 10 or b > 1:
    print 'true'
else:
    print 'false'

if not (a > 10 and b > 1):
    print 'true'
else:
    print 'false'

if not (a > 10 or b > 1):
    print 'true'
else:
    print 'false'

if (a > 2 and b > 2) or (a > 6 and b > 6):
    print 'true'
else:
    print 'false'

if (a > 2 or b > 2) and (a > 6 or b > 6):
    print 'true'
else:
    print 'false'

if not (a > 2 and b > 2) or (a > 6 and b > 6):
    print 'true'
else:
    print 'false'

if not (a > 2 or b > 2) and (a > 6 or b > 6):
    print 'true'
else:
    print 'false'