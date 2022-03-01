# 4. Remove all of the vowels in a string (use string above)



string = "Practice Problems to Drill List Comprehension in Your Head."
vowel="aeiouAEIOU"
print("".join([char for char in string if char not in vowel]))
