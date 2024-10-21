#Testf

def change_directory(dir_name):
    try:
        os.chdir(dir_name)
        print(f"Changed directory to '{dir_name}'.")
    except FileNotFoundError:
        print(f"Error: The directory '{dir_name}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")
