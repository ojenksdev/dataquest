## 1. Overview ##

f = open("movie_metadata.csv", "r")
data = f.read()
data_split = data.split("\n")

movie_data = []

for row in data_split:
    r_split = row.split(",")
    movie_data.append(r_split)
    
print(movie_data[:5])

## 3. Writing Our Own Functions ##

def el_in_list(input_lst):
    d_list = []
    for e in input_lst:
        d_list.append(e[0])
    return d_list
    
movie_names = el_in_list(movie_data)
print(movie_names[:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
    
wonder_woman_usa = is_usa(wonder_woman)
avatar_film = is_usa(movie_data[1])
spect = is_usa(movie_data[3])
    


## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
def index_equals_str(input_lst, indx, input_str):
    if input_lst[indx] == input_str:
        return True
    else:
        return False
    
wonder_woman_in_color = index_equals_str(wonder_woman, 2, "Color")


## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst, index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt


num_of_us_movies = feature_counter(movie_data,6,"USA", header_row = True)
                               

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6, "Japan", header_row = True)
    num_color_films = feature_counter(input_lst,2, "Color", header_row = True)
    num_films_in_english = feature_counter(input_lst,5, "English", header_row = True)
    
    stat_dict = {"japan_films":num_japan_films,
                 "color_films":num_color_films,
                 "films_in_english":num_films_in_english
                }
    return stat_dict


summary = summary_statistics(movie_data)