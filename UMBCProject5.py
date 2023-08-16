# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#Assign text reading function to variable
draculaText = readBook()

#Split Dracula and make all lowercase
draculaText = draculaText.lower().split()

#Creat Dictionary where Key is each word that appears in Dracula and Value is the number of times it appears
draculaDict = {}

#for loop adding each word in Dracula to dictionary
for word in draculaText:
  if word not in draculaDict:
    draculaDict[word] = 1
  if word in draculaDict:
    draculaDict[word] += 1

##Count four letter words in Dracula 

#Blank list for 4 letter words
fourLetterCounter = []

#For loop running through Dracula text to count all for letter words
for word in draculaText:
  if(len(word) == 4 and word not in fourLetterCounter):
    fourLetterCounter.append(word)

#print results 
print(f"There are {len(fourLetterCounter)} four letter words in Dracula")
    
##Find word used the most and show how many times it is used

#blank value for king word and king count
kingWord = ""
kingCount = 0

#For loop running through dict. Dracula comparing each value to each other value to find the highest 
for key, value in draculaDict.items():
  if value > kingCount:
    kingCount = value
    kingWord = key

#print results 
print()
print(f"The word that appears the most in Dracula is '{kingWord.upper()}', appearing {kingCount} times")

##Show all words that appear over 500 times

#print intro line
print()
print("The following words appear more than 500 times: ")

#For loop running though dict. Dracula finding each value over 500
for key, value in draculaDict.items():
  if value >= 500:
    print()
    print(f"{key.lower()} : {value}")

