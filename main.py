import cv2
import numpy as np


# Load the image (Replace 'image_path' with the actual path of your image)
image = cv2.imread('1.jpg')

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (31, 31), 0)

# Create a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 9, -1],
                   [0, -1, 0]])

# Apply the sharpening kernel using filter2D
sharpened_image = cv2.filter2D(image, -1, kernel)

# Combine images horizontally for comparison (Original, Blurred, Sharpened)
comparison = cv2.hconcat([image, blurred_image, sharpened_image])

# Save the comparison image
cv2.imwrite('comparison_image.jpg', comparison)

# Display the image (optional, if you want to see it in a window)
cv2.imshow( "Comparison",comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()
