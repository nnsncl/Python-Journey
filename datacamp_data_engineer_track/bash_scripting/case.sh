# Create a CASE statement matching the first ARGV element
case $1 in
  # Match on all weekdays
  Monday|Tuesday|Wednesday|Thursday|Friday)
  echo "It is a Weekday!";;
  # Match on all weekend days
  Saturday|Sunday)
  echo "It is a Weekend!";;
  # Create a default
  * )
  echo "Not a day!";;
esac


# Use a FOR loop for each file in 'model_out/'
for file in tree_models/*
do
    # Create a CASE statement for each file's contents
    case $(cat $file) in
      # Match on tree and non-tree models
      *"Random Forest"*|*GBM*|*XGBoost*)
      mv $file tree_models/ ;;
      *KNN*|*Logistic*)
      rm $file ;;
      # Create a default
      * ) 
      echo "Unknown model in $file" ;;
    esac
done
