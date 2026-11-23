"""Scrape job listings from the Fake Python Jobs site and save them to CSV."""

import csv

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"
FIELDS = ["title", "company", "location", "url"]


def fetch_page(url):
    """Download the page and return its HTML, or None if the request fails."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises an error for 404, 500, etc.
        return response.text
    except requests.RequestException as error:
        print(f"Could not fetch {url}: {error}")
        return None


def get_text(element):
    """Return clean text from a tag, or an empty string if the tag is missing."""
    return element.get_text(strip=True) if element else ""


def get_apply_link(card):
    """Return the 'Apply' link of a job card, or an empty string if absent."""
    for link in card.find_all("a", href=True):
        if link.get_text(strip=True).lower() == "apply":
            return link["href"]
    return ""


def parse_jobs(html):
    """Extract job data from the page HTML into a list of dictionaries."""
    soup = BeautifulSoup(html, "html.parser")
    container = soup.find(id="ResultsContainer")
    if container is None:
        print("Results container not found - the page layout may have changed.")
        return []

    jobs = []
    for card in container.find_all("div", class_="card-content"):
        jobs.append(
            {
                "title": get_text(card.find("h2", class_="title")),
                "company": get_text(card.find("h3", class_="company")),
                "location": get_text(card.find("p", class_="location")),
                "url": get_apply_link(card),
            }
        )
    return jobs


def save_to_csv(jobs, filename):
    """Write the list of job dictionaries to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(jobs)


def main():
    html = fetch_page(URL)
    if html is None:
        return

    jobs = parse_jobs(html)
    if not jobs:
        print("No jobs found.")
        return

    save_to_csv(jobs, OUTPUT_FILE)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
