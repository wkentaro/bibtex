#!/usr/bin/env python

from __future__ import print_function
import sys

import bibtexparser


def main():
    parser = bibtexparser.bparser.BibTexParser(
        interpolate_strings=False, homogenize_fields=True
    )
    with open('bibtex.bib') as f:
        try:
            bibtexparser.load(f, parser=parser)
        except Exception as e:
            print('Encounter following error:', file=sys.stderr)
            print(e)
            sys.exit(1)


if __name__ == '__main__':
    main()
