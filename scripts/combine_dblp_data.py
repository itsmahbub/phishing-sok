import json

def main():
    # JSON file paths
    json_file1 = "dblp-89.json"
    json_file2 = "dblp-1000.json"

    papers = []
    with open(json_file1, 'r') as file:
        data = json.load(file)
        papers += data.get("result", {}).get("hits", {}).get("hit", [])
    with open(json_file2, 'r') as file:
        data = json.load(file)
        papers += data.get("result", {}).get("hits", {}).get("hit", [])
   
    with open("dblp-phishing.json", "w") as file:
        json.dump(papers, file, indent=4)

if __name__ == "__main__":
    main()

