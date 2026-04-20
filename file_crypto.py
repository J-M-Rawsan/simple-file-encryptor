import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        messagebox.showinfo("Key Generated", "Encryption key generated and saved done")

def load_key():
    return open("secret.key", "rb").read()
def encrypt_file():
    filepath = filedialog.askopenfilename(title="Select a file to encrypt")
    if not filepath:
        return
    key = load_key()
    fernet = Fernet(key)    
    f= fernet
    with open(filepath, "rb") as file:

        file_data = file.read()
    encrypted_data = f.encrypt(file_data)       
    with open(filepath + ".enc", "wb") as file:
        file.write(encrypted_data)  
    messagebox.showinfo("success", "File encrypted successfully")

def decrypt_file():
    filepath = filedialog.askopenfilename(title="Select a file to decrypt", filetypes=[("Encrypted files", "*.enc")])
    if not filepath:
        return
    key = load_key()
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        decrypted_filepath = os.path.splitext(filepath)[0]
        with open(decrypted_filepath, "wb") as file:
            file.write(decrypted_data)
        messagebox.showinfo("Success", "File decrypted successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

        # GUI Interface
        
root = tk.Tk()
root.title("simple file crypttl")
root.geometry("300x200")

tk.Button(root, text="Generate Key", command=generate_key).pack(pady=10)
tk.Button(root, text="Encrypt File", command=encrypt_file).pack(pady=10)
tk.Button(root, text="Decrypt File", command=decrypt_file).pack(pady=10)    
root.mainloop()