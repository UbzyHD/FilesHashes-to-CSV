# Python program to calculate hashes of files
# and output results to a .csv formatted file.

import os
import hashlib
import csv

# Pre-defined columns with values from coursework specification
columns = ['Unique Reference Number', 'Filename', 'MD5', 'SHA-1']

# Create new file in 'write' mode
f = open('File Hash Table.csv', 'w')

with f:
    # Define how data will be organised by utilising headers.
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

    for count, files in enumerate(os.scandir("ScanDir/")):
        # open file in read binary to ensure proper hashing
        with open(files, "rb") as file:
            # read file contents
            data = file.read()
            # append count provided by enumerate, file name & hashes.
            # column with integer ties to column array
            writer.writerow({columns[0]: str(count),
                             columns[1]: str(files.name),
                             columns[2]: hashlib.md5(data).hexdigest(),
                             columns[3]: hashlib.sha1(data).hexdigest()})
