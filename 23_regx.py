import re

message = 'Call me 456-288-5588 asdf asdf asdfasdf asdf asljdkfhlkasdjf ashjdfaskdklaksjdf 554-874-3315'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)