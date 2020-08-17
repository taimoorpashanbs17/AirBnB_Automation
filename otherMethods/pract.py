import os
import platform

os_name = platform.system()
current_path = os.getcwd()
parent_directory = os.path.dirname(current_path)
path = os.path.abspath(parent_directory +"//Resources//data.ini")
print(path)




