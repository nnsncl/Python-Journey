# Import the datetime object from datetime
from datetime import datetime

# Iterate over the dates_list 
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')
    
    # Print each date_dt
    print(date_dt)

# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(datetime.strftime(item, ('%m/%d/%Y')))
    
    # Print out the record as an ISO standard string
    print(item.isoformat())