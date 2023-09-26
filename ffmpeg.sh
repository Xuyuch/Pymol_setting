ffmpeg -framerate 5 -i  -c:v libx264 -pix_fmt yuv420p -b:v 10M -s 1280x720 ./test.mp4
ffmpeg -i source_video.mp4 -c:v libx264 -profile:v high -pix_fmt yuv420p -s 1280x720 -b:v 5162k -r 30 output_video.mp4
ffmpeg -framerate 5 -i ./frame_%03d.png -c:v libx264 -profile:v high -pix_fmt yuv420p -s 1280x720 -b:v 5162k test.mp4
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
ffmpeg -i video1.mp4 -i video2.mp4 -i video3.mp4 -filter_complex "[0:v:0][1:v:0][2:v:0]concat=n=3:v=1[v]" -map "[v]" output.mp4

#This one is used for preserve the depth-cue in pymol
for file in *.png; do
    convert "$file" -background black -alpha background -flatten "output/$file"
done

for number in {1..15}; do
    file="Raw_data_Dong/OPC_15groups/$number/imputed/OPC_$number.pairs.gz"
    echo -n "Number of lines in $file: "
    zcat "$file" | wc -l
done
#change the names of different png files.
for i in {364..644}; do
    old_name="frame_${i}.png"
    new_name="frame_$((i - 80)).png"
    mv "$old_name" "$new_name"
done

counter=1

# sort the files
for file in $(ls *.png | sort -n -t_ -k2); do
    # Format the counter to have leading zeros and construct new filename
    new_name=$(printf "frame_%03d.png" $counter)
    mv "$file" "$new_name"
    ((counter++))
done

#This is used when we have several copies of the same file
counter=1
temp_dir="temp_dir_for_renaming"

# Create a temporary directory
mkdir -p $temp_dir

# Save the current IFS value and set IFS to newline for proper iteration over files
old_IFS=$IFS
IFS=$'\n'

# Rename and move files to the temporary directory
for file in $(ls *.png | sort -V); do
    new_name=$(printf "frame_%03d.png" $counter)
    mv "$file" "${temp_dir}/${new_name}"
    ((counter++))
done

# Restore IFS
IFS=$old_IFS

# Move files back from the temporary directory
mv ${temp_dir}/* .

# Remove the temporary directory
rmdir $temp_dir

