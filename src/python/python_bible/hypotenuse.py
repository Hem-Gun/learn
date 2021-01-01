from __future__ import division
import math

print 'Enter a number for side 1:'
side_1 = raw_input ()
side_1 = abs(float(side_1))
print 'Enter a number for  side 2:'
side_2 = raw_input ()
side_2 = abs(float(side_2))
print 'How many decimals do you want to round to: '
round_to = raw_input ()
round_to = int (round_to)
hypotenuse = math.hypot(side_1, side_2)
print 'Side 1 = ', round (side_1, round_to)
print 'Side 2 = ', round (side_2, round_to)
print 'Hypotenuse =' , round (hypotenuse, round_to)

print
