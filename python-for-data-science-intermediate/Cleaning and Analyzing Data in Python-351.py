## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)

## 2. Reading our MoMA Data Set ##

import csv

f = open('artworks.csv')

reader = csv.reader(f)

moma = list(reader)

moma = moma[1:]



## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

# remove parentheses from the nationality column
for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    row[2] = nationality
    
    genre = row[5]
    genre = genre.replace('(', '')
    genre = genre.replace(')', '')
    row[5] = genre
    


## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    # convert the gender to title case
    gender = gender.title()
    # if there is no gender, set a descriptive value
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    
for row in moma:
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality
    
    

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    date = date.replace("(", "")
    date = date.replace(")", "")
    if date != "":
        date = int(date)
    return date

for row in moma:
    begin_d = row[3]
    end_d = row[4]
    converted_bd = clean_and_convert(begin_d)
    converted_ed = clean_and_convert(end_d)
    row[3] = converted_bd
    row[4] = converted_ed
    
   

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1870-79", "1929",
             "1913\\-1923", "(1951)", "1994",
             "1934", "c. 1915", "2009", "1978",
             "1947", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "1964\\-65", "c. 1955.",
             "c. 1970's", "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(a_str):
    for bad in bad_chars:
        a_str = a_str.replace(bad, '')
    a_str = a_str.strip()
    return a_str

stripped_test_data = []

for d in test_data:
    cl_str = strip_characters(d)
    cl_str = cl_str.strip()
    stripped_test_data.append(cl_str)



    

## 8. Parsing Numbers from Complex Strings, Part Two ##

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    string = string.strip()
    return string

stripped_test_data = ['1912', '1870-79', '1929',
                      '1913-1923', '1951', '1994', 
                      '1934', '1915', '2009', '1978',
                      '1947', '1995', '1912', '1988',
                      '2002', '1957-1959', '1964-65',
                      '1955', '1970', '1990-1999']

# 1 check to see if dash exists, split on that
# 2 add first two digits from first string to start of 2nd string
# 3 convert the numbers to int and avg by adding and / by 2
# 4 Use round() to round values
# if not range, convert to int



def process_date(date):
    if "-" in date:
        s_date = date.split('-')
        d_one = s_date[0]
        d_two = s_date[1]
        if len(d_two) == 2:
            d_two = d_one[:2] + d_two 
        date = (int(d_one) + int(d_two)) / 2
        date = round(date)
    else:
        date = int(date)
    return date

processed_test_data = []

for d in stripped_test_data:
    d = process_date(d)
    processed_test_data.append(d)

for data in moma:
    date = data[6]
    date = strip_characters(date)
    date = process_date(date)
    data[6] = date
    
    
    
                
                


## 9. Summarizing Numeric Data ##

def calculate_decades(decades):
    decade_ranges = {}
    for d in decades:
        if d in decade_ranges:
            decade_ranges[d] += 1
        else:
            decade_ranges[d] = 1
    return decade_ranges
decades = []

for data in moma:
    art_year = data[6]
    artist_birth = data[3]
    try: 
        artist_age = art_year - artist_birth
        if (art_year - artist_birth) < 20:
            artist_age = 'Unknown'
        elif (art_year - artist_birth) >= 20:
            artist_age = str(artist_age)[:-1] + "0s"
    except:
        artist_age = "Unknown"
    decades.append(artist_age)

decade_summary = calculate_decades(decades)
        
        
    

## 10. String Formatting ##

def parse_birth_year(artist):
    """
    For a given artist, return the birth year on the first
    artwork found.
    """
    for row in moma:
        if row[1] == artist:
            birth_date = row[3]
            if birth_date == "":
                birth_date = "unknown"
            return birth_date
        
def artist_summary(name):
    '''The function takes the name of an artist and 
    sprints a string with their birth year'''
    
    birth_year = parse_birth_year(name)
    artist_summary = "{}'s birth year is {}".format(name.title(), birth_year)
    print(artist_summary)
    
artist_summary("Louise Bourgeois")

## 11. Formatting Numbers Inside Strings ##

# create frequency table dists for both the number
# of artists and number of artworks by gender,
# excluding unknown/other genders
gender_artworks_count = {}
gender_artist_list = {}

for row in moma:
    gender = row[5]
    artist = row[1]
    if gender != "Gender Unknown/Other":
        if gender in gender_artworks_count:
            gender_artworks_count[gender] += 1
            if artist not in gender_artist_list[gender]:
                gender_artist_list[gender].append(artist)
        else:
            gender_artworks_count[gender] = 1
            gender_artist_list[gender] = [artist]


# Combine the two frequency tables into a list
# of lists which summarizes the data
gender_data = []

for gender in gender_artworks_count:
    artworks_count = gender_artworks_count[gender]
    artists_count = len(gender_artist_list[gender])
    average_works = artworks_count / artists_count
    gender_data.append([gender, artworks_count, average_works])
   
for g in gender_data:
    summarizes = "There are {:,} artworks by {} artists \
    at an average of {:.1f} each.".format(g[1], g[0], g[2])
    print(summarizes)


## 12. Creating a Function to Summarize Data ##

def widest_key_value(dictionary):
    """
    Returns the width of the string representation
    for the longest key and value in the dict.
    """
    max_key_width = 0
    max_val_width = 0

    for key, value in dictionary.items():
        key_width = len(str(key))
        val_width = len(str(value))
        
        if key_width > max_key_width:
            max_key_width = key_width
        
        if val_width > max_val_width:
            max_val_width = val_width

    return max_key_width, max_val_width

def moma_freq_table(index):
    '''Takes any index from the list and returns
    a formatted frequency table with the data.'''
    moma_fq_tb = {}
    
    for data in moma:
        n_data = data[index]
        if n_data in moma_fq_tb:
            moma_fq_tb[n_data] += 1
        else:
            moma_fq_tb[n_data] = 1
        
        key_width, val_width = key_width, val_width =           widest_key_value(moma_fq_tb)
        val_width += 1
        
    for key, value in sorted(moma_fq_tb.items()):
        print("{:<{}} : {:>{},}".format(key, key_width, value, val_width))
                    
moma_freq_table(7)