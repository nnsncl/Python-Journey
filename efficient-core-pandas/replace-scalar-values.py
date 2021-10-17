# Replace Class 1 to -2 
poker_hands['Class'].replace(1, -2, inplace=True)
# Replace Class 2 to -3
poker_hands['Class'].replace(2, -3, inplace=True)

print(poker_hands[['Class', 'Explanation']])


start_time = time.time()

# Replace all the entries that has 'FEMALE' as a gender with 'GIRL'
names['Gender'].replace('FEMALE', 'GIRL', inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))

start_time = time.time()

# Replace all non-Hispanic ethnicities with 'NON HISPANIC' using loc
names['Ethnicity'].loc[(names['Ethnicity'] == 'BLACK NON HISP') | 
                      (names['Ethnicity'] == 'BLACK NON HISPANIC') | 
                      (names['Ethnicity'] == 'WHITE NON HISP') | 
                      (names['Ethnicity'] ==  'WHITE NON HISPANIC')] = 'NON HISPANIC'

print("Time using .loc[]: sec".format(time.time() - start_time))


start_time = time.time()

# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].replace(['BLACK NON HISP', 'BLACK NON HISPANIC', 'WHITE NON HISP' , 'WHITE NON HISPANIC'], 'NON HISPANIC', inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))