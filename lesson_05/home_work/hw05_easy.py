# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# 1:
print("1st part:")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# 2
print("2nd part:")

directories = os.listdir()
print(directories)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# 3
print("3rd part:")
import os
import shutil


cwd = __file__
file_name = __file__.split("/")
file_name = file_name[-1]
file_name = file_name.split(".")
copy = "_copy."
dst = os.path.join(os.getcwd(), (file_name[0] + copy + file_name[1]))

shutil.copy2(cwd, dst)


