# SINTA-Scraper
 
## Overview
A program to retrieve university data and publication scores on the SINTA website using Scrapy. The website to be scraped is a static website, data is not loaded using javascript. 
Therefore, Scrapy is a suitable choice because it has speed and efficiency for static data on websites.

URL: https://sinta.kemdikbud.go.id/affiliations

Website:


## Official Docs
Scrapy Documentation
https://scrapy.org/

## Installation
```
pip install scrapy
pip3 install scrapy
```

## Run Program
    scrapy runspider scraper.py
    
## Export Data
### csv
    scrapy runspider scraper.py -o data.csv

### json
    scrapy runspider scraper.py -o data.json


