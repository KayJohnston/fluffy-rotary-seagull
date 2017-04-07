# Fib

old = 0
new = 1

position = 2
position_max = 30

while position <= position_max:
    number = old + new
##    print('Fi:',position,'Old',old,'New',new,'Number',number)
    print('Fi:',position,'is',number)
    position += 1
    old = new
    new = number
