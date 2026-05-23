# ALL Report - Excel Sheet Merger 📂

A sleek, dark-themed Windows Desktop Application built with Python and Tkinter to automate the process of merging specific sheets (`Sheet1`, `Sheet2`, `Sheet3`, `Sheet4`) from multiple `*.xlsx` Excel files into a single consolidated file.

## ✨ Features
* **User-Friendly UI:** Modern dark theme interface matching professional tools.
* **Bulk Upload:** Select multiple `.xlsx` Excel files at once using a native file explorer.
* **Smart Sorting:** Files are automatically sorted alphabetically before merging to maintain data order.
* **Custom Download Location:** Choose exactly where and under what name you want to save the merged output file.
* **Standalone Execution:** Can be compiled into a single `.exe` file that runs on any Windows PC without installing Python.

---

## 🛠️ Requirements & Installation

If you want to run the source code directly, make sure you have Python installed, then install the required dependencies:

```bash
pip install pandas openpyxl
```


🚀 How to Run the App

Clone or download this repository.
Open your terminal/command prompt in the project folder.
Run the following command:

```Bash

    python app_gui.py
```


📦 How to Convert into a Windows Installer (.exe)

To share this app with someone who doesn't have Python installed, you can pack it into a single .exe file using PyInstaller.

1. Install PyInstaller:
```
pip install pyinstaller
pyinstaller --noconsole --onefile app_gui.py
```
2. Once completed, find your standalone app inside the dist/ folder named app_gui.exe.

📖 How to Use

Launch the application.

 Click on the "Upload & Create" button.

 Hold Ctrl and select all the AG2*.xlsx files you want to merge.

 A save dialog will pop up. Choose your desired folder and click Save.

 Wait for the "Successful !" status, and you are done!
    
