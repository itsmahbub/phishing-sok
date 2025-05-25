import bibtexparser
import json

# Load the BibTeX file
with open("dblp-2014-2025-sel-conf-journ.bib", "r") as bib_file:
    bib_database = bibtexparser.load(bib_file)

# Convert BibTeX entries to JSON
bib_entries_json = json.dumps(bib_database.entries, indent=4)

# Save JSON to a file
with open("dblp-2014-2025-sel-conf-journ.json", "w") as json_file:
    json_file.write(bib_entries_json)

