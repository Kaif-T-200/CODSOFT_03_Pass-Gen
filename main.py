# MADE BY KAIF TARASAGAR
import tkinter as tk
from tkinter import messagebox# MADE BY KAIF TARASAGAR
import random, string
# MADE BY KAIF TARASAGAR
def make_password():
    chars = ""
    if letters.get(): chars += string.ascii_letters
    if numbers.get(): chars += string.digits# MADE BY KAIF TARASAGAR
    if symbols.get(): chars += string.punctuation
    if not chars:# MADE BY KAIF TARASAGAR
        messagebox.showerror("Error", "Pick at least one option!")
        return
    pwd = "".join(random.choice(chars) for _ in range(length.get()))
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, pwd)
    entry.config(state="readonly")# MADE BY KAIF TARASAGAR
    check_strength(pwd)

def check_strength(pwd):
    l = len(pwd)
    if l >= 12 and any(c in string.punctuation for c in pwd):
        text, color = "Strong", "green"# MADE BY KAIF TARASAGAR
    elif l >= 8:
        text, color = "Medium", "orange"
    else:# MADE BY KAIF TARASAGAR
        text, color = "Weak", "red"
    strength.config(text=f"Strength: {text}", fg=color)

def copy_pwd(e):
    pwd = entry.get()
    if pwd:
        root.clipboard_clear()# MADE BY KAIF TARASAGAR
        root.clipboard_append(pwd)
        msg.config(text="✅ Copied!")
        root.after(2000, lambda: msg.config(text=""))

def reset():
    entry.config(state="normal")# MADE BY KAIF TARASAGAR
    entry.delete(0, tk.END)
    entry.config(state="readonly")
    strength.config(text="Strength: N/A", fg="black")# MADE BY KAIF TARASAGAR
    msg.config(text="")
root = tk.Tk()# MADE BY KAIF TARASAGAR
root.title("Password Generator")
root.geometry("400x470")
root.config(bg="white")

tk.Label(root, text="🔑 Password Generator", font=("Arial", 20, "bold"), bg="white").pack(pady=15)
# MADE BY KAIF TARASAGAR
length = tk.IntVar(value=12)
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="white").pack()
tk.Scale(root, from_=4, to=32, orient="horizontal", variable=length, bg="white", length=250).pack()

letters = tk.BooleanVar(value=True)# MADE BY KAIF TARASAGAR
numbers = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)
for text, var in [("Include Letters", letters), ("Include Numbers", numbers), ("Include Symbols", symbols)]:
    tk.Checkbutton(root, text=text, variable=var, bg="white").pack(anchor="w", padx=40)
tk.Button(root, text="Generate Password", command=make_password,# MADE BY KAIF TARASAGAR
          font=("Arial", 16, "bold"), bg="#007bff", fg="white", width=15, height=2).pack(pady=15)
tk.Button(root, text="♻️ Reset", command=reset, bg="#dc3545", fg="white", font=("Arial", 12, "bold"), width=12).pack()
entry = tk.Entry(root, font=("Arial", 16), width=25, justify="center", state="readonly")
entry.pack(pady=15)
entry.bind("<Button-1>", copy_pwd)# MADE BY KAIF TARASAGAR

msg = tk.Label(root, text="", font=("Arial", 12), fg="green", bg="white")
msg.pack()
strength = tk.Label(root, text="Strength: N/A", font=("Arial", 12, "bold"), bg="white")
strength.pack(pady=10)
# MADE BY KAIF TARASAGAR
root.mainloop()


                                        #-- MADE BY KAIF TARASAGAR 
                                               
                                         # https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                         # https://x.com/Kaif_T_200