for i in range(0,5):
    print '*'
    
print '----------------'

for i in range(0,5):
    print '*',
print

print '----------------'

for i in range(0,5):
    for j in range(0,5):
        print "*",
    print 

print '----------------'
for i in range(0,5):
    for j in range(0,i+1):
        print '*', 
    print

print '----------------'

for i in range(0,5):
    for j in range(0,5):
        print i,j

print '----------------'

for i in range(0,5):
    for j in range(0,5):
        print '*',
    print
    
print '----------------'

def sayHello(someone): #dingyihanshu sayHello
    print someone + ' say hello!'
sayHello('Ben')
print '----------------'

from random import choice
print 'Choose one side to shoot:'
print 'left,center,right'
you = raw_input()
print 'You kicked ' + you
direction = ['left','center','right']
com = choice(direction)
print 'Computer saved ' + com
if you != com:
    print 'Goal'
else:
    print 'Oops...'
