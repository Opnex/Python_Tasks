# Different Ways to Import Modules

#1. Import the whole module
import math

# Lets put it to use
print(math.sqrt(9))

# - Note that you must specify the module name when calling a function within it.



# 2. import as an alias
import math as m
# lets put it to use
print(m.sqrt(25))



# 3. Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)



# 4. Import everything from the module
from math import *
print(sqrt(49))
print(pi)


