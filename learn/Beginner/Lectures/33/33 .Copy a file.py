# copy a file:

# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (files creation and modification times)

import shutil

shutil.copyfile('test.txt','high_copy.txt') #src,dst