import json

# edu mapping
with open("mapping/edu_mapping.json") as f:
    edu_mapping = json.load(f)
    edu_mapping = {val: key for key, val in edu_mapping.items()} # reversed

# gender mapping
with open('mapping/gender_mapping.json') as f:
    gender_mapping = json.load(f)
    gender_mapping = {val: key for key, val in gender_mapping.items()} # reversed

# dept score
with open('mapping/mapping_dept_score.json') as f:
    mapping_dept_score = json.load(f)

# wilayah mapping
with open('mapping/wilayah_mapping.json') as f:
    wilayah_mapping = json.load(f)
    wilayah_mapping = {val: key for key, val in wilayah_mapping.items()} # reversed
