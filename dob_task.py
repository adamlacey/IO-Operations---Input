def dob_txt(file_path, delimiter=' '):                  # Defines text file which is in same directory as python file. Delimiter=' ' used to split string into separate elements e.g. names and birthdates.
    names_list = []
    birthdates_list = []

    try:
        with open(file_path, 'r') as file:              # 'r' for reading text file.
            lines = file.readlines()

            for line in lines:
                                                        # Split each line into name and number.
                parts = line.strip().split(delimiter)
                
                names = ' '.join(parts[:-3])            # Slicing the sequence from start to third last element.
                birthdates = ' '.join(parts[-3:])       # Slicing the sequence from third last element to the end.
                
                names_list.append(names)                # Append function used to add the names and birthdates onto separate lists.
                birthdates_list.append(birthdates)
        
    except FileNotFoundError:                           # Errors to show that text file is not found.
        print(f"The file {file_path} was not found.")
    except ValueError:
        print("Error converting a string to an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return names_list, birthdates_list

# Example usage:
file_path = 'DOB.txt'                                   # This is the text file in the same directory as Python file.
names, birthdates = dob_txt(file_path)

print("Names:")                                         # Prints out both lists of names and birthdates.
for names in names:
    print(names)

print("\nBirthdates:")
for birthdates in birthdates:
    print(birthdates)
