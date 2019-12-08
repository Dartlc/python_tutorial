"""
    Regular Expression
"""

import re

a = "hello World"

x = re.findall("[e-i]", a)
print(x)