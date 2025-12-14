# 🤖 Python Business Automation Suite

### 🚀 Executive Summary
**Goal:** Eliminate manual administrative bottlenecks by automating common data and file management tasks.
**Result:** Developed a toolkit of Python scripts that handle **data cleaning**, **report formatting**, and **file organization**. These tools reduce hours of manual work into seconds of execution time, ensuring consistency and accuracy in business workflows.

---

### 🛠️ Tools Included

#### 1. `csv_cleaner.py` (Data Quality Pipeline)
* **Problem:** Raw sales data often comes with missing values, whitespace, and incorrect types (e.g., currency strings like "$1,200").
* **Solution:** A script that ingests raw CSVs, strips whitespace, converts data types, calculates total price (`quantity * unit_price`), and handles errors gracefully.
* **Business Value:** Prepares dirty data for immediate analysis in SQL or BI tools.

#### 2. `excel_formatter.py` (Report Automation)
* **Problem:** Weekly inventory reports require manual highlighting of low-stock items.
* **Solution:** Uses the `openpyxl` library to scan Excel files and automatically apply **bold** or color formatting to cells where inventory < 10.
* **Business Value:** Automates visual reporting standards, allowing managers to spot critical shortages instantly.

#### 3. `renamer.py` (File System Organization)
* **Problem:** Managing hundreds of files with inconsistent naming conventions leads to data retrieval errors.
* **Solution:** An OS-level script that iterates through directories and standardizes filenames (e.g., `Report_1.txt`, `Report_2.txt`) in milliseconds.
* **Business Value:** Ensures organized digital archives and effortless file retrieval.

---

### 💻 Technical Skills Demonstrated
* **File I/O:** robust reading/writing of `.csv` and `.txt` files using Python's standard library.
* **Excel Automation:** programmatic manipulation of spreadsheets using `openpyxl`.
* **OS Interaction:** direct file system management using the `os` module.
* **Error Handling:** implemented `try-except` blocks to prevent crashes during batch processing.

---

### ⚙️ How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/python-business-automation.git](https://github.com/YOUR_USERNAME/python-business-automation.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install openpyxl
    ```
3.  **Run a tool (example):**
    ```bash
    python csv_cleaner.py
    ```
