# Define the exponential transformation
exp_tr = lambda x: np.exp(-x.mean()*x) * x.mean()

# Group the data according to the time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_exp_group = restaurant_grouped['tip'].transform(exp_tr)
print(restaurant_exp_group.head())

zscore = lambda x: (x - x.mean()) / x.std()

# Apply the transformation
poker_trans = poker_grouped.transform(zscore)
print(poker_trans.head())

# Group both objects according to smoke condition
restaurant_nan_grouped = restaurant_nan.groupby('smoker')

# Store the number of present values
restaurant_nan_nval = restaurant_nan_grouped['tip'].count()

# Print the group-wise missing entries
print(restaurant_nan_grouped['total_bill'].count() - restaurant_nan_nval)


# Define the lambda function to fill na
missing_trans = lambda x: x.fillna(x.median())

# Define the lambda function
missing_trans = lambda x: x.fillna(x.median())

# Group the data according to time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_impute = restaurant_grouped.transform(missing_trans)
print(restaurant_impute.head())

# Filter the days where the count of total_bill is greater than $40
total_bill_40 = restaurant_data.groupby('day').filter(lambda x: x['total_bill'].count() > 40)

# Print the number of tables where total_bill is greater than $40
print('Number of tables where total_bill is greater than $40:', total_bill_40.shape[0])

# Filter the days where the count of total_bill is greater than $40
total_bill_40 = restaurant_data.groupby('day').filter(lambda x: x['total_bill'].count() > 40)

# Select only the entries that have a mean total_bill greater than $20
total_bill_20 = total_bill_40.groupby('day').filter(lambda x : x['total_bill'].mean() > 20)

# Print days of the week that have a mean total_bill greater than $20
print('Days of the week that have a mean total_bill greater than $20:', total_bill_20.day.unique())