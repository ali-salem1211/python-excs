def file_reader(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    print("Number of lines:", len(lines))

# file_reader('example.txt')  # Uncomment and use a valid file path
