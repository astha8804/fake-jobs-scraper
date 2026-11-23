# Fake Python Jobs Scraper

Project URL:https://roadmap.sh/projects/job-listings-scraper

A Python web scraper that collects job listings from
https://realpython.github.io/fake-jobs/ and saves them to a CSV file.

## Features
- Extracts job title, company name, location, and job detail URL
- Saves all results to `jobs.csv`
- Handles missing fields and network errors

## Requirements
- Python 3.8+
- requests
- beautifulsoup4

## Setup
```
pip install requests beautifulsoup4
```

## Usage
```
python job_scraper.py
```

The results are saved to `jobs.csv` with these columns:
`title`, `company`, `location`, `url`

## Technologies Used
- Python
- Requests
- Beautiful Soup (bs4)
- CSV module
