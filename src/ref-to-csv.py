import sys
import csv

file_name = sys.argv[1]
txt_name = file_name + '.txt'
csv_name = file_name + '.csv'
in_file = open(txt_name, 'r')
#out_file = open('science.csv', 'w') using csv i/o

title = False
link = False
abstract = False
keyword = False

new_line = {}
new_list = []

for line in in_file:
	if line != '\n':
		if not title:
			new_line['title'] = line
			title = True
			continue
		if not link:
			new_line['link'] = line
			link = True
			continue
		if not abstract:
			if line == 'Abstract: Abstract\n': continue
			new_line['abstract'] = line
			abstract = True
			continue
		if not keyword:
			new_line['keyword'] = line
	if new_line == {}: continue

	new_list.append(new_line)
	title = link = abstract = keyword = False
	new_line = {}

with open(csv_name, 'w') as out_file:
	fieldnames = ['title', 'link', 'abstract', 'keyword']
	writer = csv.DictWriter(out_file, fieldnames=fieldnames)
	writer.writeheader()
	for line in new_list:
		writer.writerow(line)
