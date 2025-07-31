import string
import random

s = string.ascii_letters + string.digits
print (s)
numbers = random.sample(s, 15)
print(numbers)
numbers = ''.join(numbers)
print(numbers)