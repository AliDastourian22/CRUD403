from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title("MaxTechnology")
root.geometry("%dx%d+%d+%d" % (800, 550, 10, 30))
root.configure(bg="#00003f")
root.resizable(False,False)
user=[]

frame=Frame(root, width=235, height=290, border=0)
frame.configure(bg="#00003f")
frame.place(x=15, y=30)

def onclickregister(e):
    try:
        if btn_register.cget("state") == NORMAL:
            dic = {"name": txt_name.get(), "lastname": txt_lastname.get(), "age": int(txt_age.get()), "location": txt_location.get()}
            if not exist(dic):
                register(dic)
                insert(dic)
                cleartxt()
                messagebox.showinfo("Register", "Done Successfully")
            else: messagebox.showwarning("ripeated", "person existing")
    except:
        messagebox.showwarning("Warning", "fill all fileds")

def register(value):
    user.append(value)

def insert(value):
    tbl.insert('', "end", values=[value["name"], value["lastname"], value["location"], int(value["age"])])


txtnamevar = StringVar()
txtlastnamevar = StringVar()
txtlocationvar = StringVar()
txtagevar = StringVar()
txtphonevar = StringVar()
txtsearchvar = StringVar


def cleartxt():
    txtnamevar.set("")
    txtlastnamevar.set("")
    txtlocationvar.set("")
    txtagevar.set("")

def activebtn(e):
    if txt_name.get() == "":
        btn_register.configure(state=DISABLED)
    else:
        btn_register.configure(state=NORMAL)

def getselection(e):
    selection = tbl.selection()
    if selection!=():
        s = tbl.item(selection)["values"]
        txtnamevar.set(s[0])
        txtlastnamevar.set(s[1])
        txtagevar.set(s[3])
        txtlocationvar.set(s[2])

def onclicksearch(e):
    a1 = txt_search.get()
    result = search(a1)
    clear()
    for item in result:
        insert(item)
def search(value):
    resultlis = []
    for item in user:
        if item["name"] == txt_search.get() or item["lastname"] == txt_search.get() or str(item["age"]) == txt_search.get() or item["location"] == txt_search.get():
            resultlis.append(item)

    return resultlis


def clear():
    for item in tbl.get_children():
        sel = str(item,)
        tbl.delete(sel)

def load_and_clear(value):
    for item in tbl.get_children():
        sel = str(item, )
        tbl.delete(sel)
    for item in value:
        tbl.insert('', "end", values=[value["name"], value["lastname"], value["location"], str(value["age"])])

def exist(value):
    for item in user:
        if item["name"]==value["name"] and item["lastname"] == value["lastname"] and item["age"] == value["age"] and item["location"] == value["location"]:
            return True
    return False

def onclickdelete(e):
    dialog = messagebox.askyesno("Delete warning", "are you sure to delete")
    if dialog==True:
        dic = {"name": txt_name.get(), "lastname": txt_lastname.get(), "location": txt_location.get(), "age": int(txt_age.get())}
        delete(dic)
        remove_tbl()
        cleartxt()

def delete(value):
    for item in user:
        if item["name"] == value["name"] and item["lastname"] == value["lastname"] and item["age"] == value["age"] and item["location"] == value["location"]:
            user.remove(value)

def remove_tbl():
    selection = tbl.selection()
    if selection != ():
        tbl.delete(selection)

def load ():
    clear()
    list=user.sort()
    for item in list:
        insert(item)

def onclickupdate(e):
    selct = tbl.selection()
    if selct !=():
        select_item = tbl.item(selct)["values"]
        dic = {"name": select_item[0], "lastname": select_item[1], "age": int(select_item[3]), "location": select_item[2]}
        index1 = update(dic)
        p = user[index1]
        tbl.item(selct, values=[p["name"], p["lastname"], p["location"], p["age"]])


def update(value):
    index = user.index(value)
    user[index] = {"name": txt_name.get(), "lastname": txt_lastname.get(), "age": int(txt_age.get()), "location": txt_location.get()}
    return index

def onenter(e):
    txt_name.delete(0, "end")

def onleave(e):
    name = txt_name.get()
    if name == (""):
        txt_name.insert(0, "name")

txt_name = Entry(frame, width=235, border=0, bg="#00003f", fg="#fff")
txt_name.configure(font="Mj_Elit 18", textvariable=txtnamevar)
txt_name.bind("<FocusIn>", onenter)
txt_name.bind("<FocusOut>", onleave)
txt_name.insert(0, "name")
txt_name.place(x=0, y=25)
Frame(frame, width=235, height=1, border=0, bg="#c4196f").place(x=0, y=55)

