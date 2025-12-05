
import datetime
import random

try:
    number = int("abc")     
except ValueError:
    print("Invalid number format!")

now = datetime.now()
print("Current Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

rand_id = random.randint(1000,2500)
print("Random ID:",rand_id)