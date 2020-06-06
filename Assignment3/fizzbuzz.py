
def fizz_buzz(length):
    output_list = []
    for x in range(0, length):
        if x % 3 == 0 and x % 5 == 0:
            output_list.append('FizzBuzz')
            
        elif x % 3 == 0:
            output_list.append('Fizz')
    
        elif x % 5 == 0:
            output_list.append('Buzz')
     
        else:
            output_list.append(str(x))
            
    return output_list


'''
length = input('Let us have fun with fizzbuzz! Give me a number!')
n = int(length)
print fizz_buzz(n)
'''




'''
    fizz_buzz takes in an integer, length
    It returns a list of strings that is 'length' strings long
    For the each entry in the returned list: 
        - if the index is a multiple of three, the list element will be 'Fizz'
        - if the index is a multiple of five, the list element will be 'Buzz'
        - if the index is a multiple of both three and five, the list element will be 'FizzBuzz'
        - otherwise, the list element will be a string of the value of the index
'''


    
