def file_read_write():
    try:
        # Ask the user for the filename
        input_file = input("Enter the name of the file to read from: ")
        
        # Open the file for reading
        with open(input_file, "r") as file:
            content = file.readlines()
        
        # Modify the content (e.g., add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Ask for the output file name
        output_file = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the new file
        with open(output_file, "w") as file:
            file.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file}.")
    
    except FileNotFoundError:
        # Handle the case where the input file doesn't exist
        print("Error: The file you specified does not exist. Please check the filename.")
    except IOError:
        # Handle other I/O errors
        print("Error: The file could not be read or written. Please check your permissions.")
    except Exception as e:
        # Catch all other exceptions and show an error message
        print(f"An unexpected error occurred: {e}")

# Run the program
file_read_write()
