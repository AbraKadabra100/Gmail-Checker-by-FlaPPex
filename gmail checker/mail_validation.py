#gmail address validation
import string

#!?=

inc= 0
gmail = input('Enter email address:')
special_char = string.punctuation
if gmail[-10:] == '@gmail.com':
   name = gmail[:-10]
print(name)
for c in special_char:
   if c in name and c != '.' and c != '-' and c != '_':
      print('The Email address is NOT valid')
      break

else:
    print('The Email address IS valid')
