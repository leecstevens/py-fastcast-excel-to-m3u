# py-fastcast-excel-to-m3u
A conversion tool from Fastcast Excel format to M3U files.

## About this tool
This tool was created as a thank you to the fine folks at Fastcast, who have always treated me so well as a customer.  This tool takes the Fastcast Excel playlist export, and converts it into a M3U file for import.  This is useful in the following scenarios:
- Migrating from one server to another
- Archiving of playlists for backup or later import.

This is meant to be a single file solution, so it is nice and portable.

## Good to knows
- Requires openpyxl for reading Excel files (pip install openpyxl)
- This is specifically formatted for Fastcast Exports as of the time of this writing.  If it is useful for any other purpose, that is by accident and not design.
- If you are migrating between servers, your file structure needs to be the same
- If you delete the media files in the M3U, they will not import properly.

## Some fun code examples:
- If you just want to read an Excel file and process it, there is some sample code for you.
- The procedure to convert time from hh:mm:ss to an integer is a nice way to walk a list and use the "power of" operator.

## How to Use
The v1.0 script is a basic starter.  Just do the following:
- Where this script lives, place your imported Excel exports from Fastcast.
- Launch the script however you like (python itself, Visual Studio Code, etc.)
- The script will find all Excel files and process them.
- In the same folder, you will see the converted M3U files.

## Release Notes:
0.7: Initial Release: Simply reads the Excel exports and saves them to M3U files suitable for import with the same file name, different extension.

## Future Plans!?!?!?!?
If I get time, add a GUI to this to make it somewhat more user friendly.