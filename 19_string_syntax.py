
# Escape character Prints as

# \'               Single quote

# \"               Double quote

# \t               Tab

# \n               Newline (line break)

# \\               Backslash

# Multiline Strings with Triple Quotes:
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Indexing and Slicing Strings
spam = 'Hello, world!'
spam[0] #H
spam[4] #'o'
spam[-1] #'!'
spam[0:5] #'Hello'
spam[:5] #'Hello'
spam[7:] #'world!'

# >>> 'Hello' in 'Hello, World'
# True
# >>> 'Hello' in 'Hello'
# True
# >>> 'HELLO' in 'Hello, World'
# False
# >>> '' in 'spam'
# True
# >>> 'cats' not in 'cats and dogs'
# False