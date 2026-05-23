import os
import glob
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# --- LOGIC FUNCTION ---
def process_and_merge_files():
    # 1. Multiple Files Select karne ka option (Challenge 1 Solved)
    files_selected = filedialog.askopenfilenames(
        title="Select AG2 Excel Files",
        filetypes=[("Excel Files", "AG2*.xlsx"), ("All Excel Files", "*.xlsx")]
    )
    
    if not files_selected:
        return  # Agar user cancel kar de

    # Files ko alphabetically sort karna (aapke original logic ke mutabik)
    all_files = sorted(list(files_selected))
    
    # Configuration
    sheets_to_merge = ['SOC', 'HT', 'DG in Manual', 'Node Isolation']
    
    # 2. Save location poochna (Challenge 2 Solved: Proper Download/Save Button workflow)
    output_file = filedialog.asksaveasfilename(
        title="Save Merged File As",
        defaultextension=".xlsx",
        initialfile="Final_Merged_All2.xlsx",
        filetypes=[("Excel Files", "*.xlsx")]
    )
    
    if not output_file:
        return  # Agar user save location select na kare

    # Processing Start (UI state change)
    status_label.config(text="Processing... Please wait.", fg="#ffcc00")
    root.update()

    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for sheet in sheets_to_merge:
                data_frames = []
                for f in all_files:
                    try:
                        xl = pd.ExcelFile(f)
                        if sheet in xl.sheet_names:
                            data_frames.append(pd.read_excel(f, sheet_name=sheet))
                    except Exception:
                        continue
                
                if data_frames:
                    pd.concat(data_frames, ignore_index=True).to_excel(writer, sheet_name=sheet, index=False)
        
        status_label.config(text="Successful !", fg="#00ff00")
        messagebox.showinfo("Success", f"File successfully merged and saved at:\n{output_file}")
        
    except Exception as e:
        status_label.config(text="Error Occurred", fg="#ff3333")
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# --- FRONTEND UI DESIGN (Matching your Image) ---
root = tk.Tk()
root.title("ILA OADM Report")
root.geometry("600x420")  # Window Size
root.configure(bg="#212121")  # Dark Theme Background color matching your pic

# Window icon customization (Optional)
# root.iconbitmap('your_icon.ico')

# Top Heading Label
heading_label = tk.Label(
    root, 
    text="Upload SOC, DG & HT Dumps", 
    font=("Arial", 22, "bold"), 
    bg="#212121", 
    fg="#ffffff"  # White text
)
heading_label.pack(pady=(60, 40))

# Custom Styled "Upload & Create" Button (Matching the blue button in your pic)
style = ttk.Style()
style.theme_use('default')

upload_btn = tk.Button(
    root,
    text="Upload & Create",
    font=("Arial", 14, "bold"),
    bg="#1f6aa5",  # Blue color from your sample image
    fg="white",
    activebackground="#144871",
    activeforeground="white",
    bd=0,
    padx=30,
    pady=10,
    cursor="hand2",
    command=process_and_merge_files
)
upload_btn.pack(pady=20)

# Status Label (To show "Processing" or "Successful !")
status_label = tk.Label(
    root, 
    text="", 
    font=("Arial", 12, "bold"), 
    bg="#212121", 
    fg="#ffffff"
)
status_label.pack(pady=20)

# App Loop Start
root.mainloop()
