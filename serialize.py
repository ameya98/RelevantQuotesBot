import pickle
word_id = {}

with open("hitwords.txt", "r") as f1:
    lines = f1.readlines()

lines = [x.strip() for x in lines]

for iden, line in enumerate(lines):    
    word_id[line] = iden

with open("serialize.txt", "wb") as f2:
    pickle.dump(word_id, f2)
