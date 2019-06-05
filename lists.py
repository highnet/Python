nums = [1, 2, 3, 4]
print (nums)
nums.remove(3) # remove the number 3 from the list
print (nums)
nums.pop() # removes last number from the list
print (nums)
nums.pop(0) # removes the 0th index from the list
print (nums)
nums.extend([3,4]) # extends the list with another list
print (nums)
nums.insert(0,1) # insert at index 0 the number 1 
print (nums)
nums.insert(2,"two point five")
print (nums)
nums.append(6) # add to the end of list
print (nums)
copyOfNums = nums.copy() # copy list
copyOfNums.remove(3)
copyOfNums.pop(0)
copyOfNums.append(6)
print (copyOfNums)



