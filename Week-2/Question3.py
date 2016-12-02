"""
    210CT - Programming, Algorithms and Data Structures.
    Question3.py
    Purpose:  A function which returns the highest perfect square less than
              or equal to its parameter.
             
        
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 26/10/16
    
"""



def highestPerfectSquare(n):
    """
    Function which returns the highest perfect square less than or equal to its parameter.
    
    Parameters:
        n (int or float); the number for which the highest perfect square below it is to calculated.

    Returns:
        ans(int); the highest perfect square less than or equal to 'n'

    Raises:
        Exception; If an unexpected error occurs. Eg; if user enters an negative value.
        
    """
    try:
        
        nearestInt = int(n**0.5) #Calculating sqaure root of n
        ans = (nearestInt) ** 2  #Simply squaring the nearestInt
        return ans
    
    except:
        
        print("Error in calculating highest perfect square. Please try again with a valid 'positive' number.")
        



if __name__ == "__main__":

    test1 = 1
    test2 = 0
    test3 = 111199.00
    test4 = 12.28
    test5 = -16
    test6 = 100
    test7 = "99"
    test8 = (1,2)
    

    tests = [test1, test2, test3, test4, test5, test6,test7,test8]
    testresults = [1,0,110889,9,None,100,None,None]
    count = 0
    passed = 0
    failed = 0
    for test in tests:
        print("Performing Test " + str(count+1) + "; input = "+str(test) + " of " + str(type(test)))
        result = highestPerfectSquare(test)
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
