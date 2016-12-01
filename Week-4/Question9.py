def binary_search( sequence, a, b ):
  """ 
  Function to search a value between a given interval in sequence using binary search algorithm. 
  
  Parameters:
      sequence(list); the sequence of different values 
      a(int); the lower limit of the interval
      b(int); the upper limit of the interval
  Returns:
      A boolean value; True if a value is found between the given interval, otherwise false. 
  """
  
  start = 0
  end = len(sequence)-1
  while start <= end:
    mid = (start+end)//2
    if a <= sequence[mid] <= b :
      return True
    elif b < sequence[mid]:
      end = mid -1
    else: # b > sequence[mid]:
      start = mid +1
  
  return False
