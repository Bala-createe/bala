import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import webbrowser 
#creating the main window for projection
window = Tk() 
window.title("Project Crypto")
window.geometry("1270x700") 
#placing BG image
bg = PhotoImage(file =r"C:\Users\user\Downloads\vta.png")
label1 = Label( window, image = bg) 
label1.place(x = 0, y = 0) 
#this label for simple title
label = tk.Label(text= ' CRYPTO ANALYSIS ',font=("Century",16),bg="BLACK",fg="WHITE")
label.pack(pady=150,anchor=CENTER,padx=0)
#In this function if,elif,else executed to perform the currency name and password 
#elif used for get heterogeneous names and passwords
def login(event=None):
    username = username_entry.get()
    password = password_entry.get() 
    if (username == "BTC" and password == "bala")or(password=="2004"):
#here if,else used to question the user and proceed
        result = messagebox.askyesno("Confirmation", " Do you want to \n connect with external web?")
        if result==YES:
           messagebox.showinfo("Hi","***This page is only for study purpose***")
           webbrowser.open('https://www.google.com/finance/quote/BTC-usd?window=5Y') 
        else:
            window.minsize(20,20)
               
    elif(username == "ETC" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***")
        webbrowser.open('https://www.google.com/finance/quote/ETC-INR?window=5Y')  

    elif(username == "USDT" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***")  
        webbrowser.open('https://www.google.com/finance/quote/USDT-INR?window=5Y')

    elif(username == "BNB" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***")   
        webbrowser.open('https://www.google.com/finance/quote/BNB-INR?window=5Y')

    elif(username == "LTC" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***")  
        webbrowser.open('https://www.google.com/finance/quote/LTC-INR?window=5Y') 

    elif(username == "DOGE" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***")  
        webbrowser.open('https://www.google.com/finance/quote/DOGE-INR?window=5Y') 

    elif(username == "NXT" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***") 
        webbrowser.open('https://www.google.com/finance/quote/NXT-INR?window=5Y')  

    elif(username == "TRON" and password == "bala"):
        messagebox.showinfo("Hi","Login Successful")
        messagebox.showinfo("Hi","***This page is only for study purpose***")  
        webbrowser.open('https://www.google.com/finance/quote/TRX-INR?window=5Y') 

    else:
        messagebox.showerror("Retry", "Need help?... contact your admin Bala",)
#user enty box    
tk.Label(window,background="white",text="Search Crypto here ",fg="white",bg="indigo",font="Algerian").pack(pady=5,anchor=W,padx=100) 
username_entry = tk.StringVar()
username_entry = tk.Entry(window)
username_entry = ["BTC", 
                  "ETC", 
                  "USDT", 
                  "BNB",
                  "LTC",
                  "DOGE",
                  "NXT",
                  "TRON",]
username_entry = ttk.Combobox(window, textvariable=username_entry, values= username_entry,foreground="limegreen")
username_entry.pack(pady=5,anchor=W,padx=100) 
#password entry box
tk.Label(window,text="Password",fg="white",bg="indigo",font=("Algerian")).pack(pady=5,anchor=W,padx=100) 
password_entry = tk.Entry(window)
password_entry = (["Hint:Admin's name"])
password_entry = ttk.Combobox(window, textvariable=password_entry, values= password_entry,show="*",foreground="black")
password_entry.pack(pady=10,anchor=W,padx=100)
#login button 
login_button = tk.Button(window,background="WHITE",text="click here", command=login,fg="BLACK")
login_button.pack(pady=20,anchor=W,padx=100)
#simple label
a= Label(window, text='Server: INDIA ',fg="green",bg="black")
a.pack(anchor=W,pady=120,padx=10)
#run window
username_entry.bind("<Return>", lambda event:login(event))

password_entry.bind("<Return>", lambda event:login(event))

login_button.bind("<Return>", lambda event:login(event))


window.mainloop()

