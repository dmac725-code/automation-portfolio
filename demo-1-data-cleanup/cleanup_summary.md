# Data Cleanup Demo: CRM Contact List

## The Problem
Client had a CRM export with 28 rows of contact data riddled with issues:
- Duplicate entries (same person appearing 2-3 times with inconsistent formatting)
- Inconsistent capitalization (mix of uppercase, lowercase, title case)
- Phone numbers in 5+ different formats
- Missing fields (names, emails, companies)
- Blank/empty rows
- Invalid data (e.g., "NULL" as an email, "N/A" as a phone number)
- State names mixing abbreviations and full names

## What I Delivered
A clean, deduplicated file with 13 unique contacts:

| Metric | Before | After |
|--------|--------|-------|
| Total rows | 28 | 13 |
| Duplicates removed | 15 | 0 |
| Blank rows removed | 2 | 0 |
| Phone format standardized | 5+ formats | 1 format |
| Missing fields recovered | 6 | 0 |
| Invalid entries fixed | 2 | 0 |

## Cleanup Rules Applied
1. **Deduplication** — Matched on email + name fuzzy match, merged best data from each duplicate
2. **Phone standardization** — All converted to (555) 123-4567 format
3. **Capitalization** — Title case for names/cities, uppercase for state abbreviations
4. **Missing data recovery** — Where one duplicate had data the other lacked, preserved the populated field
5. **Invalid data removal** — "NULL" emails and "N/A" phones replaced with actual values where available
6. **Notes consolidation** — Most detailed/recent note preserved from duplicates
7. **Audit trail** — Added Duplicates_Merged column so client can verify merge decisions

## Turnaround
Completed in under 2 hours from receiving the file.
