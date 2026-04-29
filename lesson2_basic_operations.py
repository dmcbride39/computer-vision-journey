import cv2

# Load the image
image = cv2.imread("my_photo.jpg")

if image is None:
    print("Error: Could not load image")
else:
    print("✅ Image loaded!")

    # 1. Make it Black & White (Grayscale)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Blur the image
    blurred = cv2.GaussianBlur(image, (15, 15), 0)

    # Show all versions
    cv2.imshow("Original", image)
    cv2.imshow("Black & White", gray)
    cv2.imshow("Blurred", blurred)

    print("\nThree windows should open.")
    print("Press any key to close all windows...")

    cv2.waitKey(0)
    cv2.destroyAllWindows()