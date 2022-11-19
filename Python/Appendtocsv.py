import os
import csv
import time

#Zistenie poctu suborov v priecinku

APP_FOLDER = 'Python\Files'
totalFiles = 0
for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for Files in files:
        totalFiles += 1

print('Total number of files',totalFiles)
  


x = time.strftime("%Y%m%d")
print ("Zadaj sumu na ucte TatraBanky")
tb = input()


with open(r'Python\Files\Database.csv', 'a', newline='') as csvfile:
    fieldnames = ['Datum','Suma']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'Datum':x, 'Suma':tb})
    print ("Udaje boli uspesne zapisane do csv suboru")
   #zistenie velkosti csv suboru
    file_size = os.path.getsize('Python\Files\Database.csv')
    print ("Nova velkost suboru je:" , file_size, " bytov")
