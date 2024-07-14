import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from ctypes import windll
import os

GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080

def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    # re-assert the new window style
    root.wm_withdraw()
    root.after(1, lambda: root.wm_deiconify())

def main():
    #root = tk.Tk()
    root = Tk()
    root.wm_title("")
    
    # Adjust size  
    #root.geometry("500x400")
    root.geometry("230x200+1130+530")    
  
    # Add image file 
    bg = PhotoImage(file = "icon1.png") 
      
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 

    style = ttk.Style(root)
    #style.configure('TButton', background = 'red', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
    style.configure('TButton', background = 'white', foreground = '#006400', padding=(-5, -5), width=3, borderwidth=0)
    style.map('TButton', background=[('active','#006400')])
    button = ttk.Button(root, text='X', style='TButton', command=lambda: root.destroy())
    button.pack()
    button.place(x=215,y=0)
    
    style1 = ttk.Style(root)
    style1.configure('Padded.TButton', padding=(-5, -5), width=10)
    button1 = ttk.Button(text="PRESS ME", command=greet , style='Padded.TButton')
    button1.pack()
    button1.place(x=0, y=0)
    
    
    root.overrideredirect(True)
    root.after(1, lambda: set_appwindow(root))
    root.mainloop()
    
def greet():
    os.system("C:/babu/pycode/botbatch.bat ")


if __name__ == '__main__':
    main()