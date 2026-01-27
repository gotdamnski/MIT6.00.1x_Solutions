# -*- coding: utf-8 -*-

s = input("input string: ")


longest = s[0]
current = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        current += s[i]
        
    else:
        current = s[i]
        
    if len(current) > len(longest):
        longest = current
        
print(longest)