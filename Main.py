import Xulydulieu;
import testLaydulieu;
import Savefile;
import pandas as pd

def layApi(url,so): #lấy tất cả các link từ một trang web vd https://thanhnien.vn/
    data=[]
    ds=testLaydulieu.getData(url)
    for i in ds[:int(so)]:
        try:
            x=Xulydulieu.Phanloaivanban(i)
            data.append(x)
        except:
            pass
    Savefile.luuexcel(data)
    return data

def phanloaiUrl(url): #lay thong tin tu link vd 'https://zingnews.vn/show-dien-cua-super-junior-o-tphcm-gay-buc-xuc-post1411059.html'
    x=Xulydulieu.Phanloaivanban(url)
    return x

def phanloaiText(document): #lay thong tin tu doan text
    x=Xulydulieu.PhanloaivanbanText(document)
    return x
def phanloaituFile(): # lay thong tin tu file .txt
    data=Savefile.chonfile()
    x=Xulydulieu.PhanloaivanbanText(data)
    return x
# url='https://thanhnien.vn/'
# layApi(url,1000)