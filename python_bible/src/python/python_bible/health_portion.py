from __future__ import division
import random

print 

health = 50

difficulty = 3

portion_1 = round((random.randint(25,50)/difficulty), 2)

health_1 = health + portion_1

print 'Health =', health
print 'Portion health (random between 25 and 50) =', portion_1
print 'New health =', health_1

print

portion_1 = int(random.randint(25,50)/difficulty)

health_1 = health + portion_1

print 'Health =', health
print 'Portion health (random between 25 and 50) =', portion_1
print 'New health =', health_1

print

portion_random = [50, 25, 10]
portion_2 = random.choice(portion_random)

health_2 = health + portion_2

print 'Health =', health
print 'Portion health (random 10, 25 or 50) =', portion_2
print 'New health =', health_2

print

portion_beginner = 50
portion_intermediate = 25
portion_expert = 10

print

print 'Health=', health

print 'Select difficulty: \n 1. Beginner \n 2. Intermediate \n 3. Expert \n Enter 1, 2 or 3'
response = raw_input ()
while response not in {'1', '2', '3'}:
    response = raw_input('Enter 1, 2, or 3: \n')
if response is '1':
    health_3 = health + portion_beginner
    print 'Health=', health
    print 'Portion health beginner', portion_beginner
    print 'New health =', health_3
elif response is '2':
    health_3 = health + portion_intermediate
    print 'Health=', health
    print 'Portion health intermediate', portion_intermediate
    print 'New health =', health_3
elif response is '3':
    health_3 = health + portion_expert
    print 'Health=', health
    print 'Portion health expert', portion_expert
    print 'New health =', health_3
