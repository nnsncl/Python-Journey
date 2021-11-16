for filename in $@
do
    head -n 2 $filename | tail -n 1
    tail -n 1 $filename
done