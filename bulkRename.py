import os
newName = input("Enter the name for all the files in the directory: ")
filesInDir = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
filesInDir.remove(os.path.basename(__file__))
for index, file in enumerate(filesInDir):
    extension = file.split(".")[-1]
    os.rename(file, f"{newName}({index}).{extension}")
