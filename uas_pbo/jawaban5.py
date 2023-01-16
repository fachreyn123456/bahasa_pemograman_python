import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.configure(bg="Lightblue")
root.geometry("600x700")
root.title("Rey Garden Plant")
root.resizable(False,False)

input_Frame = ttk.Frame(root)
input_Frame.pack(padx=70,pady=70,fill="x",expand=True)

L1 = ttk.Label(input_Frame, text="Anggrek, Mawar, Melati")
L1.pack(padx=70,fill="x",expand=True)

Beri_Air = tk.StringVar()
Beri_Pupuk = tk.StringVar()

# Beri Air
beri_air_label = ttk.Label(input_Frame, text="Jumlah Air: ")
beri_air_label.pack(padx=70,fill="x",expand=True)

beri_air_entry = ttk.Entry(input_Frame, textvariable="Beri_Air")
beri_air_entry.pack(padx=70,fill="x",expand=True)

# Beri Pupuk
beri_pupuk_label = ttk.Label(input_Frame, text="Jumlah Pupuk: ")
beri_pupuk_label.pack(padx=70,fill="x",expand=True)

beri_pupuk_entry = ttk.Entry(input_Frame, textvariable="Beri_Pupuk")
beri_pupuk_entry.pack(padx=70,fill="x",expand=True)

def Pilih():
    message = f"{Beri_Air.get()} {Beri_Pupuk.get()}, Berhasil Ditambahkan !"
    showinfo(title= "Done", message=message)

tombol_klik = ttk.Button(input_Frame, text="Pilih", command=Pilih)
tombol_klik.pack(fill='x',expand=True,padx=70,pady=70)

root.mainloop()