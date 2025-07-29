# a = 2
# b = 3
# c = a+b
# print(c)
# print('Hello World!')

# if(a == b):print('its not the same')
# else:print('same thing')



for attempt in range(3):
    name = input('Enter Username: ')
    if name == 'FAVOUR':
        print('Welcome')
        break
    else:
        print('access denied')
else:
    print ("too many failed attempts big bro")
    


# # # # # Step 1: Define a function to encrypt a message
# # # # def encrypt(text, shift):
# # # #     result = ""
# # # #     for char in text:
# # # #         if char.isalpha():
# # # #             # For uppercase and lowercase separately
# # # #             base = ord('A') if char.isupper() else ord('a')
# # # #             # Shift the character and wrap around using modulo
# # # #             result += chr((ord(char) - base + shift) % 26 + base)
# # # #         else:
# # # #             result += char  # Leave punctuation, numbers, spaces unchanged
# # # #     return result

# # # # # Step 2: Define a function to decrypt a message
# # # # def decrypt(text, shift):
# # # #     return encrypt(text, -shift)  # Just use negative shift to reverse

# # # # # Step 3: Get user input
# # # # message = input("Enter your message: ")
# # # # shift = int(input("Enter shift value (e.g., 3): "))
# # # # mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# # # # # Step 4: Perform the chosen operation
# # # # if mode == 'encrypt':
# # # #     encrypted_message = encrypt(message, shift)
# # # #     print("Encrypted message:", encrypted_message)
# # # # elif mode == 'decrypt':
# # # #     decrypted_message = decrypt(message, shift)
# # # #     print("Decrypted message:", decrypted_message)
# # # # else:
# # # #     print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

# # # import tkinter as tk
# # # from tkinter import messagebox

# # # # Caesar Cipher Functions
# # # def encrypt(text, shift):
# # #     result = ""
# # #     for char in text:
# # #         if char.isalpha():
# # #             base = ord('A') if char.isupper() else ord('a')
# # #             result += chr((ord(char) - base + shift) % 26 + base)
# # #         else:
# # #             result += char
# # #     return result

# # # def decrypt(text, shift):
# # #     return encrypt(text, -shift)

# # # # Button Event Handler
# # # def perform_cipher():
# # #     message = entry_message.get()
# # #     shift = entry_shift.get()
    
# # #     # Validation
# # #     if not shift.isdigit():
# # #         messagebox.showerror("Invalid Input", "Shift must be a number.")
# # #         return
    
# # #     shift = int(shift)
# # #     action = cipher_mode.get()

# # #     if action == "Encrypt":
# # #         result = encrypt(message, shift)
# # #     else:
# # #         result = decrypt(message, shift)

# # #     messagebox.showinfo(f"{action}ed Message", result)

# # # # Set up the main window
# # # window = tk.Tk()
# # # window.title("Caesar Cipher GUI")
# # # window.geometry("400x250")
# # # window.resizable(False, False)

# # # # Labels and Inputs
# # # tk.Label(window, text="Enter your message:").pack(pady=5)
# # # entry_message = tk.Entry(window, width=40)
# # # entry_message.pack()

# # # tk.Label(window, text="Enter shift value:").pack(pady=5)
# # # entry_shift = tk.Entry(window, width=10)
# # # entry_shift.pack()

# # # # Encrypt/Decrypt Option
# # # cipher_mode = tk.StringVar(value="Encrypt")
# # # tk.Radiobutton(window, text="Encrypt", variable=cipher_mode, value="Encrypt").pack()
# # # tk.Radiobutton(window, text="Decrypt", variable=cipher_mode, value="Decrypt").pack()

# # # # Submit Button
# # # tk.Button(window, text="Submit", command=perform_cipher).pack(pady=10)

# # # # Run the GUI loop
# # # window.mainloop()

# # import tkinter as tk
# # from tkinter import messagebox

