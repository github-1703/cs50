import numpy as np
import matplotlib.pyplot as plt
import random

# Set the random seed for reproducibility
random.seed(42)

# Constants
num_stars = 500
min_distance = 5000
x_min, x_max = -110000, 110000
y_min, y_max = -110000, 110000

# Function to check the minimum distance between the new star and existing ones
def is_valid_position(star, stars):
    for existing_star in stars:
        distance = np.sqrt((star[0] - existing_star[0]) ** 2 + (star[1] - existing_star[1]) ** 2)
        if distance < min_distance:
            return False
    return True

# Generate star positions
stars = []
while len(stars) < num_stars:
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    new_star = (x, y)
    
    if is_valid_position(new_star, stars):
        stars.append(new_star)

# Extract the x and y coordinates of the stars
x_coords, y_coords = zip(*stars)

# Plot the stars
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, c='white', marker='o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.gca().set_facecolor('orange')  # Set the background color to black for the night sky effect
plt.title("Simulated Star Placement")
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.show()
