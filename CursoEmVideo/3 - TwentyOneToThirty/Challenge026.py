"""First and Last Occurrence of a String"""

print("Challenge 026")
print("Make a program that read a sentence from the keyboard and shows:")
print("> How many times appeared the letter 'A'.")
print("> In what position does it appear for the first time.")
print("> In what position does it appear for the last time.")

sentence = str(input('Type a sentence: ')).upper().strip()

print("The letter 'A' appear {} times in the sentence".format(sentence.count('A')))
print("The first letter 'A' appeared in the position {}".format(sentence.find('A') + 1))
print("The last letter 'A' appeared in the position {}".format(sentence.rfind('A') + 1))
