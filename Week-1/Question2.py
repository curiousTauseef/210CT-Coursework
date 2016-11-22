"""
    210CT - Programming, Algorithms and Data Structures.
    Question2.py
    Purpose:  A function which allows user to count the number of trailing 0s in a factorial number. 
             
        
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 15/10/16
    
"""


def factorialTrailingZeros(n):
    """
    Function to count the number of trailing 0s in a factorial number.

    Parameters:
    n (int); the number for which the factorial and trailing 0s are to be calculated.

    Returns:
    trailingZeros (int); the number of 0s in the calculated factorial number.
    
    """
    
    ans = 1
    trailingZeros = 0
    
    # Calculating the factorial of 'n'
    
    while n >= 1: # Loop stops when n becomes 0
        ans *= n
        n -= 1

    # Calculating the number of 0s in 'ans'
    
    while float(ans % 10) == 0: # Loop stops when 'ans' is not divisible by 10, also means it no longer has 0s in it.
    	trailingZeros += 1
    	ans = ans // 10
    	
    	
    return trailingZeros #When both the while loops finish

