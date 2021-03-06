## 2. Introduction to the Data ##

import csv

f = open("nfl_suspensions_data.csv", "r")

csvreader = csv.reader(f)

nfl_suspensions = list(csvreader)

nfl_no_header = nfl_suspensions[1:]

nfl_suspensions = nfl_no_header

years = {}

for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1
print(years)



## 3. Unique Values ##

unique_teams = []
unique_games = []

t_list = [unique_teams.append(row[1]) for row in nfl_suspensions]

unique_teams = set(unique_teams)

g_list = [unique_games.append(row[2]) for row in nfl_suspensions]

unique_games = set(unique_games)


print(unique_teams)
print(unique_games)





## 4. Suspension Class ##

class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]

third_suspension = Suspension(nfl_suspensions[2])

        
        

     

    

        
       
        

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        
        
class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
            
    def get_year(self):
        return(self.year)
    
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
            