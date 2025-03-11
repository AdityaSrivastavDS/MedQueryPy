# 📚 PubMed Fetcher

🚀 A Python tool to fetch research papers from PubMed and filter those with non-academic authors affiliated with pharmaceutical or biotech companies.

---

## 📌 Features
✅ Fetches research papers using the **PubMed API**
✅ Identifies papers with **non-academic authors** from biotech/pharma companies
✅ Saves results in **CSV format**
✅ **Command-line interface** for ease of use
✅ **Poetry-based** dependency management
✅ Modular design with **separate CLI and core module**

---

## 🛠 Installation

### 1️⃣ Install Poetry (if not already installed)
```bash
pip install poetry
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/AdityaSrivastavDS/pubmed_fetcher
cd pubmed_fetcher
```

### 3️⃣ Install Dependencies
```bash
poetry install
```

---

## 🚀 Usage

### 🔍 Fetch Papers by Query
```bash
poetry run python cli.py "COVID-19 vaccines"
```

### 📂 Save Results to a CSV File
```bash
poetry run python cli.py "COVID-19 vaccines" -f results.csv
```

### 🛠 Debug Mode
```bash
poetry run python cli.py "COVID-19 vaccines" -d
```

---

## 🏗 Project Structure
```
pubmed_fetcher/
│── pubmed_fetcher/        # Package directory
│   │── __init__.py        # Makes the folder a Python package
│   │── fetcher.py         # Module for fetching PubMed papers
│── cli.py                 # Command-line interface script
│── README.md              # Documentation
│── pyproject.toml         # Poetry configuration
│── poetry.lock            # Poetry lock file
│── .gitignore             # Git ignore file
```

---

## 🤖 Technology Stack
- **Python** 🐍
- **Requests** (for API calls) 🌐
- **CSV** (for saving results) 📊
- **Poetry** (for package management) 📦

---

## ⚡ How It Works
1. The CLI takes a **search query** as input.
2. Fetches **PubMed papers** matching the query.
3. Extracts papers **with non-academic authors**.
4. Outputs results to **console or CSV**.

---

## 🌟 Contributing
🎯 Contributions are welcome! Feel free to fork the repo and submit a PR.

---

## 📄 License
📝 MIT License. See [LICENSE](LICENSE) for details.

---

## ✨ Author
👨‍💻 **Aditya Srivastav**  

