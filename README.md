# Data Scraping and SQL Ingestion Project

This project demonstrates a full pipeline of data scraping from a web source and ingesting it into a SQL database. The code is structured to scrape notebook listings from Mercado Livre and store the relevant information in a local SQL Server database.

## Features

- **Web Scraping**: The project utilizes the `BeautifulSoup` library to extract product details like name, specifications, and price from a web page.
- **Regex for Data Parsing**: Regular expressions (`re`) are used to accurately extract the brand and specs from product titles.
- **SQL Database Insertion**: The scraped data is stored in a local SQL Server database using the `pyodbc` library for connection and query execution.
- **Error Handling**: Ensures that the script runs smoothly, with checks for failed HTTP requests.

## File Structure

- **`datascrapping.py`**: Responsible for scraping the notebook data from the web. It parses the HTML of the target page, extracts relevant details using CSS selectors, and stores them in a list of dictionaries.
- **`sqlconnect.py`**: Establishes a connection to a local SQL Server database and inserts the scraped data into a predefined table (`infonote`). It ensures that duplicate IDs are avoided by checking the current maximum ID in the table.

## How It Works

### Step 1: Web Scraping (`datascrapping.py`)

The script `datascrapping.py` fetches the web page from Mercado Livre and uses `BeautifulSoup` to parse the HTML content. The key product details—name, specifications, price, and store—are extracted and organized into a list of dictionaries.

#### Example of scraped data:

```json
{
    "name": "Notebook Dell Inspiron 15",
    "specs": "Core i5 8GB RAM 512GB SSD",
    "price": "3500.00",
    "store": "Mercado Livre"
}
```

### Step 2: SQL Insertion (`sqlconnect.py`)

The `sqlconnect.py` script connects to a local SQL Server instance using `pyodbc`. It retrieves the current maximum ID from the `infonote` table to prevent duplicate entries and then inserts each notebook's information into the database.

#### SQL Table Structure:

```sql
CREATE TABLE infonote (
    id INT PRIMARY KEY,
    name NVARCHAR(255),
    specs NVARCHAR(255),
    price FLOAT,
    store NVARCHAR(100)
);
```

## Requirements

- Python 3.x
- `beautifulsoup4`
- `requests`
- `pyodbc`
- Local SQL Server instance

You can install the required Python packages via:

```bash
pip install beautifulsoup4 requests pyodbc
```

## Running the Code

1. Ensure that your local SQL Server is running and accessible.
2. Run the scraping script:

```bash
python datascrapping.py
```

3. Insert the scraped data into the SQL Server database:

```bash
python sqlconnect.py
```

## Customization

- The URL for scraping can be customized in `datascrapping.py`.
- The database connection details (server name, database) can be configured in `sqlconnect.py`.
