# Image-Modification-Program

 Image Modification & Pixel Transformation Tool

Overview

A Python project that applies pixel-level corrections and transformations to an image using the Pillow (PIL) library. It demonstrates foundational skills in image processing, including RGB manipulation, region-based editing, and mathematical transitions.

⸻

Features

✔ correct_rhs(picture)

Adjusts the colours on the right half of the image using pixel-by-pixel operations.

✔ correct_bottom(picture)

Applies a smooth colour correction to the bottom 35% of the image.

✔ vary_rect_h(picture)

Creates a horizontal green gradient bar using a ratio-based transition.

✔ correct_picture(picture)

Runs all corrections, saves intermediate images, and shows the final output.

⸻

Techniques Demonstrated
	•	Pixel-level image manipulation
	•	Reading & writing images with PIL
	•	Working with width/height and coordinate grids
	•	RGB channel math
	•	Ratio-based transitions & gradients
	•	Region-of-interest (ROI) editing
	•	Sequential image transformations

These skills are foundational in computer vision and AI preprocessing pipelines.

⸻

Project Structure

Image Modification.py    # Image transformation functions
pumpkin.png              # Input image
pumpkin1.png             # RHS-corrected output
pumpkin2.png             # Bottom-corrected output


⸻

How to Run

Install Pillow:

pip install pillow

Run the script:

python "Image Modification.py"

The program will load the image, apply all transformations, save the results, and display the final version.

⸻

Future Improvements
	•	Add convolution filters (blur, sharpen, edge detection)
	•	Add mask-based editing
	•	Add colour-grading functions
	•	Build a small Tkinter GUI for user uploads
	•	Package the functions into a reusable module

