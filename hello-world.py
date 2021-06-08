print('Hello world')

message = 'I can print from a variable'
print(message)

nextMessage = ' and I can concatonate'
print(message + nextMessage)

thisNumber = 42
numberMessage = 'even with a number '
print(numberMessage + str(42))

newNumberMessage = 'and a number variable '
print(newNumberMessage + str(thisNumber))

print(newNumberMessage, thisNumber)

def printThis():
  print('I can print in a function')

printThis()

for c in 'I can loop through a string':
  print(c)

def xo(s):
  x = 0
  o = 0
  for c in s:
    c = c.lower()
    if c == 'x':
      x += 1
    
    if c == 'o':
      o += 1
  if x == o:
    print(x == o)
    return True
  else:
    print(x == o)
    return False


xo('xo')
xo('xoxoxoxo')
xo('oxo')
xo('Xo')
xo('xo with other characters')
xo('xo with other characters and an x')

def xoBetter(s):
  s = s.lower()
  return s.count('x') == s.count('o')

xoBetter('xo')
xoBetter('xoxoxoxo')
xoBetter('oxo')
xoBetter('Xo')
xoBetter('xo with other characters')
xoBetter('xo with other characters and an x')

def xoInOneLine(s):
  return s.lower().count('x') == s.lower().count('o')

xoInOneLine('xo')
xoInOneLine('xoxoxoxo')
xoInOneLine('oxo')
xoInOneLine('Xo')
xoInOneLine('xo with other characters')
xoInOneLine('xo with other characters and an x')