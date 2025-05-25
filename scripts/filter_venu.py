import json

top_venus = [
    "USENIX Security Symposium",
    "IEEE Access",
    "Expert Syst. Appl.",
    "CCS",
    "Comput. Secur.",
    "eCrime",
    "EuroS&amp;P",
    "IEEE Symposium on Security and Privacy",
    "IEEE Trans. Inf. Forensics Secur.",
    "NDSS",
    "IEEE Trans. Dependable Secur. Comput.",
    "J. Inf. Secur. Appl.",
    "Secur. Commun. Networks",
    "Secur. Priv.",
    "AsiaCCS",
    "ESORICS",
    "RAID",
    "ACSAC",
    "DSN",
    "IMC",
    "CODASPY",
    "SOUPS",
    "SACMAT",
    "SecureComm",
    "CNS",
    "DIMVA",
    "SAC",
    "ACISP",
    "ICICS",
    "ISC"   
]

def filter_venues(venues, min_count=4):
    filtered_venues = {}
    for venue in venues:
        if venues[venue]["count"] >= min_count or venue in top_venus:
            filtered_venues[venue] = venues[venue]
    return filtered_venues


def main():
    with open("venus.json", "r") as file:
        venues = json.load(file)

    filtered_venues = filter_venues(venues, min_count=5)
    print("Total number of venues after filtering:", len(filtered_venues))
    
    with open("filtered_venues.json", "w") as file:
        json.dump(filtered_venues, file, indent=4)
  
if __name__ == "__main__":
    main()
