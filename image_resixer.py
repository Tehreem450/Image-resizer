from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize((new_width, new_height))

            # Save the resized image
            resized_img.save(output_path)

            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Get input parameters from the user
    input_path = input("Enter the path to the input image: ")
    output_directory = input("Enter the path to save the resized image directory: ")
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))

    # Check if the input file exists
    if not os.path.isfile(input_path):
        print("Error: Input file does not exist.")
        return

    # Extract the file name and extension from the input path
    file_name, file_extension = os.path.splitext(os.path.basename(input_path))

    # Construct the output path with a new file name and extension
    output_path = os.path.join(output_directory, f"{file_name}_resized{file_extension}")

    # Resize the image
    resize_image(input_path, output_path, new_width, new_height)

if __name__ == "__main__":
    main()
