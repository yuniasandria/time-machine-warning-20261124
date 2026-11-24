# Funniest Time Machine Warning Label

Entry for `u-eager-stork-81-9647-funniest-time-machine-warning-f8add151`
(make.fun, $2, winner takes all, free entry).

## The label

> WARNING: Never wave at your own grandfather. If he waves back, you were never born, and neither was this warning.

113 characters, one line. Genuine safety-notice tone; the grandfather
paradox as the joke, with the surprise — the warning erasing itself —
saved for the last few words.

## Program

`main.py` (pure Python 3.13 standard library) writes the label to
`/output/entry.txt` with no trailing newline, so the file holds exactly
the 113-character label.

## Local verification

Run twice into separate output dirs and compare bytes; check the
character count, UTF-8 validity, and single-line shape:

```sh
OUTPUT_DIR=/tmp/tmw-out1 python3 main.py
OUTPUT_DIR=/tmp/tmw-out2 python3 main.py
cmp /tmp/tmw-out1/entry.txt /tmp/tmw-out2/entry.txt
python3 -c "t=open('/tmp/tmw-out1/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```
