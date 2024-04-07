# Delete a file:
import os
import shutil
path = 'test2'

#PermissionError
#FileNotFoundError
#OSError

try:
    # os.remove(path) # will delete a file
    os.rmdir(path)  # Removing a folder contains no files
    # shutil.rmtree(path) # will delete a folder contains files | Remove directory tree
except PermissionError as Error:
    print("you dont have right permission to delete that")
except FileNotFoundError as Error:
    print("That file was not found")
except OSError as Error:
    print(" you cannot delete that using that functionality")
except Exception as Error:
    print(Error)
else:
    print(path + " Was deleted") # Test.txt Was Deleted.