for i in $(seq 10000 3000 43001)
do
    echo $i
    ID=$i python preload_data_models.py
done
