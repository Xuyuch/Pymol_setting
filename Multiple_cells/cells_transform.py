'''
This code is used for create a searies of png files to show the dynamic changes of chromsome stucture.
Need to be Optimize sothat we can control the number of input cells
Worked on female mouse cell only.
'''

import pymol
import os

chromosomes = [f"chr{i}" if i != 20 else "chrX" for i in range(1, 21)]
objects = [chr(i) for i in range(97, 97 + 18) if i != 112]#112 is skipped is because 112=p and it is reserved for python or Pymol

# Create an empty dictionary for each object to store coordinates
coords_dicts = {}
for target_obj in objects:
    coords_dicts[target_obj] = {}

# Loop through each chromosome to align

for chr_name in chromosomes:
    suffixes = ["mat", "pat"]
    for suffix in suffixes:
        for target_obj in objects:
            obj_name_base = f"{chr_name}_{suffix}"
            obj_name = f"{target_obj}_{obj_name_base}"
            if target_obj != "a" and target_obj != "r":  # Added the check for target_obj != "r"
                pymol.cmd.align(obj_name, f"a_{obj_name_base}")


# Loop for getting and modifying coordinates for each object
for chrom in chromosomes:
    suffixes = ["mat", "pat"]
    for suffix in suffixes:
        obj_base_name = f"{chrom}_{suffix}"

        min_shape = float('inf')  # start with infinity, then minimize
        for target_obj in objects:
            obj_name = f"{target_obj}_{obj_base_name}"
            coords = pymol.cmd.get_coords(obj_name)
            min_shape = min(min_shape, coords.shape[0])

        for target_obj in objects:
            obj_name = f"{target_obj}_{obj_base_name}"
            selection_name = f"{obj_name}_sel"
            pymol.cmd.select(selection_name, f"(byobj {obj_name}) and (index 1-{min_shape})")
            pymol.cmd.remove(f"{obj_name} and not {selection_name}")

            # Store the modified coordinates in the dictionaries
            coords = pymol.cmd.get_coords(obj_name)
            coords_dicts[target_obj][obj_name] = coords

# Interpolation loop
num_frames = 40
output_folder = "/home/yuchen/Raw_data_Dong/OPC_15groups/movie/viewset_new2"

for frame in range(1, 17 * num_frames + 1):
    interp_factor = ((frame-1) % num_frames) / num_frames

    for chrom in chromosomes:
        suffixes = ["mat", "pat"]
        for suffix in suffixes:
            obj_base_name = f"{chrom}_{suffix}"

            # Determine which objects we're interpolating between
            current_obj_idx = (frame-1) // num_frames
            next_obj_idx = current_obj_idx + 1
            if next_obj_idx == len(objects):
                next_obj_idx = 0

            current_obj = objects[current_obj_idx]
            next_obj = objects[next_obj_idx]

            for target_obj in objects:
                obj_name = f"a_{obj_base_name}"
                interpolated_coords = (1 - interp_factor) * coords_dicts[current_obj][f"{current_obj}_{obj_base_name}"] + interp_factor * coords_dicts[next_obj][f"{next_obj}_{obj_base_name}"]

                # Load interpolated coordinates into the object in PyMOL
                pymol.cmd.load_coords(interpolated_coords, obj_name)

            # After processing all objects for this chrom and suffix:
    file_path = os.path.join(output_folder, f"frame_{frame+3:03d}.png")
    pymol.cmd.png(file_path, width=1280, height=720, ray=1)

