import random
import string
latters=string.ascii_latters
numbers=string.digites
symbol="!@#$^&
all_char=latters+number+symbols
lenght=int(input("enter password lenght:"))
password=" "
for i in range(length):
  password+=random.choice(all_char)
print("generate password:",password)
