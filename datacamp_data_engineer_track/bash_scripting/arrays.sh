# Create a normal array with the mentioned elements using the declare method
declare -a capital_cities

# Add (append) the elements
capital_cities[0]="Sydney"
capital_cities[1]="Sydney"
capital_cities+=("Paris")

# The array has been created for you
capital_cities=("Sydney" "Albany" "Paris")

# Print out the entire array
echo ${capital_cities[@]}

# Print out the array length
echo ${#capital_cities[@]}

# Create empty associative array
declare -A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn"
model_metrics[model_f1]=0.82