def onenter(e):
    txt_lastname.delete(0, "end")

def onleave(e):
    lastname = txt_lastname.get()
    if lastname == (""):
        txt_lastname.insert(0, "lastname")

txt_lastname = Entry(frame, width=235, border=0, bg="#00003f", fg="#fff")
txt_lastname.configure(font="Mj_Elit 18", textvariable=txtlastnamevar)
txt_lastname.bind("<FocusIn>", onenter)
txt_lastname.bind("<FocusOut>", onleave)
txt_lastname.insert(0, "lastname")
txt_lastname.place(x=0, y=75)
Frame(frame, width=235, height=1, border=0, bg="#c4196f").place(x=0, y=105)

def onenter(e):
    txt_age.delete(0, "end")

def onleave(e):
    age = txt_age.get()
    if age == (""):
        txt_age.insert(0, "age")

txt_age=Entry(frame, width=235, border=0, bg="#00003f", fg="#fff")
txt_age.configure(font="Mj_Elit 18", textvariable=txtagevar)
txt_age.bind("<FocusIn>", onenter)
txt_age.bind("<FocusOut>", onleave)
txt_age.insert(0,"age")
txt_age.place(x=0,y=126)
Frame(frame, width=235, height=1, border=0, bg="#c4196f").place(x=0, y=155)

def onenter(e):
    txt_location.delete(0, "end")

def onleave(e):
    age = txt_location.get()
    if age == (""):
        txt_location.insert(0, "location")

txt_location=Entry(frame, width=235, border=0, bg="#00003f", fg="#fff")
txt_location.configure(font="Mj_Elit 18", textvariable=txtlocationvar)
txt_location.bind("<FocusIn>", onenter)
txt_location.bind("<FocusOut>", onleave)
txt_location.insert(0, "location")
txt_location.place(x=0, y=180)
Frame(frame, width=235, height=1, border=0, bg="#c4196f").place(x=0, y=211)

def on_enter(e):
    txt_search.delete(0, "end")

def on_leave(e):
    search = txt_search.get()
    if search == "":
        txt_search.insert(0, "Search")

txt_search=Entry(root,fg="#ffffff", width=10, border=0, bg="#00003f")
txt_search.configure(font="Mj_Elit 15")
txt_search.insert(0, "Search")
txt_search.bind("<FocusIn>", on_enter)
txt_search.bind("<FocusOut>", on_leave)
Frame(root, width=112, height=1, bg="#c4196f").place(x=470, y=285)
txt_search.place(x=470, y=260)

btn_register=Button(root, text="Register", width=15, fg="#ffffff", font="arial 8 bold")
btn_register.configure(bg="#cb4382", fg="#ffffff", border=0)
btn_register.bind("<Button-1>", onclickregister)
btn_register.place(x=140, y=260)

btn_delete = Button(root,text="Delete", width=15, fg="#ffffff", font="arial 8 bold")
btn_delete.configure(bg="#cb4382", fg="#ffffff", border=0)
btn_delete.bind("<Button-1>", onclickdelete)
btn_delete.place(x=140, y=290)

btn_search = Button(root, text="Search", width=15, border=0, bg="#cb4382", fg="#ffffff", font="arial 8 bold")
btn_search.configure(bg="#cb4382")
btn_search.place(x=596, y=263)
btn_search.bind("<Button-1>", onclicksearch)

btn_update = Button(root, text="update", width=15, border=0, bg="#cb4382", fg="#ffffff", font="arial 8 bold")
btn_update.configure(bg="#cb4382")
btn_update.place(x=15, y=260)
btn_update.bind("<Button-1>", onclickupdate)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#000066", foreground="white", fieldbackground="#000066", rowheight=20, border=0)
style.map("Treeview", background=[("selected", "#248fc7")])

column = ("c1", "c2", "c3", "c4")
tbl = ttk.Treeview(root, column=column, show="headings")
tbl.heading(column[0], text="name")
tbl.column(column[0], width=60)
tbl.heading(column[1], text="lastname")
tbl.column(column[1], width=60)
tbl.heading(column[3], text="age")
tbl.column(column[3], width=60)
tbl.heading(column[2], text="loaction")
tbl.column(column[2], width=60)
tbl.bind("<Button-1>", getselection)
tbl.place(x=470, y=310)



root.mainloop()
