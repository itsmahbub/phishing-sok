import json

with open("dblp-search-2025-02-12.json", 'r') as file:
    papers_a = json.load(file)
            
with open("dblp-283.json", 'r') as file:
    papers_b = json.load(file)

diff = set([x["info"]["title"] for x in papers_b]) - set([x["info"]["title"] for x in papers_a]) 
for d in diff:
    print(d)