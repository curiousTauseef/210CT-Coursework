"""
    210CT - Programming, Algorithms and Data Structures.
    Question1.py
    Purpose:  A function that randomly shuffles an array of elements. 
             
        
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 15/10/16
    
"""


import random

def shuffleArray(arr):
    """
    Function to randomly shuffle an array.
    Parameters:
    arr (list); the array to be shuffled.

    Returns:
    shuffledArray(list); A list of elements in 'arr' arranged in an random order.
    
    """
    try:
        
        if isinstance(arr,tuple) or isinstance(arr,dict) or isinstance(arr,str):
            raise TypeError
        
        size = len(arr)
        shuffledArray = []
        
        if size == 0: #When the user provides an empty array
            print("Error in shuffling, please provide a valid array with ELEMENTS to shuffle.")
            return arr
		
        elif size == 1: #When the user provides an array containing only 1 element
            return arr
		
        else:
            
            while size > 0: #Loop finishes when all elements have been appended to shuffledArray
                
                randomIndex = random.randint(0,size-1) #Getting Random Index Number
                shuffledArray.append(arr[randomIndex]) #Adding element with random Index to shuffledArray
                del arr[randomIndex] #Removing it from 'arr'
                size = size - 1
                
            return shuffledArray 
                
    except:
        print("Error: Please provide a valid array to shuffle and try again.")
        



if __name__ == "__main__":

    test1 = 1
    test2 = (1,2,5,6,7,8,9,10)
    test3 = {"a":"b","c":"d","e":"f","g":"h"}
    test4 = "abcdefgh"
    test5 = [1,2,3,4,5,6,7,8,9,10]
    test6 = ["a","b","c","d","d","e","f"]

    tests = [test1, test2, test3, test4, test5, test6]
    testresults = [None,None,None,None,[],[]]
    count = 0
    passed = 0
    failed = 0
    for test in tests:
        print("Performing Test " + str(count+1))
        result = shuffleArray(test)
        if type(result) == type(testresults[count]):
            passed += 1
        else:
            failed += 1

        count = count + 1
        
        print("-"*20)

    print("Total tests performed: "+str(count))
    print("Tests passed: "+str(passed))
    print("Tests failed: "+str(failed))
        

    
