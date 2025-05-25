import json
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict


if __name__ == "__main__":

    with open("dblp-phishing-final-3.json", 'r') as file:
        papers = json.load(file)

    # Count papers by venue
    venue_counter = Counter(paper['info']['venue'] for paper in papers)
    sorted_venues = OrderedDict(sorted(venue_counter.items()))

    # Plot number of papers by venue
    plt.figure(figsize=(10, 5))
    plt.bar(sorted_venues.keys(), sorted_venues.values())
    plt.xlabel('Venue')
    plt.ylabel('Number of Papers')
    plt.title('Number of Papers by Venue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("papers_by_venue.png")

    # Count papers by year
    year_counter = Counter(paper['info']['year'] for paper in papers)
    sorted_year = OrderedDict(sorted(year_counter.items()))
    
    # Plot number of papers by year
    plt.figure(figsize=(10, 5))
    plt.bar(sorted_year.keys(), sorted_year.values())
    plt.xlabel('Year')
    plt.ylabel('Number of Papers')
    plt.title('Number of Papers by Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("papers_by_year.png")
    
    with open("venue_counter.json", "w") as file:
        json.dump(sorted_venues, file, indent=4)
    
    with open("year_counter.json", "w") as file:
        json.dump(sorted_year, file, indent=4)
    