
def removeVowels (word):
	
	if len(word) == 0:
		return word
		
	elif word[0] in "aeiouAEIOU": # first character is vowel
		return removeVowels(word[1:]) # skip first character and process rest
	
	return word[0] + removeVowels(word[1:]) # return first character and process rest


print(removeVowels("beautiful"))
