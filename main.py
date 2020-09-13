from tkinter import *

def click(event):
    global uservalue
    text = event.widget.cget("text")
    if text == "=":
        if uservalue.get().isdigit():
            value = int(uservalue.get())
            
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                value = "Error"    

        uservalue.set(value)
        screen.update()

    elif text == "C":
        uservalue.set("")
        screen.update()
        
    else:
        uservalue.set(uservalue.get() + text )
        screen.update()

root =Tk()
root.minsize(400,600)
root.maxsize(400,600)
root.wm_iconbitmap("c_icon.ico")
root.title("Calculator-GUI")

uservalue = StringVar()
uservalue.set("")
screen = Entry(root, textvariable= uservalue, bd=10, bg ="powder blue", fg ="blue",font ="lucida 35 bold")
screen.pack(side=TOP,padx =5,pady = 5,fill = BOTH, expand = YES)

frame1 = Frame(root, relief=RIDGE, borderwidth=2,bg ="powder blue")

b = Button(frame1,text="1",comman=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame1,text="2",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame1,text="3",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

frame1.pack(fill=BOTH,expand=YES)

frame2 = Frame(root, relief=RIDGE, borderwidth=2,bg ="powder blue")

b= Button(frame2,text="4",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame2,text="5",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame2,text="6",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

frame2.pack(fill=BOTH,expand=YES)

frame3 = Frame(root, relief=RIDGE, borderwidth=2,bg ="powder blue")

b = Button(frame3,text="7",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame3,text="8",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame3,text="9",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

frame3.pack(fill=BOTH,expand=YES)

frame6 = Frame(root, relief=RIDGE, borderwidth=2,bg ="powder blue")

b = Button(frame6,text="0",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame6,text="=",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame6,text=".",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

frame6.pack(fill=BOTH,expand=YES)

frame4 = Frame(root, relief=RIDGE, borderwidth=2,bg ="powder blue")

b = Button(frame4,text="+",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame4,text="-",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame4,text="*",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

frame4.pack(fill=BOTH,expand=YES)

frame5 = Frame(root, relief=RIDGE, borderwidth=2,bg ="powder blue")

b = Button(frame5,text="/",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame5,text="exit",command=root.destroy, bd =15, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

b = Button(frame5,text="C",command=click, bd =20, bg ="blue",fg ="white")
b.pack(side=LEFT,anchor = NW, padx = 40, pady = 5)
b.bind("<Button-1>",click)

frame5.pack(fill=BOTH,expand=YES)

root.mainloop()
