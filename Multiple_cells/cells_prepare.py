'''
This script is used to load 3dg files into pymol and uses female mouse cells
The 3dg files should be names as 'a.exp.n' to 'z.exp.n'
The 'p.exp.n' can't be loaded successfully. Reason maybe p is a reserved word for Pymol or Python
Remember to turn off the undo to save time.
'''
for object_letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o']:
    cmd.do(f'load {object_letter}.exp.n.cif, {object_letter}.exp.n')  # Add this line to load the file.
    cmd.do(f'as sticks, {object_letter}.exp.n')
    cmd.do(f'set_bond stick_radius, 0.1, {object_letter}.exp.n')
    cmd.do(f'spectrum b, rainbow, {object_letter}.exp.n, 1, 21')
    if object_letter != 'a':
        cmd.do(f'hide everything, {object_letter}.exp.n')

    for chr_name in ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chrX"]:
        cmd.do(f'extract {object_letter}_{chr_name}_mat, {object_letter}.exp.n and chain "{chr_name}(mat)"')
        cmd.do(f'extract {object_letter}_{chr_name}_pat, {object_letter}.exp.n and chain "{chr_name}(pat)"')
