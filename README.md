# Power BI Dashboard for Olympic Data

## Overview

This repository contains a Power BI dashboard visualizing Olympic data. The dashboard includes the following key features:

- **NOC vs. Total Medals**: A stacked bar chart showing the distribution of gold, silver, and bronze medals won by each National Olympic Committee (NOC).
- **Geographical Map**: A map visualization showing the locations of NOCs or medal-winning countries (if applicable).

## Data Source

The data used in this dashboard was scraped from Wikipedia using Python and BeautifulSoup. The script extracts medal counts and NOC information, which is then used to populate the Power BI dashboard.

### Data Scraping

1. **Python Script**:
   - The data was scraped from Wikipedia using BeautifulSoup, a Python library for parsing HTML and XML documents.
   - The script collects data on medal counts and NOCs, and formats it for use in Power BI.

2. **Script Details**:
   - **File Name**: `scrape_data.py`
   - **Libraries Used**: `BeautifulSoup`, `requests`, `pandas`
   - **Data Extracted**: Medal counts (gold, silver, bronze) and NOC details

## Getting Started

To use or modify this Power BI dashboard, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
