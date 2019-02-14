## 1. Functions ##

list_1 = [1, 8, 10, 9, 7, 5, 9, 1, 8, 4, 5, 3, 3, 2, 0, 9,
          6, 5, 2, 6, 9, 8, 8, 1, 2, 8, 0, 3, 4, 8, 6, 2,
          2, 6, 9, 2, 9, 9, 1, 8, 10, 10, 2, 2, 3, 6, 10,
          9, 8, 7]

sum_1 = 0
for num in list_1:
    sum_1 += num
    

list_2 = [678, 685, 870, 927, 176, 893, 366, 780, 261, 815,
          204, 946, 465, 670, 19, 632, 182, 46, 13, 202, 566,
          609, 481, 18, 992, 490, 878, 398, 942, 694, 763,
          986, 825, 843, 798, 658, 426, 613, 14, 369, 638,
          831, 585, 608, 588, 418, 117, 18, 755, 680]

sum_2 = 0
for num in list_2:
    sum_2 += num

list_3 = [4444, 8897, 6340, 9896, 4835, 4324, 10000, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280, 1318,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 3717,
          5929, 7061, 4214, 5127, 6171, 3782, 3798, 8970,
          3102, 9771, 746, 4974, 7996, 3122, 1362, 8140, 4412,
          1390, 2240, 3063, 4228, 7030, 8479, 5081, 66]
sum_3 = 0
for num in list_3:
    sum_3 += num
    

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
n_unique = len(content_ratings)

## 3. Creating Our Own Functions ##

def square(a_number):
    squared_number = a_number * a_number
    return squared_number

squared_10 = square(a_number=10)
squared_16 = square(16)

def square_2(a_number):
    squared_number = a_number ** 2
    return squared_number

squared_20 = square_2(20)
squared_100 = square(100)

def add_10(num):
    num += 10
    return num

add_30 = add_10(30)
add_90 = add_10(90)


## 5. Parameters and Arguments ##

a_list = [2, 1, 'data point', 'five', 89, 1, 'zero', True, 2.332]
a_dictionary = {1: 'Name', 2: True, 3: [1,2,3], 4: 9.2221, 5: 5}

def square(num):
    return num * num

squared_6 = square(6)
squared_11 = square(11)

def len_2(iterable):
    length = 0
    for i in iterable:
        length += 1
    return length

list_length = len_2(a_list)

dictionary_length = len_2(a_dictionary)




## 6. Extract Values From Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(column):
    '''extracts column from dataset list'''
    new_list = []
    for ldata in apps_data[1:]:
        new_data = ldata[column]
        new_list.append(new_data)
    return new_list

def freq_table(a_list):
    '''builds a frequency table from a list'''
    f_table = {}
    for t_data in a_list:
        if t_data in f_table:
            f_table[t_data] += 1
        else:
            f_table[t_data] = 1
    return f_table

content_ratings = extract(10)
content_ratings_ft = freq_table(content_ratings)

ratings = extract(7)
ratings_ft = freq_table(ratings)

genres = extract(11)
genres_ft = freq_table(genres)


       

## 8. Writing a Single Function ##

def freq_table(column):
    f_table = {}
    for col in apps_data[1:]:
        t_data = col[column]
        if t_data in f_table:
            f_table[t_data] += 1
        else:
            f_table[t_data] = 1
    return f_table

content_ratings_ft = freq_table(10)
ratings_ft = freq_table(7)
genres_ft = freq_table(11)

    

## 9. Reusability and Multiple Parameters ##

def freq_table(index, data_set):
    frequency_table = {}
    
    for row in data_set:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

content_ratings_ft = freq_table(10, apps_data[1:])
ratings_ft = freq_table(7, apps_data[1:])
genres_ft = freq_table(11, apps_data[1:])

                    

## 10. Keyword and Positional Arguments ##

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1


content_ratings_ft = freq_table(apps_data[1:], 10)

ratings_ft = freq_table(data_set=apps_data[1:], index=7)

genres_ft = freq_table(index=11, data_set=apps_data[1:])

      

## 11. Combining Functions ##

def extract(index, data_set):
    d_list = []
    for col in data_set:
        new_d = col[index]
        d_list.append(new_d)
    return d_list

def find_sum(a_list):
    l_sum = 0
    for num in a_list:
        l_sum += float(num)
    return l_sum

def find_length(a_list):
    len_list = len(a_list)
    return len_list

def mean(index, data_set):
    new_list = extract(index, data_set)
    return find_sum(new_list) / find_length(new_list)

avg_price = mean(4, apps_data[1:])

avg_rating = mean(7, apps_data[1:])

    

## 12. Debugging Functions ##

def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)