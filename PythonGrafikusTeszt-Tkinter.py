import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("400x400")
    
    root.title('Az első grafikus ablakom!')
    label = tk.Label(root, text = 'Helló Világ!',
                     font=("calibri", 12, "bold"))
    label.pack()
    
    def btnGomb_clicked():
        print("Rákattintottál a gombra!")
        
    def btnKikapcsolas_clicked():
        root.destroy()
        
    
    btnGomb = tk.Button(root, text="Kattints rám!",
                     command=btnGomb_clicked,
                     activebackground="blue",
                     activeforeground="white",
                     anchor="center",
                     bd=3,
                     bg="lightgray",
                     cursor="hand2",
                     disabledforeground="gray",
                     fg="black",
                     font=("calibri", 12, "normal"),
                     height=2,
                     highlightbackground="black",
                     highlightcolor="green",
                     highlightthickness=2,
                     justify="center",
                     overrelief="raised",
                     padx=10,
                     pady=5,
                     width=15,
                     wraplength=100)
    btnGomb.pack(padx=20, pady=20)
    
    message_var = tk.StringVar()
    
    lblOutput_label = tk.Label(root, text="",
                               font=("calibri", 12, "normal"))
    
    def submit():
        message = message_var.get()
        print("Az üzenet:", message)
        lblOutput_label.config(text=message)
        message_var.set("")
        
    lblMessage_label = tk.Label(root, text='Üzenet', 
                                font=('calibre', 12, 'normal'))
    
    txtUzenet_entry = tk.Entry(root, textvariable = message_var,
                               font=('calibre', 12, 'normal'))
    
    btnSubmit = tk.Button(root, text='Küldés!',
                          command=submit,
                          activebackground="green",
                          activeforeground="white",
                          font=("calibri", 12, "normal"),
                          bd=3,
                          padx=10,
                          pady=5,
                          width=15,
                          wraplength=100,
                          justify="center",
                          overrelief="raised",
                          cursor="hand2")
    
    lblMessage_label.pack()
    txtUzenet_entry.pack()
    btnSubmit.pack(padx=10, pady=10)
    lblOutput_label.pack(padx=10, pady=10)
    
    btnKikapcsolas = tk.Button(root, text="Kilépés!",
                     command=btnKikapcsolas_clicked,
                     activebackground="red",
                     activeforeground="white",
                     anchor="center",
                     bd=3,
                     bg="lightgray",
                     cursor="hand2",
                     disabledforeground="gray",
                     fg="black",
                     font=("calibri", 12, "bold"),
                     height=2,
                     highlightbackground="black",
                     highlightcolor="green",
                     highlightthickness=2,
                     justify="center",
                     overrelief="raised",
                     padx=10,
                     pady=5,
                     width=15,
                     wraplength=100)
    btnKikapcsolas.pack(padx=20, pady=20)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
