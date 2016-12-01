"""
    210CT - Programming, Algorithms and Data Structures.
    Question7.py
    Purpose:  A recursive function to check if a number
              is a prime number.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""

def isPrime(number):
    """
    Function to check if a number is a prime number.

    Parameters:
        number (int); the number which is to be checked if its a prime or not.

    Returns:
        A boolean Value (True or False); If 'number' is a prime, True. Else, False.

    Raises:
        TypeError: If user enters an invalid number such as floats.
        RuntimeError: If the number is too large to perform recursive calls.
    """
    
    try:
        #If a user enters integers in decimal format, eg, 1.0, 12.00
        if isinstance(number,float) and number - int(number) == 0.0: 
            number = int(number)
            
        elif not(isinstance(number,int)): #Checking if the input is a valid int
            raise TypeError
        
        if number < 2: #Case 1: When 'number' is less than 2, it is not a prime.
            return False
        
        else:
            return check(number,number-1)
        
    except TypeError:
        print("Error: Please provide a valid number and try again.")
        return False
    except RuntimeError:
        print("Error: Number too large to check if its a prime using recursion.")
        


def check(number,divisor):
    """
    Recursive Function to check if a number is divisible by all numbers below it.

    Parameters:
        number (int); the number which is to be checked if its a prime or not.
        divisor (int);

    Returns:
        A boolean Value (True or False); If 'number' is divisible by 1, True. Else, False.
        
    """
    
    if divisor == 1: #Base Case
        return True
    
    elif (number%divisor) == 0: #If number is divisible by the divisor
        return False
    else:
        return check(number,divisor-1) #Recursive Call until divisor is 1



# Testing isPrime Function

if __name__ == "__main__":

    test1 = 1
    test2 = 0
    test3 = 111199.00
    test4 = 12.28
    test5 = -16
    test6 = 11
    test7 = "99"
    test8 = [1,2]
    test9 = 17.00
    test10 = 18.49
    
    tests = [test1, test2, test3, test4, test5, test6,test7,test8,test9,test10]
    testresults = [False,False,None,False,False,True,False,False,True,False]
    
    count = 0
    passed = 0
    failed = 0
    
    for test in tests:
        print("Performing Test " + str(count+1) + "; input = "+str(test) + " of " + str(type(test)))
        result = isPrime(test)
        if result == testresults[count]:
            print("Function Output = " + str(result))
            print("Test Passed.")
            passed += 1
        else:
            print("Function Output = " + str(result))
            print("Expected Output = " + str(testresults[count]))
            print("Test Failed.")
            failed += 1

        count = count + 1
        
        print("-"*20)

    print("Total tests performed: "+str(count))
    print("Tests passed: "+str(passed))
    print("Tests failed: "+str(failed))
    
    

