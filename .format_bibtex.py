#!/usr/bin/env python

import collections

import bibtexparser


def main():
    parser = bibtexparser.bparser.BibTexParser(
        interpolate_strings=False, homogenize_fields=True
    )
    with open('bibtex.bib') as f:
        bib = bibtexparser.load(f, parser=parser)

    for entry in bib.entries:
        if entry['ENTRYTYPE'] == 'article':
            publisher = entry['journal']
        elif entry['ENTRYTYPE'] == 'inproceedings':
            publisher = entry['booktitle']
        else:
            raise ValueError(
                'unexpected ENTRYTYPE: {}'.format(entry['ENTRYTYPE'])
            )
        if publisher in list(bib.strings):
            assert entry['ID'].split(':')[0] == entry['author'].split(',')[0]
            assert entry['ID'].split(':')[-1] == \
                publisher.upper() + entry['year']

    bib.entries = sorted(bib.entries, key=lambda x: x['ID'])
    bib.strings = collections.OrderedDict(sorted(bib.strings.items()))

    writer = bibtexparser.bwriter.BibTexWriter()
    writer.add_trailing_comma = True
    with open('bibtex.bib', 'w') as f:
        bibtexparser.dump(bib, f, writer=writer)


if __name__ == '__main__':
    main()
