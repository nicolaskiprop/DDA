import sys
import numpy as np

# Read the image data from stdin
image_data = sys.stdin.buffer.read()

# Convert the image data to a NumPy array
nparr = np.frombuffer(image_data, np.uint8)

# Calculate the number of pixels in the image
image_size = nparr.shape[0]

# Calculate the number of pixels in the desired shape
desired_shape = (2240, 1150)
desired_size = desired_shape[0] * desired_shape[1]

# Reshape the image array to the desired shape
reshaped_image = nparr.reshape(desired_shape)

# Print the reshaped image
for row in reshaped_image:
    row_str = ' '.join(str(val) for val in row)
    print(row_str)
