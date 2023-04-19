# SINTA-Scraper
 
## Overview
The program aimed to extract university data and publication scores from the SINTA website using Scrapy. The targeted website is static, and the data is not loaded using JavaScript, which makes Scrapy an appropriate choice due to its efficiency and speed in handling static data on websites. The extracted data included relevant data such as the university's name, location, and publication scores. The data was saved in CSV format for further processing and analysis.

URL: https://sinta.kemdikbud.go.id/affiliations

Website:
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/74947224/211182068-56532403-52bc-42df-94d8-30115e7b37ef.png">

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


