import io

def file_writer():
    names = ["Ali", "Sara", "John"]
    fake_file = io.StringIO()
    
    for name in names:
        fake_file.write(name + "\n")
    
    # Move back to the start and print contents
    fake_file.seek(0)
    print("Written names:\n" + fake_file.read())

# Call the function
file_writer()
