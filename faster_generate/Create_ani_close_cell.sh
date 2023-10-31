dir="/home/yuchen/Raw_data_Dong/OPC_new_bin/aggregate/filtered/3D_MARK2/test/test_new/exp_align1"

# Convert the list of .cif files into an array
files=($(ls $dir/*.cif))

# Loop through the files and start PyMOL in parallel
#!/bin/bash

max_jobs=5

for ((i=0; i<${#files[@]}-1; i++)); do
    file1=${files[$i]}
    file2=${files[$i+1]}
    order=$((i+1))
    
    # Start the process in the background
    ~/pipeline/pymol/pymol -c ~/R_script/pymol_settings/Slice_pymol_better_parameter.py -- -i1 $file1 -i2 $file2 -v ~/view.txt -O /home/yuchen/Raw_data_Dong/OPC_new_bin/aggregate/filtered/3D_MARK2/test/test_new/exp_align1/align1 -o $order -N 20 &

    # If the number of background jobs hits max_jobs, wait for any of them to finish
    if (( (i+1) % max_jobs == 0 )); then
        wait -n
    fi
done

# Wait for all remaining background jobs to finish
wait


wait # Wait for all background processes to finish
