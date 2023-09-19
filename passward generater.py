import tkinter as tk
import random
import string

# Function to generate a random password based on length
def generate_password():
    password_length = int(length_entry.get())
    
    if password_length < 4:
        password_result.config(text="Password length must be at least 4 characters.")
        generated_password_entry.delete(0, tk.END)
    else:
        if password_length < 8:
            characters = string.ascii_lowercase + string.digits
        elif password_length < 12:
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        else:
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_result.config(text="Generated Password:")
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, password)

# Function to clear all text fields
def reset_password():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)
    #password_result.config(text="")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Styling for the "Password Generator" label
generator_label = tk.Label(root, text="Password Generator", font=("Helvetica", 25, "underline"), fg="#00008B")
generator_label.grid(row=0, column=0, columnspan=2, pady=30)

# Label and Entry for username
username_label = tk.Label(root, text="Enter Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1,pady=20)

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=2, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1, pady=20)

# Generate Password button with styling
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#00008B", fg="white", borderwidth=2, relief="solid")
generate_button.grid(row=3, column=0, columnspan=2)

# Label to display the generated password
password_result = tk.Label(root, text="Generated Password:")
password_result.grid(row=4, column=0)

# Text Entry for displaying the generated password
generated_password_entry = tk.Entry(root)
generated_password_entry.grid(row=4, column=1, pady=20)

# Accept and Reset buttons with styling
accept_button = tk.Button(root, text="Accept", state=tk.NORMAL, bg="white", fg="#00008B", borderwidth=2, relief="solid")  # You can implement this functionality as needed.
accept_button.grid(row=5, column=0, columnspan=2,pady=5)
reset_button = tk.Button(root, text="Reset", command=reset_password, bg="white", fg="#00008B",borderwidth=2, relief="solid")
reset_button.grid(row=6, column=0, columnspan=2,pady=5)

root.mainloop()