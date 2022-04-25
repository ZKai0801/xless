# xless

`xless` is a python script that allows display excel files directly on linux command line.

```bash
[kai@admin ~]$ xless test.xlsx -s 1 -g -H None -N 
+------+----------+---------+------+----------+----------+
|index |0         |1        |2     |3         |4         |
+------+----------+---------+------+----------+----------+
|0     |Bat25     |KIT      |chr4  |55598212  |55598236  |
|1     |Bat-26    |MSH2     |chr2  |47641560  |47641586  |
|2     |MONO-27   |MAP4K3   |chr2  |39564894  |39564921  |
|3     |NR-21     |SLC7A8   |chr14 |23652347  |23652367  |
|4     |NR-24     |ZNF2     |chr2  |95849362  |95849384  |
|5     |MSI-01    |NAV1     |chr1  |201754411 |201754427 |
|6     |MSI-03    |FAM161A  |chr2  |62063094  |62063110  |
|7     |MSI-04    |RGPD4    |chr2  |108479623 |108479640 |
|8     |MSI-06    |ATP6V0E1 |chr5  |172421761 |172421775 |
|9     |MSI-07    |GPR126   |chr6  |142691951 |142691967 |
|10    |MSI-08    |ELFN1    |chr7  |1787520   |1787536   |
|11    |MSI-09    |GTF2IP1  |chr7  |74608741  |74608753  |
|12    |MSI-11    |GUCY1A2  |chr11 |106695515 |106695526 |
|13    |MSI-12    |BLOC1S6  |chr15 |45897772  |45897785  |
|14    |MSI-13    |SMG1     |chr16 |18882660  |18882674  |
|15    |MSI-14    |RNF112   |chr17 |19314918  |19314935  |
|16    |HSPH1-T17 |HSPH1    |chr13 |31722621  |31722637  |
|17    |EWSR1     |EWSR1    |chr22 |29696469  |29696484  |
+------+----------+---------+------+----------+----------+
```



## Install 

`xless` requires only the `pandas` and `openpyxl` library and no other dependencies.

Install `xless` via `pip`:

`pip3 install xless`

or simply clone from Github:

```bash
git clone https://github.com/ZKai0801/xless.git 
cp xless/xless /usr/local/bin/
```



## Usage

```bash
[kai@admin ~]$ xless -h
usage: xless [-h] [-H HEADER] [-s [SHEET [SHEET ...]]] [-g] [-N] [-F FIELD_SEPARATOR] [-v] excel

Display excel directly on the screen

positional arguments:
  excel                 Input excel, or use '-' to read from stdin

optional arguments:
  -h, --help            show this help message and exit
  -H HEADER, --header HEADER
                        Row (0-indexed) to use for the column labels of the
                        parsed DataFrame; Use None if there is no header.
  -s [SHEET [SHEET ...]], --sheet [SHEET [SHEET ...]]
                        0-indexed sheet position, or sheet name. set 'all' to
                        display all sheets
  -g, --show_grid       Showing grid for cells
  -N, --show_index      Showing index for rows
  -F FIELD_SEPARATOR, --field_separator FIELD_SEPARATOR
                        Use this for the input field separator. If this is
                        specified, then the input file will be treated as a
                        plain-txt file
  -v, --version         show program's version number and exit
```



The input file could be in `xlsx`, `tsv` or `csv` format. All files will be automatically parsed and output as tab-delimited that could be easily processed by other tools like `awk`. Files in other format will not be parsed by the xless.
