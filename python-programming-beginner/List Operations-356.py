## 2. Parsing the File ##

f = open("la_weather.csv", "r")
wd = f.read()
rows = wd.split('\n')

weather_data = []

for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)
    

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for item in weather_data:
    value = item[1]
    weather.append(value)
    

## 4. Counting the Items in a List ##

count = 0

for i in weather:
    count += 1 
    

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for w in weather_types:
    found = w in new_weather
    weather_type_found.append(found)
    
        