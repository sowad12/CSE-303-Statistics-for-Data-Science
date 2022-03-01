#6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)


string = "Practice Problems to Drill List Comprehension in Your Head."
li =  string.split(' ')

d={ word: len(word) for word in  li}
print(d)


