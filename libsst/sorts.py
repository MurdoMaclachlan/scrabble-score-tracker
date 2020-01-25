def bubbleSort(nArray):
  for i in range(len(nArray)-1, 0, -1):
    for j in range(i):

      #looks for the next number being larger than the current number, and if so, swaps them
      if nArray[j].score > nArray[j+1].score:

        temp = nArray[j] #temporary variable prevents numbers from being lost

        nArray[j] = nArray[j+1]
        nArray[j+1] = temp

  return nArray
