import json
from scholarly import scholarly

def extract_venues(json_file, venues = {}):
    """
    Extract all venues from the given JSON file.
    
    JSON structure:
    {
        "result": {
            "hits": {
                "hit": [
                    {
                        "info": {
                            "venue": "venue_name"
                        }
                    },
                    ...
                ]
            }
        }
    }
    Args:
        json_file (str): Path to the JSON file.

    Returns:
        list: A list of venues found in the JSON file.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

            # Navigate the JSON structure to extract venues
            hits = data.get("result", {}).get("hits", {}).get("hit", [])
            for hit in hits:
                venue = hit.get("info", {}).get("venue")
                if venue:
                    if venue not in venues:
                        venues[venue] = {"count": 0, "full_name": "", "rank": ""}
                    venues[venue]["count"] += 1
                    # venues.append(venue)
    except Exception as e:
        print(f"Error reading file {json_file}: {e}")

    return venues

def filter_venues(venues, min_count=4):
    filtered_venues = {}
    for venue in venues:
        if venues[venue]["count"] >= min_count:
            filtered_venues[venue] = venues[venue]
    return filtered_venues

def update_citation_count(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error reading file {json_file}: {e}")
        return

    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    for hit in hits:
        title = hit.get("info", {}).get("title")
        search_query = scholarly.search_pubs(title)
        paper = next(search_query, None)
        citation_count = 0
        if paper:
            citation_count = paper.get('num_citations', 0)
        else:
            print(f"Could not find paper with title '{title}'")
        hit["info"]["citation_count"] = citation_count
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # JSON file paths
    json_file1 = "dblp-89.json"
    json_file2 = "dblp-1000.json"

    # Update citation count for each paper in the JSON file
    update_citation_count(json_file1)
    update_citation_count(json_file2)

    # Extract venues from both files
    venues = extract_venues(json_file1)
    venues = extract_venues(json_file2, venues=venues)

   
    with open("venus.json", "w") as file:
        json.dump(venues, file, indent=4)

    print("Total number of venues:", len(venues))
    
    filtered_venues = filter_venues(venues)
    print("Total number of venues after filtering:", len(filtered_venues))
    
    with open("filtered_venues.json", "w") as file:
        json.dump(filtered_venues, file, indent=4)
  
if __name__ == "__main__":
    main()


