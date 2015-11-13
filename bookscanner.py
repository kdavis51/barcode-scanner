#!/usr/bin/python
"""
Goal: Dump barcodes.

This script is intentionally bare.
"""
import datetime
import sqlite3
import os

INPUT_STATEMENT = "Please scan the next book. Type 'quit' to exit:" 

def sqlite_save(barcodes):
    """ Accept a list of barcodes and dump it to an output file.
    """
    output_dir = "data"


if __name__ == "__main__":
    """
    Dump barcodes in to sqlite.
    """

    barcodes = list()
    _inputline = "" # sentinel value (no do while in python)
    while _inputline != "quit":

        _inputline = raw_input(INPUT_STATEMENT)

        # capture empty values, for good UX
        if _inputline == "":
            continue
        # capture 'quit'
        if _inputline == "quit":
            continue
        if _inputline == "save":
            sqlite_save(barcodes)
            _inputline = ""
            continue

        print "   * * *"
        print "   * * *"
        print "Barcode has {} numbers.".format(len(_inputline))

        _accept_inputline = raw_input("Accept barcode? (y):")
        if _accept_inputline.lower() == "y":
            barcodes.append(_inputline)
            print "Success. There are now {} barcodes unsaved.".format(len(barcodes))
            print "   * * *"
        else:
            print "This barcode has been discarded."
            print "   * * *"

