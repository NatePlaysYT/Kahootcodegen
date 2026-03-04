import random
import string
import tkinter as tk

def generate_code():

    rc_list = [random.choice(string.ascii_uppercase + string.digits) for _ in range(6)]
    new_code = "".join(rc_list)

    result_label.config(text="Room Code: " + new_code)
    print("Generated: " + new_code) # Still prints to terminal too

root = tk.Tk()
root.title("Kahoot Number Generator")
root.geometry("400x300")

# Top text
result_label = tk.Label(root, text="Click to generate", font=("Arial", 24))
result_label.pack(pady=50)

# Button
btn = tk.Button(root, text="Generate Code", command=generate_code, font=("Arial", 14))
btn.pack(pady=20)

root.mainloop()
