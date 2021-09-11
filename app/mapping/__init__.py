import json 

# reading the data mapping from the file
with open("mapping/edu_mapping.json") as f: 
    edu_mapping = json.load(f)
    edu_mapping = {val:key for key, val in edu_mapping.items()} # reversed 

# genre mapping
with open('mapping/genre_mapping.json') as f:
    genre_mapping = json.load(f)
    genre_mapping = {val:key for key, val in genre_mapping.items()} # reversed 

# dept score
with open('mapping/mapping_dept_score.json') as f:
    mapping_dept_score = json.load(f)

# wilayah mapping
with open('mapping/wilayah_mapping.json') as f:
    wilayah_mapping = json.load(f)
    wilayah_mapping = {val:key for key, val in wilayah_mapping.items()} # reversed 