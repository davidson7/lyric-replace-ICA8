#Please use 1 late day for this assignment
#Dana Davidson
#2299509
#ddavidson@chapman.edu
#230-08
#ICA8


def most_word(text_file):
    
    occur = {}
    for line in text_file:
        
        words = line.split()
        
        for w in words:
            if w in occur:
                occur[w] += 1
            else:
                occur[w] = 1
    most_often = next(iter(occur))
    
    return most_often


    

text_file = open("lyrics2.txt","r")

word1 = most_word(text_file)

text_file.close()

user_word = input("Replace the most common word with:")
lines = []
text_file = open("lyrics2.txt", "r")
for line in text_file:

    words = line.split()

    for w in words:
        if w == word1:
            line = line.replace(w, user_word, 1)

    lines.append(line)
    

write_file = open("new_lyrics.txt", "w")
write_file.writelines(lines)

write_file.close()
text_file.close()
