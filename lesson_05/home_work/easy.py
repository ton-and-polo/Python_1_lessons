import os
import re

# function - list dir:
def list_dir():
    files = dir_cont()
    result = []
    for i in files:
        if is_dir(i):
            result.append(i)
    return result

# function - is directory
def is_dir(file):
    pattern = ".\w+"
    result = re.findall(pattern, file)

    if len(result) == 1:
        return True
    elif len(result) > 1:
        return False

# function - dir content:
def dir_cont():
    return os.listdir()

# function - make dir:
def mk_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    return os.mkdir(path)

# function  - delete dir:
def rm_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    return os.rmdir(path)

# fucntion - change dir:
def ch_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    return os.chdir(path)

# function - is dir:
def is_dir(file):
    pattern = ".\w+"
    result = re.findall(pattern, file)

    if len(result) == 1:
        return True
    elif len(result) > 1:
        return False