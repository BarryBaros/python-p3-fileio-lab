def write_file(file_name, file_content):
   #Add .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    # Write content to the file 
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    pass

def read_file(file_name):
    pass
