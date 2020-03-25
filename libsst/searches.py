def binarySearch(nArray, target):

  #sets up the search
  first = 0
  last = len(nArray)-1
  found = False

  #defines the midpoint of the array using the beginning and end
  while first <= last and not found:
    midpoint = (first + last)//2

    #detects if the current midpoint is equal to the target
    if nArray[midpoint].idnum == target:
      found = True

    #if not, and the target is LESS than the midpoint, it will switch to the first half of the list, if it is GREATER than the midpoint, it will switch to the second half
    else:
      if int(target) < nArray[midpoint].idnum:
        last = midpoint - 1
      else:
        first = midpoint + 1

  #returns that the target has been found
  return midpoint

def linearSearch(nArray, target):
    pos = 0

    #goes through array from the beginning until it finds the target
    for i in range(len(nArray)):
        if nArray[i].name == target:
            pos = i
            break
    return pos
