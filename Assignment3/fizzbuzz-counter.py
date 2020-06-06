

fizzcounter = 0
buzzcounter = 0
fizzbuzzcounter = 0

def fizzbuzz(length):

    for x in range(0, length+1):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
            fizzbuzzcounter += 1
            
        elif x % 3 == 0:
            print('Fizz')
            fizzcounter += 1
            
        elif x % 5 == 0:
            print('Buzz')
            buzzcounter += 1
            
        else:
            print(x)


print("____________________________________")
print("Fizz\tBuzz\tFizzbuzz")
print(str(fizzcounter) + "\t" + str(buzzcounter) + "\t" + str(fizzbuzzcounter))


length = input('Let us play fizzbuzz! Give me a number!')
n = int(length)
fizzbuzz(n)



'''
    fizz_buzz takes in an integer, length
    It returns a list of strings that is 'length' strings long
    For the each entry in the returned list: 
        - if the index is a multiple of three, the list element will be 'Fizz'
        - if the index is a multiple of five, the list element will be 'Buzz'
        - if the index is a multiple of both three and five, the list element will be 'FizzBuzz'
        - otherwise, the list element will be a string of the value of the index
'''


    
