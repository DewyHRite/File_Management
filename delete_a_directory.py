#Test

def remove_directory(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' removed.")
    except FileNotFoundError:
        print(f"Error: The directory '{dir_name}' does not exist.")
    except OSError:
        print(f"Error: The directory '{dir_name}' is not empty")
    except Exception as e:
        print(f"Error: {e}")