# # # Caesar Cipher Functions
# # def encrypt(text, shift):
# #     result = ""
# #     for char in text:
# #         if char.isalpha():
# #             base = ord('A') if char.isupper() else ord('a')
# #             result += chr((ord(char) - base + shift) % 26 + base)
# #         else:
# #             result += char
# #     return result

# # def decrypt(text, shift):
# #     return encrypt(text, -shift)

# # # Perform cipher and copy result
# # def perform_cipher():
# #     message = text_input.get("1.0", tk.END).strip()
# #     shift_val = shift_entry.get()

# #     if not shift_val.isdigit():
# #         messagebox.showerror("Error", "Shift must be a number.")
# #         return

# #     shift = int(shift_val)
# #     action = mode.get()

# #     if action == "Encrypt":
# #         result = encrypt(message, shift)
# #     else:
# #         result = decrypt(message, shift)

# #     # Show result and copy to clipboard
# #     result_output.delete("1.0", tk.END)
# #     result_output.insert(tk.END, result)
# #     window.clipboard_clear()
# #     window.clipboard_append(result)
# #     messagebox.showinfo("Copied!", f"{action}ed text copied to clipboard!")

# # # Create main window
# # window = tk.Tk()
# # window.title("Caesar Cipher (Dark Mode)")
# # window.geometry("500x500")
# # window.configure(bg="#1e1e1e")  # Dark background

# # # Shared styling
# # label_style = {"bg": "#1e1e1e", "fg": "white", "font": ("Arial", 12)}
# # entry_style = {"bg": "#2d2d2d", "fg": "white", "insertbackground": "white", "font": ("Arial", 12)}

# # # Widgets
# # tk.Label(window, text="Enter your message:", **label_style).pack(pady=5)
# # text_input = tk.Text(window, height=6, width=50, **entry_style, wrap="word")
# # text_input.pack(pady=5)

# # tk.Label(window, text="Shift value:", **label_style).pack(pady=5)
# # shift_entry = tk.Entry(window, width=10, **entry_style)
# # shift_entry.pack(pady=5)

# # mode = tk.StringVar(value="Encrypt")
# # tk.Radiobutton(window, text="Encrypt", variable=mode, value="Encrypt", bg="#1e1e1e", fg="white", selectcolor="#2d2d2d").pack()
# # tk.Radiobutton(window, text="Decrypt", variable=mode, value="Decrypt", bg="#1e1e1e", fg="white", selectcolor="#2d2d2d").pack()

# # tk.Button(window, text="Submit", command=perform_cipher, bg="#444", fg="white", font=("Arial", 12)).pack(pady=10)

# # tk.Label(window, text="Result:", **label_style).pack(pady=5)
# # result_output = tk.Text(window, height=6, width=50, **entry_style, wrap="word")
# # result_output.pack(pady=5)

# # # Run the app
# # window.mainloop()

# import tkinter as tk
# from tkinter import messagebox, filedialog

# # Caesar Cipher Functions
# def encrypt(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             base = ord('A') if char.isupper() else ord('a')
#             result += chr((ord(char) - base + shift) % 26 + base)
#         else:
#             result += char
#     return result

# def decrypt(text, shift):
#     return encrypt(text, -shift)

# # Apply cipher and show result
# def apply_cipher(event=None):
#     message = text_input.get("1.0", tk.END).strip()
#     shift_val = shift_entry.get()

#     if not shift_val.isdigit():
#         result_output.delete("1.0", tk.END)
#         result_output.insert(tk.END, "[Error] Shift must be a number.")
#         return

#     shift = int(shift_val)
#     action = mode.get()

#     if action == "Encrypt":
#         result = encrypt(message, shift)
#     else:
#         result = decrypt(message, shift)

#     result_output.delete("1.0", tk.END)
#     result_output.insert(tk.END, result)
#     window.clipboard_clear()
#     window.clipboard_append(result)

