"""
    210CT - Programming, Algorithms and Data Structures.
    Question8.py
    Purpose:  A recursive function which removes all vowels
              in a word/sentence.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""

def removeVowels(word):
    """
    Recursive Function to remove alll vowels in a words/sentence.

    Parameters:
        word (string); the word in which the vowels are to be removed.

    Returns:
        A string with no vowels after the all recursions are complete.

    Raises:
        TypeError: If user enters an invalid number such as floats.
        Exception: If any unexpected error occurs. Eg, RuntimeError when there are
                   too many recursive calls.
    """

    try:
        
        if not(isinstance(word,str)): #Checking if input is a valid string.
            raise TypeError
        
        if len(word) == 0: #Base Case
            return word
    
        elif word[0] in "AEIOUaeiou": #Checking If the first letter of word is a vowel
            return removeVowels(word[1:]) #Skip that letter and proceed with the rest of letters in word
        
        else: #Else, keep the first letter and proceed until length of word becomes 0.
            return word[0] + removeVowels(word[1:]) 

    except TypeError: #If the provided input is not a string.
        print("Error: Please provide a valid word/sentence of type string and try again.")
    
    except: #If any other unexpected error occurs
        print("Error in removing vowels. Please try again.")
        

# Testing removeVowels Function

if __name__ == "__main__":

    test1 = "Beautiful"
    test2 = "book"
    test3 = "word here"
    test4 = "aeivbwrubvjcbrjwavrbvhevhbvriocwrjvbu"
    test5 = 999
    test6 = "99"
    test7 = ["a","b","c","d"]
    test8 = "AEIOUooo"
    
    
    tests = [test1, test2, test3, test4, test5, test6,test7,test8]
    testresults = ["Btfl","bk","wrd hr","vbwrbvjcbrjwvrbvhvhbvrcwrjvb",None,"99",None,""]
    
    count = 0
    passed = 0
    failed = 0
    
    for test in tests:
        print("Performing Test " + str(count+1) + "; input = "+str(test) + " of " + str(type(test)))
        result = removeVowels(test)
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
