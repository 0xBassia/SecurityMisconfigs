#!/usr/bin/env python3
"""Display statistics about the SecurityMisconfigs database."""

import csv
from collections import Counter

def main():
    with open('SecurityMisconfigs.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Total entries: {len(rows)}")
    print(f"Unique products: {len(set(r['product'] for r in rows))}")
    print()

    print("By category:")
    cats = Counter(r['category'] for r in rows)
    for cat, count in cats.most_common():
        print(f"  {cat}: {count}")
    print()

    print("By severity:")
    sevs = Counter(r['severity'] for r in rows)
    for sev in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        print(f"  {sev}: {sevs.get(sev, 0)}")
    print()

    print(f"Products with most entries:")
    prods = Counter(r['product'] for r in rows)
    for prod, count in prods.most_common(10):
        print(f"  {prod}: {count}")

if __name__ == '__main__':
    main()
