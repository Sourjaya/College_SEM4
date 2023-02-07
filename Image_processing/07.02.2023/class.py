import os
path=r"C:\Users\vfd\Desktop\538_SourjayaDas\Image_processing\IMAGE PROCESSING@SP\image folder"

def get_file_list(path):
    return os.listdir(path)
#print(os.listdir(path))
#WAFP to access the image folder and return the count of the total number of file

def count_file(path):
    return len(os.listdir(path))
print(count_file(path))

#WAFP to count the no of files of each extension type in a folder
def count_group(path):
    files=get_file_list(path)
    l_count={}
    for i in files:
        ext=i.split(".")[-1]

        if ext in l_count:
            l_count[ext]+=1
        else:
            l_count[ext]=1
    return l_count

print(count_group(path))