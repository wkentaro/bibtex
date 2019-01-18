#!/usr/bin/env python

import bibtexparser


def main():
    parser = bibtexparser.bparser.BibTexParser(
        interpolate_strings=False, homogenize_fields=True
    )
    with open('bibtex.bib') as f:
        bib = bibtexparser.load(f, parser=parser)

    bib.entries = sorted(bib.entries, key=lambda x: x['ID'])
    bib.strings = dict(sorted(bib.strings.items()))

    writer = bibtexparser.bwriter.BibTexWriter()
    writer.add_trailing_comma = True
    with open('bibtex.bib', 'w') as f:
        bibtexparser.dump(bib, f, writer=writer)


if __name__ == '__main__':
    main()
