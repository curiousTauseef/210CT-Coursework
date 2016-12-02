"""
    210CT - Programming, Algorithms and Data Structures.
    Question2.py
    Purpose:  A function which allows user to count the number
              of trailing 0s in a factorial number. 
             
        
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""


def factorialTrailingZeros(n):
    """
    Function to count the number of trailing 0s in a factorial number.

    Parameters:
    n (int); the number for which the factorial and trailing 0s are to be calculated.

    Returns:
    trailingZeros (int); the number of 0s in the calculated factorial number.
    
    """
    try:

        if not(isinstance(n,int)) or (n<0): #If n is not a positive int
            raise TypeError
        
        ans = 1
        trailingZeros = 0
    
        # Calculating the factorial of 'n'
    
        while n >= 1: # Loop stops when n becomes 0
            ans *= n
            n -= 1

        # Calculating the number of 0s in 'ans'
    
        while float(ans % 10) == 0: # Loop stops when 'ans' is not divisible by 10, in other words it no longer has 0s in it.
            trailingZeros += 1
            ans = ans // 10
    	
    	
        return trailingZeros 

    except:
        print("Error: Invalid input. Please try again with a positive integer only.")
        return "Failed"



if __name__ == "__main__":

    test1 = 19
    test2 = 1001
    test3 = "15"
    test4 = 12.28
    test5 = [16]
    test6 = -6

    tests = [test1, test2, test3, test4, test5, test6]
    testresults = [3,249,"Failed","Failed","Failed","Failed"]
    count = 0
    passed = 0
    failed = 0
    for test in tests:
        print("Performing Test " + str(count+1) + "; input = "+str(test) + " of " + str(type(test)))
        result = factorialTrailingZeros(test)
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

