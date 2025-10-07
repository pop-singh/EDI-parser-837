#!/usr/bin/env python3
"""
Configuration file for EDI 837 Parser
Modify the EDI_DIRECTORY path to point to your EDI files location

INSTRUCTIONS:
1. Change EDI_DIRECTORY to your actual EDI files path
2. Run: python extract_edi_837_business_format.py
3. The script will use your configured directory instead of auto-discovery
"""

# Path to directory containing EDI files (.d, .edi, .txt, .x12 files)
# CHANGE THIS PATH TO YOUR EDI FILES DIRECTORY:
EDI_DIRECTORY = "/path/to/your/edi/files"

# Alternative examples:
# EDI_DIRECTORY = "C:/Users/YourName/Documents/EDI_Files"        # Windows
# EDI_DIRECTORY = "/home/user/edi_data"                         # Linux
# EDI_DIRECTORY = "./my_edi_files"                              # Relative path
# EDI_DIRECTORY = None                                          # Use auto-discovery

# Maximum number of files to process (set to None for all files)
MAX_FILES = 1000

# File extensions to look for
EDI_FILE_EXTENSIONS = ('.d', '.edi', '.txt', '.x12')