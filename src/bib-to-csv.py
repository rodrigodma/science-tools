import sys
import csv

from pybtex.database.input import bibtex

file_name = sys.argv[1]
bib_name = file_name + '.bib'
csv_name = file_name + '.csv'

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file(bib_name)

with open(csv_name, 'w') as out_file:
        fieldnames = ['title', 'author', 'year']
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        for bib_id in bibdata.entries:
		b = bibdata.entries[bib_id].fields
		print(b['title'])
		print(b['author'])
		print(b['year'])
		csv_entries = {'title' : b["title"], 'author' : b["author"], 'year' : b["year"]}
		try:
	                writer.writerow(csv_entries)
		except(UnicodeEncodeError):
			csv_entries = {'title' : unicode(b["title"]).encode('utf-8'),
					'author' : unicode(b["author"]).encode('utf-8'),
					'year' : unicode(b["year"]).encode('utf-8')}
			writer.writerow(csv_entries)
