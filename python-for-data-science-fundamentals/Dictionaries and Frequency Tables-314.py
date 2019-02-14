## 1. Storing Data ##

content_ratings = {'4+': 4433, '9+':987, '12+':1155, '17+':622}

over_4 = content_ratings['4+']
over_9 = content_ratings['9+']
over_12 = content_ratings['12+']
over_17 = content_ratings['17+']

top_genres = {
    'Games':3862,
    'Entertainment':535,
    'Education':453,
    'Photo & Video': 349, 
    'Utilities':248
}

number_of_gaming_apps = top_genres['Games']

## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}

content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']

top_genres = {}

top_genres['Games'] = 3862
top_genres['Entertainment'] = 535
top_genres['Education'] = 453
top_genres['Photo & Video'] = 349
top_genres['Utilities'] = 248

n_apps_education = top_genres['Education']


## 6. Checking for Membership ##

content_ratings = {'4+':4433, '9+':987, '12+':1155,
                  '17+':622}

is_in_dictionary_1 = '4+' in content_ratings

is_in_dictionary_2 = '20+' in content_ratings

is_in_dictionary_3 = 4433 in content_ratings

is_in_dictionary_4 = 987 in content_ratings

if '17+' in content_ratings:
    result = "'17+' exists in content_ratings"

print(result)

## 7. Counting with Dictionaries ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = csv.reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+':0, '9+':0, '12+':0, '17+':0}

for app in apps_data[1:]:
    c_rating = app[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1

print(content_ratings)

## 8. Finding the Unique Values ##

content_ratings = {}

for app in apps_data[1:]:
    c_rating = app[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
        
print(content_ratings)

genre_counting = {}

for g in apps_data[1:]:
    prime_genre = g[11]
    if prime_genre in genre_counting:
        genre_counting[prime_genre] += 1
    else:
        genre_counting[prime_genre] = 1

most_common_genre = "Games"

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197

for iteration in content_ratings:
    content_ratings[iteration] /= total_number_of_apps
    content_ratings[iteration] *= 100

percentage_17_plus = content_ratings['17+']

percentage_15_allowed = content_ratings['4+'] + content_ratings['12+'] + content_ratings['9+']

for i in genre_counting:
    genre_counting[i] /= total_number_of_apps
    genre_counting[i] *= 100
    
percentage_games = genre_counting['Games']

percentage_non_games = 0

for ng in genre_counting:
    if genre_counting[ng] != genre_counting['Games']:
        percentage_non_games += genre_counting[ng]


## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for key in content_ratings:
    propo = content_ratings[key] / total_number_of_apps
    c_ratings_proportions[key] = propo
    
for key in c_ratings_proportions:
    perce = c_ratings_proportions[key] * 100
    c_ratings_percentages[key] = perce
    
genre_proportions = {}
genre_percentages = {}

for key in genre_counting:
    propo = genre_counting[key] / total_number_of_apps
    genre_proportions[key] = propo
    
    genre_percentages[key] = genre_proportions[key] * 100
    
    
    


## 12. Frequency Tables for Numerical Columns ##

data_sizes = []

for app in apps_data[1:]:
    size = float(app[2])
    data_sizes.append(size)
    
min_size = min(data_sizes)
max_size = max(data_sizes)


## 13. Filtering for the Intervals ##

r_count_total = []

for r in apps_data[1:]:
    rating_c = float(r[5])
    r_count_total.append(rating_c)
    
min_rating = min(r_count_total)
max_rating = max(r_count_total)

'''intervals:
    0 to 50000
    50001 to 100000
    100001 to 150000
    150001 to 200000
    200001+ 
'''

tot_r_count = {'0 to 50k': 0, '50k to 100k':0, '100k to 150k':0,
               '150k to 200k':0, '200k+':0}

for tot in r_count_total:
    if tot <= 50000:
        tot_r_count['0 to 50k'] += 1
    elif 50000 < tot <= 100000:
        tot_r_count['50k to 100k'] += 1
    elif 100000 < tot <= 150000:
        tot_r_count['100k to 150k'] += 1
    elif 150000 < tot <= 200000:
        tot_r_count['150k to 200k'] += 1
    elif tot > 200000:
        tot_r_count['200k+'] += 1
        
double_checking = {'0 to 50k': 0, '50k to 100k':0, '100k to 150k':0,
               '150k to 200k':0, '200k+':0}

for tot in apps_data[1:]:
    tc = float(tot[5])
    
    if tc <= 50000:
        double_checking['0 to 50k'] += 1
    elif 50000 < tc <= 100000:
        double_checking['50k to 100k'] += 1
    elif 100000 < tc <= 150000:
        double_checking['100k to 150k'] += 1
    elif 150000 < tc <= 200000:
        double_checking['150k to 200k'] += 1
    elif tc > 200000:
        double_checking['200k+'] += 1
    
    

tot_r_count
double_checking

    