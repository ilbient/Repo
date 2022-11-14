#Program na ulahcenie vyrovnania, ktore robim kazdy tyzden 
#Krok cislo jedna, urcit aktualny datum

#Import kniznic
from datetime import datetime

#Vypise aktualny den v pozadovanom formate
today = datetime.today().strftime('%d.%m.%Y')
print("Dnesny datum je: ", today)


