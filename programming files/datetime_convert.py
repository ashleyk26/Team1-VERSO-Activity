from datetime import datetime
#Set date as a string
date_str = "2022-03-17 10:45:30"
#create a date object
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')
#Print the formatted date
print(formatted_date)
