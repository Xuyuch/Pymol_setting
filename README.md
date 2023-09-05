# Pymol_setting
Pymol's script for roatate and transform

1 Get the exp.py file and copy it to /pymol/pymol_mive_exp.py (step for broad and rotate)

2 Modify the new exp.py based on a_exp.rotate.py
	a. remenber to get_view during the process

3 Get movie from pymol remeber to set width to 1280 and height to 720

4 Run the script linear_change.py(transfer the chromosome from A cell to B cell)
	a. rember to set the file_path in the linear_change.py

5 Open the b.n.cif and run back_to_ball.py
	a Remember run the files in the #anotation# area first
	b Remember set the save file_path

6 Open the saved file_path in step 3 use the code below to genrate a mp4 file.
	Code:ffmpeg -framerate 5 -i ./frame_%03d.png -c:v libx264 -profile:v high -pix_fmt yuv420p -s 1280x720 -b:v 5162k test.mp4

7 Do step 5 again for result in step4

8 get a list.txt which includes 3 mp4 file
	list file sample
	file 'rotate_pro.mp4'
	file 'test.mp4'
	file 'back_to_ball.mp4'
 
9 Run the code below to genrate the final video
	ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
