"""
Fastcast Excel Export to M3U conversion tool.
Written By: Lee Stevens
"""
import os
import openpyxl
import openpyxl.workbook #For reading Excel files in Python

def find_excel():
    # Grab all the xlsx files and return dictionary for processing
    excel_files = []
    for file in os.listdir():
        if file.endswith('xlsx'):
            excel_files.append(file)
    return excel_files

def process_excel_files(file_list):
    #Variables more verbose for readability
    for file in file_list:
        print('Processing File: %s' % (file))
        m3u_data = ['#EXTM3U'] # Start staging the output file
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.worksheets[0] # Only need Sheet1
        playlist_items = list(sheet.values)[1:]
        for item in playlist_items:
            file_path = item[1]
            artist = item[2]
            track = item[3]
            length = time_to_seconds(item[4]) # Convert time to integer seconds
            m3u_data.append("EXTINF:%s,%s - %s\n%s" % (
                    length,
                    artist,
                    track,
                    file_path
                )
            )
        print('\n'.join(m3u_data))

def time_to_seconds(in_time):
    time_split = in_time.split(':')
    
    seconds = int(time_split[-1]) # Add just the seconds
    seconds += int(time_split[-2]) * 60 # Add 60 seconnds per minute
    if len(time_split) == 3:
        seconds += int(time_split[-3]) * 3600 # In case track is > 1 hour, add 3600 seconds per hour

    return seconds


def main():
    process_excel_files(find_excel())

main()