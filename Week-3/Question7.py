def isPrime(n):
        
	if n < 2:
		return False
	else:
		return check(n,n-1)

def check(n,d):
	if d == 1:
		return True
		
	elif (n%d == 0):
		return False
		
	else:
		return check(n,d-1)
		

print(isPrime(7))
