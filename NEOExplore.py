#!/usr/bin/env python3

import json

info = []

with open('cad.json', 'r') as infile:
	data = json.load(infile)

for x in range(len(data['data'])):
	if '2000-Jan-01' in data['data'][x][3] and data['data'][x][0] == '2002 PB':
		print(data['data'][x][7])
