# 5. Find all of the words in a string that are less than 5 letters (use string above)



string = "Practice Problems to Drill List Comprehension in Your Head."

words=[x for x in string.split(' ')]
new_word=[word for word in words if(len(word)<5)]
print(new_word)