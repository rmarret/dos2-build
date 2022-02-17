#!python

from os import listdir, rename
from os.path import isfile, join
import re
import json

path = 'static/img'

files = [f for f in listdir(path) if isfile(join(path, f))]

db = {'abilities': [], 'damages': [], 'equipments': [], 'portraits': [], 'roles': [], 'skills': [], 'talents': []}

for f in files:
	if f.endswith('.png'):
		parts = f.split('_')
		prefix = parts[0]
		last_part = parts[-1]
		parts = parts[:-1]
		parts.append(last_part.replace('.png', ''))
		key = '_'.join(parts[1:]).lower()
		name = ' '.join(parts[1:]).title()
		name = name.replace('Dragons Blaze', 'Dragon\'s Blaze') \
				   .replace('Marksmans Fang', 'Marksman\'s Fang') \
				   .replace('Summon Ifans Soul Wolf', 'Summon Ifan\'s Soul Wolf') \
				   .replace('Ifan Ben-Mezd', 'Ifan ben-Mezd')

		if name:
			if prefix == "abilities":
				combat = False if name in ['Bartering', 'Lucky Charm', 'Persuasion', 'Loremaster', 'Telekinesis', 'Sneaking', 'Thievery'] else True
				db['abilities'].append({'key': key, 'combat': combat, 'name': name, 'image': f })
			elif prefix in db:
				db[prefix].append({'key': key, 'name': name, 'image': f })
			elif prefix == "misc" or prefix == "icon" :
				pass
			else:
				db['skills'].append({'key': key, 'name': name, 'school': prefix.title(), 'image': f })

print(json.dumps(db, sort_keys=True))