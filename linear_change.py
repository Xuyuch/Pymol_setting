
# Define the chromosomes
chromosomes = [f"chr{i}" for i in range(1, 20)] 

# Loop through each chromosome and align both mat and pat
for chr_name in chromosomes:
    for suffix in ["mat", "pat"]:
        object_name_b = f"b_{chr_name}_{suffix}"  # e.g., b_chr1_mat
        object_name_a = f"{chr_name}_{suffix}"  # e.g., chr1_mat
        pymol.cmd.align(object_name_b, object_name_a)
        
'''
for chr_name in chromosomes:
    for suffix in ["mat", "pat"]:
        object_name_b = f"c_{chr_name}_{suffix}"  # e.g., b_chr1_mat
        object_name_a = f"{chr_name}_{suffix}"  # e.g., chr1_mat
        pymol.cmd.align(object_name_b, object_name_a)


num_frames = 20  # 动画帧数 
for suffix in ["mat", "pat"]:
    for chrom in chromosomes:
        obj_A_name = f"{chrom}_{suffix}"
        for state in range(1, num_frames + 2): # 
            pymol.cmd.create(obj_A_name, obj_A_name, 1, state) 
            
'''





            
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
output_folder = "/home/yuchen/Pymol_pseudocells/movie/"  
  
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
            interpolated_coords = (1 - interp_factor) * crds_A + interp_factor * crds_B
            # Load interpolated coordinates into the object in PyMOL
            
            pymol.cmd.load_coords(interpolated_coords, obj_A_name)

    # After interpolating all chromosomes for both 'mat' and 'pat', save the view for the frame
    file_path = os.path.join(output_folder, f"frame_{frame:03d}.png")
    pymol.cmd.png(file_path, width=1280, height=720, ray=1)
        
'''            
coords_chr1_mat_A = pymol.cmd.get_coords("chr1_mat")
coords_chr1_mat_B = pymol.cmd.get_coords("b_chr1_mat")
coords3 = pymol.cmd.get_coords("C")
coords4 = pymol.cmd.get_coords("D")
shape1=coords1.shape[0]
shape2=coords2.shape[0]
shape3=coords3.shape[0]
shape4=coords4.shape[0]
min_shape=min(shape1,shape2,shape3,shape4)
pymol.cmd.select("A1", f"(byobj A) and (index 1-{min_shape})")
pymol.cmd.select("B1", f"(byobj B_) and (index 1-{min_shape})")
pymol.cmd.select("C1", f"(byobj C) and (index 1-{min_shape})")
pymol.cmd.select("D1", f"(byobj D) and (index 1-{min_shape})")
crds1 = pymol.cmd.get_coords("A1")
crds2 = pymol.cmd.get_coords("B1")
crds3 = pymol.cmd.get_coords("C1")
crds4 = pymol.cmd.get_coords("D1")

pymol.cmd.show("sticks", "A1")  # 显示tad_object1为sticks样式




for frame in range(1, num_frames + 1):
    interp_factor = frame / num_frames
    interpolated_coords = (1 - interp_factor) * coords_dict_A["chr1_mat"] + interp_factor * coords_dict_B["b_chr1_mat"]
    pymol.cmd.load_coords(interpolated_coords, "chr1_mat")

    pymol.cmd.mview('store', frame)



for frame in range(num_frames + 1):
    interp_factor = frame * interp_increment
    interpolated_coords = (1 - interp_factor) * crds1 + interp_factor * crds2
    current_color = [(1 - interp_factor) * start_col + interp_factor * end_col for start_col, end_col in zip(A_color, B_color)]
    pymol.cmd.load_coords(interpolated_coords, "A1")
    temp_color_name = f"temp_color_{frame}"
    pymol.cmd.set_color(temp_color_name, current_color)
    pymol.cmd.color(temp_color_name, "A1")
    pymol.cmd.bg_color('black')
    file_path = os.path.join(output_folder, f"frame_{frame:03d}.png")
    pymol.cmd.png(file_path, width=800, height=800, ray=1)
pymol.cmd.hide("everything") 
pymol.cmd.show("sticks", "B1")  # 显示tad_object1为sticks样式
for frame in range(num_frames + 1):
    interp_factor = frame * interp_increment
    interpolated_coords = (1 - interp_factor) * crds2 + interp_factor * crds3
    current_color = [(1 - interp_factor) * start_col + interp_factor * end_col for start_col, end_col in zip(B_color, C_color)]
    pymol.cmd.load_coords(interpolated_coords, "B1")
    temp_color_name = f"temp_color_{frame}"
    pymol.cmd.set_color(temp_color_name, current_color)
    pymol.cmd.color(temp_color_name, "B1")
    file_path = os.path.join(output_folder, f"frame_{frame+41:03d}.png")
    pymol.cmd.png(file_path, width=800, height=800, ray=1)
pymol.cmd.hide("everything") 
pymol.cmd.show("sticks", "C1")  # 显示tad_object1为sticks样式
for frame in range(num_frames + 1):

    interp_factor = frame * interp_increment
    interpolated_coords = (1 - interp_factor) * crds2 + interp_factor * crds3
    current_color = [(1 - interp_factor) * start_col + interp_factor * end_col for start_col, end_col in zip(B_color, C_color)]
    pymol.cmd.load_coords(interpolated_coords, "C1")
    temp_color_name = f"temp_color_{frame}"
    pymol.cmd.set_color(temp_color_name, current_color)
    pymol.cmd.color(temp_color_name, "C1")
    file_path = os.path.join(output_folder, f"frame_{frame+82:03d}.png")
    pymol.cmd.png(file_path, width=800, height=800, ray=1)
'''











