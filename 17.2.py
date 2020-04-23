import re

text = "Bieg na orientację dookoła miejskiego zoo"

result = re.findall(".oo.*", text, re.IGNORECASE)

print(result)
