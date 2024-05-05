import random
import string

pass_len=int(input("Enter the length of password:"))
charvalues=(string.ascii_letters+string.digits+string.punctuation)

password=""
for i in range(pass_len):
    password+=random.choice(charvalues)

print("Your Desired Password is:",password)