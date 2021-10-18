

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

#%timeit formal_list = list()
# 66.6 ns +- 3.18 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

#%timeit literal_list = []
# 16 ns +- 0.568 ns per loop (mean +- std. dev. of 7 runs, 100000000 loops each)


%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462