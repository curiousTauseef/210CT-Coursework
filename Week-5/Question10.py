"""
    210CT - Programming, Algorithms and Data Structures.
    Question10.py
    Purpose:  A function which extracts the sub-sequence
              of maximum length which is in ascending order.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""

def maxSeq(arr):
    """
    A function to extract the sub-sequence of maximum length which
    is in ascending order.

    Parameters:
        arr (list); the sequence from which the sub-sequence of maximum length
                    should be extracted

    Returns:
        maximumSeq (list); the sub-sequence of maximum length in ascending order

    Raises:
        TypeError: If user enters an invalid sequence such as dictionaries.
        
    """
    
    try:
        
        if not(isinstance(arr,list)): #Checking if sequence is invalid or not
            raise TypeError

        maximumSeq = [] # stores the sub-sequence of maximum length
        tempSeq = [] #temporary sequence

        if len(arr) == 0 or len(arr) == 1: #if user provides empty or 1 element sequences
            return arr

        for i in range(len(arr)-1):
            
            tempSeq.append(arr[i]) #add each element in temporary sequence
            
            if arr[i+1]<arr[i]: #When the sequence breaks
                
                if len(maximumSeq) < len(tempSeq): #if temporary sequence has more elements than maximum sequence
                    
                    maximumSeq = tempSeq #Make temporary sequence the current maximum sequence
                    
                tempSeq = [] #Reset the temporary sequence 
                
        tempSeq.append(arr[-1]) #Adding the last element in arr, because loop stops at second last element
        
        if len(maximumSeq) < len(tempSeq):
            
            maximumSeq = tempSeq

        return maximumSeq

    except TypeError:
        
        print("Error: Please provide a sequence of type 'list' and try again.")



# Testing maxSeq Function

if __name__ == "__main__":

    test1 = [11,12,13,14,15,16,1,2,3,4,5,16,17,18]
    test2 = [0.1,0.2,0.3,0.4,0.05,0.06,0.08,0.1,0.3]
    test3 = ["g","h","i","j","k","l","a","b","c"]
    test4 = [1,2,3,4,5,0.1,0.2,0.3,0.4,0.5]

    tests = [test1,test2,test3,test4]
    testresults = [[1,2,3,4,5,16,17,18],[0.05,0.06,0.08,0.1,0.3],["g","h","i","j","k","l"],
                   [1,2,3,4,5]]
    
    count = 0
    passed = 0
    failed = 0
    
    for test in tests:
        print("Performing Test " + str(count+1) + "; input = "+str(test) + " of " + str(type(test)))
        result = maxSeq(test)
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
        
        print("-"*60)

    print("Total tests performed: "+str(count))
    print("Tests passed: "+str(passed))
    print("Tests failed: "+str(failed))
	

            
