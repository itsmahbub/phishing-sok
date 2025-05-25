import json

with open("dblp-search-2025-02-12.json") as f:
    papers = json.load(f)

with open("venus-ranks.json") as f:
    venues = json.load(f)


selected_papers = []
for paper in papers:
    venue = paper.get("info", {}).get("venue")
    rank = venues.get(venue, {}).get("rank")
    if rank in ["A*", "A", "B", "Q1"]:
        selected_papers.append(paper)

with open("selected_papers.json", "w") as f:
    json.dump(selected_papers, f, indent=4)
