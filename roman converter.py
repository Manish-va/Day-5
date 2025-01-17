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