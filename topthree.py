# This program generates 10 random numbers.
# prints them out, then
# prints out the top 3

import random

howmany = 10
tophowmany = 3
rangefrom = 0
rangeto = 100

numbers = []

for i in range (0, 10):
    numbers.append(random.randint(rangefrom,rangeto))
print ("{} random numbers\t {}".format(howmany,numbers))

topones = numbers.copy()
topones.sort(reverse= True)
print ("The top {} are \t\t {}".format(tophowmany,topones[0:tophowmany]))
