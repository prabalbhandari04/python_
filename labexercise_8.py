#Given a three-digit number. Find the sum of its digits.

# The random() function generates
# a random fractional number from 0 to 1
from random import random
# When the number is multiplied by 900,
# a random number is obtained from 0 to 899.(9).
# If you add 100 to it,
# you get a number from 100 to 999.(9).
n = random() * 900 + 100
n = int(n)
print(n)

# The number is converted to a string type
s = str(n)

# The first [0] character of the string is extracted,
# converted to an integer.
# Similarly, the second [1] and the third [2].
a = int(s[0])
b = int(s[1])
c = int(s[2])

print(a + b + c)