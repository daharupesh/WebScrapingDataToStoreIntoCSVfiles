
# Data Gethering By Web Scrapping

This repository contains a Python-based web scraper that extracts company data (company name, description, rating, and reviews) from [AmbitionBox](https://www.ambitionbox.com) and saves the results into a CSV file. The scraper utilizes `requests` for fetching the web page and `BeautifulSoup` for parsing the HTML content. The extracted data is then processed and stored in a structured format using `pandas`.

## Features

- Extracts company name, description, rating, and the number of reviews.
- Saves the data into a CSV file for easy analysis.
- Easily extendable for additional fields or data sources.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)

## Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/company-data-scraper.git
    cd company-data-scraper
    ```

2. **Install the required dependencies**:
    You can install the necessary libraries using the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

    If you prefer to install them manually, the script requires the following packages:
    ```bash
    pip install requests
    pip install beautifulsoup4
    pip install pandas
    ```

## Usage

1. **Run the scraper**:
    The script can be run directly using Python. It will scrape data from the first page of companies listed on AmbitionBox and save it as a CSV file.

    ```bash
    python company_scraper.py
    ```

2. **Output**:
    Once the script finishes executing, it will create a `company_data.csv` file in the current directory. This file will contain the scraped data in the following format:

    | Company Name   | Description                          | Rating | Reviews |
    |----------------|--------------------------------------|--------|---------|
    | Company A      | Description of Company A             | 4.5    | 200     |
    | Company B      | Description of Company B             | 3.9    | 150     |

## How It Works

1. **Sending the Request**: The script sends an HTTP request to the AmbitionBox website and retrieves the HTML content of the first page of companies.

2. **Parsing the HTML**: Using `BeautifulSoup`, the HTML content is parsed, and the relevant data (company name, description, rating, and reviews) is extracted by targeting specific HTML elements.

3. **Storing the Data**: The extracted data is stored in Python lists, which are then converted into a `pandas` DataFrame.

4. **Saving the CSV**: The DataFrame is saved into a CSV file (`company_data.csv`) for further analysis or reporting.

## Extending the Script

If you wish to extract additional fields or modify the script for different pages:

- Update the `find()` or `find_all()` methods inside the loop where data is being extracted. These methods use CSS classes to identify the desired elements.
- Modify the `webpage` URL to scrape additional pages (for example, changing `page=1` to `page=2`).


## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements. Contributions are always welcome!

## Contact

For any inquiries or suggestions, feel free to contact me at daharupesh21@gmail.com.
