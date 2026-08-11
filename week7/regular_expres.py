## Validate
# import re

# email = input("Enter your email address: ").strip()

# # re.search(pattern, string, flags=0)
#   if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(com|edu)$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")

# Format
# import re

# name = input("Enter your name: ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello, {name}!")

## twitter
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
# if matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: {matches.group(2)}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")