# # Import text from file
# def import_text():
#     file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#     if file_path:
#         with open(file_path, "r", encoding="utf-8") as file:
#             content = file.read()
#             text_input.delete("1.0", tk.END)
#             text_input.insert(tk.END, content)
#         apply_cipher()

# # Export result to text file
# def export_result():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt",
#                                              filetypes=[("Text Files", "*.txt")])
#     if file_path:
#         result = result_output.get("1.0", tk.END).strip()
#         with open(file_path, "w", encoding="utf-8") as file:
#             file.write(result)
#         messagebox.showinfo("Saved", "Result saved to file.")

# # Toggle light/dark mode
# def toggle_theme():
#     global dark_mode
#     dark_mode = not dark_mode
#     colors = dark_theme if dark_mode else light_theme

#     window.config(bg=colors["bg"])

#     # Text and Entry widgets that support insertbackground
#     for widget in [text_input, result_output, shift_entry]:
#         widget.config(
#             bg=colors.get("bg", "white"),
#             fg=colors.get("fg", "black"),
#             insertbackground=colors.get("fg", "black")
#         )

#     # Other widgets (Radiobuttons, Labels)
#     for widget in [encrypt_radio, decrypt_radio]:
#         widget.config(
#             bg=colors.get("bg", "white"),
#             fg=colors.get("fg", "black"),
#             selectcolor=colors.get("select", "white")
#         )

#     submit_button.config(
#         bg=colors.get("button", "gray"),
#         fg=colors.get("fg", "black")
#     )

# # Initialize window
# window = tk.Tk()
# window.title("Caesar Cipher GUI")
# window.geometry("550x600")

# # Themes
# dark_theme = {"bg": "#1e1e1e", "fg": "white", "button": "#444", "select": "#2d2d2d"}
# light_theme = {"bg": "#f5f5f5", "fg": "black", "button": "#ddd", "select": "#fff"}
# dark_mode = True  # Default

# # Input widgets
# label_style = {"font": ("Arial", 12)}
# entry_style = {"font": ("Arial", 12), "width": 50, "height": 6, "wrap": "word"}

# tk.Label(window, text="Enter your message:", **label_style).pack(pady=5)
# text_input = tk.Text(window, **entry_style)
# text_input.pack()
# text_input.bind("<KeyRelease>", apply_cipher)

# tk.Label(window, text="Shift value:", **label_style).pack(pady=5)
# shift_entry = tk.Entry(window, width=10, font=("Arial", 12))
# shift_entry.pack()
# shift_entry.bind("<KeyRelease>", apply_cipher)

# mode = tk.StringVar(value="Encrypt")
# encrypt_radio = tk.Radiobutton(window, text="Encrypt", variable=mode, value="Encrypt", command=apply_cipher)
# decrypt_radio = tk.Radiobutton(window, text="Decrypt", variable=mode, value="Decrypt", command=apply_cipher)
# encrypt_radio.pack()
# decrypt_radio.pack()

# submit_button = tk.Button(window, text="Apply Cipher", command=apply_cipher)
# submit_button.pack(pady=10)

# tk.Label(window, text="Result:", **label_style).pack(pady=5)
# result_output = tk.Text(window, **entry_style)
# result_output.pack()

# # Import/Export & Theme Buttons
# tk.Button(window, text="📂 Import from File", command=import_text).pack(pady=5)
# tk.Button(window, text="💾 Export Result", command=export_result).pack(pady=5)
# tk.Button(window, text="🌓 Toggle Theme", command=toggle_theme).pack(pady=5)

# # Group all widgets for theme switching
# all_widgets = [
#     text_input, result_output, shift_entry,
#     encrypt_radio, decrypt_radio,
# ]

# # Apply initial theme
# toggle_theme()

# # Run the app
# window.mainloop()

import tkinter as tk
from tkinter import messagebox, filedialog

