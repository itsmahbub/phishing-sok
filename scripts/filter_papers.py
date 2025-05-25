import json

year_citation_map = {
    "2025": 0,
    "2024": 1,
    "2023": 5,
    "2022": 15,
    "2021": 25,
    "2020": 35
}
count = 45
for year in range(2019, 2000, -1):
    year_citation_map[str(year)] = count
    count += 15

def filter_papers(papers):
    with open("filtered_venues.json", 'r') as file:
        venues = json.load(file)
        venues = list(venues.keys())
    filtered_papers = []
    for paper in papers:
        # if "doi" in paper["info"]:
        #     continue
        # if paper["info"]["type"] in ["Books and Theses", "Informal and Other Publications"]:
        #     continue
        # title_lower = paper["info"]["title"].lower()
        # if "email" in title_lower or "e-mail" in title_lower:
        #     continue
        # if "citation_count" in paper["info"]:
        #     continue
        # if paper["info"]["venue"] not in venues:
        #     continue
        # filtered_papers.append(paper)
        
        # year = int(paper["info"]["year"])
        # citation_count = paper["info"]["citation_count"]
        # if citation_count >= year_citation_map.get(str(year), 0):
        #     filtered_papers.append(paper)
        
        if paper["info"].get("citation_count", 0) >= 100:
            filtered_papers.append(paper)

    return filtered_papers

def main():
    json_file = "dblp-phishing-no-duplicates.json"
    with open(json_file, 'r') as file:
        papers = json.load(file)
    
    filtered_papers = filter_papers(papers)
    with open("dblp-phishing-cite-100.json", "w") as file:
        json.dump(filtered_papers, file, indent=4)
  
if __name__ == "__main__":
    main()

