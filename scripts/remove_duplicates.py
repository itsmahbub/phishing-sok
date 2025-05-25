import json

duplicate_count = 0
def remove_duplicates(data):
    global duplicate_count
    seen_titles = {}
    for entry in data:
        title = entry['info']['title'].lower()
        if title not in seen_titles:
            seen_titles[title] = entry
        else:
            print(f"Duplicate entry found: {title}")
            duplicate_count += 1
    return list(seen_titles.values())

if __name__ == "__main__":
    json_file = "dblp-phishing-filtered.json"
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    filtered_data = remove_duplicates(data)
    with open("dblp-phishing-no-duplicates.json", "w") as file:
        json.dump(filtered_data, file, indent=4)
    
    print(f"Removed {duplicate_count} duplicate entries")
