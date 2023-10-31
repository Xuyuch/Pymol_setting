#~/pipeline/pymol/pymol -c ~/R_script/pymol_settings/Slice_pymol_better_parameter.py  -- -i1 /home/yuchen/Viterbi/PA_OPC_oligo/cif_file/a.exp.n.cif -i2 /home/yuchen/Viterbi/PA_OPC_oligo/cif_file/b.exp.n.cif -v ~/view.txt -O /home/yuchen/Viterbi/PA_OPC_oligo/cif_file/test -o 2 -N 4

import sys
import pymol
import os
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="PyMOL script with customizable inputs.")
parser.add_argument('-i1', required=True, help='Input file 1')
parser.add_argument('-i2', required=True, help='Input file 2')
parser.add_argument('-v', required=True, help='Path to the view file')
parser.add_argument('-O', required=True, help='Output directory')
parser.add_argument('-o', required=True, type=int, help='Order')
parser.add_argument('-N', required=True, type=int, help='Number of frames')

args = parser.parse_args()

# Now, you can use args.i1, args.i2, ... in your script
a_path = args.i1
b_path = args.i2
view_file = args.v
output_folder = args.O
order = args.o
num_frames = args.N

pymol.cmd.set("connect_mode", 4)
cmd.do("set ray_shadows","0")
cmd.do("set depth_cue", "0")
cmd.do(f'load {a_path}, a.exp.n')# Add this line to load the file.
cmd.do(f'as sticks, a.exp.n')
cmd.do(f'set_bond stick_radius, 0.1, a.exp.n')
cmd.do(f'spectrum b, rainbow, a.exp.n, 1, 21')
if view_file:
    with open(view_file, 'r') as f:
        content = f.read()
        cleaned_content = content.replace('(', '').replace(')', '').replace('\n', '').replace(' ', '')
        stored_view = tuple(float(item) for item in cleaned_content.split(','))
    cmd.set_view(stored_view)

for chr_name in ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19"]:
    cmd.do(f'extract a_{chr_name}_mat, a.exp.n and chain "{chr_name}(mat)"')
    cmd.do(f'extract a_{chr_name}_pat, a.exp.n and chain "{chr_name}(pat)"') 
cmd.do(f'load {b_path}, b.exp.n') # Add this line to load the file.
cmd.do(f'as sticks, b.exp.n')
cmd.do(f'set_bond stick_radius, 0.1, b.exp.n')
cmd.do(f'spectrum b, rainbow, b.exp.n, 1, 21')
cmd.do(f'hide everything, b.exp.n')
for chr_name in ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19"]:
    cmd.do(f'extract b_{chr_name}_mat, b.exp.n and chain "{chr_name}(mat)"')
    cmd.do(f'extract b_{chr_name}_pat, b.exp.n and chain "{chr_name}(pat)"')
if len(sys.argv) > 3:
    with open(view_file, 'r') as f:
        content = f.read()
        cleaned_content = content.replace('(', '').replace(')', '').replace('\n', '').replace(' ', '')
        stored_view = tuple(float(item) for item in cleaned_content.split(','))
cmd.set_view(stored_view)
chromosomes = [f"chr{i}" for i in range(1, 20)]
objects = ['a','b']

# Create an empty dictionary for each object to store coordinates
coords_dicts = {}
for target_obj in objects:
    coords_dicts[target_obj] = {}


# Loop for getting and modifying coordinates for each object
for chrom in chromosomes:
    suffixes = ["mat", "pat"]
    for suffix in suffixes:
        obj_base_name = f"{chrom}_{suffix}"        
        for target_obj in objects:
            obj_name = f"{target_obj}_{obj_base_name}"
            coords = pymol.cmd.get_coords(obj_name)
            coords_dicts[target_obj][obj_base_name] = coords

# Interpolation loop

  
for frame in range(1, num_frames + 1):
    interp_factor = frame / num_frames
    
    for chrom in chromosomes:
        suffixes = ["mat", "pat"]
        for suffix in suffixes:
            obj_base_name = f"{chrom}_{suffix}"
            obj_name = f"a_{obj_base_name}"
            interpolated_coords = (1 - interp_factor) * coords_dicts["a"][f"{obj_base_name}"] + interp_factor * coords_dicts["b"][f"{obj_base_name}"]
            # Load interpolated coordinates into the object in PyMOL
            pymol.cmd.load_coords(interpolated_coords, obj_name)

            # After processing all objects for this chrom and suffix:
    file_path = os.path.join(output_folder, f"frame_{num_frames*(order-1)+frame:04d}.png")
    pymol.cmd.png(file_path, width=1280, height=720, ray=1)