# Caesar Cipher Functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Apply cipher and show result
def apply_cipher(event=None):
    message = text_input.get("1.0", tk.END).strip()
    shift_val = shift_entry.get()

    if not shift_val.isdigit():
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, "[Error] Shift must be a number.")
        return

    shift = int(shift_val)
    action = mode.get()

    if action == "Encrypt":
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, result)
    window.clipboard_clear()
    window.clipboard_append(result)

# Import text from file
def import_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, content)
        apply_cipher()

# Export result to file
def export_result():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        result = result_output.get("1.0", tk.END).strip()
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(result)
        messagebox.showinfo("Saved", "Result saved to file.")

# Toggle light/dark theme
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    colors = dark_theme if dark_mode else light_theme

    window.config(bg=colors["bg"])
    welcome_label.config(bg=colors["bg"], fg=colors["fg"])
    for widget in [text_input, result_output, shift_entry]:
        widget.config(bg=colors["bg"], fg=colors["fg"], insertbackground=colors["fg"])
    for widget in [encrypt_radio, decrypt_radio]:
        widget.config(bg=colors["bg"], fg=colors["fg"], selectcolor=colors["select"])
    submit_button.config(bg=colors["button"], fg=colors["fg"])

# Show About
def show_about():
    messagebox.showinfo("About", "Caesar Cipher GUI\nBuilt with ❤️ using Python Tkinter")

# Clear all inputs and outputs
def reset_app():
    text_input.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    result_output.delete("1.0", tk.END)

# Setup window
window = tk.Tk()
window.title("🔐 Caesar Cipher GUI")
window.geometry("600x650")
window.resizable(False, False)

# Themes
dark_theme = {"bg": "#1e1e1e", "fg": "white", "button": "#444", "select": "#2d2d2d"}
light_theme = {"bg": "#f0f0f0", "fg": "#111", "button": "#ddd", "select": "#fff"}
dark_mode = True

# Welcome message
welcome_label = tk.Label(window, text="🔑 Favour's Cipher Tool. Dare to Decrypt!", font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=10)

# Message input
tk.Label(window, text="Enter your message:", font=("Arial", 12)).pack()
text_input = tk.Text(window, height=6, width=60, font=("Arial", 12), wrap="word")
text_input.pack(pady=5)
text_input.bind("<KeyRelease>", apply_cipher)

# Shift value
tk.Label(window, text="Enter shift value:", font=("Arial", 12)).pack()
shift_entry = tk.Entry(window, font=("Arial", 12), width=10)
shift_entry.pack()
shift_entry.bind("<KeyRelease>", apply_cipher)

# Mode selection
mode = tk.StringVar(value="Encrypt")
encrypt_radio = tk.Radiobutton(window, text="Encrypt", variable=mode, value="Encrypt", font=("Arial", 11), command=apply_cipher)
decrypt_radio = tk.Radiobutton(window, text="Decrypt", variable=mode, value="Decrypt", font=("Arial", 11), command=apply_cipher)
encrypt_radio.pack()
decrypt_radio.pack()

# Submit button
submit_button = tk.Button(window, text="Apply Cipher", font=("Arial", 12, "bold"), command=apply_cipher)
submit_button.pack(pady=10)

# Result output
tk.Label(window, text="Result:", font=("Arial", 12)).pack()
result_output = tk.Text(window, height=6, width=60, font=("Arial", 12), wrap="word")
result_output.pack(pady=5)

# Action buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
tk.Button(button_frame, text="📂 Import", font=("Arial", 11), command=import_text).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="💾 Export", font=("Arial", 11), command=export_result).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="🔁 Reset", font=("Arial", 11), command=reset_app).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="🌓 Theme", font=("Arial", 11), command=toggle_theme).grid(row=0, column=3, padx=5)

# Menu bar
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Import", command=import_text)
file_menu.add_command(label="Export", command=export_result)
file_menu.add_separator()
file_menu.add_command(label="Reset", command=reset_app)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

# Apply initial theme
toggle_theme()

# Start GUI loop
window.mainloop()