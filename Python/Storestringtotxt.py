#Priklad na ulozenie stringu do txt suboru
# Writing a Single Line to a Text File
text = 'Tento text chcem ulozit do .txt suboru'

with open('Python\MyFile.txt', 'w') as f:
    f.write(text)

