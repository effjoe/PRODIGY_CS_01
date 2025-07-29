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