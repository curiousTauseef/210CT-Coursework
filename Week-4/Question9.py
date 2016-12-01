"""
    210CT - Programming, Algorithms and Data Structures.
    Question9.py
    Purpose:  A function to search a value between a given interval
              in sequence using binary search algorithm.
                    
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""


def rangeBinarySearch( sequence, a, b ):
  """ 
  Function to search a value between a given interval in sequence using binary search algorithm. 
  
  Parameters:
      sequence(list); the sequence of different values 
      a(int); the lower limit of the interval
      b(int); the upper limit of the interval
      
  Returns:
      A boolean value; True if a value is found between the given interval, otherwise false.

  Raises:
      TypeError: If user provides inputs of an unsupported type.
  
  """

  try:

    typeSeq = isinstance(sequence,list)
    typeA = isinstance(a,int) or isinstance(a,float)
    typeB = isinstance(b,int) or isinstance(b,float)

    if not(typeSeq) or not(typeA) or not(typeB): #If wrong types of input are provided
      raise TypeError

    if b < a: #When the user provides upper limit value lesser than lower limit value
      (a,b) = (b,a)
      print("The upper limit value is lesser than lower limit value.")
      print("Inorder to proceed, This function has swapped the values of upper and lower limits")
      
      

    #Binary Search Algorithm
      
    start = 0
    end = len(sequence)-1
    
    while start <= end:
      
      mid = (start+end)//2 #pivot
      
      if a <= sequence[mid] <= b : #if the middle value of sequence is in the range
        
        return True
      
      elif b < sequence[mid]: #if upper limit is lesser than middle value
        
        end = mid -1 #Eliminate the right side of the sequence
        
      else: # if upper limit is greater than middle value
        
        start = mid +1 #Eliminate the left side of the sequence
  
    return False # After loop finishes, if nothing is found then return False

  except TypeError: #If user provides unsupported types of input
    
    print("Error: Please provide the sequence of type 'list'")
    print("       and limits of type 'int' and try again.")
    return False


# Testing rangeBinarySearch Function

if __name__ == "__main__":

    sequence = [-2.5,-2,-1,0,1,1.32,2,3,5,6,7,16.5,19,29,39,40,43,46,49]
    print("Sequence: "+str(sequence))
    
    test1 = (20,40)
    test2 = (1,1)
    test3 = (1,3)
    test4 = (0,1)
    test5 = (1,-5)
    test6 = (100,200)
    test7 = ("a","b")
    test8 = (16.4,16.6)
    
    
    tests = [test1, test2, test3, test4, test5, test6,test7,test8]
    testresults = [True,True,True,True,True,False,False,True]
    
    count = 0
    passed = 0
    failed = 0
    
    for test in tests:
        print("Performing Test " + str(count+1) + ";")
        print("lower range = "+str(test[0]) + ", upper range = "+ str(test[1]))
        result = rangeBinarySearch(sequence, test[0], test[1])
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
