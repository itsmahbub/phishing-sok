import json

def json_to_bib(json_data):
    info = json_data['info']
    authors = ' and '.join([author['text'] for author in info['authors']['author']])
    
    if info['type'] == 'Journal Articles':
        bibtex_entry = f"@article{{{info['key']},\n"
        bibtex_entry += f"  journal = {{{info['venue']}}},\n"
        bibtex_entry += f"  volume = {{{info.get('volume', '')}}},\n"
        bibtex_entry += f"  number = {{{info.get('number', '')}}},\n"
        
    elif info['type'] == 'Conference and Workshop Papers':
        bibtex_entry = f"@inproceedings{{{info['key']},\n"
        bibtex_entry += f"  booktitle = {{{info['venue']}}},\n"
        
    
    bibtex_entry += f"  author = {{{authors}}},\n"
    bibtex_entry += f"  title = {{{info['title']}}},\n"
    bibtex_entry += f"  year = {{{info['year']}}},\n"
    if 'pages' in info:
            bibtex_entry += f"  pages = {{{info['pages']}}},\n"
    bibtex_entry += f"  doi = {{{info.get('doi', '')}}},\n"
    bibtex_entry += f"  url = {{{info['ee']}}},\n"
    bibtex_entry += f"  keywords = {{citation_count: {info['citation_count']}}}\n"
    bibtex_entry += "}"
    return bibtex_entry

if __name__ == "__main__":
    input_file = 'dblp-phishing-final-3.json'
    output_file = 'ref.bib'

    with open(input_file, 'r') as json_file:
        papers = json.load(json_file)

    # Convert JSON to BibTeX and write to file
    with open(output_file, 'w') as bib_file:
        for paper in papers:
            bibtex = json_to_bib(paper)
            if bibtex:
                bib_file.write(bibtex + '\n\n')

    print(f"BibTeX file '{output_file}' has been created successfully.")
