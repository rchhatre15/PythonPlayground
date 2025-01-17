import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
cipher = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ")
val = [cipher[letter.upper()] for letter in word]
print(val)

