import Main
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import Tk
from Main import phanloaiText;
from Main import phanloaituFile
from Main import  phanloaiUrl
from Main import layApi

win = Tk(className='Phân loại văn bản')

win.geometry("700x600")

bg_image = Image.open("anh.png")
resized_image = bg_image.resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resized_image)

bg_label = Label(win, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)




def Phanloaitext():
    inp = inputtxt.get(1.0, "end-1c")
    result = phanloaiText(inp)
    title,document=result
    suffix = title.split("__")[-1]
    suffix2=suffix.split("']")[0]
    lbl.config(text = ""+ str(suffix2))
    lbl2.insert(INSERT,""+ str(document))

def Choosefile():
    result = phanloaituFile()
    title,document=result
    suffix = title.split("__")[-1]
    suffix2=suffix.split("']")[0]
    lbl.config(text = ""+ str(suffix2))
    lbl2.insert(INSERT,""+ str(document))
def PhanloaiUrl():
    inp = Url.get(1.0, "end-1c")
    print('xxxx',inp)
    result=[]
    result = phanloaiUrl(inp)
    title=result['Title']
    theloai=result['Thể loại']
    link=result['Link']
    vanban=result['Nội dung']
    suffix = theloai.split("__")[-1]
    suffix2=suffix.split("']")[0]
    document='Title: \t'+title+"\n"+'Link: \t'+link+"\n\n"+'Nội dung: \t'+vanban
    lbl.config(text = ""+ str(suffix2))
    lbl2.insert(INSERT,""+ str(document))

Label(win, text="Phân loại văn bản", fg='#ff1a1a',font=("Arial", 30)).pack(pady=15)

inputtxt = Text(win, height = 5, width = 150) #heigh cu 15
inputtxt.pack(padx=30)

styl = ttk.Style()
styl.configure('blue.TSeparator', background='blue')

separator = ttk.Separator(win, orient='horizontal',style='blue.TSeparator' ,takefocus= 1,
    cursor='plus'  )
separator.pack(fill='x', pady=30)

Label(win, text="Loại văn bản: ",font=("Arial", 16)).place(x=200, y=200)

lbl = Label(win, text = "",font=("Arial", 16))
lbl.place(x=360, y=200)


separator = ttk.Separator(win, orient='horizontal',style='blue.TSeparator' ,takefocus= 1,
    cursor='plus' )
separator.pack(fill='x', pady=5)

lbl2 = Text(win,font=("Arial", 10),height = 10, width = 150,wrap="word")
lbl2.pack(padx=20)

separator = ttk.Separator(win, orient='horizontal',style='blue.TSeparator' ,takefocus= 1,
    cursor='plus' )
separator.pack(fill='x', pady=5)

Url = Text(win,font=("Arial", 15),width=150,height=1,wrap="word")
Url.pack(padx=20)

lbl3 = Label(win, text = "Import Url ↥",font=("Arial", 20),width=10)
lbl3.place(x=150, y=450)
printButton = Button(win,
                        text  = "Phân loại URL",font=("Arial", 15),  width =15,
                        command = PhanloaiUrl)
printButton.place(x=340, y=450)


button = Button(win, text="Choose file ", command=Choosefile,width=15,font=("Arial", 15))
button.place(x=240, y=500)
# button.pack()

printButton = Button(win,
                        text  = "Xử lý",font=("Arial", 15),  width =15,
                        command = Phanloaitext)
printButton.place(x=340, y=550)
def clearText():
    inputtxt.delete('1.0', 'end')
    Url.delete('1.0', 'end')
    lbl2.delete('1.0', 'end')

exit_button = Button(win, text="Clear Text", bg='#ffff00', fg='#000000',font=("Arial", 15), width =15, command=clearText)
exit_button.place(x=150, y=550)

win.mainloop()