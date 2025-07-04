# 🗂️ File System Analyzer

A modular and efficient Python tool to analyze, search, and export details about file system contents. Built for developers, students, and system admins who want a better understanding of their directory structure and file usage.

---

## 🚀 Features

- 📁 Recursively scans directories
- 📊 Calculates file system statistics
- 🔍 Supports file searching by name or extension
- 📤 Exports data in JSON format
- 🧱 Modular code structure for easy maintenance

---

## 📁 Project Structure

```
file_system_analyzer/
├── main.py              # Entry point for CLI usage
├── _main.py             # Alternative or test entry
└── analyzer/
    ├── traversal.py     # Handles directory traversal
    ├── statistics.py    # Gathers file system stats
    ├── search.py        # Provides search capabilities
    ├── json_export.py   # Handles exporting results
    ├── utils.py         # Utility functions
```

---

## 🛠️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/Ay-developerweb/file-system-analyzer.git
cd file-system-analyzer
```

2. **(Optional) Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
> If no `requirements.txt` exists, the project likely uses only standard libraries.

---

## ▶️ Usage

### Run the analyzer:

```bash
python main.py [target_directory]
```

If no directory is passed, it defaults to the current working directory.

---

## 📤 JSON Export

The tool supports exporting results to a `.json` file:
```bash
python main.py /path/to/dir --export report.json
```

---

## 🤝 Contribution

Feel free to fork this repo and submit pull requests. Ideas and improvements are always welcome!

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Adediran Ayomide Mathew**  
📧 ayomideadediran45@gmail.com 
🌐 [GitHub Profile](https://github.com/Ay-developerweb)
