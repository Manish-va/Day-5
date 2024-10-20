# Day-5
## 1. Compute Factorial of a Number.
```
def factorial(n):  
   if n == 0:  
      return 1  
   else:  
      return n * factorial(n-1)  
  
print(factorial(5)) 

```
Output:-120



## 2. Roman Numeral Converter.
```
def roman_to_int(s):  
   roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  
   int_val = 0  
   for i in range(len(s)):  
      if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i - 1]]:  
        int_val += roman_numerals[s[i]] - 2 * roman_numerals[s[i - 1]]  
      else:  
        int_val += roman_numerals[s[i]]  
   return int_val  
  
print(roman_to_int("III")) 
print(roman_to_int("IV")) 
print(roman_to_int("IX")) 
print(roman_to_int("LVIII"))   
print(roman_to_int("MCMXCIV"))
```
Output:-3<br>4<br>9<br>1994



## 3. Word Reversal Class.
```
class WordReversal:  
   def __init__(self, word):  
      self.word = word  
  
   def reverse(self):  
      return self.word[::-1]  
  
word = WordReversal("hello")  
print(word.reverse())  

```
Output:-olleh



## 4. Remove Duplicates with Maximum Two Occurrences.
```
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

```
Output:-[1, 1, 2, 2, 3]<br>[0, 0, 1, 1, 2, 3, 3]



## 5. Rotate the array.
```
def rotate_array(nums, k):  
   k = k % len(nums)  
   return nums[-k:] + nums[:-k]  
  
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_array([-1, -100, 3, 99], 2))

```
Output:- [5, 6, 7, 1, 2, 3, 4] <br>[3, 99, -1, -100]




