import cv2

# Load the photo
image = cv2.imread("my_photo.jpg")

if image is None:
    print("ERROR: Could not load the image!")
    print("Make sure my_photo.jpg is in this folder")
else:
    print("✅ SUCCESS! Image loaded successfully!")
    print("Image shape (height, width, colors):", image.shape)
    
    # Show the image
    cv2.imshow("My First Computer Vision Window", image)
    
    print("\nA window should appear with your photo.")
    print("Press ANY key on your keyboard to close the window.")
    
    cv2.waitKey(0)        # Wait for key press
    cv2.destroyAllWindows()