
# importing datetime module
# import datetime
import os


#Zistenie poctu suborov v priecinku

APP_FOLDER = 'Python\Files'
totalFiles = 0
for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for Files in files:
        totalFiles += 1

print('Total number of files',totalFiles)
  

# if totalFiles == 1: 
#     print os.listdir("""Python\Files""")
# else:
#     print ('Niekde sa stala chyba')

# #Zistenie poctu suborov v priecinku, ak je 0 potom vytvorit novu Databazu!


# # datetime.datetime.now() to get 
# # current date as filename.
# filename = (datetime.datetime.now())
  
# # create empty file
# def create_file():
#     # Function creates an empty file
#     with open(filename.strftime("Python\Files\Database")+".csv", "w") as file:
#         file.write("")
  
# # Driver Code
# print ('Subor vytvoreny!')
# create_file()


