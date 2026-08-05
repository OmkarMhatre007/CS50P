# Validate
import re

email = input("Enter your email address: ").strip()

# re.search(pattern, string, flags=0)
if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")