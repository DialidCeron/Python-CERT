import re

pattern = r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$'

print(re.search(pattern, 'work 1 - (800) 555.1212 #1234').groups())