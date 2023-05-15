# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
for i in text.casefold():
    if i.isalnum():
        if i in word_count:
            word_count[i] +=1
        else:
            word_count[i]=1
 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)