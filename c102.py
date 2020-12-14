import cv2
import dropbox
import time
import random

starttime=time.time()

def takesnapshot():
    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
    return imagename
    print("snapshot taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()

def ulpoadfile(imagename):
    accesstoken="sl.Ana8-6VaEL4h_KcDDtO4v1Dg_Plvh3NzQVjGn3Fv7hbWhWeb0ixucQ0Np4juLXg4N-63gPO_iHhKtW2FzjyQKAgXiBaF_TOwY48yyvkcrt3jtzXK3GYdkunVBI3cjNdaQyE4UPw"
    file=imagename
    filefrom=file
    fileto="/newfolder/"+imagename
    dbx=dropbox.Dropbox(accesstoken)

    with open(filefrom,"rb") as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("file uploader")

def main():
    while(True):
        if((time.time()-starttime)>=1):
            name=takesnapshot()
            ulpoadfile(name)
main()