# Python to Exe
# windows defender may prevent you from running.
# make sure to pip and pyinstaller are installed/updated

#cd location, then pyinstaller file.py
# -F : all in 1 file
# -w : remove terminal windows (if use a gui app)
# -i icon.ico : add customer icon to .exe
# project.py : name of main python file

# example : pyinstaller -F -w -i face.ico project.py

# === Alternative easy using a simple graphical interface
# pip install auto-py-to-exe
# auto-py-to-exe
# ===