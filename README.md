# 📄 get-papers-list

Fetch research papers from PubMed using a query, filter those with at least one author affiliated with a pharmaceutical or biotech company, and export the results to a CSV file.

## 🧩 Project Structure

``` bash
get-papers-list/ 
├── get_papers_list/ 
│   ├── init.py 
│   ├── fetcher.py # Handles PubMed queries and article parsing 
│   ├── utils.py # Utilities for filtering and email extraction 
│   ├── writer.py # Handles writing the results to a CSV 
│   └── main.py # Entry point for the CLI application 
├── pyproject.toml # Poetry configuration 
├── poetry.lock # Lock file for deterministic installs 
└── README.md # You’re reading it!
```

## 🛠️ Setup Instructions

### 1. Prerequisites

- Python >= 3.11
- [Poetry](https://python-poetry.org/docs/#installation)

#### Install Poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
```bash
poetry --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/get-papers-list.git
cd get-papers-list
```
### 3. Install Project Dependencies
```bash
poetry install
```

### 4. Run the Program
```bash
poetry run get-papers-list "your pubmed query here" -f output.csv
```
#### Optional Flags
- `-h` or `--help` -> to get help
- `-d` or `--debug` -> debug logs
- `-f` or `--file` -> to input output file name (Mandatory)