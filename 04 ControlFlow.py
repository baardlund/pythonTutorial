
#x = int(input("Please enter an integer: "))
x = 3
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))


for i in range (8):
    print(i)
    
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in  range(len(a)):
    print(i, a[i])
    
#see also enumerate()

#4.4 brean and continue
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
  
