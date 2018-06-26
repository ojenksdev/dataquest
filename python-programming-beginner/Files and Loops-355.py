## 1. Opening Files ##

f = open("crime_rates.csv", "r")

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows[:5])

## 5. Practice - Loops ##

ten_rows = rows[0:10]

for i in ten_rows:
    print(i)
    

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

final_data = []

for row in rows:
    r = row.split(',')
    final_data.append(r)
print(final_data[:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)

cities_list = []

for city in five_elements:
    c = city[0]
    cities_list.append(c)
    


## 9. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
cities_list = []

for city in final_data:
    c = city[0]
    cities_list.append(c)
    

## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

int_crime_rates = []

for row in rows:
    r = row.split(",")
    rint = int(r[1])
    int_crime_rates.append(rint)
    