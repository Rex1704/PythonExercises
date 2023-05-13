import os

def Pretify(dirPath,fileTobeModify,format):
    os.chdir(dirPath)
    print(os.getcwd())
    folderComp = os.listdir()
    print(folderComp)
    for file in folderComp:
        if (os.path.isfile(os.path.join(dirPath,file))):
            os.rename(file, file.split(".")[0].title()+"."+file.split(".")[1].lower())

    filewithFormat = list(filter(lambda x: x.split(".")[1].lower() == format, folderComp))
    for count,name in enumerate(filewithFormat):
        try:
            os.rename(name,str(count+1)+"."+format)
        except Exception as e :
            pass

    if (os.path.isfile(os.path.join(dirPath, fileTobeModify))):
        with open(fileTobeModify, "r") as f:
            a = f.read().split(" ")
            b = list()
            for i in a:
                b.append(i.title()+" ")
            f.close()

        with open(fileTobeModify, "w") as f:
            for i in b:
                f.write(i)
            f.close()


if __name__ == '__main__':

    Pretify("C:/Users/DEEPAK/OneDrive/Desktop/PretifySample", "Deepak.Txt", "jpg")
