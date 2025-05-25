import json
from scholarly import ProxyGenerator, scholarly
import time
import requests
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

def get_citation_count_from_google_scholar(title):
    time.sleep(10)
    try:
        search_query = scholarly.search_pubs(title)
        p = next(search_query, None)
        if p:
            return p.get('num_citations', 0)
        else:
            print(f"Could not find paper with title '{title}'")
            return None
    except Exception as e:
        print(f"Error fetching citation count: {e}")
        return None

def get_citation_count_from_crossref(doi):
    url = f"https://api.crossref.org/works/{doi}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['message']['is-referenced-by-count']
    except Exception as e:
        print(f"Error fetching citation count: {e}")
        return None

def add_citation_count(json_file, output_file):
    try:
        with open(json_file, 'r') as file:
            papers = json.load(file)
    except Exception as e:
        print(f"Error reading file {json_file}: {e}")
        return

    for paper in papers:
        if "citation_count" in paper["info"]:
            continue
        try:
            citation_count = get_citation_count_from_crossref(paper["info"]["doi"])
            print(f"Title: {paper['info']['title']}, Citation count: {citation_count}")
        
            if citation_count is not None:
                paper["info"]["citation_count"] = citation_count
        except Exception as e:
            print(paper["info"]["title"])
            print(f"Error fetching citation count: {e}")
        
        if "citation_count" not in paper["info"]:
            paper["info"]["citation_count"] = -1
            
    with open(output_file, 'w') as file:
        json.dump(papers, file, indent=4)


if __name__ == "__main__":
    add_citation_count("dblp-phishing-selected-venues.json", "dblp-phishing-with-citation.json")
