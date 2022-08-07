print('May name is:')

for i in range(5):
    print('Jimmy Five Times ' + str(i))
print('----------------')

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
print('----------------')

total = 0
for num in range(101):
    total = total + num
print(total)

print('----------------')
#starts at 12 and goes up to but not including 16
for i in range(12, 16):
    print(i)
print('----------------')

#The first two arguments will be the start and stop values,
#and the third will be the step argument.

#will count from zero to eight by intervals of two.
for i in range(0, 10, 2):
    print(i)
print('----------------')

#will count from 5 to 0
for i in range(5, -1, -1):
    print(i)