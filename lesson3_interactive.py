import cv2

print("Starting Interactive Computer Vision Program...\n")

# Load the image
image = cv2.imread("my_photo.jpg")

if image is None:
    print("Error: Cannot find my_photo.jpg")
else:
    print("✅ Image loaded! Now let's play with it.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Show Original")
        print("2. Show Black & White")
        print("3. Show Blurred")
        print("4. Show Edges (Canny)")
        print("0. Exit")

        choice = input("Type a number and press Enter: ")

        if choice == "1":
            cv2.imshow("Original", image)
            
        elif choice == "2":
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Black & White", gray)
            
        elif choice == "3":
            blurred = cv2.GaussianBlur(image, (15, 15), 0)
            cv2.imshow("Blurred", blurred)
            
        elif choice == "4":
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            cv2.imshow("Edges", edges)
            
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

        cv2.waitKey(1)   # Small delay

    cv2.destroyAllWindows()