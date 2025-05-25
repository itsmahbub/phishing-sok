import json

def extract_venues(json_file, venues = {}):
    try:
        with open(json_file, 'r') as file:
            papers = json.load(file)
            for paper in papers:
                venue = paper.get("info", {}).get("venue")
                type = paper.get("info", {}).get("type")
                if venue not in venues:
                    venues[venue] = {"count": 0, "full_name": "", "rank": ""}
                venues[venue]["count"] += 1
                venues[venue]["type"] = type
                # else:
                #     print(venue_list)
                #     print(f"Venue not found for paper: {paper['@id']}")
                    # venues.append(venue)
    except Exception as e:
        print(f"Error reading file {json_file}: {e}")

    return venues

# def filter_venues(venues, min_count=4):
#     filtered_venues = {}
#     for venue in venues:
#         if venues[venue]["count"] >= min_count:
#             filtered_venues[venue] = venues[venue]
#     return filtered_venues

def main():
    json_file = "dblp-283.json"
    venues = extract_venues(json_file)

    with open("venus-new.json", "w") as file:
        json.dump(venues, file, indent=4)

    print("Total number of venues:", len(venues))
    
    # filtered_venues = filter_venues(venues, min_count=3)
    # print("Total number of venues after filtering:", len(filtered_venues))
    
    # with open("filtered_venues.json", "w") as file:
    #     json.dump(filtered_venues, file, indent=4)
  
if __name__ == "__main__":
    main()
