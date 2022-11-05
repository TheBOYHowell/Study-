#fizz_buzz

for i in range(1,100):
    if (i % 3 == 0) and (i % 5 == 0): #check for multiple of 3 and  check for multiple of   5 
        print('FizzBuzz')
    elif i % 3 ==0 :
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)    #   print   the number  of times        