import easy
# 1:
print("1st part:")


menu = print("Menu:\n[1] go to file\n[2] list files in dir\n[3] delete dir\n[4] make dir ")
user_input = int(input("Enter menu item [1-4]: "))


files = easy.list_dir()

if user_input == 1:
    dir_name = input("Enter dir_name:\n")
    if dir_name not in files:
        print("Directory \"{}\" doesn't".format(dir_name), "exist")
    else:
        easy.ch_dir(dir_name)
        print("Directory was changed: {}".format(dir_name))
elif user_input == 2:
    list_dir = easy.list_dir()
    print(list_dir)
elif user_input == 3:
    dir_name = input("Enter dir_name:\n")
    if dir_name not in files:
        print("Directory \"{}\" doesn't".format(dir_name), "exist")
    else:
        easy.rm_dir(dir_name)
        print("\"{}\" directory was deleted".format(dir_name))
elif user_input == 4:
    dir_name = input("Enter dir_name:\n")
    if dir_name in files:
        print("Directory \"{}\"".format(dir_name), "already exists")
    else:
        easy.mk_dir(dir_name)
        print("\"{}\" directory was made".format(dir_name))