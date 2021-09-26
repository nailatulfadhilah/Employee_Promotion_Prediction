import json 

# reading the data mapping from the file
with open("mapping/edu_mapping.json") as f:
    edu_mapping = json.load(f)
    edu_keys = [val for key, val in edu_mapping.items()]

# gender mapping
with open('mapping/gender_mapping.json') as f:
    gender_mapping = json.load(f)
    gender_keys = [val for key, val in gender_mapping.items()]

# dept score
with open('mapping/mapping_dept_score.json') as f:
    mapping_dept_score = json.load(f)
    dept_keys = [key for key, val in mapping_dept_score.items()]

# wilayah mapping
with open('mapping/wilayah_mapping.json') as f:
    wilayah_mapping = json.load(f)
    wilayah_keys = [val for key, val in wilayah_mapping.items()]