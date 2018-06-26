## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [apple * 2 for apple in apple_prices]
apple_prices_lowered = [apple - 100 for apple in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for row in legislators:
    if row[3] == "F":
        if row[7] > 1940:
            name = row[1]
            if name in name_counts:
                name_counts[name] = name_counts[name] + 1
            else:
                name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for val in values:
    check = val is not None and val > 30
    checks.append(check)
        

## 8. Highest Female Name Count ##

max_value = None

for name in name_counts:
    count = name_counts[name]
    if max_value is None or count > max_value:
        max_value = count
        

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for plant, val in plant_types.items():
    print(plant)
    print(val)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for key, val in name_counts.items():
    if val == 2:
        top_female_names.append(key)
        

## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = {}

for row in legislators:
    if row[3] == "M":
        if row[7] > 1940:
            name = row[1]
            if name in male_name_counts:
                male_name_counts[name] = male_name_counts[name] + 1
            else:
                male_name_counts[name] = 1
                
highest_male_count = None

for name in male_name_counts:
    count = male_name_counts[name]
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count
        
for key, val in male_name_counts.items():
    if val == highest_male_count:
        top_male_names.append(key)


