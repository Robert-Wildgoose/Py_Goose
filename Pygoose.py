from tkinter import *
#Assignment Submission
#N0507072 - Robert Wildgose
#Program Name PyGoose


from subprocess import Popen, PIPE, call
from tkinter.filedialog import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
        menu = Menu(root)
        root.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New",command=self.new_file)
        filemenu.add_separator()
        filemenu.add_command(label="Open",command=self.file_open)
        filemenu.add_command(label="Save As",command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=self.do_exit)

    def do_exit(self):
        root.destroy()

    def new_file(self):
        self.content.delete(0.0,END)
        self.output.delete(0.0,END)
        self.error.delete(0.0,END)

    def file_save(self):
        fout = asksaveasfile(mode='w', defaultextension=".py")
        programcode = str(self.content.get(0.0,END))
        fout.write(programcode)
        fout.close()

    def file_open(self):
        initial_dir = "C:\Temp"
        mask = \
        [("Text and Python files","*.txt *.py *.pyw"), 
        ("HTML files","*.htm"), 
        ("All files","*.*")]        
        fin = askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
        text = fin.read()
        if text != None:
            self.content.delete(0.0, END)
            self.content.insert(END,text)

    def create_widgets(self):
        self.contentlabel=Label(self,text="Welcome To PyGoose")
        self.contentlabel.grid(row=0,column=0)
        self.content=Text(self,width=40,height=20)
        self.content.grid(row=1,column=0)
        self.output=Text(self,width=40,height=6,fg="blue")
        self.output.grid(row=2,column=0)
        self.error=Text(self,width=40,height=6,fg="red")
        self.error.grid(row=3,column=0)
        self.test=Button(self,text="Test Code",width=40,command=self.test)
        self.test.grid(row=4,column=0)

    def test(self):
        self.output.insert(0.0,"\n>>------END------<<\n")
        self.error.insert(0.0,"\n>>------END------<<\n")
        content=self.content.get(0.0,END)
        filename="default.py" 
        text_file=open(filename,"w") 
        text_file.write(content) 
        text_file.close()
        pipe = Popen('python default.py', stdout=PIPE,stderr=PIPE)
        output=pipe.communicate()
        self.output.insert(0.0,output[0]) 
        self.error.insert(0.0,output[1])

root = Tk() 
root.configure(background='black')
root.title("Pygoose")  
#root.geometry("515x570") 
root.resizable(0,0) 
app=Application(root) 
#root.wm_iconbitmap('MyIcon.ico') 
root.mainloop()
