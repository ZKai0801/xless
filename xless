#!/usr/bin/env python3

__doc__ = "Display excel directly on the screen"
__version__ = "v1.7"
__author__ = "Kai"


import argparse
import tempfile
import os
import re
import pandas as pd
import subprocess
from collections import OrderedDict
import sys


def df2text(df, show_index, show_grid):
    """
    convert dataframe to pure text
    """
    df = remove_newlines(df)
    text = ""

    if show_grid:
        grid_sizes = get_grid_size(df)

        # The character "index" has length of 5
        index_cell_size = max(length(str(df.index[-1])) + 1, 6)

        # format header
        # ----------------
        # 1. create the top grid
        if show_index:
            text += "+" + "-" * index_cell_size

        for colname in df.columns:
            text += "+" + "-" * grid_sizes[colname]
        text += "+\n"
        horizon_line = text

        # 2. create colnames row
        if show_index:
            text += "|index" + " " * (index_cell_size - 5)

        for colname in df.columns:
            text += "|" + colname + " " * (grid_sizes[colname] - length(colname))
        text += "|\n"

        # 3. append a header grid
        text += horizon_line

        # format body
        # ------------------
        for index, row in df.iterrows():
            if show_index:
                text += "|" + str(index)  + " " *  (index_cell_size - length(str(index)))
            for colname in grid_sizes:
                text += "|" + str(row[colname])  + " " * (grid_sizes[colname] - length(str(row[colname])))
            text += "|\n"
        
        text += horizon_line

        return text
    
    # Not showing grids
    header = df.columns.to_list()

    if show_index:
        text += "index\t"

    text += "\t".join(header) + "\n"

    for index, row in df.iterrows():
        if show_index:
            text += str(index) + "\t"
        text += "\t".join(list(map(str, row.to_list()))) + "\n"
    return text


def get_grid_size(df):
    """ calculate cell size for each column """
    grid_size = OrderedDict()
    for col in df.columns:
        whole_column = list(df[col]) + [col]
        max_cell_size = max(map(length, map(str, whole_column))) + 1 
        grid_size[col] = max_cell_size
    return grid_size



def remove_newlines(df):
    """ replace newline with a space """
    df.columns = df.columns.astype(str)
    df.columns = list(map(lambda x: x.replace("\n", " "), df.columns))
    df = df.replace(r"\\n", " ", regex = True)
    return df


def show_text(text):
    """
    use less to show text
    """
    tempname = tempfile.mktemp()
    with open(tempname, "w", errors='backslashreplace') as fh:
        fh.write(text)
    
    cmd = ['less', '-S', tempname]
    p = subprocess.Popen(cmd)
    p.communicate()
    os.unlink(tempname)


def length(text):
    """
    Chinese character return twice of length
    """
    chinese = re.findall(r'[\u4e00-\u9fff]+', text)
    chinese_length = sum(map(len, chinese))
    return len(text) + chinese_length


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument("excel", help = "Input excel, or use '-' to read from stdin")
    parser.add_argument("-H", "--header", default = "0", type = str,
                        help = "Row (0-indexed) to use for the column labels of the parsed DataFrame; Use None if there is no header.")
    parser.add_argument("-s", "--sheet", default = ["0"], nargs = "*",
                        help = "0-indexed sheet position, or sheet name. set 'all' to display all sheets")
    parser.add_argument("-g", "--show_grid", action='store_true', default=False,
                        help = "Showing grid for cells")
    parser.add_argument("-N", "--show_index", action='store_true', default=False,
                        help = "Showing index for rows")
    parser.add_argument("-F", "--field_separator", default="\t",
                        help = "Use this for the input field separator. If this is specified, then the input file will be treated as a plain-txt file")
    parser.add_argument("--get-sheetnames", action='store_true', default=False, help="print sheetnames only")
    parser.add_argument("-v", "--version", action='version', version="%(prog)s " + __version__)
    
    args = parser.parse_args()
    
    assert os.path.exists(args.excel) or args.excel == "-", "Cannot find input file"
    
    header = int(args.header) if args.header.isnumeric() else None

    # read from stdin
    if args.excel == "-":
        tempname = tempfile.mktemp()
        with open(tempname, "w", errors='backslashreplace') as fh:
            for line in sys.stdin:
                fh.write(line)
        
        df = pd.read_csv(tempname, sep = args.field_separator, dtype = str, header = header)
        text = df2text(df, args.show_index, args.show_grid)
        show_text(text)

    elif args.excel.endswith("xlsx"):

        if args.get_sheetnames:
            excels = pd.read_excel(args.excel, dtype = str, header = header, sheet_name = None)
            print("\n".join(excels.keys()))
            sys.exit()

        sheet = [int(i) if i.isnumeric() else i for i in args.sheet]
        sheet = None if (args.sheet[0] == "all") else sheet

        excels = pd.read_excel(args.excel, dtype = str, header = header, sheet_name = sheet)

        for each_sheet in excels:
            text = df2text(excels[each_sheet], args.show_index, args.show_grid)
            show_text(text)
    
    elif args.field_separator:
        df = pd.read_csv(args.excel, sep = args.field_separator, dtype = str, header = header)
        text = df2text(df, args.show_index, args.show_grid)
        show_text(text)
    
    elif args.excel.endswith("csv"):
        csv = pd.read_csv(args.excel, dtype = str, header = header)
        text = df2text(csv, args.show_index, args.show_grid)
        show_text(text)

    elif args.excel.endswith("tsv"):
        tsv = pd.read_csv(args.excel, sep = "\t", dtype = str, header = header)
        text = df2text(tsv, args.show_index, args.show_grid)
        show_text(text)

    else:
        p = subprocess.Popen(['less', '-S', args.excel])
        p.communicate()

