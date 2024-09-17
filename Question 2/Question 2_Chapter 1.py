import time
from PIL import Image

# Step 1: Generate the number (n)

current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
print(f"Generated Number: {generated_number}")

# Step 2: Load the image and modify the pixel values

image_path = "Question 2/chapter1.jpg"
image = Image.open(image_path)
pixels = image.load()

for i in range(image.width):
    for j in range(image.height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (
            r + generated_number,
            g + generated_number,
            b + generated_number,
        )

# Step 3: Save the modified image

output_image_path = "Question 2/chapter1out.png"
image.save(output_image_path)

# Step 4: Calculate the sum of all red pixel values in the new image

red_sum = 0
for i in range(image.width):
    for j in range(image.height):
        r, g, b = pixels[i, j]
        red_sum += r
print(f"Sum of all red pixel values: {red_sum}")
