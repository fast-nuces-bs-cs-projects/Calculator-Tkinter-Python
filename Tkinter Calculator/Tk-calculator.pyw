#############################################
### Author      : M.ROHAN FAROOQUI          #
##  Application : Tkinter Calculator        #
##  File        : Calculator- Tk.pyw        #
############################################# 


###Imports

###Gui Libraries
import tkinter as tk
import tkinter.ttk as ttk
from   tkinter import *
#MSG dialog box
from tkinter import messagebox
#Ask to save File
from tkinter.filedialog import asksaveasfile
from tkinter  import simpledialog
#Tkinter Theme File 
from ttkthemes import ThemedStyle
### Other Lib
import webbrowser
### Math Library
from math import sqrt


expression_solved = False
###Main Code
class Main_Window(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    ## Change Color
    def on_enter_github_link(self,e):
            self.copyright_symbol['foreground'] = '#f68557'
    def on_leave_github_link(self,e):
            self.copyright_symbol['foreground'] = 'black'

    ## Open Link in Browser
    def callback_1(self,event):
          webbrowser.open_new(r"https://rohanfarooqui.wordpress.com/")            

    ## Get Operands and Numbers
    def get_numbers(self,x):
        global expression_solved
        self.entry.configure(state='normal')
        if(expression_solved == True):
            self.entry.delete(0, END)
            expression_solved =  False

        temp = str(self.entry.get())
        temp = temp+str(x)
        self.entry.delete(0,END)
        self.entry.insert(0,temp)
        self.entry.configure(state='disabled')

    ## Clear Entry 
    def clear_entry(self):
        self.entry.configure(state='normal')
        self.entry.delete(0, END)
        self.entry.configure(state='disabled')

    ## Solve Expression
    def solve_expression(self):
        global expression_solved
        if(len(self.entry.get())>1):
            if("%" in self.entry.get()):
                try:
                    temp = self.entry.get()
                    temp = temp.replace("%","/100")
                    temp = eval(temp)
                    self.entry.configure(state='normal')
                    self.entry.delete(0, END)
                    self.entry.insert(0,temp)
                    self.entry.configure(state='disabled')
                except:
                    self.entry.configure(state='normal')
                    self.entry.delete(0, END)
                    self.entry.insert(0,"Error .. !!")
                    self.entry.configure(state='disabled')
            else:
                try:
                    temp = eval(self.entry.get())
                    self.entry.configure(state='normal')
                    self.entry.delete(0, END)
                    self.entry.insert(0,temp)
                    self.entry.configure(state='disabled')
                except:
                    self.entry.configure(state='normal')
                    self.entry.delete(0, END)
                    self.entry.insert(0,"Error .. !!")
                    self.entry.configure(state='disabled')
        expression_solved = True


    ## Solve Square Root
    def solve_square_root(self):
        global expression_solved
        temp = self.entry.get()
        try:
            temp = eval(temp)
            temp = round(sqrt(int(temp)),4)
            self.entry.configure(state='normal')
            self.entry.delete(0, END)
            self.entry.insert(0,temp)
            self.entry.configure(state='disabled')
        except:
            self.entry.configure(state='normal')
            self.entry.delete(0, END)
            self.entry.insert(0,"Error .. !!")
            self.entry.configure(state='disabled')            
        expression_solved = True

        
        



            



    ## Init Main Window
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Tk - Simple - Calculator')
        self.root.geometry("324x340")
        self.root.resizable(width=False, height=False)
        try:
            self.root.iconbitmap("logo\logo.ico")
        except:
            pass

        #=> Style Add
        style = ThemedStyle(self.root)
        style.set_theme("radiance")
        
        style.configure('W.TButton', font =('Times', 25),foreground = 'black')
        style.configure('B.TButton', font =('Times', 10),foreground = 'black')

 
        

        self.entry   = ttk.Entry(self.root,width="17",justify='left',font = ('Times', 26, 'bold'))
        self.entry.grid(row=0,column=1,padx=5, pady=5)


        #=> First Box
        self.root.first_box = ttk.Frame(self.root,relief=FLAT,borderwidth=1)

        
        self.button_generate= ttk.Button(self.root.first_box, width=6,style ='B.TButton',text="CE",command= self.clear_entry)
        self.button_generate.grid(row=1,column=0,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.first_box, width=5,style ='B.TButton',text="SQRT",command= self.solve_square_root)
        self.button_generate.grid(row=1,column=1,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.first_box, width=2,style ='W.TButton',text="%",command= lambda: self.get_numbers("%"))
        self.button_generate.grid(row=1,column=2,padx=5, pady=5)

        self.button_generate= ttk.Button(self.root.first_box, width=2,style ='W.TButton',text="÷",command= lambda: self.get_numbers("/"))
        self.button_generate.grid(row=1,column=3,padx=3, pady=3)

        self.root.first_box.place(relx=0.001, rely=0.15,anchor=NW)

        #=> Second Box

        self.root.second_box = ttk.Frame(self.root,relief=FLAT,borderwidth=1)
        
        self.button_generate= ttk.Button(self.root.second_box, width=2,style ='W.TButton',text="7",command= lambda: self.get_numbers(7))
        self.button_generate.grid(row=2,column=0,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.second_box, width=2,style ='W.TButton',text="8",command= lambda: self.get_numbers(8))
        self.button_generate.grid(row=2,column=1,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.second_box, width=2,style ='W.TButton',text="9",command= lambda: self.get_numbers(9))
        self.button_generate.grid(row=2,column=2,padx=5, pady=5)

        self.button_generate= ttk.Button(self.root.second_box, width=2,style ='W.TButton',text="x",command= lambda: self.get_numbers("*"))
        self.button_generate.grid(row=2,column=3,padx=3, pady=3)

        self.root.second_box.place(relx=0.001, rely=0.29,anchor=NW)

        #=> Third Box

        self.root.third_box = ttk.Frame(self.root,relief=FLAT,borderwidth=1)
        
        self.button_generate= ttk.Button(self.root.third_box, width=2,style ='W.TButton',text="4",command= lambda: self.get_numbers(4))
        self.button_generate.grid(row=3,column=0,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.third_box, width=2,style ='W.TButton',text="5",command= lambda: self.get_numbers(5))
        self.button_generate.grid(row=3,column=1,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.third_box, width=2,style ='W.TButton',text="6",command= lambda: self.get_numbers(6))
        self.button_generate.grid(row=3,column=2,padx=5, pady=5)

        self.button_generate= ttk.Button(self.root.third_box, width=2,style ='W.TButton',text="+",command= lambda: self.get_numbers("+"))
        self.button_generate.grid(row=3,column=3,padx=3, pady=3)

        self.root.third_box.place(relx=0.001, rely=0.43,anchor=NW)

        #=> Fourth Box
        
        self.root.fourth_box = ttk.Frame(self.root,relief=FLAT,borderwidth=1)
        
        self.button_generate= ttk.Button(self.root.fourth_box, width=2,style ='W.TButton',text="1" ,command= lambda: self.get_numbers(1))
        self.button_generate.grid(row=4,column=0,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.fourth_box, width=2,style ='W.TButton',text="2",command= lambda: self.get_numbers(2))
        self.button_generate.grid(row=4,column=1,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.fourth_box, width=2,style ='W.TButton',text="3",command= lambda: self.get_numbers(3))
        self.button_generate.grid(row=4,column=2,padx=5, pady=5)

        self.button_generate= ttk.Button(self.root.fourth_box, width=2,style ='W.TButton',text="-",command= lambda: self.get_numbers("-"))
        self.button_generate.grid(row=4,column=3,padx=3, pady=3)

        self.root.fourth_box.place(relx=0.001, rely=0.57,anchor=NW)

        #=> Fifth Box
        self.root.fifth_box = ttk.Frame(self.root,relief=FLAT,borderwidth=1)
        
        self.button_generate= ttk.Button(self.root.fifth_box, width=6,style ='W.TButton',text="0",command= lambda: self.get_numbers(0))
        self.button_generate.grid(row=1,column=0,padx=3, pady=3)

        self.button_generate= ttk.Button(self.root.fifth_box, width=2,style ='W.TButton',text=".",command= lambda: self.get_numbers("."))
        self.button_generate.grid(row=1,column=2,padx=10, pady=3)

        self.button_generate= ttk.Button(self.root.fifth_box, width=2,style ='W.TButton',text="=",command= self.solve_expression)
        self.button_generate.grid(row=1,column=3,padx=5, pady=3)
        
        self.root.fifth_box.place(relx=0.001, rely=0.71,anchor=NW)

        
        #=> Copyright Symbol -> Changing Color / Open Website link in Browser
        style.configure('A.TButton', font =('Times', 10),foreground = 'black')
        self.copyright_symbol = ttk.Label(self.root,style ='A.TButton',text="M.ROHAN FAROOQUI ©")
        self.copyright_symbol.bind("<Button-1>", self.callback_1)
        self.copyright_symbol.place(relx=0.23, rely=0.91,anchor=NW)
        self.copyright_symbol.bind("<Enter>", self.on_enter_github_link)
        self.copyright_symbol.bind("<Leave>", self.on_leave_github_link)

        
             
        


       

        
        
if __name__ == '__main__':
    root = tk.Tk()
    Main_Window(root)
    root.mainloop()
