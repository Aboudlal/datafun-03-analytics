# DataFun-03-Analytics

## 📌 Description

This project demonstrates how to **fetch** and **process** different types of data with Python: CSV, Excel, JSON, and Text.
It uses a professional Python workflow with a virtual environment, GitHub, and organized scripts.

---

## 📥 Fetchers

Scripts to download files from the web and save them in the `data/` folder.

* **CSV Fetcher**

  * Downloads the World Happiness 2020 dataset.
  * **Command:**

    ```bash
    python abdellah_get_csv.py
    ```

* **Excel Fetcher**

  * Downloads an example Excel file.
  * **Command:**

    ```bash
    python abdellah_get_excel.py
    ```

* **JSON Fetcher**

  * Downloads an example JSON file.
  * **Command:**

    ```bash
    python abdellah_get_json.py
    ```

* **Text Fetcher**

  * Downloads a plain text file.
  * **Command:**

    ```bash
    python abdellah_get_text.py
    ```

---

## 📊 Processors

Scripts to read files from `data/`, analyze a simple metric, and save the results in the `processed/` folder.

* **CSV Processor**

  * Analyzes the *Ladder score* column (min, max, mean, stdev).
  * **Command:**

    ```bash
    python abdellah_process_csv.py
    ```

* **Excel Processor**

  * Analyzes numeric columns in the Excel file (mean, min, max).
  * **Command:**

    ```bash
    python abdellah_process_excel.py
    ```

* **JSON Processor**

  * Counts objects and extracts a simple statistic.
  * **Command:**

    ```bash
    python abdellah_process_json.py
    ```

* **Text Processor**

  * Counts the number of words and lines in the text file.
  * **Command:**

    ```bash
    python abdellah_process_text.py
    ```

---

## ⚙️ Installation and Execution

### 1. Clone the project

```bash
git clone https://github.com/Aboudlal/datafun-03-analytics.git
cd datafun-03-analytics
```

### 2. Create and activate a virtual environment

```bash
py -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
```

### 4. Run the scripts

Example:

```bash
python abdellah_get_csv.py
python abdellah_process_csv.py
```

---

