import tkinter as tk
from tkinter import ttk, messagebox
from recommendation import RecommendationEngine

# Load recommendation engine
engine = RecommendationEngine("dataset.csv")


def recommend():
    name = name_entry.get().strip()
    interests = interest_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return

    if not interests:
        messagebox.showerror("Error", "Please enter your interests.")
        return

    results = engine.recommend(interests)

    # Update Progress Bar
    if len(results) > 0:
        progress["value"] = float(results.iloc[0]["Score"]) * 100
    else:
        progress["value"] = 0

    # Clear previous output
    output.delete("1.0", tk.END)

    # Display Welcome
    output.insert(tk.END, f"Welcome, {name}!\n")
    output.insert(tk.END, "=" * 55 + "\n\n")

    # Display Recommendations
    for index, row in results.iterrows():
        output.insert(tk.END, f"📚 Title      : {row['Title']}\n")
        output.insert(tk.END, f"📂 Category   : {row['Category']}\n")
        output.insert(tk.END, f"🎯 Match      : {row['Score']*100:.2f}%\n")
        output.insert(tk.END, "-" * 55 + "\n")


def clear():
    name_entry.delete(0, tk.END)
    interest_entry.delete(0, tk.END)
    output.delete("1.0", tk.END)
    progress["value"] = 0


def save():
    with open("history.txt", "w", encoding="utf-8") as file:
        file.write(output.get("1.0", tk.END))

    messagebox.showinfo("Success", "Recommendations saved in history.txt")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Smart AI Recommendation System")
root.geometry("850x700")
root.configure(bg="#dbeafe")

title = tk.Label(
    root,
    text="🤖 Smart AI Recommendation System",
    font=("Arial", 24, "bold"),
    bg="#dbeafe",
    fg="#0f172a"
)
title.pack(pady=15)

tk.Label(
    root,
    text="Enter Your Name",
    font=("Arial", 12, "bold"),
    bg="#dbeafe"
).pack()

name_entry = ttk.Entry(root, width=60)
name_entry.pack(pady=5)

tk.Label(
    root,
    text="Enter Your Interests",
    font=("Arial", 12, "bold"),
    bg="#dbeafe"
).pack()

interest_entry = ttk.Entry(root, width=60)
interest_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#dbeafe")
button_frame.pack(pady=10)

ttk.Button(
    button_frame,
    text="Get Recommendations",
    command=recommend
).grid(row=0, column=0, padx=5)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear
).grid(row=0, column=1, padx=5)

ttk.Button(
    button_frame,
    text="Save Results",
    command=save
).grid(row=0, column=2, padx=5)

# Progress Bar
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=500,
    mode="determinate"
)
progress.pack(pady=10)

# Output Box
output = tk.Text(
    root,
    width=95,
    height=22,
    font=("Consolas", 11)
)
output.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Developed by Nahah Butt | BS Artificial Intelligence",
    bg="#dbeafe",
    fg="gray",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=5)

root.mainloop()