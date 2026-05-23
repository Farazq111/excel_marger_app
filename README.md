# ILA OADM Report - Excel Sheet Merger 📂

A sleek, dark-themed Windows Desktop Application built with Python and Tkinter to automate the process of merging specific sheets (`SOC`, `HT`, `DG in Manual`, `Node Isolation`) from multiple `AG2*.xlsx` Excel files into a single consolidated file.

## ✨ Features
* **User-Friendly UI:** Modern dark theme interface matching professional tools.
* **Bulk Upload:** Select multiple `AG2` Excel files at once using a native file explorer.
* **Smart Sorting:** Files are automatically sorted alphabetically before merging to maintain data order.
* **Custom Download Location:** Choose exactly where and under what name you want to save the merged output file.
* **Standalone Execution:** Can be compiled into a single `.exe` file that runs on any Windows PC without installing Python.

---

## 🛠️ Requirements & Installation

If you want to run the source code directly, make sure you have Python installed, then install the required dependencies:

```bash
pip install pandas openpyxl
