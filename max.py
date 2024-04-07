from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title("MaxTechnology")
root.geometry("%dx%d+%d+%d"%(800,550,10,30))
root.configure(bg="#00003f")
root.resizable(False,False)
user=[]

frame=Frame(root,width=235,height=290,border=0)
frame.configure(bg="#00003f")
frame.place(x=15,y=30)

def onclickregister(e):
    try:
        if btn_register.cget("state")==NORMAL:
            dic = {"name": txt_name.get(), "lastname": txt_lastname.get(), "age": int(txt_age.get()), "location": txt_location.get()}
            if exist(dic)==False:
                register(dic)
                insert(dic)
                cleartxt()
                messagebox.showinfo("Register","Done Successfully")
            else:messagebox.showwarning("ripeated","person existing")
    except:
        messagebox.showwarning("Warning","fill all fileds")

def register(value):
    user.append(value)

def insert(value):
    tbl.insert('',"end",values=[value["name"],value["lastname"],value["location"],int(value["age"])])


def cleartxt():
    txtnamevar.set("")
    txtlastnamevar.set("")
    txtlocationvar.set("")
    txtagevar.set("")

def activebtn(e):
    if txt_name.get()=="":
        btn_register.configure(state=DISABLED)
    else:
        btn_register.configure(state=NORMAL)

def getselection(e):
    selection=tbl.selection()
    if selection!=():
        s=tbl.item(selection)["values"]
        txtnamevar.set(s[0])
        txtlastnamevar.set(s[1])
        txtagevar.set(s[3])
        txtlocationvar.set(s[2])

def onclicksearch(e):
    a1=txt_search.get()
    result=search(a1)
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
        tbl.insert('', "end", values=[value["name"], value["lastname"],value["location"], str(value["age"])])

def exist(value):
    for item in user:
        if item["name"]==value["name"] and item["lastname"]==value["lastname"] and item["age"]==value["age"] and item["location"]==value["location"]:
            return True
    return False

def onclickdelete(e):
    dialog= messagebox.askyesno("Delete warning","are you sure to delete")
    if dialog==True:
        dic={"name":txt_name.get(),"lastname":txt_lastname.get(),"location":txt_location.get(),"age":int(txt_age.get())}
        delete(dic)
        remove_tbl()
        cleartxt()

def delete(value):
    for item in user:
        if item["name"] == value["name"]  and item["lastname"] == value["lastname"]  and item["age"] == value["age"] and item["location"] == value["location"]:
            user.remove(value)

def remove_tbl():
    selection = tbl.selection()
    if selection != ():
        tbl.delete(selection)

def load ():
    clear()
    list=user.sort()
    for item in list:
        Insert(item)

def onclickupdate(e):
    selct=tbl.selection()
    if selct !=():
        select_item=tbl.item(selct)["values"]
        dic={"name":select_item[0],"lastname":select_item[1],"age":int(select_item[3]),"location":select_item[2]}
        index1=update(dic)
        p=user[index1]
        tbl.item(selct,values=[p["name"],p["lastname"],p["location"],p["age"]])


def update(value):
    index=user.index(value)
    user[index]={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get()),"location":txt_location.get()}
    return index
















