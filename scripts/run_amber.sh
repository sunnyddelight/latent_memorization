for j in $(seq 120 10 350)
do
    for i in {0..15}
    do
        sbatch single_runner_amber.sbatch $j $i
    done
done
