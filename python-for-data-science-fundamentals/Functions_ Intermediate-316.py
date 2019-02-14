## 2. Default Arguments ##

import csv

def open_dataset(csv_file="AppleStore.csv"):
    f = open(csv_file)
    f_read = csv.reader(f)
    f_list = list(f_read)
    return f_list
    
apps_data = open_dataset()



## 3. The Official Python Documentation ##

one_decimal = round(3.43,1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2225227, 5)



## 4. Multiple Return Statements ##

def open_dataset(header, file_name='AppleStore.csv'):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header == True:
        return data[1:]
    
    return data

apps_data = open_dataset(header=True)

## 5. Returning Multiple Variables ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]
    else:
        return data
    
all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

## 6. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:], 
    else:
        return data
    
header, apps_data = open_dataset()


## 7. Functions — Code Running Quirks ##

def print_constant():
    x = 3.14
    print(x)
    
   
print_constant()
print(x)

## 8. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e ** x

result = exponential(5)
print(e) # will show "mathematical constant" as this is global scope

def divide():
    print(a_sum)
    print(length)
    return a_sum / length

result_2 = divide()




## 9. Scopes — Searching Order ##

file_name = 'AppleStore.csv'

def open_iOS_dataset():       
    global apps_data 
    global header_row
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    apps_data = data[1:]
    header_row = data[0]
    
open_iOS_dataset()
header_row
first_five = apps_data[:5]

## 10. Functions — More Quirks ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

def relative_freqs(freq_table):
    total_sum = 0
    for val in freq_table:
        count = freq_table[val]
        total_sum += count
        
    for val in freq_table:
        freq_table[val] = (freq_table[val] / total_sum) * 100
            
    return freq_table
    
c_ratings_percentages = relative_freqs(content_ratings)

print(content_ratings)

changed = True
        
        
        

## 11. Mutable and Immutable Types ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

def relative_freqs(freq_table):
    freq_table = freq_table.copy()
    total = 0 
    for key in freq_table:
        count = freq_table[key]
        total += count
    
    for key in freq_table:
        freq_table[key] = (freq_table[key] / total) * 100
    
    return freq_table

print(content_ratings)
changed = False
checking_code = relative_freqs(content_ratings)