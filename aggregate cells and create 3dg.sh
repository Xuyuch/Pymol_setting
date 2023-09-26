conda activate mapping
PARENT_DIR="/home/yuchen/Raw_data_Dong/OPC_15groups"
for sub_dir in "$PARENT_DIR"/*/; do
    # Ensure that it's a directory before proceeding
    if [ -d "$sub_dir" ]; then
        # Process each subdirectory in the background
        (
            echo "Starting processing for directory: $sub_dir"

            # Create the "imputed" directory within sub_dir
            mkdir -p "${sub_dir}/imputed"

            # Change to the subdirectory
            cd "$sub_dir" || continue

            # Process each .pairs.gz file
            for file in *.pairs.gz; do
                base_name="${file%.*}"
                ~/pipeline/hickit/hickit -i "$file" -u -o - | bgzip > "imputed/${base_name}.impute.pairs.gz"
            done

            echo "Finished processing for directory: $sub_dir"
        ) &
    fi
done

wait  # This will ensure the script waits for all background processes to finish before moving on

echo "All directories have been processed!"

/home/yuchen/R_script/merge-pairs.sh oligo ./*pairs.gz
~/pipeline/hickit/hickit -i oligo.pairs.gz -Sr1m -c1 -r10m -c5 -b4m -b1m -b200k -D5 -b50k -D5 -b20k -O oligo.3dg
awk 'BEGIN {OFS="\t"} { $3=$3*30; $4=$4*30; $5=$5*30; print }' OPC_$sub_file.3dg > C_OPC_$sub_file.3dg
grep -v "^#" 30_OPC_$sub_file.3dg | sed 's/a/(pat)/g; s/b/(mat)/g' >30_OPC_$sub_file.dip-c.3dg


PARENT_DIR="/home/yuchen/Raw_data_Dong/OPC_15groups"  # replace with your actual parent directory path

cd "$PARENT_DIR"

for sub_dir in *; do
    if [ -d "$sub_dir/imputed" ]; then
        (
            cd "$sub_dir/imputed"
            ~/R_script/merge-pairs.sh "OPC_$sub_dir" ./*pairs.gz
            ~/pipeline/hickit/hickit -i "OPC_$sub_dir.pairs.gz" -Sr1m -c1 -r10m -c5 -b4m -b1m -b200k -D5 -b50k -D5 -b20k -O "OPC_$sub_dir.3dg"
            awk 'BEGIN {OFS="\t"} { $3=$3*30; $4=$4*30; $5=$5*30; print }' "OPC_$sub_dir.3dg" > "30_OPC_$sub_dir.3dg"
            grep -v "^#" "30_OPC_$sub_dir.3dg" | sed 's/a/(pat)/g; s/b/(mat)/g' >"30_OPC_$sub_dir.dip-c.3dg"
        ) &
    fi
done

wait  # This will wait for all background processes to finish

echo "All parallel processes are finished!"

conda deactivate
conda activate py2_env
PARENT_DIR="/home/yuchen/Raw_data_Dong/OPC_15groups"
cd "$PARENT_DIR"

for sub_dir in *; do
    if [ -d "$sub_dir/imputed" ]; then
        (
            cd "$sub_dir/imputed"
            python ~/pipeline/dip-c/dip-c color -n ~/pipeline/dip-c/color/mm10.chr.txt "30_OPC_$sub_dir.dip-c.3dg" |python ~/pipeline/dip-c/dip-c vis -c /dev/stdin "30_OPC_$sub_dir.dip-c.3dg"> "30_OPC_$sub_dir.n.cif"
            python ~/pipeline/dip-c/dip-c exp "30_OPC_$sub_dir.dip-c.3dg"> "30_OPC_$sub_dir.exp.3dg" 2> "30_OPC_$sub_dir.exp.py"
            python ~/pipeline/dip-c/dip-c color -n ~/pipeline/dip-c/color/mm10.chr.txt "30_OPC_$sub_dir.exp.3dg" |python ~/pipeline/dip-c/dip-c vis -c /dev/stdin  "30_OPC_$sub_dir.exp.3dg"> "30_OPC_$sub_dir.exp.n.cif"
        ) &
    fi
done

python ~/pipeline/dip-c/dip-c color -n ~/pipeline/dip-c/color/mm10.chr.txt 30_oligo.dip-c.3dg |python ~/pipeline/dip-c/dip-c vis -c /dev/stdin 30_oligo.dip-c.3dg > 30_oligo.n.cif
python ~/pipeline/dip-c/dip-c exp 30_oligo.dip-c.3dg > 30_oligo.exp.3dg 2> 30_oligo.exp.py
python ~/pipeline/dip-c/dip-c color -n ~/pipeline/dip-c/color/mm10.chr.txt 30_oligo.exp.3dg |python ~/pipeline/dip-c/dip-c vis -c /dev/stdin  30_oligo.exp.3dg> 30_oligo.exp.n.cif

#grep -v "^#" 30\*oligo_7cell.3dg | sed 's/a/(pat)/g; s/b/(mat)/g; s/X/X(mat)/g; s/Y/Y(pat)/g' >30_oligo_7cell.dip-c.3dg


