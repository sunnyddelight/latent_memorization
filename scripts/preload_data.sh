for i in $(seq 130 10 350)
do
    echo $i
    ID=$i python preload_data_models.py
done
