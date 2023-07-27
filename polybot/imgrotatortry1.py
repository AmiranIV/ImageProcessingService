
def rotate_image_clockwise(image):
    # Get the number of rows and columns in the original image
    rows = len(image)
    cols = len(image[0])

    # Create a new empty image with swapped rows and columns
    rotated_image = [[0 for _ in range(rows)] for _ in range(cols)]

    # Find the center of the original image
    center_row = rows // 2
    center_col = cols // 2

    # Perform the clockwise rotation by repositioning pixels
    for i in range(rows):
        for j in range(cols):
            rotated_row = j  # New row position after rotation
            rotated_col = cols - 1 - i  # New column position after rotation

            # Copy the pixel value to the new position
            rotated_image[rotated_row][rotated_col] = image[i][j]

    return rotated_image
with open('images/Img1.jpg') as new_image:
    rotated_image = rotate_image_clockwise(new_image)

print(rotated_image)