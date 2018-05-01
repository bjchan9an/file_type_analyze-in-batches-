import filetype
import os

def GetFileList(search_dir,fileList):
    newDir = search_dir
    if os.path.isfile(search_dir):
        fileList.append(search_dir)
    elif os.path.isdir(search_dir):  
        for s in os.listdir(search_dir):
            #if s == "xxx":        #to avoid some folders
                #continue
            newDir=os.path.join(search_dir,s)
            GetFileList(newDir, fileList)  
    return fileList

#def analyze(file_list)
file_list = GetFileList(r'C:\Users\Administrator\Desktop\re1\log', [])
result_list={}
print len(file_list)
for name in file_list:
    tmp=filetype.guess(name)
    if  tmp is not None:
        print name,tmp

