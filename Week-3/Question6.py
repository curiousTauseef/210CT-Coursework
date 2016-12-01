def revSentence(sentence):
    """
    A function which reverses the words in a sentence.
    
    Parameters:
        sentence(string); the sentence which is to be reversed.

    Returns:
        reversedSentence(string); the reversed version of 'sentence'.

    Raises:
        Exception; If an unexpected error occurs. Eg; if user enters an invalid input(int,float,list etc).   
    """

    try:
        
        reversedSentence = ""
    
        words = sentence.split(" ")                            # Getting a list of words in the sentence

        if len(words) == 1:
            return sentence
    
        for i in range(len(words)-1,-1,-1):                    # For loop which counts backwards from number of words - 1 till 0.
            
            reversedSentence = reversedSentence + words[i]     # Adding words backwards to form a new string (reversed sentence)
        
            if i != 0:                                         # Adding spaces between words while it is not the last word
                
                reversedSentence += " "
			
        return reversedSentence                                # After the for loop finishes

    except:
        print("Error in reversing sentence. Please try again with a sentence of type 'string' in which the words are seperated with spaces.")


# Testing of revSentence Function

if __name__ == "__main__":

    test1 = "this is awesome"
    test2 = "this?is?awesome"
    test3 = "this"
    test4 = "This is question 6 from 210CT Coursework. 210CT is a module taught in second year Computer Science at Coventry University"
    test5 = ""
    test6 = ["hello","its","me"]
    test7 = 101
    test8 = (1,2)
    

    tests = [test1, test2, test3, test4, test5, test6,test7,test8]
    testresults = ["awesome is this","this?is?awesome","this","University Coventry at Science Computer year second in taught module a is 210CT Coursework. 210CT from 6 question is This","",None,None,None]
    count = 0
    passed = 0
    failed = 0
    for test in tests:
        print("Performing Test " + str(count+1) + "; input = "+str(test))
        result = revSentence(test)
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
