import random


hangman_words = {
    "A fruit that's red or green": "apple",
    "A place to read books": "library",
    "A musical instrument with strings": "guitar",
    "A large mammal with a trunk": "elephant",
    "A device used to compute and work": "laptop",
    "A person who travels to space": "astronaut",
    "A shape that changes patterns as you turn it": "kaleidoscope",
    "The study of the human mind": "psychology",
    "An object used to view very small things": "microscope",
    "A game played to guess letters of a hidden word": "hangman",
    "A flightless bird often found in Antarctica": "penguin",
    "A yellow tropical fruit with a crown of leaves": "pineapple",
    "A reptile that can change colors": "chameleon",
    "A natural satellite of the Earth": "moon",
    "The largest ocean on Earth": "pacific",
    "A small insect known for its colonies and teamwork": "ant",
    "A tool used to cut wood": "saw",
    "A common pet known for purring": "cat",
    "A person who writes code": "programmer",
    "A place where planes take off and land": "airport",
    "The process of creating artwork with paint": "painting",
    "A bird known for its colorful tail feathers": "peacock",
    "The human body's organ responsible for pumping blood": "heart",
    "A mammal known for living in the ocean and being playful": "dolphin",
    "A portable device for making calls and sending messages": "smartphone"
}

hint, word = random.choice(list(hangman_words.items()))
lenght=len(word)
str=["_"]
while(lenght>1):
    str.append("_")
    lenght=lenght-1
ans=list(word)
#print(ans)
i=7
flag=0
while i>=0:
    if "_" not in str:
        flag=1
        break
    print(f"YOU HAVE {i} LIFE LEFT")
    print(f"Hint: {hint}")
    input_letter = input("Enter your guess: ").lower()
    if(input_letter in word):
        j=-1
        for x in ans:
            j=j+1
            if input_letter == x:
                str[j]=input_letter
        print(str)
    else:
        i=i-1
 
if flag== 1:
    print("YOU WIN")
else:
    print("YOU LOSS")
    


