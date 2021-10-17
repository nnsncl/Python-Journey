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

start_time = time.time()

# Replace ethnicities as instructed
names['Ethnicity'].replace(['ASIAN AND PACI','BLACK NON HISP', 'WHITE NON HISP'], ['ASIAN AND PACIFIC ISLANDER','BLACK NON HISPANIC','WHITE NON HISPANIC'], inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))

# Replace Royal flush or Straight flush to Flush
poker_hands.replace({'Straight flush':'Flush', 'Royal flush':'Flush'}, inplace=True)
print(poker_hands['Explanation'].head())

# Replace the number rank by a string
names['Rank'].replace({1:'FIRST', 2:'SECOND', 3:'THIRD'}, inplace=True)
print(names.head())