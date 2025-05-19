import cv2

# Load the image
image = cv2.imread('url.jpg')  # Replace with your image path

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()