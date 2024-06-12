import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
print(emails)

