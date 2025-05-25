import json

def main():
    json_file = "dblp-phishing-final-3.json"
    with open(json_file, 'r') as file:
        papers = json.load(file)
    
    sorted_papers = sorted(papers, key=lambda x: x["info"]["citation_count"], reverse=True)
    with open("dblp-phishing-final-3-sorted.json", "w") as file:
        json.dump(sorted_papers, file, indent=4)
  
if __name__ == "__main__":
    main()

