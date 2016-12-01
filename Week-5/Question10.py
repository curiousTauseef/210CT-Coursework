
def maxSeq(arr):
	results = []
	temp = []
	#edge cases
	for i in range(len(arr)-1):
		temp.append(arr[i])
		
		if arr[i+1] < arr[i]:
			if len(results) < len(temp):
				results = temp
			temp = []
	
	temp.append(arr[-1])
	
	if len(results) < len(temp):
		results = temp
	return results
	

sequence = [ 1, 2, 3, 4,5,9,9,9,50,51,8, 3, 9, 10, 11, 12, 13, 1, 2, 3 ]
	
test = []
	
print( maxSeq( sequence ) )
