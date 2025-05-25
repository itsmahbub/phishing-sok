import requests
import re

def get_paper_metadata(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['message']
    return None

def extract_references(metadata):
    if 'reference' in metadata:
        return metadata['reference']
    return []

def format_reference(ref):
    return {
        "title": ref.get("article-title", ""),
        "DOI": ref.get("DOI", ""),
    }
  
def find_references(doi):
    metadata = get_paper_metadata(doi)
    if metadata:
        references = extract_references(metadata)
        return [format_reference(ref) for ref in references]
    return []

if __name__ == "__main__":
    # input_doi = input("Enter the DOI of the paper: ")
    input_doi = "10.1016/J.ESWA.2023.121183"
    references = find_references(input_doi)
    
    if references:
        print(f"\nReferences found in the paper (DOI: {input_doi}):")
        for i, ref in enumerate(references, 1):
            print(f"{i}. {ref}")
    else:
        print("No references found or unable to retrieve paper metadata.")
