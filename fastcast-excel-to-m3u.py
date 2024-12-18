"""
Fastcast Excel Export to M3U conversion tool.
Written By: Lee Stevens
"""
import os

def find_excel():
    # Grab all the xlsx files and return dictionary for processing
    excel_files = []
    for file in os.listdir():
        if file.endswith('xlsx'):
            excel_files.append(file)
    return excel_files

def main():
    import_files = find_excel()

main()