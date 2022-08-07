spam = 0 
while spam < 5:
    spam = spam + 1
    #Will jump to start of whille and skip printing spam is 3
    if spam == 3:
        continue
    print('spam is ' + str(spam))