
#! using for loop
a='python is easy and python is powerful'
split_word=a.split()

empty={}

for word in split_word:
    if word in empty:
        empty[word]+=1
    else:
        empty[word]=1
print(empty)

#! using while loop

a='python is easy and python is powerful'
split_word=a.split()

empty={}
i=0
while i<len(split_word):
    if split_word[i] in empty:
        empty[split_word[i]]+=1
    else:
        empty[split_word[i]]=1
    i+=1
print(empty)


