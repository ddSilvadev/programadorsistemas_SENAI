import tkinter as tk
from tkinter import ttk


def main():
    root = root = tk.Tk()
    root.title("janela")
    root.geometry("400x300")
    root.resizable(True,True)

    label = ttk.Label(root, text="Olá, feriadão!", font=("TkDefaultFont", 16))
    label.pack(expand=True)

    btn = ttk.Button(root, text="Fechar", command=root.destroy)
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()