# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do  
    # Echo out each file
    echo $file
done

# Create a FOR statement on files in directory
for file in robs_files/*.py
do  
    # Create IF statement using grep
    if grep -q 'RandomForestClassifier' $file ; then
        # Move wanted files to to_keep/ folder
        mv $file to_keep/
    fi
done
