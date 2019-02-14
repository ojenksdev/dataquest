## 1. Introduction ##

import csv
f = open('potus_visitors_2015.csv')
f_read = csv.reader(f)
potus = list(f_read)
potus = potus[1:]

## 3. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16)

microsoft_founded = dt.datetime(1975, 4, 4)

man_on_moon = dt.datetime(1969, 7, 20, 20, 17)

jfk_shot = dt.datetime(1963, 11, 22, 12, 30)

## 4. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
import datetime as dt

date_format = "%m/%d/%y %H:%M"

for row in potus:
    start_date = row[2]
    converted_date = dt.datetime.strptime(start_date, date_format)
    row[2] = converted_date
    
 



## 5. Using Strftime to format dates ##

visitors_per_month = {}

for row in potus:
    appt_date = row[2]
    d_string = appt_date.strftime("%B, %Y")
    if d_string in visitors_per_month:
        visitors_per_month[d_string] += 1
    else:
        visitors_per_month[d_string] = 1


## 6. The Time Class ##

appt_times = {}

for row in potus:
    dt_appt = row[2]
    new_time = dt_appt.time()
    if new_time in appt_times:
        appt_times[new_time] += 1
    else:
        appt_times[new_time] = 1
        
min_time = min(appt_times)
max_time = max(appt_times)


## 7. The Date Class ##

date_freq = {}

for row in potus:
    dt_appt = row[2]
    dt_date = dt_appt.date()
    if dt_date in date_freq:
        date_freq[dt_date] += 1
    else:
        date_freq[dt_date] = 1
        
max_v_num = 0

for key, value in date_freq.items():
    if value > max_v_num:
        max_v_num = value
        max_v_date = key
        

            

## 8. Calculations with Dates and Times ##

import datetime as dt

date_format = "%m/%d/%y %H:%M"

for row in potus:
    apt_end = row[3]
    dt_end = dt.datetime.strptime(apt_end, date_format)
    row[3] = dt_end

appt_lengths = []

for row in potus:
    appt_start = row[2]
    appt_end = row[3]
    appt_length = appt_end - appt_start
    appt_lengths.append(appt_length)
    
min_length = min(appt_lengths)
print(min_length)
max_length = max(appt_lengths)
print(max_length)
total_lengths = sum(appt_lengths, dt.timedelta(0))
avg_length = total_lengths / len(appt_lengths)


                       


## 9. Challenge: How far ahead are appointments made ##

import datetime as dt

lead_times = []

for row in potus:
    apt_made = row[1]
    ap_dt = dt.datetime.strptime(apt_made, "%Y-%m-%dT%H:%M:%S")
    apt_date = row[2]
    lead_time = apt_date - ap_dt
    lead_times.append(lead_time)

max_time = max(lead_times)
min_time = min(lead_times)
total_times = sum(lead_times, dt.timedelta(0))
avg_time = total_times / len(lead_times)

    

## 10. Challenge: Create an Appointment Summary Function ##

import datetime as dt

def appt_summary(year, month, day):
    target = dt.date(year, month, day)
    print("Appointments for {:%A %B %-d, \
          %Y}:\n".format(target))
          
    template = "{} at {:%-I:%M %p}."
    for row in potus:
        visitee = row[0].title()
        appt_time = row[2]
          
        if appt_time.date() == target:
            print(template.format(visitee, appt_time))
        

    
appt_summary(2015, 5, 20)    
    
    
    

## 11. Epoch Time ##

import datetime as dt

epochs = [
           ['first', 1139444034],
           ['second', 1430583565],
           ['third', 1318037820],
           ['fourth', 751652064]
         ]

for e in epochs:
    ep = e[1]
    epo_ts = dt.datetime.fromtimestamp(e[1])
    e[1] = epo_ts
    
