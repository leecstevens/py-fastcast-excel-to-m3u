"""
Fastcast Excel Export to M3U conversion tool.
Written By: Lee Stevens
"""
import os
import openpyxl #For reading Excel files in Python

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
            playlist_name = file.split('.xls')[0]
            output_file = '%s.m3u' % (playlist_name)
            file_path = item[1]
            artist = item[2]
            track = item[3]
            length = time_to_seconds(item[4]) # Convert time to integer seconds
            
            m3u_data.append("EXTINF:%s,%s - %s\n%s" % (
                    length,
                    artist,
                    track,
                    file_path
                ) # Accomodate the file format of M3U
            )
        try:
            with open(output_file,'w') as m3u_file: # This will overwrite if it exists.
                m3u_file.write('\n'.join(m3u_data))
                m3u_file.close()
                print('Output File Created: %s' % (output_file))
        except Exception as e:
            print('File %s not created.\nReason: %s' % (output_file, e))

def time_to_seconds(time_split):
    # This is needed in the M3U format file
    time_split = time_split.split(':') # Create a list from the input
    seconds = 0
    for i in range(len(time_split)):
        diff = (len(time_split)-1)-i # Breaking this up so it's more readable
        seconds += (60 ** diff) * int(time_split[i]) # Multiply 60 to the power of sec/min/hours
    return seconds

def main():
    process_excel_files(find_excel())
    
main()