from pathlib import Path

def write_file(file_name, file_content):
    # Convert file_name to string if it is a PosixPath object
    if isinstance(file_name, Path):
        file_name = str(file_name)
        
    # Add .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    # Write content to the file 
    with open(file_name, 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    # Convert file_name to string if it is a PosixPath object
    if isinstance(file_name, Path):
        file_name = str(file_name)
        
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    with open(file_name, 'a') as file:
        file.write(append_content)
    

def read_file(file_name):
    # Convert file_name to string if it is a PosixPath object
    if isinstance(file_name, Path):
        file_name = str(file_name)
        
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    with open(file_name, 'r') as file:
        return file.read()
