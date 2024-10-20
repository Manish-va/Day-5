def remove_duplicates(nums):  
  count = {}  
  result = []  
  for num in nums:  
    if num not in count or count[num] < 2:  
        result.append(num)  
        count[num] = count.get(num, 0) + 1  
  return result  
  
print(remove_duplicates([1, 1, 1, 2, 2, 3]))  
print(remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])) 