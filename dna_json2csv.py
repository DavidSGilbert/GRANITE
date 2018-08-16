import json
import csv

report = '/Users/david/PycharmProjects/GRANITE/granite_data/'
source = '/Users/david/PycharmProjects/GRANITE/'

with open(report + "charter_dna.json") as dna_file:
     dna = json.loads(dna_file.read())

def parse_slot(me, slot):
    if len(slot.keys()) == 12:
        return [me] + [(key + ':' + str(slot[key])) for key in slot]
    elif len(slot.keys()) == 1:
        for i, x in enumerate(slot):
            if slot[x][0]:
                for key in slot[x][0]:
                        return [me, x] + [(key + ':' + slot[x][0][key]) for key in slot[x][0]]
            else:
                return [me, x]
    else:
        print(slot)

lo_slots = []
for me in dna:
    for i, x in enumerate(dna[me]):
        if isinstance(dna[me][i], dict):
            slot = dict(dna[me][i])
        if isinstance(dna[me][i], list):
            if len(dna[me][i]) > 1:
                for tom in dna[me][i][1:]:

                    slot = dict(tom[0])
                    lo_slots.append(parse_slot(me, slot))
            slot = dict(dna[me][i][0])
        try:
             lo_slots.append(parse_slot(me, slot))
        except:
            pass

with open(report + 'charter_dna.csv', 'w') as f:
    writer = csv.writer(f, delimiter =',')
    for slot in lo_slots:
        writer.writerow(slot)
