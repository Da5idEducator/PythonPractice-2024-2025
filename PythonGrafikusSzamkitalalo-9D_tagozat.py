import tkinter as tk
import random

def main():
    root = tk.Tk()
    root.geometry("400x400")
    intSecretNumber = -999
    tipp_var = tk.StringVar
    
    def cmdGenerateNumber():
        intSecretNumber = random.randint(1, 100)
        btnGenerateNumber.config(state="disabled")
        txtTipp.config(state="enabled")
    
    root.title('Találd ki a számot!')
    label = tk.Label(root, 
                     text="Találd ki a titkos számot!",
                     font=("calibri", 12, "normal",),
                     justify="center",
                     wraplength="300",
                     padx=20,
                     pady=20,
                     bd=3)
    label.pack(padx=10, pady=10)
    
    btnGenerateNumber = tk.Button(root, 
                                  text='Gondolj egy számra!',
                                  font=("calibri", 12, "normal"),
                                  command = cmdGenerateNumber)
    
    lblTipp = tk.Label(root,
                       text="Tipp:",
                       font=("calibri", 12, "normal"))
    
    txtTipp = tk.Entry(root,
                       font=("calibri", 12, "normal"),
                       textvariable=tipp_var,
                       state="disabled")
    
    btnGenerateNumber.pack(padx=10, pady=10)
    lblTipp.pack(padx=10, pady=5)
    txtTipp.pack(padx=10, pady=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()