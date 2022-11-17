
# importing datetime module
import datetime
  
#Zistenie poctu suborov v priecinku, ak je 0 potom vytvorit novu Databazu!






# datetime.datetime.now() to get 
# current date as filename.
filename = datetime.datetime.now()
  
# create empty file
def create_file():
    # Function creates an empty file
    # %d - date, %B - month, %Y - Year
    with open(filename.strftime("Database")+".csv", "w") as file:
        file.write("")
  
# Driver Code
print ('Subor vytvoreny!')
create_file()