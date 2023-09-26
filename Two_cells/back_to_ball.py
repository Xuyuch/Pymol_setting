'''
as sticks, B.n
set_bond stick_radius, 0.5, B.n
spectrum b, rainbow, B.n, 1, 21
hide everything, b.n


   
extract chr1_mat, b.n and chain "chr1(mat)"
extract chr1_pat, b.n and chain "chr1(pat)"
extract chr10_mat, b.n and chain "chr10(mat)"
extract chr10_pat, b.n and chain "chr10(pat)"
extract chr11_mat, b.n and chain "chr11(mat)"
extract chr11_pat, b.n and chain "chr11(pat)"
extract chr12_mat, b.n and chain "chr12(mat)"
extract chr12_pat, b.n and chain "chr12(pat)"
extract chr13_mat, b.n and chain "chr13(mat)"
extract chr13_pat, b.n and chain "chr13(pat)"
extract chr14_mat, b.n and chain "chr14(mat)"
extract chr14_pat, b.n and chain "chr14(pat)"
extract chr15_mat, b.n and chain "chr15(mat)"
extract chr15_pat, b.n and chain "chr15(pat)"
extract chr16_mat, b.n and chain "chr16(mat)"
extract chr16_pat, b.n and chain "chr16(pat)"
extract chr17_mat, b.n and chain "chr17(mat)"
extract chr17_pat, b.n and chain "chr17(pat)"
extract chr18_mat, b.n and chain "chr18(mat)"
extract chr18_pat, b.n and chain "chr18(pat)"
extract chr19_mat, b.n and chain "chr19(mat)"
extract chr19_pat, b.n and chain "chr19(pat)"
extract chr2_mat, b.n and chain "chr2(mat)"
extract chr2_pat, b.n and chain "chr2(pat)"
extract chr3_mat, b.n and chain "chr3(mat)"
extract chr3_pat, b.n and chain "chr3(pat)"
extract chr4_mat, b.n and chain "chr4(mat)"
extract chr4_pat, b.n and chain "chr4(pat)"
extract chr5_mat, b.n and chain "chr5(mat)"
extract chr5_pat, b.n and chain "chr5(pat)"
extract chr6_mat, b.n and chain "chr6(mat)"
extract chr6_pat, b.n and chain "chr6(pat)"
extract chr7_mat, b.n and chain "chr7(mat)"
extract chr7_pat, b.n and chain "chr7(pat)"
extract chr8_mat, b.n and chain "chr8(mat)"
extract chr8_pat, b.n and chain "chr8(pat)"
extract chr9_mat, b.n and chain "chr9(mat)"
extract chr9_pat, b.n and chain "chr9(pat)"
extract chrX_mat, b.n and chain "chrX(mat)"
extract chrX_pat, b.n and chain "chrX(pat)"

set_view (\
     0.750269890,    0.324408263,    0.576068759,\
     0.147000015,    0.767668426,   -0.623760700,\
    -0.644581974,    0.552670181,    0.528270006,\
     0.000002384,    0.000001788, -1049.974853516,\
    -6.021775723,   -6.870912552,   -2.041615725,\
   812.712585449, 1287.237182617,  -20.000000000 )
'''
chromosomes = [f"chr{i}" for i in range(1, 20)] 
coords_dict_A = {}
coords_dict_B = {}

for chrom in chromosomes:
    for suffix in ["mat", "pat"]:
        # Original object names
        obj_A_name = f"{chrom}_{suffix}"
        obj_B_name = f"b_{obj_A_name}"

        # Get coordinates for original objects
        coords_A = pymol.cmd.get_coords(obj_A_name)
        coords_B = pymol.cmd.get_coords(obj_B_name)
        
        # Determine the minimum number of atoms between the two structures
        min_shape = min(coords_A.shape[0], coords_B.shape[0])

        # Create new selections based on the minimum atom count
        selection_A_name = f"{obj_A_name}_A"
        selection_B_name = f"{obj_B_name}_B"
        
        pymol.cmd.select(selection_A_name, f"(byobj {obj_A_name}) and (index 1-{min_shape})")
        pymol.cmd.select(selection_B_name, f"(byobj {obj_B_name}) and (index 1-{min_shape})")
        pymol.cmd.remove(f"{obj_A_name} and not {selection_A_name}")
        pymol.cmd.remove(f"{obj_B_name} and not {selection_B_name}")

        # Get coordinates for new selections
        crds_A = pymol.cmd.get_coords(selection_A_name)
        crds_B = pymol.cmd.get_coords(selection_B_name)
        
        # Store the coordinates in the dictionaries
        coords_dict_A[obj_A_name] = crds_A
        coords_dict_B[obj_B_name] = crds_B
        
        
num_frames = 40 
output_folder = "/home/yuchen/Pymol_pseudocells/movie/back_to_ball"  
  
for frame in range(1, num_frames + 1):
    interp_factor = frame / num_frames
    
    for suffix in ["mat", "pat"]:
        for chrom in chromosomes:
            # Define the object names based on the current chromosome and suffix
            obj_A_name = f"{chrom}_{suffix}"
            obj_B_name = f"b_{obj_A_name}"

            # Ensure that the names are in the dictionaries before proceeding
                # Get coordinates from dictionaries
            crds_A = coords_dict_A[obj_A_name]
            crds_B = coords_dict_B[obj_B_name]   
                # Calculate interpolated coordinates
            interpolated_coords = (1 - interp_factor) * crds_B + interp_factor * crds_A  
                # Load interpolated coordinates into the object in PyMOL
            pymol.cmd.load_coords(interpolated_coords, obj_B_name)

    # After interpolating all chromosomes for both 'mat' and 'pat', save the view for the frame
    file_path = os.path.join(output_folder, f"frame_{frame:03d}.png")
    pymol.cmd.png(file_path, width=1280, height=720, ray=1)
