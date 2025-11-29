import os

#Specify the folder containing the files to be renamed
folder_path = input("Enter the folder path: ")

#Get a list of all files in the specified folder
files = os.listdir(folder_path)

# Sort files to ensure consistent ordering
files.sort()

#Loop through each file and rename it
for index, filename in enumerate(files):
    #Construct the old file path
    old_file_path = os.path.join(folder_path, filename)
    
    #Check if it's a file (not a directory)
    if os.path.isfile(old_file_path):
        #Extract the file extension
        file_extension = os.path.splitext(filename)[1]
        
        #Create the new file name with a sequential number
        new_file_name = f'file_{index + 1}{file_extension}'
        
        #Construct the new file path
        new_file_path = os.path.join(folder_path, new_file_name)
        
        #Rename the file
        os.rename(old_file_path, new_file_path)
        
        print(f'Renamed: {filename} to {new_file_name}')
        