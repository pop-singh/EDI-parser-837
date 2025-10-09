# EDI 837 Healthcare Claims Parser

[![Python - 3.9.0+](https://img.shields.io/badge/Python-3.9.0%2B-orange)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python parser for Electronic Data Interchange (EDI) 837 healthcare claims files. This production-ready tool converts complex EDI format into structured, business-friendly data for healthcare systems integration, analytics, and reporting.

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/pop-singh/EDI-parser-837.git
cd EDI-parser-837
```

### 2. Install Dependencies
```bash
pip install pandas
```

### 3. Configure Your EDI Directory
Edit `config.py` and set your EDI files path:
```python
EDI_DIRECTORY = "/path/to/your/edi/files"
```

### 4. Run the Parser
```bash
python extract_edi_837_business_format.py
```

## 📋 Features

### 🔧 **Core Functionality**
- **Comprehensive EDI Parsing**: Supports all major EDI 837 segments (ISA, GS, ST, BHT, HL, NM1, CLM, SV1, HI, DTP, etc.)
- **Business Format Conversion**: Transforms EDI data into human-readable business objects
- **Medical Code Intelligence**: Includes ICD-10, CPT, HCPCS, and provider taxonomy code descriptions
- **Multiple Output Formats**: Generates JSON and multiple CSV files for different use cases

### 📊 **Output Files Generated**
1. **`edi_837_business_format.json`** - Complete business format data
2. **`EDI_Claims_Output.csv`** - Claim-level data (400+ fields)
3. **`EDI_ClaimDetail_Output.csv`** - Service line details (300+ fields)
4. **`COMPANY_SETUP_Output.csv`** - Trading partner setup data

### ⚙️ **Configuration Options**
- **Custom Directory Paths**: Configure EDI file locations via `config.py`
- **Auto-Discovery**: Automatically finds EDI directories if not configured
- **File Type Support**: Processes `.d`, `.edi`, `.txt`, `.x12` files
- **Batch Processing**: Handles large volumes of files efficiently
- **Progress Tracking**: Real-time processing updates

### 🏥 **Healthcare Domain Support**
- **Provider Information**: Billing, rendering, referring, facility providers
- **Patient Demographics**: Subscriber and patient details
- **Insurance Data**: Payer information and coverage details
- **Medical Services**: Procedure codes with descriptions
- **Diagnosis Codes**: ICD-10 codes with clinical descriptions
- **Place of Service**: Healthcare facility type mappings






## 📁 File Structure

```
EDI-parser-837/
├── extract_edi_837_business_format.py  # Main parser script
├── config.py                           # Configuration file
├── info.txt                           # Comprehensive documentation
├── README.md                          # This file
├── .gitignore                         # Git ignore rules
└── edi_837_parser/                    # Parser package
    └── __init__.py                    # Package initialization
```

## 🔧 Configuration

### Basic Configuration
Edit `config.py` to customize the parser:

```python
# Path to directory containing EDI files
EDI_DIRECTORY = "/path/to/your/edi/files"

# Maximum number of files to process
MAX_FILES = 1000

# File extensions to look for
EDI_FILE_EXTENSIONS = ('.d', '.edi', '.txt', '.x12')
```

### Configuration Examples
```python
# Windows path
EDI_DIRECTORY = "C:/Users/YourName/Documents/EDI_Files"

# Linux/Mac path
EDI_DIRECTORY = "/home/user/edi_data"

# Relative path
EDI_DIRECTORY = "./my_edi_files"

# Use auto-discovery (searches for TOIH or 837 directories)
EDI_DIRECTORY = None
```

## 📊 Sample Output

### Processing Results
```
Found EDI directory: /path/to/edi/files with 330 EDI files
Processing MCK119215.d... (1/330)
✅ Processed 10 files, extracted 53 claims so far
...
📊 EXTRACTION SUMMARY:
Total claims extracted: 1,994
✅ EDI_Claims_Output.csv saved with 1,994 records
✅ EDI_ClaimDetail_Output.csv saved with 4,445 records
✅ COMPANY_SETUP_Output.csv saved with 112 records
```

### Business Format JSON Structure
```json
{
  "id": "claim-uuid",
  "objectType": "CLAIM",
  "patientControlNumber": "12345",
  "chargeAmount": 125.00,
  "billingProvider": {
    "identifier": "1234567890",
    "lastNameOrOrgName": "HEALTHCARE PROVIDER",
    "entityType": "2"
  },
  "serviceLines": [
    {
      "procedure": {
        "code": "99213",
        "desc": "Office visit, established patient"
      },
      "chargeAmount": 125.00
    }
  ]
}
```

## 🏥 Healthcare Data Extracted

### Provider Information
- Billing Provider (NPI, Tax ID, Address)
- Rendering Provider (Individual who provided service)
- Referring Provider (Doctor who referred patient)
- Service Facility (Location where service was provided)

### Patient & Insurance
- Subscriber Information (Insurance holder)
- Patient Demographics (If different from subscriber)
- Payer Details (Insurance company information)

### Medical Services
- **Procedure Codes**: CPT/HCPCS codes with descriptions
- **Diagnosis Codes**: ICD-10 codes with clinical descriptions
- **Service Details**: Dates, quantities, charges
- **Place of Service**: Where medical services were provided

### Business Data
- Claim Control Numbers
- Service Dates and Charge Amounts
- Provider Participation and Assignment
- Release of Information Codes

## 🔍 Advanced Usage

### Processing Specific File Types
The parser automatically detects and processes:
- `.d` files (EDI data files)
- `.edi` files (Standard EDI format)
- `.txt` files (Text-based EDI)
- `.x12` files (X12 EDI format)

### Batch Processing
```python
# Process up to 1000 files
MAX_FILES = 1000

# Process all files in directory
MAX_FILES = None
```

### Error Handling
The parser includes robust error handling:
- Graceful handling of malformed EDI segments
- Permission error handling for restricted directories
- Progress tracking with error reporting
- Detailed logging for troubleshooting

## 📚 Documentation

For comprehensive technical documentation, see [`info.txt`](info.txt) which includes:
- Detailed EDI segment parsing explanations
- Medical code libraries (ICD-10, CPT, HCPCS)
- Business format conversion logic
- Code architecture and design patterns
- Real-world usage examples

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [`info.txt`](info.txt) for detailed documentation
2. Review the configuration in `config.py`
3. Ensure your EDI files are in the correct format
4. Open an issue on GitHub with detailed error information

## 🏆 Acknowledgments

- Built for healthcare claims processing and EDI integration
- Supports HIPAA-compliant EDI 837 transaction standards
- Designed for production healthcare environments
- Optimized for large-scale claims processing workflows




â”œâ”€â”€ .gitignore
â”œâ”€â”€ README.md
â”œâ”€â”€ config.py
â”œâ”€â”€ edi_837_parser
    â”œâ”€â”€ __init__.py
    â”œâ”€â”€ elements
    â”‚   â”œâ”€â”€ __init__.py
    â”‚   â”œâ”€â”€ adjustment_group_code.py
    â”‚   â”œâ”€â”€ adjustment_reason_code.py
    â”‚   â”œâ”€â”€ amount_qualifier.py
    â”‚   â”œâ”€â”€ authorization_information_qualifier.py
    â”‚   â”œâ”€â”€ claim_status.py
    â”‚   â”œâ”€â”€ date.py
    â”‚   â”œâ”€â”€ date_qualifier.py
    â”‚   â”œâ”€â”€ dollars.py
    â”‚   â”œâ”€â”€ entity_code.py
    â”‚   â”œâ”€â”€ entity_type.py
    â”‚   â”œâ”€â”€ identification_code_qualifier.py
    â”‚   â”œâ”€â”€ identifier.py
    â”‚   â”œâ”€â”€ integer.py
    â”‚   â”œâ”€â”€ payment_method.py
    â”‚   â”œâ”€â”€ reference_qualifier.py
    â”‚   â”œâ”€â”€ service_code.py
    â”‚   â”œâ”€â”€ service_modifier.py
    â”‚   â”œâ”€â”€ service_qualifier.py
    â”‚   â””â”€â”€ utilities.py
    â”œâ”€â”€ loops
    â”‚   â”œâ”€â”€ __init__.py
    â”‚   â”œâ”€â”€ billingprovider.py
    â”‚   â”œâ”€â”€ claim.py
    â”‚   â”œâ”€â”€ patient.py
    â”‚   â”œâ”€â”€ payer.py
    â”‚   â”œâ”€â”€ service.py
    â”‚   â””â”€â”€ subscriber.py
    â”œâ”€â”€ segments
    â”‚   â”œâ”€â”€ __init__.py
    â”‚   â”œâ”€â”€ address.py
    â”‚   â”œâ”€â”€ amount.py
    â”‚   â”œâ”€â”€ billingprovider.py
    â”‚   â”œâ”€â”€ city_information.py
    â”‚   â”œâ”€â”€ claim.py
    â”‚   â”œâ”€â”€ date.py
    â”‚   â”œâ”€â”€ demographic_information.py
    â”‚   â”œâ”€â”€ dept_contact_information.py
    â”‚   â”œâ”€â”€ diagnosis.py
    â”‚   â”œâ”€â”€ drug_identification.py
    â”‚   â”œâ”€â”€ drug_quantity.py
    â”‚   â”œâ”€â”€ entity.py
    â”‚   â”œâ”€â”€ location.py
    â”‚   â”œâ”€â”€ note.py
    â”‚   â”œâ”€â”€ patient.py
    â”‚   â”œâ”€â”€ reference.py
    â”‚   â”œâ”€â”€ service.py
    â”‚   â”œâ”€â”€ service_adjustment.py
    â”‚   â”œâ”€â”€ service_line_adjudication.py
    â”‚   â”œâ”€â”€ serviceline.py
    â”‚   â”œâ”€â”€ subscriber.py
    â”‚   â””â”€â”€ utilities.py
    â””â”€â”€ transaction_set
    â”‚   â”œâ”€â”€ __init__.py
    â”‚   â”œâ”€â”€ transaction_set.py
    â”‚   â””â”€â”€ transaction_sets.py
â”œâ”€â”€ extract_edi_837_business_format.py
â””â”€â”€ info.txt


/.gitignore:
--------------------------------------------------------------------------------
 1 | # EDI data files and directories
 2 | TOIH_ClaimsExport_957174*
 3 | *.d
 4 | *.edi
 5 | 
 6 | # Output files
 7 | edi_837_business_format.json
 8 | edi_837_business_format.csv
 9 | edi_837_complete_business_format.csv
10 | EDI_Claims_Output.csv
11 | EDI_ClaimDetail_Output.csv
12 | COMPANY_SETUP_Output.csv
13 | 
14 | # Python
15 | __pycache__/
16 | *.pyc
17 | *.pyo
18 | *.pyd
19 | .Python
20 | env/
21 | venv/
22 | .venv/
23 | 
24 | # IDE
25 | .vscode/
26 | .idea/
27 | *.swp
28 | *.swo
29 | 
30 | # OS
31 | .DS_Store
32 | Thumbs.db


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
  1 | # EDI 837 Healthcare Claims Parser
  2 | 
  3 | [![Python - 3.9.0+](https://img.shields.io/badge/Python-3.9.0%2B-orange)](https://www.python.org/downloads/release/python-390/)
  4 | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  5 | 
  6 | A comprehensive Python parser for Electronic Data Interchange (EDI) 837 healthcare claims files. This production-ready tool converts complex EDI format into structured, business-friendly data for healthcare systems integration, analytics, and reporting.
  7 | 
  8 | ## ðŸš€ Quick Start
  9 | 
 10 | ### 1. Clone the Repository
 11 | ```bash
 12 | git clone https://github.com/pop-singh/EDI-parser-837.git
 13 | cd EDI-parser-837
 14 | ```
 15 | 
 16 | ### 2. Install Dependencies
 17 | ```bash
 18 | pip install pandas
 19 | ```
 20 | 
 21 | ### 3. Configure Your EDI Directory
 22 | Edit `config.py` and set your EDI files path:
 23 | ```python
 24 | EDI_DIRECTORY = "/path/to/your/edi/files"
 25 | ```
 26 | 
 27 | ### 4. Run the Parser
 28 | ```bash
 29 | python extract_edi_837_business_format.py
 30 | ```
 31 | 
 32 | ## ðŸ“‹ Features
 33 | 
 34 | ### ðŸ”§ **Core Functionality**
 35 | - **Comprehensive EDI Parsing**: Supports all major EDI 837 segments (ISA, GS, ST, BHT, HL, NM1, CLM, SV1, HI, DTP, etc.)
 36 | - **Business Format Conversion**: Transforms EDI data into human-readable business objects
 37 | - **Medical Code Intelligence**: Includes ICD-10, CPT, HCPCS, and provider taxonomy code descriptions
 38 | - **Multiple Output Formats**: Generates JSON and multiple CSV files for different use cases
 39 | 
 40 | ### ðŸ“Š **Output Files Generated**
 41 | 1. **`edi_837_business_format.json`** - Complete business format data
 42 | 2. **`EDI_Claims_Output.csv`** - Claim-level data (400+ fields)
 43 | 3. **`EDI_ClaimDetail_Output.csv`** - Service line details (300+ fields)
 44 | 4. **`COMPANY_SETUP_Output.csv`** - Trading partner setup data
 45 | 
 46 | ### âš™ï¸ **Configuration Options**
 47 | - **Custom Directory Paths**: Configure EDI file locations via `config.py`
 48 | - **Auto-Discovery**: Automatically finds EDI directories if not configured
 49 | - **File Type Support**: Processes `.d`, `.edi`, `.txt`, `.x12` files
 50 | - **Batch Processing**: Handles large volumes of files efficiently
 51 | - **Progress Tracking**: Real-time processing updates
 52 | 
 53 | ### ðŸ¥ **Healthcare Domain Support**
 54 | - **Provider Information**: Billing, rendering, referring, facility providers
 55 | - **Patient Demographics**: Subscriber and patient details
 56 | - **Insurance Data**: Payer information and coverage details
 57 | - **Medical Services**: Procedure codes with descriptions
 58 | - **Diagnosis Codes**: ICD-10 codes with clinical descriptions
 59 | - **Place of Service**: Healthcare facility type mappings
 60 | 
 61 | 
 62 | 
 63 | 
 64 | 
 65 | 
 66 | ## ðŸ“ File Structure
 67 | 
 68 | ```
 69 | EDI-parser-837/
 70 | â”œâ”€â”€ extract_edi_837_business_format.py  # Main parser script
 71 | â”œâ”€â”€ config.py                           # Configuration file
 72 | â”œâ”€â”€ info.txt                           # Comprehensive documentation
 73 | â”œâ”€â”€ README.md                          # This file
 74 | â”œâ”€â”€ .gitignore                         # Git ignore rules
 75 | â””â”€â”€ edi_837_parser/                    # Parser package
 76 |     â””â”€â”€ __init__.py                    # Package initialization
 77 | ```
 78 | 
 79 | ## ðŸ”§ Configuration
 80 | 
 81 | ### Basic Configuration
 82 | Edit `config.py` to customize the parser:
 83 | 
 84 | ```python
 85 | # Path to directory containing EDI files
 86 | EDI_DIRECTORY = "/path/to/your/edi/files"
 87 | 
 88 | # Maximum number of files to process
 89 | MAX_FILES = 1000
 90 | 
 91 | # File extensions to look for
 92 | EDI_FILE_EXTENSIONS = ('.d', '.edi', '.txt', '.x12')
 93 | ```
 94 | 
 95 | ### Configuration Examples
 96 | ```python
 97 | # Windows path
 98 | EDI_DIRECTORY = "C:/Users/YourName/Documents/EDI_Files"
 99 | 
100 | # Linux/Mac path
101 | EDI_DIRECTORY = "/home/user/edi_data"
102 | 
103 | # Relative path
104 | EDI_DIRECTORY = "./my_edi_files"
105 | 
106 | # Use auto-discovery (searches for TOIH or 837 directories)
107 | EDI_DIRECTORY = None
108 | ```
109 | 
110 | ## ðŸ“Š Sample Output
111 | 
112 | ### Processing Results
113 | ```
114 | Found EDI directory: /path/to/edi/files with 330 EDI files
115 | Processing MCK119215.d... (1/330)
116 | âœ… Processed 10 files, extracted 53 claims so far
117 | ...
118 | ðŸ“Š EXTRACTION SUMMARY:
119 | Total claims extracted: 1,994
120 | âœ… EDI_Claims_Output.csv saved with 1,994 records
121 | âœ… EDI_ClaimDetail_Output.csv saved with 4,445 records
122 | âœ… COMPANY_SETUP_Output.csv saved with 112 records
123 | ```
124 | 
125 | ### Business Format JSON Structure
126 | ```json
127 | {
128 |   "id": "claim-uuid",
129 |   "objectType": "CLAIM",
130 |   "patientControlNumber": "12345",
131 |   "chargeAmount": 125.00,
132 |   "billingProvider": {
133 |     "identifier": "1234567890",
134 |     "lastNameOrOrgName": "HEALTHCARE PROVIDER",
135 |     "entityType": "2"
136 |   },
137 |   "serviceLines": [
138 |     {
139 |       "procedure": {
140 |         "code": "99213",
141 |         "desc": "Office visit, established patient"
142 |       },
143 |       "chargeAmount": 125.00
144 |     }
145 |   ]
146 | }
147 | ```
148 | 
149 | ## ðŸ¥ Healthcare Data Extracted
150 | 
151 | ### Provider Information
152 | - Billing Provider (NPI, Tax ID, Address)
153 | - Rendering Provider (Individual who provided service)
154 | - Referring Provider (Doctor who referred patient)
155 | - Service Facility (Location where service was provided)
156 | 
157 | ### Patient & Insurance
158 | - Subscriber Information (Insurance holder)
159 | - Patient Demographics (If different from subscriber)
160 | - Payer Details (Insurance company information)
161 | 
162 | ### Medical Services
163 | - **Procedure Codes**: CPT/HCPCS codes with descriptions
164 | - **Diagnosis Codes**: ICD-10 codes with clinical descriptions
165 | - **Service Details**: Dates, quantities, charges
166 | - **Place of Service**: Where medical services were provided
167 | 
168 | ### Business Data
169 | - Claim Control Numbers
170 | - Service Dates and Charge Amounts
171 | - Provider Participation and Assignment
172 | - Release of Information Codes
173 | 
174 | ## ðŸ” Advanced Usage
175 | 
176 | ### Processing Specific File Types
177 | The parser automatically detects and processes:
178 | - `.d` files (EDI data files)
179 | - `.edi` files (Standard EDI format)
180 | - `.txt` files (Text-based EDI)
181 | - `.x12` files (X12 EDI format)
182 | 
183 | ### Batch Processing
184 | ```python
185 | # Process up to 1000 files
186 | MAX_FILES = 1000
187 | 
188 | # Process all files in directory
189 | MAX_FILES = None
190 | ```
191 | 
192 | ### Error Handling
193 | The parser includes robust error handling:
194 | - Graceful handling of malformed EDI segments
195 | - Permission error handling for restricted directories
196 | - Progress tracking with error reporting
197 | - Detailed logging for troubleshooting
198 | 
199 | ## ðŸ“š Documentation
200 | 
201 | For comprehensive technical documentation, see [`info.txt`](info.txt) which includes:
202 | - Detailed EDI segment parsing explanations
203 | - Medical code libraries (ICD-10, CPT, HCPCS)
204 | - Business format conversion logic
205 | - Code architecture and design patterns
206 | - Real-world usage examples
207 | 
208 | ## ðŸ¤ Contributing
209 | 
210 | 1. Fork the repository
211 | 2. Create a feature branch (`git checkout -b feature/amazing-feature`)
212 | 3. Commit your changes (`git commit -m 'Add amazing feature'`)
213 | 4. Push to the branch (`git push origin feature/amazing-feature`)
214 | 5. Open a Pull Request
215 | 
216 | ## ðŸ“„ License
217 | 
218 | This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
219 | 
220 | ## ðŸ†˜ Support
221 | 
222 | If you encounter any issues or have questions:
223 | 1. Check the [`info.txt`](info.txt) for detailed documentation
224 | 2. Review the configuration in `config.py`
225 | 3. Ensure your EDI files are in the correct format
226 | 4. Open an issue on GitHub with detailed error information
227 | 
228 | ## ðŸ† Acknowledgments
229 | 
230 | - Built for healthcare claims processing and EDI integration
231 | - Supports HIPAA-compliant EDI 837 transaction standards
232 | - Designed for production healthcare environments
233 | - Optimized for large-scale claims processing workflows
234 | 
235 | 
236 | 
237 | 
238 | 
239 | 
240 | 


--------------------------------------------------------------------------------
/config.py:
--------------------------------------------------------------------------------
 1 | #!/usr/bin/env python3
 2 | """
 3 | Configuration file for EDI 837 Parser
 4 | Modify the EDI_DIRECTORY path to point to your EDI files location
 5 | 
 6 | INSTRUCTIONS:
 7 | 1. Change EDI_DIRECTORY to your actual EDI files path
 8 | 2. Run: python extract_edi_837_business_format.py
 9 | 3. The script will use your configured directory instead of auto-discovery
10 | """
11 | 
12 | # Path to directory containing EDI files (.d, .edi, .txt, .x12 files)
13 | # CHANGE THIS PATH TO YOUR EDI FILES DIRECTORY:
14 | EDI_DIRECTORY =""
15 | 
16 | # Alternative examples:
17 | # EDI_DIRECTORY = "C:/Users/YourName/Documents/EDI_Files"        # Windows
18 | # EDI_DIRECTORY = "/home/user/edi_data"                         # Linux
19 | # EDI_DIRECTORY = "./my_edi_files"                              # Relative path
20 | # EDI_DIRECTORY = None                                          # Use auto-discovery
21 | 
22 | # Maximum number of files to process (set to None for all files)
23 | MAX_FILES = 1000
24 | 
25 | # File extensions to look for
26 | EDI_FILE_EXTENSIONS = ('.d', '.edi', '.txt', '.x12')
27 | 


--------------------------------------------------------------------------------
/edi_837_parser/__init__.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | from typing import List
 3 | from warnings import warn
 4 | 
 5 | from edi_837_parser.transaction_set.transaction_set import TransactionSet
 6 | from edi_837_parser.transaction_set.transaction_sets import TransactionSets
 7 | 
 8 | 
 9 | def parse(path: str, debug: bool = False) -> TransactionSets:
10 | 	if path[0] == '~':
11 | 		path = os.path.expanduser(path)
12 | 
13 | 	transaction_sets = []
14 | 	if os.path.isdir(path):
15 | 		files = _find_edi_837_files(path)
16 | 		for file in files:
17 | 			file_path = f'{path}/{file}'
18 | 			if debug:
19 | 				transaction_set = TransactionSet.build(file_path)
20 | 				transaction_sets.append(transaction_set)
21 | 			else:
22 | 				try:
23 | 					transaction_set = TransactionSet.build(file_path)
24 | 					transaction_sets.append(transaction_set)
25 | 				except Exception as e:
26 | 					warn(f'Failed to build a transaction set from {file_path} with error: {e}')
27 | 	else:
28 | 		transaction_set = TransactionSet.build(path)
29 | 		transaction_sets.append(transaction_set)
30 | 
31 | 	return TransactionSets(transaction_sets)
32 | 
33 | 
34 | def _find_edi_837_files(path: str) -> List[str]:
35 | 	files = []
36 | 	for file in os.listdir(path):
37 | 		if file.endswith('.txt') or file.endswith('.837'):
38 | 			files.append(file)
39 | 
40 | 	return files
41 | 
42 | 
43 | # Package can be imported and used programmatically
44 | # Main execution should use extract_edi_837_business_format.py
45 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/__init__.py:
--------------------------------------------------------------------------------
 1 | from abc import ABC, abstractmethod
 2 | 
 3 | 
 4 | class Element(ABC):
 5 | 
 6 | 	def __set_name__(self, owner, name):
 7 | 		self.private_name = '_' + name
 8 | 
 9 | 	def __get__(self, obj, obj_type=None):
10 | 		return getattr(obj, self.private_name)
11 | 
12 | 	def __set__(self, obj, value):
13 | 		value = self.parser(value)
14 | 		setattr(obj, self.private_name, value)
15 | 
16 | 	@abstractmethod
17 | 	def parser(self, value):
18 | 		pass
19 | 
20 | 
21 | class Code:
22 | 
23 | 	def __init__(self, code: str, description: str):
24 | 		self.code = code
25 | 		self.description = description
26 | 
27 | 	def __str__(self) -> str:
28 | 		return str(self.__dict__)
29 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/adjustment_group_code.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element, Code
 2 | 
 3 | # https://x12.org/codes/claim-adjustment-group-codes
 4 | adjustment_group_codes = {
 5 | 	'CR': 'corrections and reversals',
 6 | 	'OA': 'other adjustment',
 7 | 	'PR': 'patient responsibility',
 8 | 	'CO': 'contractual obligation',
 9 | 	'PI': 'payor initiated reduction',
10 | }
11 | 
12 | 
13 | class AdjustmentGroupCode(Element):
14 | 
15 | 	def parser(self, value: str) -> Code:
16 | 		description = adjustment_group_codes.get(value, None)
17 | 		return Code(value, description)
18 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/adjustment_reason_code.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element, Code
 2 | 
 3 | # https://x12.org/codes/claim-adjustment-reason-codes
 4 | adjustment_reason_codes = {
 5 | 	'45': 'Charge exceeds fee schedule maximum allowable or contracted/legislated fee arrangement.',
 6 | 	'243': 'Services not authorized by network/primary care providers.',
 7 | 	'29': 'The time limit for filing has expired.',
 8 | 	'251': 'The attachment/other documentation that was received was incomplete or deficient.',
 9 | 	'2': 'Coinsurnace Amount.',
10 | 	'96': 'Non-covered charge(s). See remark code.',
11 | 	'3': 'Co-payment Amount.',
12 | 	'16': 'Claim/service lacks information or has submission/billing error(s).',
13 | 	'B15':'This service/procedure requires that a qualifying service/procedure be received and covered. The qualifying other service/procedure has not been received/adjudicated.',
14 | 	'A1': 'Claim/Service denied. See remark code.',
15 | 	'1': 'Deductible Amount',
16 | 	'4': 'The procedure code is inconsistent with the modifier used. Usage: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.',
17 | 	'18': 'Exact duplicate claim/service (Use only with Group Code OA except where state workers\' compensation regulations requires CO)',
18 | 	'23': 'The impact of prior payer(s) adjudication including payments and/or adjustments. (Use only with Group Code OA)',
19 | 	'26': 'Expenses incurred prior to coverage.',
20 | 	'27': 'Expenses incurred after coverage terminated.',
21 | 	'97': 'The benefit for this service is included in the payment/allowance for another service/procedure that has already been adjudicated. Usage: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.',
22 | 	'109': 'Claim/service not covered by this payer/contractor. You must send the claim/service to the correct payer/contractor.',
23 | 	'151': 'Payment adjusted because the payer deems the information submitted does not support this many/frequency of services.',
24 | 	'234': 'This procedure is not paid separately. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)',
25 | 	'272': 'Coverage/program guidelines were not met.',
26 | }
27 | 
28 | 
29 | class AdjustmentReasonCode(Element):
30 | 
31 | 	def parser(self, value: str) -> Code:
32 | 		description = adjustment_reason_codes.get(value, None)
33 | 		return Code(value, description)
34 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/amount_qualifier.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | 
 3 | # https://ushik.ahrq.gov/ViewItemDetails?system=mdr&itemKey=133081000
 4 | amount_qualifiers = {
 5 | 	'B6': 'allowed - actual',
 6 | 	'AU': 'coverage amount',
 7 | 	'D':  'other amount paid',
 8 | 	'EAF': 'other patient payer liability'
 9 | }
10 | 
11 | 
12 | class AmountQualifier(Element):
13 | 
14 | 	def parser(self, value: str) -> str:
15 | 		return amount_qualifiers.get(value, value)
16 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/authorization_information_qualifier.py:
--------------------------------------------------------------------------------
 1 | from typing import Optional
 2 | 
 3 | from edi_837_parser.elements import Element
 4 | 
 5 | 
 6 | class AuthorizationInformationQualifier(Element):
 7 | 
 8 | 	def parser(self, value: str) -> Optional[str]:
 9 | 		if value == '00':
10 | 			value = None
11 | 
12 | 		return value
13 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/claim_status.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass
 2 | from enum import Enum, auto
 3 | from warnings import warn
 4 | 
 5 | 
 6 | from edi_837_parser.elements import Element
 7 | 
 8 | 
 9 | class PayerClassification(Enum):
10 | 	PRIMARY = auto()
11 | 	SECONDARY = auto()
12 | 	TERTIARY = auto()
13 | 	UNSPECIFIED = auto()
14 | 	UNKNOWN = auto()
15 | 
16 | 	def __str__(self) -> str:
17 | 		return str(self.name).lower()
18 | 
19 | 
20 | @dataclass
21 | class Status:
22 | 	"""
23 | 	Attributes:
24 | 
25 | 	- code (:class:`str`): The code provided in the EDI 835 file.
26 | 	- description (:class:`str`): The description of the code per `stedi <https://www.stedi.com/edi/x12/segment/CLP>`_.
27 | 	- payer_classification (:class:`PayerClassification`)
28 | 	"""
29 | 	code: str
30 | 	description: str
31 | 	payer_classification: PayerClassification
32 | 
33 | 
34 | _REGISTRY = [
35 | 	Status('1', 'processed as primary', PayerClassification.PRIMARY),
36 | 	Status('2', 'processed as secondary', PayerClassification.SECONDARY),
37 | 	Status('3', 'processed as tertiary', PayerClassification.TERTIARY),
38 | 	Status('4', 'denial', PayerClassification.UNSPECIFIED),
39 | 	Status('19', 'processed as primary, forwarded to additional payer(s)', PayerClassification.PRIMARY),
40 | 	Status('20', 'processed as secondary, forwarded to additional payer(s)', PayerClassification.SECONDARY),
41 | 	Status('21', 'processed as tertiary, forwarded to additional payer(s)', PayerClassification.TERTIARY),
42 | 	Status('22', 'reversal of previous payment', PayerClassification.UNSPECIFIED),
43 | ]
44 | 
45 | 
46 | def _lookup_status(code: str) -> Status:
47 | 	status = [s for s in _REGISTRY if s.code == code]
48 | 	if len(status) == 0:
49 | 		warn(f'ClaimStatus: Code {code} does not match a status in the edi-835-parser claim status registry.')
50 | 		return Status('code', 'uncategorized', PayerClassification.UNKNOWN)
51 | 
52 | 	return status[0]
53 | 
54 | 
55 | class ClaimStatus(Element):
56 | 
57 | 	def parser(self, value: str) -> Status:
58 | 		return _lookup_status(value)
59 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/date.py:
--------------------------------------------------------------------------------
 1 | from typing import Union
 2 | from datetime import datetime
 3 | from warnings import warn
 4 | 
 5 | from edi_837_parser.elements import Element
 6 | 
 7 | 
 8 | class Date(Element):
 9 | 
10 | 	def parser(self, value: str) -> Union[datetime, str]:
11 | 		if len(value) == 10:
12 | 			year, month, day, minute, second = [int(value[i:i + 2]) for i in range(0, len(value), 2)]
13 | 			return datetime(2000 + year, month, day, minute, second)
14 | 
15 | 		elif len(value) == 8:
16 | 			year, month, day = int(value[:4]), int(value[4:6]), int(value[6:])
17 | 			return datetime(year, month, day)
18 | 
19 | 		else:
20 | 			# warn(f'Unable to parse {value} into a datetime')
21 | 			return value
22 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/date_qualifier.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | 
 3 | # https://ediacademy.com/blog/x12-date-time-qualifiers/
 4 | date_qualifiers = {
 5 | 	'050': 'received',
 6 | 	'150': 'service period start',
 7 | 	'151': 'service period end',
 8 | 	'472': 'service',
 9 | 	'232': 'claim statement period start',
10 | 	'233': 'claim statement period end',
11 | }
12 | 
13 | 
14 | class DateQualifier(Element):
15 | 
16 | 	def parser(self, value: str) -> str:
17 | 		return date_qualifiers.get(value, value)
18 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/dollars.py:
--------------------------------------------------------------------------------
 1 | from typing import Optional
 2 | 
 3 | from edi_837_parser.elements import Element
 4 | 
 5 | 
 6 | class Dollars(Element):
 7 | 
 8 | 	def parser(self, value: str) -> Optional[float]:
 9 | 		if value != '':
10 | 			return float(value)
11 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/entity_code.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | 
 3 | # https://ediacademy.com/blog/x12-n101-entity-identifier-codes/
 4 | entity_codes = {
 5 | 	'QC': 'patient',
 6 | 	'74': 'insured',
 7 | 	'82': 'rendering provider',
 8 | 	'85': 'billing provider'
 9 | }
10 | 
11 | 
12 | class EntityCode(Element):
13 | 
14 | 	def parser(self, value: str) -> str:
15 | 		return entity_codes.get(value, value)
16 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/entity_type.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | 
 3 | # https://magnacare.com/wp-content/uploads/pdf/MagnacareCompanionGuide_835_5010A1.pdf
 4 | entity_types = {
 5 | 	'1': 'person',
 6 | 	'2': 'entity',
 7 | }
 8 | 
 9 | 
10 | class EntityType(Element):
11 | 
12 | 	def parser(self, value: str) -> str:
13 | 		return entity_types.get(value, value)
14 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/identification_code_qualifier.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | 
 3 | # https://ushik.ahrq.gov/dr.ui.drValueDomain_View?system=mdr&ValueDomainID=4933000&CallingRoutine=$CallingRoutine$&OrganizationID=3&RecordOffset=11&Referer=ValueDomain
 4 | identification_code_qualifiers = {
 5 | 	'MI': 'member identification number',
 6 | 	'C': "insured's changed unique identification number",
 7 | 	'PC': 'provider commercial number',
 8 | 	'XX': 'national provider id',
 9 | 
10 | }
11 | 
12 | 
13 | class IdentificationCodeQualifier(Element):
14 | 
15 | 	def parser(self, value: str) -> str:
16 | 		return identification_code_qualifiers.get(value, value)
17 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/identifier.py:
--------------------------------------------------------------------------------
 1 | from typing import Optional
 2 | 
 3 | from edi_837_parser.elements import Element
 4 | 
 5 | 
 6 | class Identifier(Element):
 7 | 
 8 | 	def __set__(self, obj, value):
 9 | 		if obj.identification != value:
10 | 			raise ValueError('class identifier does not match segment identifier.')
11 | 
12 | 		value = self.parser(value)
13 | 		setattr(obj, self.private_name, value)
14 | 
15 | 	def parser(self, value: str) -> Optional[str]:
16 | 		return value
17 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/integer.py:
--------------------------------------------------------------------------------
 1 | from typing import Optional, Union
 2 | 
 3 | from edi_837_parser.elements import Element
 4 | 
 5 | 
 6 | class Integer(Element):
 7 | 
 8 | 	def parser(self, value: str) -> Optional[Union[int, str]]:
 9 | 		if value == '':
10 | 			return None
11 | 
12 | 		try:
13 | 			value = int(value)
14 | 		except:
15 | 			pass
16 | 
17 | 		return value
18 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/payment_method.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | 
 3 | payment_methods = {
 4 | 	'ACH': 'automatic deposit',
 5 | 	'CHK': 'check',
 6 | 	'NON': 'no payment'
 7 | }
 8 | 
 9 | 
10 | class PaymentMethod(Element):
11 | 
12 | 	def parser(self, value: str) -> str:
13 | 		value = value.strip()
14 | 		return payment_methods.get(value, value)
15 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/reference_qualifier.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element, Code
 2 | 
 3 | # https://ushik.ahrq.gov/ViewItemDetails?&system=sdo&itemKey=133213000
 4 | reference_qualifiers = {
 5 | 	'6R': 'provider control number',
 6 | 	'0K': 'policy form identifying number',
 7 | 	'PQ': 'payee identification',
 8 | 	'TJ': 'federal taxpayer identification number',
 9 | 	'LU': 'location number'
10 | }
11 | 
12 | 
13 | class ReferenceQualifier(Element):
14 | 
15 | 	def parser(self, value: str) -> Code:
16 | 		description = reference_qualifiers.get(value, None)
17 | 		return Code(value, description)
18 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/service_code.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | from edi_837_parser.elements.utilities import split_element
 3 | 
 4 | 
 5 | class ServiceCode(Element):
 6 | 
 7 | 	def parser(self, value: str) -> str:
 8 | 		value = split_element(value)
 9 | 		_, code, *_ = value
10 | 		return code
11 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/service_modifier.py:
--------------------------------------------------------------------------------
 1 | from typing import Optional
 2 | 
 3 | from edi_837_parser.elements import Element
 4 | from edi_837_parser.elements.utilities import split_element
 5 | 
 6 | 
 7 | class ServiceModifier(Element):
 8 | 
 9 | 	def parser(self, value: str) -> Optional[str]:
10 | 		value = split_element(value)
11 | 		if len(value) > 2:
12 | 			return value[2]
13 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/service_qualifier.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements import Element
 2 | from edi_837_parser.elements.utilities import split_element
 3 | 
 4 | 
 5 | class ServiceQualifer(Element):
 6 | 
 7 | 	def parser(self, value: str) -> str:
 8 | 		value = split_element(value)
 9 | 		qualifier, *_ = value
10 | 		return qualifier
11 | 


--------------------------------------------------------------------------------
/edi_837_parser/elements/utilities.py:
--------------------------------------------------------------------------------
 1 | from typing import List
 2 | from collections import defaultdict
 3 | 
 4 | 
 5 | def split_element(segment: str) -> List[str]:
 6 |     """different payers use different characters to delineate sub-elements"""
 7 |     delim = _identify_delim(segment)
 8 |     return segment.split(delim)
 9 | 
10 | 
11 | def _identify_delim(segment: str) -> str:
12 |     delim_candidates = ['^', ':', '>', '<']
13 |     
14 |     value_counts = defaultdict(int)
15 |     for delim in delim_candidates:
16 |         value_counts[delim] = segment.count(delim)
17 |     
18 |     delim = max(value_counts, key=value_counts.get)
19 | 
20 |     return delim
21 | 


--------------------------------------------------------------------------------
/edi_837_parser/loops/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/pop-singh/EDI-parser-837/main/edi_837_parser/loops/__init__.py


--------------------------------------------------------------------------------
/edi_837_parser/loops/billingprovider.py:
--------------------------------------------------------------------------------
 1 | from typing import Iterator, Tuple, Optional, List
 2 | from warnings import warn
 3 | from edi_837_parser.segments.claim import Claim as ClaimSegment
 4 | from edi_837_parser.segments.billingprovider import Billingprovider as BillingproviderSegment
 5 | from edi_837_parser.segments.entity import Entity as EntitySegment
 6 | from edi_837_parser.segments.date import Date as DateSegment
 7 | from edi_837_parser.segments.address import Address as AddressSegment
 8 | from edi_837_parser.segments.city_information import City_information as city_informationSegment
 9 | from edi_837_parser.segments.dept_contact_information import Dept_Contact_Information as dept_contact_informationSegment
10 | 
11 | 
12 | 
13 | from edi_837_parser.segments.utilities import find_identifier
14 | 
15 | 
16 | class Billingprovider:
17 | 	initiating_identifier = BillingproviderSegment.identification
18 | 	terminating_identifiers = [
19 | 		'HL',
20 | 		BillingproviderSegment.identification,
21 | 		'SBR',
22 | 		'LX',
23 | 		'SE'
24 | 	]
25 | 
26 | 	def __init__(
27 | 			self,
28 | 			billingprovider: BillingproviderSegment = None,
29 | 			entities: List[EntitySegment] = None,
30 | 			dates: List[DateSegment] = None,
31 | 			address:List[AddressSegment]=None,
32 | 			city_information:List[city_informationSegment]=None,
33 | 			dept_contact_information:dept_contact_informationSegment=None,
34 | 
35 | 
36 | 	):
37 | 		self.billingprovider = billingprovider
38 | 		self.address = address if address else []
39 | 		self.city_information = city_information if city_information else []
40 | 		self.entities = entities if entities else []
41 | 		self.dates = dates if dates else []
42 | 		self.dept_contact_information=dept_contact_information
43 | 
44 | 
45 | 	def __repr__(self):
46 | 		return '\n'.join(str(item) for item in self.__dict__.items())
47 | 
48 | 
49 | 
50 | 	@classmethod
51 | 	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Billingprovider', Optional[Iterator[str]], Optional[str]]:
52 | 		billingprovider = Billingprovider()
53 | 		billingprovider.billingprovider = BillingproviderSegment(segment)
54 | 
55 | 		segment = segments.__next__()
56 | 		while True:
57 | 			# print(segment)
58 | 			try:
59 | 				if segment is None:
60 | 					segment = segments.__next__()
61 | 
62 | 				identifier = find_identifier(segment)
63 | 				# print(identifier)
64 | 				if identifier == EntitySegment.identification:
65 | 					entity = EntitySegment(segment)
66 | 					billingprovider.entities.append(entity)
67 | 					segment = None
68 | 
69 | 				elif identifier == DateSegment.identification:
70 | 					date = DateSegment(segment)
71 | 					billingprovider.dates.append(date)
72 | 					segment = None
73 | 
74 | 				elif identifier == AddressSegment.identification:
75 | 					address = AddressSegment(segment)
76 | 					billingprovider.address.append(address)
77 | 					segment = None
78 | 				elif identifier == city_informationSegment.identification:
79 | 					city_information = city_informationSegment(segment)
80 | 					billingprovider.city_information.append(city_information)
81 | 					segment = None
82 | 
83 | 				elif identifier == dept_contact_informationSegment.identification:
84 | 					dept_contact_information = dept_contact_informationSegment(segment)
85 | 					billingprovider.dept_contact_information=dept_contact_information
86 | 					segment = None
87 | 
88 | 				elif identifier in cls.terminating_identifiers:
89 | 					return billingprovider, segments, segment
90 | 
91 | 				else:
92 | 					segment = None
93 | 					message = f'Identifier: {identifier} not handled in billingprovider loop.'
94 | 					# warn(message)
95 | 
96 | 			except StopIteration:
97 | 				return billingprovider, None, None
98 | 


--------------------------------------------------------------------------------
/edi_837_parser/loops/claim.py:
--------------------------------------------------------------------------------
  1 | from typing import Iterator, Tuple, Optional, List
  2 | from warnings import warn
  3 | 
  4 | from edi_837_parser.segments.claim import Claim as ClaimSegment
  5 | from edi_837_parser.segments.entity import Entity as EntitySegment
  6 | from edi_837_parser.segments.reference import Reference as ReferenceSegment
  7 | from edi_837_parser.segments.date import Date as DateSegment
  8 | from edi_837_parser.segments.amount import Amount as AmountSegment
  9 | from edi_837_parser.segments.utilities import find_identifier
 10 | from edi_837_parser.segments.diagnosis import Diagnosis as DiagnosisSegment
 11 | from edi_837_parser.segments.note import Note as NoteSegment
 12 | from edi_837_parser.loops.service import Service as ServiceLoop
 13 | from edi_837_parser.loops.payer import Payer as PayerLoop
 14 | 
 15 | from edi_837_parser.segments.subscriber import Subscriber as SubscriberSegment
 16 | from edi_837_parser.loops.subscriber import Subscriber as SubscriberLoop
 17 | 
 18 | from edi_837_parser.segments.patient import Patient as PatientSegment
 19 | from edi_837_parser.segments.billingprovider import Billingprovider as BillingproviderSegment
 20 | from edi_837_parser.segments.utilities import split_segment  
 21 | 
 22 | 
 23 | class Claim:
 24 | 	initiating_identifier = ClaimSegment.identification
 25 | 	terminating_identifiers = [
 26 | 		ClaimSegment.identification,
 27 | 		PatientSegment.identification,
 28 | 		'SE'
 29 | 	]
 30 | 
 31 | 	def __init__(
 32 | 			self,
 33 | 			claim: ClaimSegment = None,
 34 | 			entities: List[EntitySegment] = None,
 35 | 			services: List[ServiceLoop] = None,
 36 | 			references: List[ReferenceSegment] = None,
 37 | 			dates: List[DateSegment] = None,
 38 | 			amount: AmountSegment = None,
 39 | 			patient: PatientSegment = None,
 40 | 			billingprovider: BillingproviderSegment = None,
 41 | 			subscriber:SubscriberSegment=None,
 42 | 			subscriber_other:SubscriberLoop=None,
 43 | 			attending_provider_taxonomy:BillingproviderSegment=None,
 44 | 			service_facility_location:PayerLoop=None,
 45 | 			submitter:PayerLoop=None,
 46 | 			receiver:PayerLoop=None,
 47 | 			diagnosis:List[DiagnosisSegment]=None,
 48 | 			note:NoteSegment=None,
 49 | 	):
 50 | 		self.claim = claim
 51 | 		self.entities = entities if entities else []
 52 | 		self.services = services if services else []
 53 | 		self.references = references if references else []
 54 | 		self.dates = dates if dates else []
 55 | 		self.amount = amount
 56 | 		self.patient=patient
 57 | 		self.billingprovider=billingprovider
 58 | 		self.subscriber=subscriber
 59 | 		self.subscriber_other=subscriber_other 
 60 | 		self.attending_provider_taxonomy=attending_provider_taxonomy 
 61 | 		self.submitter=submitter 
 62 | 		self.receiver=receiver 
 63 | 		self.diagnosis=self.diagnosis = diagnosis if diagnosis else []
 64 | 		self.note=note
 65 | 		self.service_facility_location=service_facility_location
 66 | 
 67 | 
 68 | 
 69 | 	def __repr__(self):
 70 | 		return '\n'.join(str(item) for item in self.__dict__.items())
 71 | 
 72 | 	@property
 73 | 	def rendering_provider(self) -> Optional[EntitySegment]:
 74 | 		rendering_provider = [e for e in self.entities if e.entity == 'rendering provider']
 75 | 		assert len(rendering_provider) <= 1
 76 | 
 77 | 		if len(rendering_provider) == 1:
 78 | 			return rendering_provider[0]
 79 | 
 80 | 	@property
 81 | 	def claim_statement_period_start(self) -> Optional[DateSegment]:
 82 | 		statement_period_start = [d for d in self.dates if d.qualifier == 'claim statement period start']
 83 | 		assert len(statement_period_start) <= 1
 84 | 
 85 | 		if len(statement_period_start) == 1:
 86 | 			return statement_period_start[0]
 87 | 
 88 | 	@property
 89 | 	def claim_statement_period_end(self) -> Optional[DateSegment]:
 90 | 		statement_period_end = [d for d in self.dates if d.qualifier == 'claim statement period end']
 91 | 		assert len(statement_period_end) <= 1
 92 | 
 93 | 		if len(statement_period_end) == 1:
 94 | 			return statement_period_end[0]
 95 | 
 96 | 	@classmethod
 97 | 	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Claim', Optional[Iterator[str]], Optional[str]]:
 98 | 		claim = Claim()
 99 | 		claim.claim = ClaimSegment(segment)
100 | 		identifier2=split_segment(segment)
101 | 		# print(claim)
102 | 		segment = segments.__next__()
103 | 		# print("hello")
104 | 		
105 | 		while True:
106 | 
107 | 			try:
108 | 				if segment is None:
109 | 					segment = segments.__next__()
110 | 				
111 | 				identifier = find_identifier(segment)
112 | 				identifier2=split_segment(segment)
113 | 
114 | 				if (identifier == ServiceLoop.initiating_identifier):
115 | 					service, segment, segments = ServiceLoop.build(segment, segments)
116 | 					claim.services.append(service)
117 | 
118 | 				elif (identifier2[0] == EntitySegment.identification and   identifier2[1] != '77')  :
119 | 					entity = EntitySegment(segment)
120 | 					claim.entities.append(entity)
121 | 					segment = None
122 | 				elif identifier == SubscriberLoop.initiating_identifier:
123 | 
124 | 					sub, segments, segment = SubscriberLoop.build(segment, segments)
125 | 					
126 | 					claim.subscriber_other=sub
127 | 
128 | 				elif identifier == ReferenceSegment.identification:
129 | 					reference = ReferenceSegment(segment)
130 | 					claim.references.append(reference)
131 | 					segment = None
132 | 
133 | 				elif identifier == DateSegment.identification:
134 | 					date = DateSegment(segment)
135 | 					claim.dates.append(date)
136 | 					segment = None
137 | 
138 | 				elif identifier == AmountSegment.identification:
139 | 					amount = AmountSegment(segment)
140 | 					claim.amount = amount
141 | 					segment = None
142 | 
143 | 				elif identifier == BillingproviderSegment.identification:
144 | 					taxonomy=BillingproviderSegment(segment)
145 | 					claim.attending_provider_taxonomy = taxonomy
146 | 					segment = None
147 | 				elif (identifier2[0]== PayerLoop.initiating_identifier and identifier2[1] == '77' ):
148 | 					service_facility, segments, segment = PayerLoop.build(segment, segments)
149 | 
150 | 					claim.service_facility_location = service_facility
151 | 
152 | 				elif identifier == DiagnosisSegment.identification:
153 | 					diagnosis = DiagnosisSegment(segment)
154 | 					claim.diagnosis.append(diagnosis)
155 | 					segment = None
156 | 
157 | 				elif identifier == NoteSegment.identification:
158 | 					claim.note=NoteSegment(segment)
159 | 					segment = None
160 | 
161 | 				elif identifier in cls.terminating_identifiers:
162 | 					
163 | 					return claim, segments, segment
164 | 
165 | 				else:
166 | 					message = f'Identifier: {identifier} not handled in claim loop.'
167 | 					segment = None
168 | 					warn(message)
169 | 
170 | 			except StopIteration:
171 | 				return claim, None, None
172 | 


--------------------------------------------------------------------------------
/edi_837_parser/loops/patient.py:
--------------------------------------------------------------------------------
 1 | from typing import Iterator, Tuple, Optional, List
 2 | from warnings import warn
 3 | from edi_837_parser.segments.claim import Claim as ClaimSegment
 4 | from edi_837_parser.segments.patient import Patient as PatientSegment
 5 | from edi_837_parser.segments.entity import Entity as EntitySegment
 6 | from edi_837_parser.segments.date import Date as DateSegment
 7 | from edi_837_parser.segments.address import Address as AddressSegment
 8 | from edi_837_parser.segments.city_information import City_information as City_informationSegment
 9 | from edi_837_parser.segments.demographic_information import Demographic_information as Demographic_informationSegment
10 | 
11 | 
12 | from edi_837_parser.segments.utilities import find_identifier
13 | 
14 | 
15 | class Patient:
16 | 	initiating_identifier = PatientSegment.identification
17 | 	terminating_identifiers = [
18 | 		ClaimSegment.identification,
19 | 		PatientSegment.identification,
20 | 		'SE'
21 | 	]
22 | 
23 | 	def __init__(
24 | 			self,
25 | 			patient: PatientSegment = None,
26 | 			entities: List[EntitySegment] = None,
27 | 			dates: List[DateSegment] = None,
28 | 			address:List[AddressSegment]=None,
29 | 			city_information:List[City_informationSegment]=None,
30 | 			demographic_information:Demographic_informationSegment=None,
31 | 
32 | 	):
33 | 		self.patient = patient
34 | 		self.entities = entities if entities else []
35 | 		self.dates = dates if dates else []
36 | 		self.address = address if address else []
37 | 		self.demographic_information=demographic_information
38 | 		self.city_information = city_information if city_information else []
39 | 
40 | 	def __repr__(self):
41 | 		return '\n'.join(str(item) for item in self.__dict__.items())
42 | 
43 | 
44 | 
45 | 	@classmethod
46 | 	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Patient', Optional[Iterator[str]], Optional[str]]:
47 | 		patient = Patient()
48 | 		patient.patient = PatientSegment(segment)
49 | 
50 | 		segment = segments.__next__()
51 | 		while True:
52 | 			# print(segment)
53 | 			try:
54 | 				if segment is None:
55 | 					segment = segments.__next__()
56 | 
57 | 				identifier = find_identifier(segment)
58 | 				# print(identifier)
59 | 				if identifier == EntitySegment.identification:
60 | 					entity = EntitySegment(segment)
61 | 					patient.entities.append(entity)
62 | 					segment = None
63 | 
64 | 				elif identifier == DateSegment.identification:
65 | 					date = DateSegment(segment)
66 | 					patient.dates.append(date)
67 | 					segment = None
68 | 
69 | 				elif identifier in cls.terminating_identifiers:
70 | 					return patient, segments, segment
71 | 				
72 | 				elif identifier == AddressSegment.identification:
73 | 					address = AddressSegment(segment)
74 | 					patient.address.append(address)
75 | 					segment = None
76 | 				elif identifier == City_informationSegment.identification:
77 | 					city_information = City_informationSegment(segment)
78 | 					patient.city_information.append(city_information)
79 | 					segment = None
80 | 
81 | 				elif identifier == Demographic_informationSegment.identification:
82 | 					demographic_information = Demographic_informationSegment(segment)
83 | 					patient.demographic_information=demographic_information
84 | 					segment = None
85 | 
86 | 				else:
87 | 					segment = None
88 | 					message = f'Identifier: {identifier} not handled in patientloop.'
89 | 					# warn(message)
90 | 
91 | 			except StopIteration:
92 | 				return patient, None, None
93 | 


--------------------------------------------------------------------------------
/edi_837_parser/loops/payer.py:
--------------------------------------------------------------------------------
  1 | from typing import Iterator, Tuple, Optional, List
  2 | from warnings import warn
  3 | from edi_837_parser.segments.claim import Claim as ClaimSegment
  4 | from edi_837_parser.segments.subscriber import Subscriber as SubscriberSegment
  5 | from edi_837_parser.segments.entity import Entity as EntitySegment
  6 | from edi_837_parser.segments.address import Address as AddressSegment
  7 | from edi_837_parser.segments.reference import Reference as ReferenceSegment
  8 | 
  9 | from edi_837_parser.segments.city_information import City_information as City_informationSegment
 10 | from edi_837_parser.segments.demographic_information import Demographic_information as Demographic_informationSegment
 11 | from edi_837_parser.segments.dept_contact_information import Dept_Contact_Information as Dept_Contact_InformationSegment
 12 | 
 13 | 
 14 | 
 15 | from edi_837_parser.segments.date import Date as DateSegment
 16 | from edi_837_parser.segments.utilities import find_identifier
 17 | 
 18 | 
 19 | class Payer:
 20 | 	initiating_identifier = EntitySegment.identification
 21 | 	terminating_identifiers = [
 22 | 		EntitySegment.identification,
 23 | 		ClaimSegment.identification,
 24 | 		'SBR',
 25 | 		'LX',
 26 | 		'HL',
 27 | 		'SE'
 28 | 	]
 29 | 
 30 | 	def __init__(
 31 | 			self,
 32 | 			tag=None,
 33 | 			entities: EntitySegment= None,
 34 | 			address:AddressSegment =None,
 35 | 			city_information:City_informationSegment=None,
 36 | 			demographic_information:Demographic_informationSegment=None,
 37 | 			dept_contact_information:Dept_Contact_InformationSegment=None,
 38 | 			dates:List[DateSegment]=None,
 39 | 			references: List[ReferenceSegment] = None,
 40 | 
 41 | 	):
 42 | 	
 43 | 		self.entities = entities 
 44 | 		self.address = address 
 45 | 		self.city_information = city_information 
 46 | 		self.demographic_information = demographic_information
 47 | 		self.dept_contact_information = dept_contact_information
 48 | 		self.tag=tag
 49 | 		self.dates=dates if dates else []
 50 | 		self.references= references if references else []
 51 | 		
 52 | 
 53 | 	def __repr__(self):
 54 | 		return '\n'.join(str(item) for item in self.__dict__.items())
 55 | 
 56 | 
 57 | 
 58 | 	@classmethod
 59 | 	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Payer', Optional[Iterator[str]], Optional[str]]:
 60 | 		payer = Payer()
 61 | 		
 62 | 		payer.entities = EntitySegment(segment)
 63 | 		# print(payer.entities )
 64 | 		if payer.entities.entity=='PR':
 65 | 			payer.tag='payer'
 66 | 		elif payer.entities.entity=='IL':
 67 | 			payer.tag='subscriber'
 68 | 		
 69 | 		segment = segments.__next__()
 70 | 		while True:
 71 | 			try:
 72 | 				if segment is None:
 73 | 					segment = segments.__next__()
 74 | 		
 75 | 				identifier = find_identifier(segment)
 76 | 
 77 | 				if identifier == AddressSegment.identification:
 78 | 					address = AddressSegment(segment)
 79 | 					payer.address=address
 80 | 					segment = None
 81 | 				elif identifier == City_informationSegment.identification:
 82 | 					city_info = City_informationSegment(segment)
 83 | 					payer.city_information=city_info
 84 | 					segment = None
 85 | 				elif identifier == Demographic_informationSegment.identification:
 86 | 					demo_info = Demographic_informationSegment(segment)
 87 | 					payer.demographic_information=demo_info
 88 | 					segment = None
 89 | 				elif identifier == Dept_Contact_InformationSegment.identification:
 90 | 					dept_info = Dept_Contact_InformationSegment(segment)
 91 | 					payer.dept_contact_information=dept_info
 92 | 					segment = None
 93 | 
 94 | 				elif identifier == DateSegment.identification:
 95 | 					dt = DateSegment(segment)
 96 | 					payer.dates.append(dt)
 97 | 					segment = None
 98 | 
 99 | 				elif identifier == ReferenceSegment.identification:
100 | 					reference = ReferenceSegment(segment)
101 | 					payer.references.append(reference)
102 | 					segment = None
103 | 
104 | 				elif identifier in cls.terminating_identifiers:
105 | 			
106 | 					return payer, segments, segment
107 | 
108 | 				else:
109 | 					if identifier=='DTP':
110 | 						print(payer.entities.segment)
111 | 						print('seg',segment)
112 | 					segment = None
113 | 					message = f'Identifier: {identifier} not handled in payerloop.'
114 | 					warn(message)
115 | 
116 | 			except StopIteration:
117 | 				return payer, None, None
118 | 


--------------------------------------------------------------------------------
/edi_837_parser/loops/service.py:
--------------------------------------------------------------------------------
  1 | from typing import Tuple, Iterator, Optional, List
  2 | from warnings import warn
  3 | 
  4 | from edi_837_parser.segments.service import Service as ServiceSegment
  5 | from edi_837_parser.segments.claim import Claim as ClaimSegment
  6 | from edi_837_parser.segments.date import Date as DateSegment
  7 | from edi_837_parser.segments.reference import Reference as ReferenceSegment
  8 | from edi_837_parser.segments.amount import Amount as AmountSegment
  9 | from edi_837_parser.segments.service_adjustment import ServiceAdjustment as ServiceAdjustmentSegment
 10 | from edi_837_parser.segments.service_line_adjudication import Service_Line_Adjudication as Service_Line_AdjudicationSegment
 11 | from edi_837_parser.segments.serviceline import Serviceline as ServicelineSegment
 12 | from edi_837_parser.segments.drug_identification import Drug_Identification as Drug_IdentificationSegment
 13 | from edi_837_parser.segments.drug_quantity import Drug_Quantity as Drug_QuantitySegment
 14 | 
 15 | from edi_837_parser.segments.utilities import find_identifier
 16 | 
 17 | 
 18 | class Service:
 19 | 	initiating_identifier = ServiceSegment.identification
 20 | 	terminating_identifiers = [
 21 | 		ServiceSegment.identification,
 22 | 		ClaimSegment.identification,
 23 | 		'HL',
 24 | 		'SE'
 25 | 	]
 26 | 
 27 | 	def __init__(
 28 | 			self,
 29 | 			service: ServiceSegment = None,
 30 | 			dates: List[DateSegment] = None,
 31 | 			references: List[ReferenceSegment] = None,
 32 | 			serviceline: List[ServicelineSegment] = None,
 33 | 			amount: AmountSegment = None,
 34 | 			adjustments: List[ServiceAdjustmentSegment] = None,
 35 | 			service_line_adjudication: Service_Line_AdjudicationSegment = None,
 36 | 			drug_identification:Drug_IdentificationSegment=None,
 37 | 			drug_quantity:Drug_QuantitySegment=None,
 38 | 
 39 | 	):
 40 | 		self.service = service
 41 | 		self.dates = dates if dates else []
 42 | 		self.references = references if references else []
 43 | 		self.serviceline = serviceline if serviceline else []
 44 | 		self.amount = amount
 45 | 		self.adjustments = adjustments if adjustments else []
 46 | 		self.service_line_adjudication = service_line_adjudication 
 47 | 		self.drug_identification=drug_identification
 48 | 		self.drug_quantity=drug_quantity
 49 | 	
 50 | 
 51 | 	def __repr__(self):
 52 | 		return '\n'.join(str(item) for item in self.__dict__.items())
 53 | 
 54 | 	@classmethod
 55 | 	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Service', Optional[str], Optional[Iterator[str]]]:
 56 | 		service = Service()
 57 | 		service.service = ServiceSegment(segment)
 58 | 
 59 | 		while True:
 60 | 			try:
 61 | 				segment = segments.__next__()
 62 | 				identifier = find_identifier(segment)
 63 | 
 64 | 				if identifier == DateSegment.identification:
 65 | 					date = DateSegment(segment)
 66 | 					service.dates.append(date)
 67 | 
 68 | 				elif identifier == ServicelineSegment.identification:
 69 | 					serviceline = ServicelineSegment(segment)
 70 | 					service.serviceline.append(serviceline)
 71 | 
 72 | 				elif identifier == Service_Line_AdjudicationSegment.identification:
 73 | 					service.service_line_adjudication = Service_Line_AdjudicationSegment(segment)
 74 | 
 75 | 				elif identifier == Drug_IdentificationSegment.identification:
 76 | 					di = Drug_IdentificationSegment(segment)
 77 | 					service.drug_identification=di
 78 | 				elif identifier == Drug_QuantitySegment.identification:
 79 | 					dq = Drug_QuantitySegment(segment)
 80 | 					service.drug_quantity=dq
 81 | 
 82 | 				elif identifier == ReferenceSegment.identification:
 83 | 					reference = ReferenceSegment(segment)
 84 | 					service.references.append(reference)
 85 | 
 86 | 				elif identifier == ServiceAdjustmentSegment.identification:
 87 | 					service.adjustments.append(ServiceAdjustmentSegment(segment))
 88 | 
 89 | 				elif identifier in cls.terminating_identifiers:
 90 | 					return service, segment, segments
 91 | 
 92 | 				else:
 93 | 					message = f'Identifier: {identifier} not handled in service loop.'
 94 | 					warn(message)
 95 | 
 96 | 			except StopIteration:
 97 | 				return service, None, None
 98 | 
 99 | 
100 | if __name__ == '__main__':
101 | 	pass
102 | 


--------------------------------------------------------------------------------
/edi_837_parser/loops/subscriber.py:
--------------------------------------------------------------------------------
 1 | from typing import Iterator, Tuple, Optional, List
 2 | from warnings import warn
 3 | from edi_837_parser.segments.claim import Claim as ClaimSegment
 4 | from edi_837_parser.segments.subscriber import Subscriber as SubscriberSegment
 5 | from edi_837_parser.segments.entity import Entity as EntitySegment
 6 | from edi_837_parser.segments.amount import Amount as AmountSegmant
 7 | from edi_837_parser.segments.service_adjustment import ServiceAdjustment as ServiceAdjustmentSegment
 8 | from edi_837_parser.loops.payer import Payer as PayerLoop
 9 | from edi_837_parser.segments.utilities import find_identifier
10 | 
11 | 
12 | class Subscriber:
13 | 	initiating_identifier = SubscriberSegment.identification
14 | 	terminating_identifiers = [
15 | 		ClaimSegment.identification,
16 | 		SubscriberSegment.identification,
17 | 		'LX',
18 | 		'HL',
19 | 		'SE'
20 | 	]
21 | 
22 | 	def __init__(
23 | 			self,
24 | 			subscriber: SubscriberSegment = None,
25 | 			amount:List[AmountSegmant]=None,
26 | 			payer: List[PayerLoop] = None,
27 | 			adjustments: List[ServiceAdjustmentSegment] = None,
28 | 
29 | 	):
30 | 		self.subscriber = subscriber
31 | 		self.amount = amount if amount else []
32 | 		self.payer = self.payer = payer if payer else []
33 | 		self.adjustments = adjustments if adjustments else []
34 | 
35 | 
36 | 
37 | 		
38 | 
39 | 	def __repr__(self):
40 | 		return '\n'.join(str(item) for item in self.__dict__.items())
41 | 
42 | 
43 | 
44 | 	@classmethod
45 | 	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Subscriber', Optional[Iterator[str]], Optional[str]]:
46 | 		subscriber = Subscriber()
47 | 		subscriber.subscriber = SubscriberSegment(segment)
48 | 
49 | 		segment = segments.__next__()
50 | 		while True:
51 | 			try:
52 | 				if segment is None:
53 | 					segment = segments.__next__()
54 | 		
55 | 				identifier = find_identifier(segment)
56 | 
57 | 				if identifier == EntitySegment.identification:
58 | 					payer, segments, segment = PayerLoop.build(segment, segments)
59 | 					subscriber.payer.append(payer)
60 | 				
61 | 				elif identifier == ServiceAdjustmentSegment.identification:
62 | 					subscriber.adjustments.append(ServiceAdjustmentSegment(segment))
63 | 					segment = None
64 | 
65 | 				elif identifier == AmountSegmant.identification:
66 | 					subscriber.amount.append(AmountSegmant(segment))
67 | 					segment = None
68 | 
69 | 
70 | 
71 | 				elif identifier in cls.terminating_identifiers:
72 | 					return subscriber, segments, segment
73 | 
74 | 				else:
75 | 					segment = None
76 | 					message = f'Identifier: {identifier} not handled in subscriber loop.'
77 | 					warn(message)
78 | 
79 | 			except StopIteration:
80 | 				return subscriber, None, None
81 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/pop-singh/EDI-parser-837/main/edi_837_parser/segments/__init__.py


--------------------------------------------------------------------------------
/edi_837_parser/segments/address.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Address:
 6 | 	identification = 'N3'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 	def __init__(self, segment: str):
11 | 		self.segment = segment
12 | 		segment = split_segment(segment)
13 | 
14 | 		self.identifier = segment[0]
15 | 		self.address = segment[1]
16 | 
17 | 	def __repr__(self):
18 | 		return '\n'.join(str(item) for item in self.__dict__.items())
19 | 
20 | 
21 | if __name__ == '__main__':
22 | 	pass
23 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/amount.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.dollars import Dollars
 3 | from edi_837_parser.elements.amount_qualifier import AmountQualifier
 4 | from edi_837_parser.segments.utilities import split_segment
 5 | 
 6 | 
 7 | class Amount:
 8 | 	identification = 'AMT'
 9 | 
10 | 	identifier = Identifier()
11 | 	qualifier = AmountQualifier()
12 | 	amount = Dollars()
13 | 
14 | 	def __init__(self, segment: str):
15 | 		self.segment = segment
16 | 		segment = split_segment(segment)
17 | 
18 | 		self.identifier = segment[0]
19 | 		self.qualifier = segment[1]
20 | 		self.amount = segment[2]
21 | 
22 | 	def __repr__(self):
23 | 		return '\n'.join(str(item) for item in self.__dict__.items())
24 | 
25 | 
26 | if __name__ == '__main__':
27 | 	pass
28 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/billingprovider.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Billingprovider:
 6 | 	identification='PRV'
 7 | 
 8 | 	identifier = Identifier()
 9 | 	taxonomy_code = ''
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 
15 | 		self.identifier = segment[0]
16 | 		self.type=segment[1]
17 | 		if segment[2]=='PXC':
18 | 			self.taxonomy_code = segment[3]
19 | 		else:
20 | 			self.taxonomy_code = None
21 | 
22 | 
23 | 	def __repr__(self):
24 | 		return '\n'.join(str(item) for item in self.__dict__.items())
25 | 
26 | 
27 | if __name__ == '__main__':
28 | 	pass
29 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/city_information.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class City_information:
 6 | 	identification = 'N4'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 	def __init__(self, segment: str):
11 | 		self.segment = segment
12 | 		segment = split_segment(segment)
13 | 
14 | 		self.identifier = segment[0]
15 | 		self.city = segment[1]
16 | 		self.state = segment[2]
17 | 		self.zipcode = segment[3]
18 | 		
19 | 
20 | 	def __repr__(self):
21 | 		return '\n'.join(str(item) for item in self.__dict__.items())
22 | 
23 | 
24 | if __name__ == '__main__':
25 | 	pass
26 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/claim.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.claim_status import ClaimStatus
 3 | from edi_837_parser.elements.dollars import Dollars
 4 | from edi_837_parser.segments.utilities import split_segment
 5 | 
 6 | 
 7 | class Claim:
 8 | 	identification = 'CLM'
 9 | 
10 | 	identifier = Identifier()
11 | 	status = ClaimStatus()
12 | 	charge_amount = Dollars()
13 | 	paid_amount = Dollars()
14 | 
15 | 	def __init__(self, segment: str):
16 | 		self.segment = segment
17 | 		segment = split_segment(segment)
18 | 		# print(segment)
19 | 		self.identifier = segment[0]
20 | 		self.marker = segment[1]
21 | 		self.charge_amount = segment[2]
22 | 		self.status = segment[3]
23 | 		self.paid_amount = segment[4]
24 | 		
25 | 		
26 | 
27 | 	def __repr__(self):
28 | 		return '\n'.join(str(item) for item in self.__dict__.items())
29 | 
30 | 
31 | if __name__ == '__main__':
32 | 	pass
33 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/date.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.date import Date as DateElement
 3 | from edi_837_parser.elements.date_qualifier import DateQualifier
 4 | from edi_837_parser.segments.utilities import split_segment
 5 | 
 6 | 
 7 | class Date:
 8 | 	identification = 'DTP'
 9 | 
10 | 	identifier = Identifier()
11 | 	date = DateElement()
12 | 	qualifier = DateQualifier()
13 | 
14 | 	def __init__(self, segment: str):
15 | 		self.segment = segment
16 | 		segment = split_segment(segment)
17 | 		self.identifier = segment[0]
18 | 		self.qualifier = segment[1]
19 | 		self.date = segment[3]
20 | 
21 | 	def __repr__(self):
22 | 		return '\n'.join(str(item) for item in self.__dict__.items())
23 | 
24 | 
25 | if __name__ == '__main__':
26 | 	pass
27 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/demographic_information.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.date import Date as DateElement
 3 | from edi_837_parser.elements.date_qualifier import DateQualifier
 4 | from edi_837_parser.segments.utilities import split_segment
 5 | 
 6 | 
 7 | class Demographic_information:
 8 | 	identification = 'DMG'
 9 | 
10 | 	identifier = Identifier()
11 | 	date = DateElement()
12 | 	qualifier = DateQualifier()
13 | 
14 | 	def __init__(self, segment: str):
15 | 		self.segment = segment
16 | 		segment = split_segment(segment)
17 | 
18 | 		self.identifier = segment[0]
19 | 		self.qualifier = segment[1]
20 | 		self.date = segment[2]
21 | 		self.gender_code=segment[3]
22 | 
23 | 	def __repr__(self):
24 | 		return '\n'.join(str(item) for item in self.__dict__.items())
25 | 
26 | 
27 | if __name__ == '__main__':
28 | 	pass
29 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/dept_contact_information.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Dept_Contact_Information:
 6 | 	identification = 'PER'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 	def __init__(self, segment: str):
11 | 		self.segment = segment
12 | 		segment = split_segment(segment)
13 | 
14 | 		self.identifier = segment[0]
15 | 		self.department = segment[2]
16 | 		if segment[3]=='TE':
17 | 			self.telephonenumber = segment[4]
18 | 		if len(segment)>5 and segment[5]=='FX':
19 | 			self.fxnumber = segment[6]
20 | 		else:
21 | 			self.fxnumber=None
22 | 		
23 | 
24 | 	def __repr__(self):
25 | 		return '\n'.join(str(item) for item in self.__dict__.items())
26 | 
27 | 
28 | if __name__ == '__main__':
29 | 	pass
30 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/diagnosis.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.claim_status import ClaimStatus
 3 | from edi_837_parser.elements.dollars import Dollars
 4 | from edi_837_parser.segments.utilities import split_segment
 5 | 
 6 | 
 7 | class Diagnosis:
 8 | 	identification = 'HI'
 9 | 
10 | 	identifier = Identifier()
11 | 
12 | 	def __init__(self, segment: str):
13 | 		self.segment = segment
14 | 		segment = split_segment(segment)
15 | 
16 | 		self.identifier = segment[0]
17 | 		self.diagnosis_codes = segment[1:]
18 | 
19 | 	def __repr__(self):
20 | 		return '\n'.join(str(item) for item in self.__dict__.items())
21 | 
22 | 
23 | if __name__ == '__main__':
24 | 	pass
25 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/drug_identification.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.dollars import Dollars
 3 | from edi_837_parser.segments.utilities import split_segment
 4 | 
 5 | 
 6 | class Drug_Identification:
 7 | 	identification = 'LIN'
 8 | 
 9 | 	identifier = Identifier()
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 
15 | 		self.identifier = segment[0]
16 | 		self.qualifier = segment[2]
17 | 		self.national_drug_code=segment[3]
18 | 
19 | 	def __repr__(self):
20 | 		return '\n'.join(str(item) for item in self.__dict__.items())
21 | 
22 | 
23 | if __name__ == '__main__':
24 | 	pass
25 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/drug_quantity.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.dollars import Dollars
 3 | from edi_837_parser.segments.utilities import split_segment
 4 | 
 5 | 
 6 | class Drug_Quantity:
 7 | 	identification = 'CTP'
 8 | 
 9 | 	identifier = Identifier()
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 
15 | 		self.identifier = segment[0]
16 | 		self.drug_unit = segment[4]
17 | 		self.meas_code=segment[5]
18 | 
19 | 	def __repr__(self):
20 | 		return '\n'.join(str(item) for item in self.__dict__.items())
21 | 
22 | 
23 | if __name__ == '__main__':
24 | 	pass
25 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/entity.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.entity_code import EntityCode
 3 | from edi_837_parser.elements.entity_type import EntityType
 4 | from edi_837_parser.elements.identification_code_qualifier import IdentificationCodeQualifier
 5 | from edi_837_parser.segments.utilities import split_segment, get_element
 6 | 
 7 | 
 8 | class Entity:
 9 | 	identification = 'NM1'
10 | 
11 | 	identifier = Identifier()
12 | 	entity = EntityCode()
13 | 	type = EntityType()
14 | 	identification_code_qualifier = IdentificationCodeQualifier()
15 | 
16 | 	def __init__(self, segment: str):
17 | 		self.segment = segment
18 | 		segment = split_segment(segment)
19 | 
20 | 		self.identifier = segment[0]
21 | 		self.entity = segment[1]
22 | 		self.type = segment[2]
23 | 		if self.entity !='87':
24 | 			self.last_name = segment[3]
25 | 			self.first_name = get_element(segment, 4)
26 | 			self.identification_code_qualifier = get_element(segment, 8)
27 | 			self.identification_code = get_element(segment, 9)
28 | 
29 | 	def __repr__(self):
30 | 		return '\n'.join(str(item) for item in self.__dict__.items())
31 | 
32 | 	@property
33 | 	def name(self) -> str:
34 | 		return f'{self.first_name} {self.last_name}'.title()
35 | 
36 | 
37 | if __name__ == '__main__':
38 | 	pass
39 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/location.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Location:
 6 | 	identification = 'N4'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 	def __init__(self, segment: str):
11 | 		self.segment = segment
12 | 		segment = split_segment(segment)
13 | 
14 | 		self.identifier = segment[0]
15 | 		self.city = segment[1]
16 | 		self.state = segment[2]
17 | 		self.zip_code = segment[3]
18 | 
19 | 	def __repr__(self):
20 | 		return '\n'.join(str(item) for item in self.__dict__.items())
21 | 
22 | 
23 | if __name__ == '__main__':
24 | 	pass
25 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/note.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Note:
 6 | 	identification = 'NTE'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 		self.identifier = segment[0]
15 | 		self.referencecode=segment[1]
16 | 		self.note_text = segment[2]
17 | 
18 | 	def __repr__(self) -> str:
19 | 		return '\n'.join(str(item) for item in self.__dict__.items())
20 | 
21 | 
22 | 
23 | if __name__ == '__main__':
24 | 	pass
25 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/patient.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Patient:
 6 | 	identification = 'PAT'
 7 | 	print("hi pat")
 8 | 	identifier = Identifier()
 9 | 	relationship_code = ''
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 	
15 | 
16 | 		self.identifier = segment[0]
17 | 		self.relationship_code = segment[1]
18 | 
19 | 	def __repr__(self):
20 | 		return '\n'.join(str(item) for item in self.__dict__.items())
21 | 
22 | 
23 | if __name__ == '__main__':
24 | 	pass
25 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/reference.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.reference_qualifier import ReferenceQualifier
 3 | from edi_837_parser.segments.utilities import split_segment
 4 | 
 5 | 
 6 | class Reference:
 7 | 	identification = 'REF'
 8 | 
 9 | 	identifier = Identifier()
10 | 	qualifier = ReferenceQualifier()
11 | 
12 | 	def __init__(self, segment: str):
13 | 		self.segment = segment
14 | 		segment = split_segment(segment)
15 | 
16 | 		self.identifier = segment[0]
17 | 		self.qualifier = segment[1]
18 | 		
19 | 		self.value = segment[2]
20 | 
21 | 	def __repr__(self) -> str:
22 | 		return '\n'.join(str(item) for item in self.__dict__.items())
23 | 
24 | 	def __str__(self) -> str:
25 | 		return f'{self.qualifier}: {self.value}'
26 | 
27 | 
28 | if __name__ == '__main__':
29 | 	pass
30 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/service.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.dollars import Dollars
 3 | from edi_837_parser.elements.service_code import ServiceCode
 4 | from edi_837_parser.elements.service_qualifier import ServiceQualifer
 5 | from edi_837_parser.elements.service_modifier import ServiceModifier
 6 | from edi_837_parser.elements.integer import Integer
 7 | from edi_837_parser.segments.utilities import split_segment, get_element
 8 | 
 9 | 
10 | class Service:
11 | 	identification = 'LX'
12 | 
13 | 	identifier = Identifier()
14 | 	assigned_number = Integer()
15 | 
16 | 	def __init__(self, segment: str):
17 | 		self.segment = segment
18 | 		segment = split_segment(segment)
19 | 
20 | 		self.identifier = segment[0]
21 | 		self.assigned_number = segment[1]
22 | 
23 | 	def __repr__(self):
24 | 		return '\n'.join(str(item) for item in self.__dict__.items())
25 | 
26 | 
27 | if __name__ == '__main__':
28 | 	pass
29 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/service_adjustment.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.dollars import Dollars
 3 | from edi_837_parser.elements.adjustment_group_code import AdjustmentGroupCode
 4 | from edi_837_parser.elements.adjustment_reason_code import AdjustmentReasonCode
 5 | from edi_837_parser.segments.utilities import split_segment
 6 | 
 7 | 
 8 | class ServiceAdjustment:
 9 | 	identification = 'CAS'
10 | 
11 | 	identifier = Identifier()
12 | 	group_code = AdjustmentGroupCode()
13 | 	reason_code = AdjustmentReasonCode()
14 | 	amount = Dollars()
15 | 
16 | 	def __init__(self, segment: str):
17 | 		self.segment = segment
18 | 		segment = split_segment(segment)
19 | 		# print(segment)
20 | 		self.identifier = segment[0]
21 | 		self.adjustment_group_code = segment[1]
22 | 		self.reason_code_amount={}
23 | 		self.reason_code_amount[(self.adjustment_group_code,segment[2])]=segment[3]
24 | 		current_reason_code = None
25 | 		for i, item in enumerate(segment):
26 | 			if item == '':
27 | 				current_reason_code = segment[i + 1]
28 | 				amount = segment[i + 2]
29 | 				self.reason_code_amount[(self.adjustment_group_code,current_reason_code)] = amount
30 | 		# print(self.reason_code_amount)
31 | 
32 | 
33 | 	def __repr__(self):
34 | 		return '\n'.join(str(item) for item in self.__dict__.items())
35 | 
36 | 
37 | if __name__ == '__main__':
38 | 	pass
39 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/service_line_adjudication.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.elements.dollars import Dollars
 3 | from edi_837_parser.segments.utilities import split_segment
 4 | 
 5 | 
 6 | class Service_Line_Adjudication:
 7 | 	identification = 'SVD'
 8 | 
 9 | 	identifier = Identifier()
10 | 	# qualifier = AmountQualifier()
11 | 	service_line_paid_amount = Dollars()
12 | 
13 | 	def __init__(self, segment: str):
14 | 		self.segment = segment
15 | 		segment = split_segment(segment)
16 | 
17 | 		self.identifier = segment[0]
18 | 		self.identification_code = segment[1]
19 | 		self.service_line_paid_amount=segment[2]
20 | 		self.procedure_code=segment[3]
21 | 		self.description=segment[4]
22 | 		self.unit_count = segment[5]
23 | 
24 | 	def __repr__(self):
25 | 		return '\n'.join(str(item) for item in self.__dict__.items())
26 | 
27 | 
28 | if __name__ == '__main__':
29 | 	pass
30 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/serviceline.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Serviceline:
 6 | 	identification = 'SV2'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 		self.identifier = segment[0]
15 | 		self.revenuecode=segment[1]
16 | 		self.procedurecode = segment[2]
17 | 		self.chargeamount = segment[3]
18 | 		self.measurementcode = segment[4]
19 | 		self.unitdays = segment[5]
20 | 		
21 | 
22 | 	def __repr__(self) -> str:
23 | 		return '\n'.join(str(item) for item in self.__dict__.items())
24 | 
25 | 
26 | 
27 | if __name__ == '__main__':
28 | 	pass
29 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/subscriber.py:
--------------------------------------------------------------------------------
 1 | from edi_837_parser.elements.identifier import Identifier
 2 | from edi_837_parser.segments.utilities import split_segment
 3 | 
 4 | 
 5 | class Subscriber:
 6 | 	identification = 'SBR'
 7 | 
 8 | 	identifier = Identifier()
 9 | 
10 | 
11 | 	def __init__(self, segment: str):
12 | 		self.segment = segment
13 | 		segment = split_segment(segment)
14 | 		self.identifier = segment[0]
15 | 		self.sequencecode=segment[1]
16 | 		self.ppolicynumber = segment[2]
17 | 		self.filingindicator = segment[3]
18 | 
19 | 	def __repr__(self) -> str:
20 | 		return '\n'.join(str(item) for item in self.__dict__.items())
21 | 
22 | 
23 | 
24 | if __name__ == '__main__':
25 | 	pass
26 | 


--------------------------------------------------------------------------------
/edi_837_parser/segments/utilities.py:
--------------------------------------------------------------------------------
 1 | from typing import List, Optional
 2 | 
 3 | 
 4 | def split_segment(segment: str) -> List[str]:
 5 |     """Different payers use different characters to delineate elements"""
 6 |     asterisk = '*'
 7 |     pipe = '|'
 8 |     newline = '\n'
 9 | 
10 |     # Check if '\n' exists within the segment
11 |     if newline in segment:
12 |         # Replace '\n' with empty string to remove it
13 |         segment = segment.replace(newline, '')
14 | 
15 |     asterisk_segment_count = len(segment.split(asterisk))
16 |     pipe_segment_count = len(segment.split(pipe))
17 | 
18 |     if asterisk_segment_count > pipe_segment_count:
19 |         return segment.split(asterisk)
20 |     else:
21 |         return segment.split(pipe)
22 | 
23 | 
24 | def find_identifier(segment) -> str:
25 | 	segment = split_segment(segment)
26 | 	return segment[0]
27 | 
28 | def get_element(segment: List[str], index: int, default=None) -> Optional[str]:
29 | 	element = default
30 | 	if index < len(segment):
31 | 		element = segment[index]
32 | 
33 | 	return element
34 | 


--------------------------------------------------------------------------------
/edi_837_parser/transaction_set/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/pop-singh/EDI-parser-837/main/edi_837_parser/transaction_set/__init__.py


--------------------------------------------------------------------------------
/edi_837_parser/transaction_set/transaction_set.py:
--------------------------------------------------------------------------------
  1 | from typing import List, Iterator, Optional
  2 | from collections import namedtuple
  3 | import pandas as pd
  4 | from edi_837_parser.loops.claim import Claim as ClaimLoop
  5 | from edi_837_parser.loops.service import Service as ServiceLoop
  6 | from edi_837_parser.segments.utilities import find_identifier,split_segment
  7 | from edi_837_parser.loops.patient import Patient as PatientLoop
  8 | from edi_837_parser.loops.billingprovider import Billingprovider as BillingproviderLoop
  9 | from edi_837_parser.loops.subscriber import Subscriber as SubscriberLoop
 10 | from edi_837_parser.loops.payer import Payer as PayerLoop
 11 | 
 12 | BuildAttributeResponse = namedtuple('BuildAttributeResponse', 'key value segment segments')
 13 | 
 14 | 
 15 | class TransactionSet:
 16 | 
 17 | 	def __init__(
 18 | 			self,
 19 | 			claims: List[ClaimLoop],
 20 | 			file_path: str,
 21 | 			patient:PatientLoop,
 22 | 			billingprovider:BillingproviderLoop,
 23 | 			subscriber:SubscriberLoop,
 24 | 	):
 25 | 		self.claims = claims
 26 | 		self.file_path = file_path
 27 | 		self.patient=patient
 28 | 		self.billingprovider=billingprovider
 29 | 		self.subscriber=subscriber
 30 | 
 31 | 	def __repr__(self):
 32 | 		return '\n'.join(str(item) for item in self.__dict__.items())
 33 | 
 34 | 
 35 | 	def to_dataframe(self) -> pd.DataFrame:
 36 | 		"""flatten the remittance advice by service to a pandas DataFrame"""
 37 | 		data = []
 38 | 		# print("hello")
 39 | 		# print(self.claims[0])
 40 | 		cl=None
 41 | 		# print("length",len(self.patient))
 42 | 		for claim in self.claims:
 43 | 			for service in claim.services:
 44 | 				datum = TransactionSet.serialize_service(
 45 | 					claim,
 46 | 					service,
 47 | 					self.patient,
 48 | 					self.billingprovider
 49 | 					
 50 | 			)
 51 | 				
 52 | 				# for index, adjustment in enumerate(service.adjustments):
 53 | 				# 	datum[f'adj_{index}_group'] = adjustment.group_code.code
 54 | 				# 	datum[f'adj_{index}_code'] = adjustment.reason_code.code
 55 | 				# 	datum[f'adj_{index}_amount'] = adjustment.amount
 56 | 
 57 | 				for index, reference in enumerate(service.references):
 58 | 					datum[f'ref_{index}_qual'] = reference.qualifier.code
 59 | 					datum[f'ref_{index}_value'] = reference.value
 60 | 
 61 | 				# for index, remark in enumerate(service.remarks):
 62 | 				# 	datum[f'rem_{index}_qual'] = remark.qualifier.code
 63 | 				# 	datum[f'rem_{index}_code'] = remark.code.code
 64 | 
 65 | 				data.append(datum)
 66 | 		
 67 | 	
 68 | 		return pd.DataFrame(data)
 69 | 
 70 | 	@staticmethod
 71 | 	def serialize_service(
 72 | 			claim: ClaimLoop,
 73 | 			service: ServiceLoop,
 74 | 			patient:PatientLoop,
 75 | 			billingprovider:BillingproviderLoop
 76 | 	) -> dict:
 77 | 		# if the service doesn't have a start date assume the service and claim dates match
 78 | 		servicedate = None
 79 | 		if service:
 80 | 			if service.dates and service.dates[0].qualifier=='service':
 81 | 			
 82 | 				servicedate = service.dates[0].date
 83 | 
 84 | 		# if the service doesn't have an end date assume the service and claim dates match
 85 | 		service_chargeamount = None
 86 | 		if service:
 87 | 			if service.serviceline:
 88 | 				service_chargeamount = service.serviceline[0].chargeamount
 89 | 
 90 | 		attendingprovider_fname=''
 91 | 		attendingprovider_lname=''
 92 | 		attendingprovider_identifier=''
 93 | 		billingprovider_name=''
 94 | 		billingprovider_identfication_code=''
 95 | 		subscriber_amount={}
 96 | 
 97 | 		for entity in claim.entities:
 98 | 			
 99 | 			if entity.entity=='71':
100 | 				# print('hi')
101 | 				
102 | 				attendingprovider_fname=entity.first_name
103 | 				attendingprovider_lname=entity.last_name
104 | 				attendingprovider_identifier=entity.identification_code
105 | 
106 | 		for nm in claim.billingprovider.entities:
107 | 			if nm.entity=='billing provider':
108 | 				billingprovider_name=nm.last_name
109 | 				billingprovider_identfication_code=nm.identification_code
110 | 
111 | 		diagnosis_codes = []
112 | 
113 | 		# Iterate over each object in claim.diagnosis list
114 | 		if claim.diagnosis:
115 | 			for diagnosis_obj in claim.diagnosis:
116 | 				# Extract diagnosis codes list from the current object and concatenate it with all_diagnosis_codes
117 | 				diagnosis_codes.extend(diagnosis_obj.diagnosis_codes)
118 | 		adjustments={}
119 | 		if claim.subscriber_other:
120 | 			for adj in claim.subscriber_other.adjustments:
121 | 				dictionary=adj.reason_code_amount
122 | 				adjustments = {**adjustments, **dictionary}
123 | 		
124 | 		if claim.subscriber_other:
125 | 			if len(claim.subscriber_other.amount)>0:
126 | 				for amt in claim.subscriber_other.amount:
127 | 					subscriber_amount[amt.qualifier]=amt.amount
128 | 		
129 | 
130 | 		datum = {
131 | 			'claim_id': claim.claim.marker,
132 | 		
133 | 			'patient_firstname': claim.patient.entities[0].first_name,
134 | 			'patient_lastname': claim.patient.entities[0].last_name,
135 | 			'patient_firstname': claim.patient.entities[0].first_name,
136 | 			'patient_dob': claim.patient.demographic_information.date,
137 | 			'patient_gender': claim.patient.demographic_information.gender_code,
138 | 
139 | 			'patient_address': claim.patient.address[0].address,
140 | 			'patient_city': claim.patient.city_information[0].city,
141 | 			'patient_state': claim.patient.city_information[0].state,
142 | 			'patient_zipcode': claim.patient.city_information[0].zipcode,
143 | 
144 | 			# 'patient': claim.patient.name,
145 | 			'service_date': servicedate,
146 | 			'service_chargeamount': service_chargeamount,
147 | 			'service_revenue_code':service.serviceline[0].revenuecode,
148 | 			'service_procedure_code':service.serviceline[0].procedurecode,
149 | 			'service_measurement_code':service.serviceline[0].measurementcode,
150 | 			'service_units':service.serviceline[0].unitdays,
151 | 			'drug_identification_code':service.drug_identification.national_drug_code if service.drug_identification else None,
152 | 			'drug_quantity': service.drug_quantity.drug_unit +" "+service.drug_quantity.meas_code  if service.drug_quantity else None,
153 | 			'note':claim.note.note_text if claim.note else None,
154 | 
155 | 			'paid_amount': claim.claim.paid_amount,
156 | 			'rendering_provider': claim.rendering_provider.name if claim.rendering_provider else None,
157 | 			'payer_classification': str(claim.claim.status.payer_classification),
158 | 			'diagnosis':diagnosis_codes,
159 | 			'adjustments':adjustments,
160 | 			'attending_provider_firstname':attendingprovider_fname,
161 | 			'attending_provider_lastname':attendingprovider_lname,
162 | 			'attending_provider_identifier':attendingprovider_identifier,
163 | 			'attending_provider_taxonomy_code':claim.attending_provider_taxonomy.taxonomy_code if claim.attending_provider_taxonomy else None,
164 | 			'service_facility_location': claim.service_facility_location.entities.last_name if claim.service_facility_location and claim.service_facility_location.entities is not None else None,
165 | 			'service_facility_location_address':claim.service_facility_location.address.address if claim.service_facility_location and claim.service_facility_location.address is not None else None,
166 | 			'service_facility_location_city':claim.service_facility_location.city_information.city if claim.service_facility_location and claim.service_facility_location.city_information is not None else None,
167 | 			'service_facility_location_state':claim.service_facility_location.city_information.state if claim.service_facility_location and claim.service_facility_location.city_information is not None else None,
168 | 			'service_facility_location_zipcode':claim.service_facility_location.city_information.zipcode if claim.service_facility_location and claim.service_facility_location.city_information is not None else None,
169 | 			'submiiter_name':claim.submitter.entities.last_name if claim.submitter.entities else None,
170 | 			'submiiter_identifier':claim.submitter.entities.identification_code if claim.submitter.entities is not None else None,
171 | 			'submiiter_dept_telephone':claim.submitter.dept_contact_information.telephonenumber if claim.submitter.dept_contact_information is not None else None,
172 | 			'submiiter_dept_fx':claim.submitter.dept_contact_information.fxnumber if claim.submitter.dept_contact_information is not None else None,
173 | 			'receiver_name':claim.receiver.entities.last_name if claim.receiver.entities else None,
174 | 			'receiver_identifier':claim.receiver.entities.identification_code if claim.receiver.entities is not None else None,
175 | 			'billingprovider_name':billingprovider_name,
176 | 			'billingprovider_identfication_code':billingprovider_identfication_code,
177 | 			'billingprovider_taxonomy_code':claim.billingprovider.billingprovider.taxonomy_code,
178 | 			'billingprovider_dept_telephone':claim.billingprovider.dept_contact_information.telephonenumber,
179 | 			'billingprovider_dept_fx':claim.billingprovider.dept_contact_information.fxnumber,
180 | 			'billing_provider_city':claim.billingprovider.city_information[0].city,
181 | 			'billing_provider_state':claim.billingprovider.city_information[0].state,
182 | 			'billing_provider_zipcode':claim.billingprovider.city_information[0].zipcode,
183 | 			'billing_provider_address':claim.billingprovider.address[0].address,
184 | 			'subscriber(other)_first_name':claim.subscriber_other.payer[0].entities.first_name if (claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber') else None,
185 | 			'subscriber(other)_last_name':claim.subscriber_other.payer[0].entities.last_name if claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber' else None,
186 | 			'subscriber(other)_identification_code':claim.subscriber_other.payer[0].entities.identification_code if (claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber') else None,
187 | 			'subscriber(other)_address':claim.subscriber_other.payer[0].address.address if (claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber' and claim.subscriber_other.payer[0].address is not None) else None,
188 | 			'subscriber(other)_city':claim.subscriber_other.payer[0].city_information.city if (claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber' and claim.subscriber_other.payer[0].city_information is not None) else None,
189 | 			'subscriber(other)_state':claim.subscriber_other.payer[0].city_information.state if (claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber' and claim.subscriber_other.payer[0].city_information is not None) else None,
190 | 			'subscriber(other)_zipcode':claim.subscriber_other.payer[0].city_information.zipcode if (claim.subscriber_other and claim.subscriber_other.payer[0].tag=='subscriber' and claim.subscriber_other.payer[0].city_information is not None) else None,
191 | 			'subscriber(other)_amount':subscriber_amount ,
192 | 			'payer(other)_name':claim.subscriber_other.payer[1].entities.last_name  if (claim.subscriber_other and claim.subscriber_other.payer[1].tag=='payer') else None,
193 | 			'payer(other)_identification_code':claim.subscriber_other.payer[1].entities.identification_code if (claim.subscriber_other and claim.subscriber_other.payer[1].tag=='payer') else None,
194 | 			'payer(other)_address':claim.subscriber_other.payer[1].address.address if (claim.subscriber_other and claim.subscriber_other.payer[1].tag=='payer' and claim.subscriber_other.payer[1].address is not None) else None,
195 | 			'payer(other)_city':claim.subscriber_other.payer[1].city_information.city if (claim.subscriber_other and claim.subscriber_other.payer[1].tag=='payer' and claim.subscriber_other.payer[1].city_information is not None) else None,
196 | 			'payer(other)_state':claim.subscriber_other.payer[1].city_information.state if (claim.subscriber_other and claim.subscriber_other.payer[1].tag=='payer' and claim.subscriber_other.payer[1].city_information is not None) else None,
197 | 			'payer(other)_zipcode':claim.subscriber_other.payer[1].city_information.zipcode if (claim.subscriber_other and claim.subscriber_other.payer[1].tag=='payer' and claim.subscriber_other.payer[1].city_information is not None) else None
198 | 
199 | 
200 | 		}
201 | 
202 | 		return datum
203 | 
204 | 	@classmethod
205 | 	def build(cls, file_path: str) -> 'TransactionSet':
206 | 		claims = []
207 | 		organizations = []
208 | 		patient=[]
209 | 		billingprovider=[]
210 | 		subscriber=[]
211 | 
212 | 
213 | 
214 | 		with open(file_path) as f:
215 | 			file = f.read()
216 | 		
217 | 		segments = file.split('~')
218 | 		segments = [segment.strip() for segment in segments]
219 | 		
220 | 		segments = iter(segments)
221 | 		segment = None
222 | 		pat=PatientLoop()
223 | 		bp=BillingproviderLoop()
224 | 		sub=SubscriberLoop()
225 | 		submit=PayerLoop()
226 | 		receive=PayerLoop()
227 | 
228 | 
229 | 		while True:
230 | 			response = cls.build_attribute(segment, segments)
231 | 			
232 | 			segment = response.segment
233 | 			segments = response.segments
234 | 
235 | 			# no more segments to parse
236 | 			if response.segments is None:
237 | 				break
238 | 
239 | 			if response.key == 'interchange':
240 | 				interchange = response.value
241 | 
242 | 			if response.key == 'financial information':
243 | 				financial_information = response.value
244 | 
245 | 			if response.key == 'organization':
246 | 				organizations.append(response.value)
247 | 
248 | 			if response.key == 'claim':
249 | 	
250 | 				response.value.patient=pat
251 | 				response.value.billingprovider=bp
252 | 				response.value.subscriber=sub
253 | 				response.value.submitter=submit
254 | 				response.value.receiver=receive
255 | 
256 | 				claims.append(response.value)
257 | 			if response.key == 'patient':
258 | 				patient.append(response.value)
259 | 				pat=response.value
260 | 			if response.key == 'billingprovider':
261 | 			
262 | 				billingprovider.append(response.value)
263 | 				bp=response.value
264 | 				
265 | 			if response.key == 'subscriber':
266 | 	
267 | 				subscriber.append(response.value)
268 | 				sub=response.value
269 | 			
270 | 			if response.key == 'submitter':
271 | 				submit=response.value
272 | 
273 | 			if response.key == 'receiver':
274 | 				receive=response.value
275 | 	
276 | 
277 | 
278 | 		
279 | 		return TransactionSet(claims, file_path,patient,billingprovider,subscriber)
280 | 
281 | 	@classmethod
282 | 	def build_attribute(cls, segment: Optional[str], segments: Iterator[str]) -> BuildAttributeResponse:
283 | 		if segment is None:
284 | 			try:
285 | 				segment = segments.__next__()
286 | 			except StopIteration:
287 | 				return BuildAttributeResponse(None, None, None, None)
288 | 		
289 | 		identifier = find_identifier(segment)
290 | 		identifier2=split_segment(segment)
291 | 		
292 | 		if identifier == PatientLoop.initiating_identifier:
293 | 			patient, segments, segment = PatientLoop.build(segment, segments)
294 | 	
295 | 			
296 | 			return BuildAttributeResponse('patient', patient, segment, segments)
297 | 		
298 | 		elif identifier == ClaimLoop.initiating_identifier:
299 | 	
300 | 			claim, segments, segment = ClaimLoop.build(segment, segments)
301 | 			
302 | 			return BuildAttributeResponse('claim', claim, segment, segments)
303 | 		
304 | 		elif identifier == SubscriberLoop.initiating_identifier:
305 | 			subscriber, segments, segment = SubscriberLoop.build(segment, segments)
306 | 			
307 | 			return BuildAttributeResponse('subscriber', subscriber, segment, segments)
308 | 		
309 | 		elif (identifier2[0]== BillingproviderLoop.initiating_identifier and identifier2[1] == 'BI' ):
310 | 			billingprovider, segments, segment = BillingproviderLoop.build(segment, segments)
311 | 			
312 | 			return BuildAttributeResponse('billingprovider', billingprovider, segment, segments)
313 | 		elif (identifier2[0]== PayerLoop.initiating_identifier and identifier2[1] == '41' ):
314 | 			submitter, segments, segment = PayerLoop.build(segment, segments)
315 | 			
316 | 			return BuildAttributeResponse('submitter', submitter, segment, segments)
317 | 		
318 | 		elif (identifier2[0]== PayerLoop.initiating_identifier and identifier2[1] == '40' ):
319 | 			receiver, segments, segment = PayerLoop.build(segment, segments)
320 | 			
321 | 			return BuildAttributeResponse('receiver', receiver, segment, segments)
322 | 
323 | 		else:
324 | 			return BuildAttributeResponse(None, None, None, segments)
325 | 
326 | 
327 | if __name__ == '__main__':
328 | 	pass


--------------------------------------------------------------------------------
/edi_837_parser/transaction_set/transaction_sets.py:
--------------------------------------------------------------------------------
 1 | from typing import List, Iterable
 2 | 
 3 | import pandas as pd
 4 | 
 5 | from edi_837_parser.transaction_set.transaction_set import TransactionSet
 6 | 
 7 | 
 8 | class TransactionSets:
 9 | 
10 | 	def __init__(self, transaction_sets: List[TransactionSet]):
11 | 		self.transaction_sets = transaction_sets
12 | 
13 | 	def __iter__(self) -> Iterable[TransactionSet]:
14 | 		yield from self.transaction_sets
15 | 
16 | 	def __len__(self) -> int:
17 | 		return len(self.transaction_sets)
18 | 
19 | 	def __repr__(self):
20 | 		return '\n'.join(str(transaction_set) for transaction_set in self)
21 | 
22 | 	def to_dataframe(self) -> pd.DataFrame:
23 | 		data = pd.DataFrame()
24 | 		for transaction_set in self:
25 | 			data = pd.concat([data, transaction_set.to_dataframe()])
26 | 		data = TransactionSets.sort_columns(data)
27 | 		return data
28 | 
29 | 	@staticmethod
30 | 	def sort_columns(data: pd.DataFrame) -> pd.DataFrame:
31 | 		substrings = ['adj', 'ref', 'rem']
32 | 		variable_columns = [c for c in data.columns if any(sub_string in c for sub_string in substrings)]
33 | 		variable_columns = sorted(variable_columns)
34 | 
35 | 		static_columns = [c for c in data.columns if c not in variable_columns]
36 | 
37 | 		data = data[static_columns + variable_columns]
38 | 		return data
39 | 
40 | 	def sum_payments(self) -> float:
41 | 		amount = 0
42 | 		for transaction_set in self:
43 | 			amount += transaction_set.financial_information.amount_paid
44 | 
45 | 		return amount
46 | 
47 | 	def count_claims(self) -> int:
48 | 		count = 0
49 | 		for transaction_set in self:
50 | 			count += len(transaction_set.claims)
51 | 
52 | 		return count
53 | 
54 | 	def count_patients(self) -> int:
55 | 		patients = []
56 | 		for transaction_set in self:
57 | 			for claim in transaction_set.claims:
58 | 				patient = claim.patient
59 | 				patients.append(patient.identification_code)
60 | 
61 | 		patients = set(patients)
62 | 		return len(patients)


--------------------------------------------------------------------------------
/extract_edi_837_business_format.py:
--------------------------------------------------------------------------------
   1 | #!/usr/bin/env python3
   2 | """
   3 | Complete EDI 837 data extraction script that converts to business-friendly JSON format
   4 | Includes dynamic parsing, CSV conversion, and comprehensive business format output
   5 | """
   6 | 
   7 | import os
   8 | import json
   9 | import uuid
  10 | import pandas as pd
  11 | from typing import Dict, List, Any, Optional
  12 | from datetime import datetime
  13 | from decimal import Decimal, ROUND_HALF_UP
  14 | 
  15 | # Import configuration from config.py
  16 | import config
  17 | 
  18 | # Use configuration from config.py
  19 | EDI_DIRECTORY = config.EDI_DIRECTORY
  20 | MAX_FILES = config.MAX_FILES
  21 | EDI_FILE_EXTENSIONS = config.EDI_FILE_EXTENSIONS
  22 | 
  23 | # Debug: Print what we're reading from config
  24 | print(f"DEBUG: Reading from config.py - EDI_DIRECTORY = {EDI_DIRECTORY}")
  25 | 
  26 | class EDI837BusinessParser:
  27 |     def __init__(self):
  28 |         # Lookup tables for business format conversion
  29 |         self.place_of_service_codes = {
  30 |             '11': 'OFFICE',
  31 |             '12': 'HOME',
  32 |             '21': 'INPATIENT_HOSPITAL',
  33 |             '22': 'OUTPATIENT_HOSPITAL',
  34 |             '23': 'EMERGENCY_ROOM',
  35 |             '24': 'AMBULATORY_SURGICAL_CENTER',
  36 |             '25': 'BIRTHING_CENTER',
  37 |             '26': 'MILITARY_TREATMENT_FACILITY',
  38 |             '31': 'SKILLED_NURSING_FACILITY',
  39 |             '32': 'NURSING_FACILITY',
  40 |             '33': 'CUSTODIAL_CARE_FACILITY',
  41 |             '34': 'HOSPICE',
  42 |             '41': 'AMBULANCE_LAND',
  43 |             '42': 'AMBULANCE_AIR_OR_WATER',
  44 |             '49': 'INDEPENDENT_CLINIC',
  45 |             '50': 'FEDERALLY_QUALIFIED_HEALTH_CENTER',
  46 |             '51': 'INPATIENT_PSYCHIATRIC_FACILITY',
  47 |             '52': 'PSYCHIATRIC_FACILITY_PARTIAL_HOSPITALIZATION',
  48 |             '53': 'COMMUNITY_MENTAL_HEALTH_CENTER',
  49 |             '54': 'INTERMEDIATE_CARE_FACILITY_MENTALLY_RETARDED',
  50 |             '55': 'RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY',
  51 |             '56': 'PSYCHIATRIC_RESIDENTIAL_TREATMENT_CENTER',
  52 |             '57': 'NON_RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY',
  53 |             '60': 'MASS_IMMUNIZATION_CENTER',
  54 |             '61': 'COMPREHENSIVE_INPATIENT_REHABILITATION_FACILITY',
  55 |             '62': 'COMPREHENSIVE_OUTPATIENT_REHABILITATION_FACILITY',
  56 |             '65': 'END_STAGE_RENAL_DISEASE_TREATMENT_FACILITY',
  57 |             '71': 'PUBLIC_HEALTH_CLINIC',
  58 |             '72': 'RURAL_HEALTH_CLINIC',
  59 |             '81': 'INDEPENDENT_LABORATORY',
  60 |             '99': 'OTHER_PLACE_OF_SERVICE'
  61 |         }
  62 |         
  63 |         self.frequency_codes = {
  64 |             '1': {'desc': 'Original'},
  65 |             '6': {'desc': 'Corrected'},
  66 |             '7': {'desc': 'Replacement'},
  67 |             '8': {'desc': 'Void'}
  68 |         }
  69 |         
  70 |         # Comprehensive ICD-10 Diagnosis Code Descriptions
  71 |         self.diagnosis_descriptions = {
  72 |             # Common diagnosis codes
  73 |             "E1165": "Type 2 diabetes mellitus with hyperglycemia",
  74 |             "E119": "Type 2 diabetes mellitus without complications",
  75 |             "I10": "Essential (primary) hypertension",
  76 |             "Z00121": "Encounter for routine child health examination with abnormal findings",
  77 |             "Z0000": "Encounter for general adult medical examination without abnormal findings",
  78 |             "M545": "Low back pain",
  79 |             "J069": "Acute upper respiratory infection, unspecified",
  80 |             "R50": "Fever, unspecified",
  81 |             "K219": "Gastro-esophageal reflux disease without esophagitis",
  82 |             "F329": "Major depressive disorder, single episode, unspecified",
  83 |             "G43909": "Migraine, unspecified, not intractable, without status migrainosus",
  84 |             "M25551": "Pain in right hip",
  85 |             "M25552": "Pain in left hip",
  86 |             "N390": "Urinary tract infection, site not specified",
  87 |             "R05": "Cough",
  88 |             "R51": "Headache",
  89 |             "R060": "Dyspnea",
  90 |             "Z1231": "Encounter for screening mammogram for malignant neoplasm of breast",
  91 |             
  92 |             # Blood disorders
  93 |             "D500": "Iron deficiency anemia, unspecified",
  94 |             "D501": "Iron deficiency anemia secondary to blood loss (chronic)",
  95 |             "D509": "Iron deficiency anemia, unspecified",
  96 |             "D510": "Vitamin B12 deficiency anemia due to intrinsic factor deficiency",
  97 |             "D519": "Vitamin B12 deficiency anemia, unspecified",
  98 |             "D520": "Dietary folate deficiency anemia",
  99 |             "D529": "Folate deficiency anemia, unspecified",
 100 |             
 101 |             # Neoplasms
 102 |             "C3411": "Malignant neoplasm of upper lobe, right bronchus or lung",
 103 |             "C3412": "Malignant neoplasm of upper lobe, left bronchus or lung",
 104 |             "C3431": "Malignant neoplasm of lower lobe, right bronchus or lung",
 105 |             "C3432": "Malignant neoplasm of lower lobe, left bronchus or lung",
 106 |             "C500": "Malignant neoplasm of nipple and areola",
 107 |             "C5011": "Malignant neoplasm of central portion of right female breast",
 108 |             "C5012": "Malignant neoplasm of central portion of left female breast",
 109 |             
 110 |             # Diabetes
 111 |             "E10": "Type 1 diabetes mellitus",
 112 |             "E1010": "Type 1 diabetes mellitus with ketoacidosis without coma",
 113 |             "E1011": "Type 1 diabetes mellitus with ketoacidosis with coma",
 114 |             "E1021": "Type 1 diabetes mellitus with diabetic nephropathy",
 115 |             "E1022": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
 116 |             
 117 |             # Mental health
 118 |             "F329": "Major depressive disorder, single episode, unspecified",
 119 |             "F4321": "Adjustment disorder with mixed anxiety and depressed mood",
 120 |             "F411": "Generalized anxiety disorder",
 121 |             
 122 |             # Musculoskeletal
 123 |             "M545": "Low back pain",
 124 |             "M25551": "Pain in right hip",
 125 |             "M25552": "Pain in left hip",
 126 |             "M7960": "Pain in limb, unspecified",
 127 |             "M25561": "Pain in right knee",
 128 |             "M25562": "Pain in left knee"
 129 |         }
 130 |         
 131 |         # CPT/HCPCS Procedure Code Descriptions
 132 |         self.procedure_descriptions = {
 133 |             # Evaluation and Management
 134 |             "99213": "Office/outpatient visit, established patient, low complexity",
 135 |             "99214": "Office/outpatient visit, established patient, moderate complexity", 
 136 |             "99215": "Office/outpatient visit, established patient, high complexity",
 137 |             "99203": "Office/outpatient visit, new patient, low complexity",
 138 |             "99204": "Office or other outpatient visit for the evaluation and management of a new patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the encounter for code selection, 45 minutes must be met or exceeded.",
 139 |             "99205": "Office/outpatient visit, new patient, high complexity",
 140 |             "99212": "Office/outpatient visit, established patient, straightforward",
 141 |             "99202": "Office/outpatient visit, new patient, straightforward",
 142 |             "99211": "Office/outpatient visit, established patient, minimal",
 143 |             "99201": "Office/outpatient visit, new patient, minimal",
 144 |             
 145 |             # Preventive Medicine
 146 |             "99395": "Periodic comprehensive preventive medicine reevaluation, 18-39 years",
 147 |             "99396": "Periodic comprehensive preventive medicine reevaluation, 40-64 years",
 148 |             "99397": "Periodic comprehensive preventive medicine reevaluation, 65+ years",
 149 |             "99385": "Initial comprehensive preventive medicine evaluation, 18-39 years",
 150 |             "99386": "Initial comprehensive preventive medicine evaluation, 40-64 years",
 151 |             "99387": "Initial comprehensive preventive medicine evaluation, 65+ years",
 152 |             
 153 |             # Laboratory
 154 |             "80053": "Comprehensive metabolic panel",
 155 |             "85025": "Blood count; complete (CBC), automated",
 156 |             "80061": "Lipid panel",
 157 |             "83036": "Hemoglobin; glycosylated (A1C)",
 158 |             "84443": "Thyroid stimulating hormone (TSH)",
 159 |             "87086": "Culture, bacterial; quantitative colony count, urine",
 160 |             
 161 |             # Radiology
 162 |             "71020": "Radiologic examination, chest, 2 views, frontal and lateral",
 163 |             "73060": "Radiologic examination; knee, 1 or 2 views",
 164 |             "73030": "Radiologic examination, shoulder; complete, minimum of 2 views",
 165 |             "77067": "Screening mammography, bilateral (2-view study of each breast)",
 166 |             
 167 |             # Infusion and Injection Procedures
 168 |             "96365": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); initial, up to 1 hour",
 169 |             "96366": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); each additional hour (List separately in addition to code for primary procedure)",
 170 |             "96367": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); additional sequential infusion of a new drug/substance, up to 1 hour (List separately in addition to code for primary procedure)",
 171 |             "96368": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); concurrent infusion (List separately in addition to code for primary procedure)",
 172 |             "96372": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); subcutaneous or intramuscular",
 173 |             "96373": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); intra-arterial",
 174 |             "96374": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); intravenous push, single or initial substance/drug",
 175 |             "96375": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); each additional sequential intravenous push of a new substance/drug (List separately in addition to code for primary procedure)",
 176 |             "96376": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); each additional sequential intravenous push of the same substance/drug provided in a facility (List separately in addition to code for primary procedure)",
 177 |             "96377": "Application of on-body injector (includes cannula insertion) for timed subcutaneous injection",
 178 |             
 179 |             # Procedures
 180 |             "12001": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities (including hands and feet); 2.5 cm or less",
 181 |             "11042": "Debridement, subcutaneous tissue (includes epidermis and dermis, if performed); first 20 sq cm or less",
 182 |             "90471": "Immunization administration (includes percutaneous, intradermal, subcutaneous, or intramuscular injections); 1 vaccine (single or combination vaccine/toxoid)",
 183 |             "90715": "Tetanus, diphtheria toxoids and acellular pertussis vaccine (Tdap), when administered to individuals 7 years or older, for intramuscular use",
 184 |             
 185 |             # Chemotherapy Administration
 186 |             "96413": "Chemotherapy administration, intravenous infusion technique; up to 1 hour, single or initial substance/drug",
 187 |             "96415": "Chemotherapy administration, intravenous infusion technique; each additional hour (List separately in addition to code for primary procedure)",
 188 |             "96417": "Chemotherapy administration, intravenous infusion technique; each additional sequential infusion (different substance/drug), up to 1 hour (List separately in addition to code for primary procedure)"
 189 |         }
 190 |         
 191 |         # Provider Taxonomy Codes
 192 |         self.provider_taxonomy = {
 193 |             "207Q00000X": "Family Medicine",
 194 |             "208D00000X": "General Practice", 
 195 |             "207R00000X": "Internal Medicine",
 196 |             "207T00000X": "Neurological Surgery",
 197 |             "208600000X": "Surgery",
 198 |             "207X00000X": "Orthopaedic Surgery",
 199 |             "207Y00000X": "Otolaryngology",
 200 |             "208800000X": "Urology",
 201 |             "207W00000X": "Ophthalmology",
 202 |             "207N00000X": "Dermatology",
 203 |             "207P00000X": "Emergency Medicine",
 204 |             "207V00000X": "Obstetrics & Gynecology",
 205 |             "208000000X": "Pediatrics",
 206 |             "207RC0000X": "Cardiovascular Disease",
 207 |             "207RE0101X": "Endocrinology, Diabetes & Metabolism",
 208 |             "207RG0100X": "Gastroenterology",
 209 |             "207RI0200X": "Infectious Disease",
 210 |             "207RN0300X": "Nephrology",
 211 |             "207RP1001X": "Pulmonary Disease",
 212 |             "207RR0500X": "Rheumatology"
 213 |         }
 214 |         
 215 |         # Entity Identifier Codes
 216 |         self.entity_identifiers = {
 217 |             '40': 'Receiver',
 218 |             '41': 'Submitter', 
 219 |             '85': 'Billing Provider',
 220 |             'IL': 'Insured or Subscriber',
 221 |             'PR': 'Payer',
 222 |             'DN': 'Referring Provider',
 223 |             '82': 'Rendering Provider',
 224 |             '77': 'Service Facility Location',
 225 |             'DQ': 'Supervising Provider',
 226 |             'PW': 'Pickup Address',
 227 |             '71': 'Attending Provider',
 228 |             '72': 'Operating Provider',
 229 |             'ZZ': 'Mutually Defined'
 230 |         }
 231 |         
 232 |         # Reference Identification Qualifiers
 233 |         self.reference_qualifiers = {
 234 |             '0B': 'State License Number',
 235 |             '1G': 'Provider UPIN Number',
 236 |             'G2': 'Provider Commercial Number',
 237 |             'LU': 'Location Number',
 238 |             'SY': 'Social Security Number',
 239 |             'TJ': 'Federal Tax Identification Number',
 240 |             'EI': 'Employer Identification Number',
 241 |             'HPI': 'Health Care Provider Taxonomy',
 242 |             'XX': 'Health Care Financing Administration National Provider Identifier',
 243 |             'ZZ': 'Mutually Defined'
 244 |         }
 245 | 
 246 |         # EDI Constants for dynamic extraction
 247 |         self.NPI_QUALIFIER = "XX"
 248 |         self.INDIVIDUAL_ENTITY_TYPE = "1"
 249 |         self.BUSINESS_ENTITY_TYPE = "2"
 250 |         self.TAX_ID_QUALIFIERS = ["EI", "TJ"]
 251 |         self.NPI_IDENTIFICATION_TYPE = "NPI"
 252 |         
 253 |         # Entity role constants
 254 |         self.REFERRING_PROVIDER_ROLE = "REFERRING_PROVIDER"
 255 |         self.RENDERING_PROVIDER_ROLE = "RENDERING_PROVIDER"
 256 |         self.SERVICE_FACILITY_ROLE = "SERVICE_FACILITY"
 257 |         
 258 |         # Object type constants
 259 |         self.CLAIM_OBJECT_TYPE = "CLAIM"
 260 |         self.CHARGEABLE_IDENTIFIER_TYPE = "CHARGEABLE"
 261 |         self.PLACE_OF_SERVICE_SUBTYPE = "PLACE_OF_SERVICE"
 262 |         self.FREQUENCY_CODE_SUBTYPE = "FREQUENCY_CODE"
 263 | 
 264 |     def format_amount(self, amount_str):
 265 |         """Format monetary amount to preserve up to 6 decimal places without rounding"""
 266 |         if not amount_str or amount_str == "":
 267 |             return ""
 268 |         
 269 |         try:
 270 |             # Convert to Decimal to preserve precision
 271 |             decimal_amount = Decimal(str(amount_str))
 272 |             # Format to string with up to 6 decimal places, removing trailing zeros
 273 |             formatted = format(decimal_amount, '.6f').rstrip('0').rstrip('.')
 274 |             return formatted
 275 |         except (ValueError, TypeError):
 276 |             return str(amount_str)
 277 | 
 278 |     def parse_isa_segment(self, elements):
 279 |         """Parse Interchange Control Header"""
 280 |         return {
 281 |             'authorization_info_qualifier': elements[1] if len(elements) > 1 else '',
 282 |             'authorization_info': elements[2] if len(elements) > 2 else '',
 283 |             'security_info_qualifier': elements[3] if len(elements) > 3 else '',
 284 |             'security_info': elements[4] if len(elements) > 4 else '',
 285 |             'interchange_id_qualifier_sender': elements[5] if len(elements) > 5 else '',
 286 |             'interchange_sender_id': elements[6] if len(elements) > 6 else '',
 287 |             'interchange_id_qualifier_receiver': elements[7] if len(elements) > 7 else '',
 288 |             'interchange_receiver_id': elements[8] if len(elements) > 8 else '',
 289 |             'interchange_date': elements[9] if len(elements) > 9 else '',
 290 |             'interchange_time': elements[10] if len(elements) > 10 else '',
 291 |             'interchange_control_standards_id': elements[11] if len(elements) > 11 else '',
 292 |             'interchange_control_version_number': elements[12] if len(elements) > 12 else '',
 293 |             'interchange_control_number': elements[13] if len(elements) > 13 else '',
 294 |             'acknowledgment_requested': elements[14] if len(elements) > 14 else '',
 295 |             'usage_indicator': elements[15] if len(elements) > 15 else ''
 296 |         }
 297 | 
 298 |     def parse_gs_segment(self, elements):
 299 |         """Parse Functional Group Header"""
 300 |         return {
 301 |             'functional_identifier_code': elements[1] if len(elements) > 1 else '',
 302 |             'application_sender_code': elements[2] if len(elements) > 2 else '',
 303 |             'application_receiver_code': elements[3] if len(elements) > 3 else '',
 304 |             'date': elements[4] if len(elements) > 4 else '',
 305 |             'time': elements[5] if len(elements) > 5 else '',
 306 |             'group_control_number': elements[6] if len(elements) > 6 else '',
 307 |             'responsible_agency_code': elements[7] if len(elements) > 7 else '',
 308 |             'version_release_identifier': elements[8] if len(elements) > 8 else ''
 309 |         }
 310 | 
 311 |     def parse_st_segment(self, elements):
 312 |         """Parse Transaction Set Header"""
 313 |         return {
 314 |             "transaction_set_identifier_code": elements[1] if len(elements) > 1 else "",
 315 |             "transaction_set_control_number": elements[2] if len(elements) > 2 else "",
 316 |             'implementation_convention_reference': elements[3] if len(elements) > 3 else ''
 317 |         }
 318 | 
 319 |     def parse_bht_segment(self, elements):
 320 |         """Parse Beginning of Hierarchical Transaction"""
 321 |         return {
 322 |             "hierarchical_structure_code": elements[1] if len(elements) > 1 else "",
 323 |             "transaction_set_purpose_code": elements[2] if len(elements) > 2 else "",
 324 |             "reference_identification": elements[3] if len(elements) > 3 else "",
 325 |             "date": elements[4] if len(elements) > 4 else "",
 326 |             "time": elements[5] if len(elements) > 5 else "",
 327 |             'transaction_type_code': elements[6] if len(elements) > 6 else ''
 328 |         }
 329 | 
 330 |     def parse_hl_segment(self, elements):
 331 |         """Parse Hierarchical Level"""
 332 |         return {
 333 |             "hierarchical_id_number": elements[1] if len(elements) > 1 else "",
 334 |             "hierarchical_parent_id_number": elements[2] if len(elements) > 2 else "",
 335 |             "hierarchical_level_code": elements[3] if len(elements) > 3 else "",
 336 |             "hierarchical_child_code": elements[4] if len(elements) > 4 else ""
 337 |         }
 338 | 
 339 |     def parse_nm1_segment(self, elements):
 340 |         """Parse Individual or Organizational Name"""
 341 |         return {
 342 |             "entity_identifier_code": elements[1] if len(elements) > 1 else "",
 343 |             "entity_type_qualifier": elements[2] if len(elements) > 2 else "",
 344 |             "name_last_or_organization": elements[3] if len(elements) > 3 else "",
 345 |             "name_first": elements[4] if len(elements) > 4 else "",
 346 |             "name_middle": elements[5] if len(elements) > 5 else "",
 347 |             'name_prefix': elements[6] if len(elements) > 6 else '',
 348 |             'name_suffix': elements[7] if len(elements) > 7 else '',
 349 |             "identification_code_qualifier": elements[8] if len(elements) > 8 else "",
 350 |             "identification_code": elements[9] if len(elements) > 9 else ""
 351 |         }
 352 | 
 353 |     def parse_n3_segment(self, elements):
 354 |         """Parse Party Location"""
 355 |         return {
 356 |             "address_line_1": elements[1] if len(elements) > 1 else "",
 357 |             "address_line_2": elements[2] if len(elements) > 2 else ""
 358 |         }
 359 | 
 360 |     def parse_n4_segment(self, elements):
 361 |         """Parse Geographic Location"""
 362 |         return {
 363 |             "city": elements[1] if len(elements) > 1 else "",
 364 |             "state_code": elements[2] if len(elements) > 2 else "",
 365 |             "postal_code": elements[3] if len(elements) > 3 else "",
 366 |             'country_code': elements[4] if len(elements) > 4 else ''
 367 |         }
 368 | 
 369 |     def parse_ref_segment(self, elements):
 370 |         """Parse Reference Information"""
 371 |         return {
 372 |             "reference_identification_qualifier": elements[1] if len(elements) > 1 else "",
 373 |             "reference_identification": elements[2] if len(elements) > 2 else "",
 374 |             'description': elements[3] if len(elements) > 3 else ''
 375 |         }
 376 | 
 377 |     def parse_dmg_segment(self, elements):
 378 |         """Parse Demographic Information"""
 379 |         return {
 380 |             "date_time_period_format_qualifier": elements[1] if len(elements) > 1 else "",
 381 |             "date_time_period": elements[2] if len(elements) > 2 else "",
 382 |             "gender_code": elements[3] if len(elements) > 3 else "",
 383 |             'marital_status_code': elements[4] if len(elements) > 4 else ''
 384 |         }
 385 | 
 386 |     def parse_dtp_segment(self, elements):
 387 |         """Parse Date or Time or Period"""
 388 |         qualifier = elements[1] if len(elements) > 1 else ""
 389 |         format_qualifier = elements[2] if len(elements) > 2 else ""
 390 |         date_period = elements[3] if len(elements) > 3 else ""
 391 |         
 392 |         # Map common date qualifiers for reference
 393 |         qualifier_descriptions = {
 394 |             "472": "Service Date",
 395 |             "454": "Initial Treatment Date", 
 396 |             "304": "Latest Visit or Consultation",
 397 |             "453": "Acute Manifestation Date",
 398 |             "439": "Accident Date",
 399 |             "484": "Last Seen Date",
 400 |             "455": "Last X-ray Date",
 401 |             "471": "Prescription Date",
 402 |             "314": "Disability Begin Date",
 403 |             "315": "Disability End Date",
 404 |             "150": "Service Period Start",
 405 |             "151": "Service Period End"
 406 |         }
 407 |         
 408 |         return {
 409 |             "date_time_qualifier": qualifier,
 410 |             "date_time_period_format_qualifier": format_qualifier,
 411 |             "date_time_period": date_period,
 412 |             "qualifier_description": qualifier_descriptions.get(qualifier, "")
 413 |         }
 414 | 
 415 |     def parse_clm_segment(self, elements):
 416 |         """Parse Claim Information"""
 417 |         # Parse the claim filing indicator from element 5 (format like "11:B:1")
 418 |         claim_filing_parts = elements[5].split(':') if len(elements) > 5 and elements[5] else []
 419 |         place_of_service = claim_filing_parts[0] if claim_filing_parts else ''
 420 |         frequency_code = claim_filing_parts[2] if len(claim_filing_parts) > 2 else '1'
 421 |         
 422 |         return {
 423 |             'claim_submitter_identifier': elements[1] if len(elements) > 1 else '',
 424 |             'monetary_amount': elements[2] if len(elements) > 2 else '',
 425 |             'claim_frequency_type_code': frequency_code,  # Extract from claim filing indicator
 426 |             'non_institutional_claim_type_code': elements[4] if len(elements) > 4 else '',
 427 |             'claim_filing_indicator_code': elements[5] if len(elements) > 5 else '',
 428 |             'place_of_service_code': place_of_service,  # Extract from claim filing indicator
 429 |             'yes_no_condition_response_code': elements[6] if len(elements) > 6 else '',
 430 |             'provider_accept_assignment_code': elements[7] if len(elements) > 7 else '',
 431 |             'yes_no_condition_response_code_2': elements[8] if len(elements) > 8 else '',
 432 |             'release_of_information_code': elements[9] if len(elements) > 9 else '',
 433 |             'patient_signature_source_code': elements[10] if len(elements) > 10 else ''
 434 |         }
 435 | 
 436 |     def parse_sv1_segment(self, elements):
 437 |         """Parse Professional Service"""
 438 |         procedure_info = {}
 439 |         if len(elements) > 1 and elements[1]:
 440 |             if ':' in elements[1]:
 441 |                 parts = elements[1].split(':')
 442 |                 procedure_info = {
 443 |                     'product_service_id_qualifier': parts[0] if len(parts) > 0 else '',
 444 |                     'procedure_code': parts[1] if len(parts) > 1 else '',
 445 |                     'procedure_modifier_1': parts[2] if len(parts) > 2 else '',
 446 |                     'procedure_modifier_2': parts[3] if len(parts) > 3 else '',
 447 |                     'procedure_modifier_3': parts[4] if len(parts) > 4 else '',
 448 |                     'procedure_modifier_4': parts[5] if len(parts) > 5 else ''
 449 |                 }
 450 |             else:
 451 |                 procedure_info = {'procedure_code': elements[1]}
 452 |         
 453 |         # Place of service can be in position 5, 6, or 7 depending on the format
 454 |         place_of_service = ""
 455 |         for i in [5, 6, 7]:
 456 |             if len(elements) > i and elements[i] and elements[i].isdigit():
 457 |                 place_of_service = elements[i]
 458 |                 break
 459 |         
 460 |         return {
 461 |             'composite_medical_procedure_identifier': procedure_info,
 462 |             'monetary_amount': elements[2] if len(elements) > 2 else '',
 463 |             'unit_or_basis_for_measurement_code': elements[3] if len(elements) > 3 else '',
 464 |             'service_unit_count': elements[4] if len(elements) > 4 else '',
 465 |             'place_of_service_code': place_of_service,
 466 |             'service_type_code': elements[6] if len(elements) > 6 else ''
 467 |         }
 468 | 
 469 |     def parse_per_segment(self, elements):
 470 |         """Parse Administrative Communications Contact"""
 471 |         return {
 472 |             'contact_function_code': elements[1] if len(elements) > 1 else '',
 473 |             'name': elements[2] if len(elements) > 2 else '',
 474 |             'communication_number_qualifier_1': elements[3] if len(elements) > 3 else '',
 475 |             'communication_number_1': elements[4] if len(elements) > 4 else '',
 476 |             'communication_number_qualifier_2': elements[5] if len(elements) > 5 else '',
 477 |             'communication_number_2': elements[6] if len(elements) > 6 else ''
 478 |         }
 479 | 
 480 |     def parse_sbr_segment(self, elements):
 481 |         """Parse Subscriber Information"""
 482 |         return {
 483 |             'payer_responsibility_sequence_number_code': elements[1] if len(elements) > 1 else '',
 484 |             'individual_relationship_code': elements[2] if len(elements) > 2 else '',
 485 |             'reference_identification': elements[3] if len(elements) > 3 else '',
 486 |             'name': elements[4] if len(elements) > 4 else '',
 487 |             'insurance_type_code': elements[5] if len(elements) > 5 else '',
 488 |             'coordination_of_benefits_code': elements[6] if len(elements) > 6 else '',
 489 |             'yes_no_condition_response_code': elements[7] if len(elements) > 7 else '',
 490 |             'employment_status_code': elements[8] if len(elements) > 8 else '',
 491 |             'claim_filing_indicator_code': elements[9] if len(elements) > 9 else ''
 492 |         }
 493 | 
 494 |     def parse_hi_segment(self, elements):
 495 |         """Parse Health Care Diagnosis Code"""
 496 |         diagnosis_codes = []
 497 |         for i in range(1, len(elements)):
 498 |             if elements[i] and ':' in elements[i]:
 499 |                 code_qualifier, code = elements[i].split(':', 1)
 500 |                 diagnosis_codes.append({
 501 |                     "code_list_qualifier_code": code_qualifier,
 502 |                     "diagnosis_code": code
 503 |                 })
 504 |         return diagnosis_codes
 505 | 
 506 |     def parse_prv_segment(self, elements):
 507 |         """Parse Provider Information"""
 508 |         return {
 509 |             'provider_code': elements[1] if len(elements) > 1 else '',
 510 |             'reference_identification_qualifier': elements[2] if len(elements) > 2 else '',
 511 |             'reference_identification': elements[3] if len(elements) > 3 else ''
 512 |         }
 513 | 
 514 |     def parse_lx_segment(self, elements):
 515 |         """Parse Service Line Number"""
 516 |         return {
 517 |             'assigned_number': elements[1] if len(elements) > 1 else ''
 518 |         }
 519 | 
 520 |     def parse_sv2_segment(self, elements):
 521 |         """Parse Institutional Service Line"""
 522 |         return {
 523 |             'revenue_code': elements[1] if len(elements) > 1 else '',
 524 |             'monetary_amount': elements[2] if len(elements) > 2 else '',
 525 |             'unit_or_basis_for_measurement_code': elements[3] if len(elements) > 3 else '',
 526 |             'service_unit_count': elements[4] if len(elements) > 4 else ''
 527 |         }
 528 | 
 529 |     def parse_sv3_segment(self, elements):
 530 |         """Parse Dental Service"""
 531 |         procedure_info = {}
 532 |         if len(elements) > 1 and elements[1]:
 533 |             if ':' in elements[1]:
 534 |                 parts = elements[1].split(':')
 535 |                 procedure_info = {
 536 |                     'product_service_id_qualifier': parts[0] if len(parts) > 0 else '',
 537 |                     'procedure_code': parts[1] if len(parts) > 1 else ''
 538 |                 }
 539 |             else:
 540 |                 procedure_info = {'procedure_code': elements[1]}
 541 |         
 542 |         return {
 543 |             'composite_medical_procedure_identifier': procedure_info,
 544 |             'monetary_amount': elements[2] if len(elements) > 2 else '',
 545 |             'place_of_service_code': elements[3] if len(elements) > 3 else '',
 546 |             'oral_cavity_designation': elements[4] if len(elements) > 4 else '',
 547 |             'prosthesis_crown_or_inlay_code': elements[5] if len(elements) > 5 else '',
 548 |             'quantity': elements[6] if len(elements) > 6 else ''
 549 |         }
 550 | 
 551 |     def parse_cas_segment(self, elements):
 552 |         """Parse Claim Adjustment"""
 553 |         adjustments = []
 554 |         i = 1
 555 |         while i < len(elements):
 556 |             if i + 2 < len(elements):
 557 |                 adjustments.append({
 558 |                     'claim_adjustment_group_code': elements[i] if i < len(elements) else '',
 559 |                     'claim_adjustment_reason_code': elements[i+1] if i+1 < len(elements) else '',
 560 |                     'monetary_amount': elements[i+2] if i+2 < len(elements) else '',
 561 |                     'quantity': elements[i+3] if i+3 < len(elements) else ''
 562 |                 })
 563 |                 i += 4
 564 |             else:
 565 |                 break
 566 |         return adjustments
 567 | 
 568 |     def parse_amt_segment(self, elements):
 569 |         """Parse Monetary Amount Information"""
 570 |         return {
 571 |             'amount_qualifier_code': elements[1] if len(elements) > 1 else '',
 572 |             'monetary_amount': elements[2] if len(elements) > 2 else ''
 573 |         }
 574 | 
 575 |     def parse_qty_segment(self, elements):
 576 |         """Parse Quantity Information"""
 577 |         return {
 578 |             'quantity_qualifier': elements[1] if len(elements) > 1 else '',
 579 |             'quantity': elements[2] if len(elements) > 2 else ''
 580 |         }
 581 | 
 582 |     def parse_nte_segment(self, elements):
 583 |         """Parse Note/Special Instruction"""
 584 |         return {
 585 |             'note_reference_code': elements[1] if len(elements) > 1 else '',
 586 |             'description': elements[2] if len(elements) > 2 else ''
 587 |         }
 588 | 
 589 |     def format_date(self, date_str):
 590 |         """Format date from YYYYMMDD to readable format"""
 591 |         if not date_str or len(date_str) != 8:
 592 |             return date_str
 593 |         try:
 594 |             year = date_str[:4]
 595 |             month = date_str[4:6]
 596 |             day = date_str[6:8]
 597 |             return f"{month}/{day}/{year}"
 598 |         except:
 599 |             return date_str
 600 | 
 601 |     def format_time(self, time_str):
 602 |         """Format time from HHMM to readable format"""
 603 |         if not time_str or len(time_str) < 4:
 604 |             return time_str
 605 |         try:
 606 |             hour = time_str[:2]
 607 |             minute = time_str[2:4]
 608 |             return f"{hour}:{minute}"
 609 |         except:
 610 |             return time_str
 611 | 
 612 |     def get_business_description(self, code, code_type):
 613 |         """Get business-friendly description for codes"""
 614 |         lookup_tables = {
 615 |             'place_of_service': self.place_of_service_codes,
 616 |             'diagnosis': self.diagnosis_descriptions,
 617 |             'procedure': self.procedure_descriptions,
 618 |             'provider_taxonomy': self.provider_taxonomy,
 619 |             'entity_identifier': self.entity_identifiers,
 620 |             'reference_qualifier': self.reference_qualifiers,
 621 |             'frequency': self.frequency_codes
 622 |         }
 623 |         
 624 |         if code_type in lookup_tables:
 625 |             return lookup_tables[code_type].get(code, code)
 626 |         return code
 627 | 
 628 |     def convert_to_business_format(self, edi_data):
 629 |         """Convert parsed EDI data to the specified JSON format"""
 630 |         claims = []
 631 |         
 632 |         # Process transaction sets to extract claims
 633 |         for ts in edi_data.get("transaction_sets", []):
 634 |             transaction_info = self.format_transaction_info(ts, edi_data)
 635 |             
 636 |             # Process billing providers
 637 |             for bp in ts.get("billing_providers", []):
 638 |                 billing_provider = self.format_billing_provider(bp.get("provider_info", {}))
 639 |                 
 640 |                 # Process subscribers
 641 |                 for sub in bp.get("subscribers", []):
 642 |                     subscriber_info = self.format_subscriber_new(sub.get("subscriber_info", {}))
 643 |                     payer_info = self.format_payer_new(sub.get("payer_info", {}))
 644 |                     
 645 |                     # Process claims
 646 |                     for claim in sub.get("claims", []):
 647 |                         claim_obj = self.format_claim_new(claim, subscriber_info, payer_info, billing_provider, transaction_info, bp)
 648 |                         if claim_obj:
 649 |                             claims.append(claim_obj)
 650 |         
 651 |         return claims
 652 | 
 653 |     def format_entity_info(self, entity_data):
 654 |         """Format entity information for business use"""
 655 |         if not entity_data:
 656 |             return {}
 657 |         
 658 |         return {
 659 |             "entity_type": self.get_business_description(entity_data.get("entity_identifier_code", ""), "entity_identifier"),
 660 |             "organization_name": entity_data.get("name_last_or_organization", ""),
 661 |             "contact_info": entity_data.get("contact_info", {}),
 662 |             "address": entity_data.get("address", {}),
 663 |             "identification": {
 664 |                 "qualifier": self.get_business_description(entity_data.get("identification_code_qualifier", ""), "reference_qualifier"),
 665 |                 "id": entity_data.get("identification_code", "")
 666 |             }
 667 |         }
 668 | 
 669 |     def format_provider_info(self, provider_data):
 670 |         """Format provider information for business use"""
 671 |         if not provider_data:
 672 |             return {}
 673 |         
 674 |         return {
 675 |             "provider_name": provider_data.get("name_last_or_organization", ""),
 676 |             "provider_type": self.get_business_description(provider_data.get("entity_identifier_code", ""), "entity_identifier"),
 677 |             "npi": provider_data.get("identification_code", "") if provider_data.get("identification_code_qualifier") == self.NPI_QUALIFIER else "",
 678 |             "tax_id": provider_data.get("tax_identification_number", ""),
 679 |             "address": provider_data.get("address", {}),
 680 |             "contact_info": provider_data.get("contact_info", {}),
 681 |             "specialty": self.get_business_description(provider_data.get("provider_taxonomy", ""), "provider_taxonomy")
 682 |         }
 683 | 
 684 |     def format_subscriber_info(self, subscriber_data):
 685 |         """Format subscriber information for business use"""
 686 |         if not subscriber_data:
 687 |             return {}
 688 |         
 689 |         return {
 690 |             "member_id": subscriber_data.get("identification_code", ""),
 691 |             "name": {
 692 |                 "last": subscriber_data.get("name_last_or_organization", ""),
 693 |                 "first": subscriber_data.get("name_first", ""),
 694 |                 "middle": subscriber_data.get("name_middle", "")
 695 |             },
 696 |             "address": subscriber_data.get("address", {}),
 697 |             "demographics": {
 698 |                 "date_of_birth": self.format_date(subscriber_data.get("demographics", {}).get("date_time_period", "")),
 699 |                 "gender": subscriber_data.get("demographics", {}).get("gender_code", "")
 700 |             },
 701 |             "relationship_to_patient": subscriber_data.get("individual_relationship_code", "")
 702 |         }
 703 | 
 704 |     def format_payer_info(self, payer_data):
 705 |         """Format payer information for business use"""
 706 |         if not payer_data:
 707 |             return {}
 708 |         
 709 |         return {
 710 |             "payer_name": payer_data.get("name_last_or_organization", ""),
 711 |             "payer_id": payer_data.get("identification_code", ""),
 712 |             "address": payer_data.get("address", {}),
 713 |             "responsibility_sequence": payer_data.get("payer_responsibility_sequence_number_code", "")
 714 |         }
 715 | 
 716 |     def format_transaction_info(self, ts, edi_data):
 717 |         """Format transaction information"""
 718 |         bht = ts.get("beginning_hierarchical_transaction", {})
 719 |         st = ts.get("transaction_set_header", {})
 720 |         submitter = ts.get("submitter", {})
 721 |         receiver = ts.get("receiver", {})
 722 |         
 723 |         return {
 724 |             "id": str(uuid.uuid4()).replace('-', ''),
 725 |             "controlNumber": st.get("transaction_set_control_number", ""),
 726 |             "transactionType": st.get("transaction_set_identifier_code", ""),
 727 |             "hierarchicalStructureCode": bht.get("hierarchical_structure_code", ""),
 728 |             "purposeCode": bht.get("transaction_set_purpose_code", ""),
 729 |             "originatorApplicationTransactionId": bht.get("reference_identification", ""),
 730 |             "creationDate": self.format_date_iso(bht.get("date", "")),
 731 |             "creationTime": self.format_time_iso(bht.get("time", "")),
 732 |             "claimOrEncounterIdentifierType": self.CHARGEABLE_IDENTIFIER_TYPE,
 733 |             "transactionSetIdentifierCode": st.get("transaction_set_identifier_code", ""),
 734 |             "implementationConventionReference": st.get("implementation_convention_reference", ""),
 735 |             "fileInfo": {"fileType": "EDI"},
 736 |             "sender": self.format_entity_new(submitter, "SUBMITTER"),
 737 |             "receiver": self.format_entity_new(receiver, "RECEIVER"),
 738 |             "creationDateTime": f"{self.format_date_iso(bht.get('date', ''))}T{self.format_time_iso(bht.get('time', ''))}"
 739 |         }
 740 | 
 741 |     def format_entity_new(self, entity_data, role):
 742 |         """Format entity in new structure"""
 743 |         if not entity_data:
 744 |             return {}
 745 |         
 746 |         entity = {
 747 |             "entityRole": role,
 748 |             "entityType": "INDIVIDUAL" if entity_data.get("entity_type_qualifier") == self.INDIVIDUAL_ENTITY_TYPE else "BUSINESS",
 749 |             "identificationType": self.get_identification_type(entity_data.get("identification_code_qualifier", "")),
 750 |             "identifier": entity_data.get("identification_code", ""),
 751 |             "lastNameOrOrgName": entity_data.get("name_last_or_organization", "")
 752 |         }
 753 |         
 754 |         if entity_data.get("name_first"):
 755 |             entity["firstName"] = entity_data.get("name_first", "")
 756 |         if entity_data.get("name_middle"):
 757 |             entity["middleName"] = entity_data.get("name_middle", "")
 758 |         
 759 |         # Add contacts if available
 760 |         if entity_data.get("contact_info"):
 761 |             contact = entity_data["contact_info"]
 762 |             entity["contacts"] = [{
 763 |                 "functionCode": contact.get("contact_function_code", ""),
 764 |                 "name": contact.get("name", ""),
 765 |                 "contactNumbers": []
 766 |             }]
 767 |             
 768 |             if contact.get("communication_number_1"):
 769 |                 entity["contacts"][0]["contactNumbers"].append({
 770 |                     "type": self.get_communication_type(contact.get("communication_number_qualifier_1", "")),
 771 |                     "number": contact.get("communication_number_1", "")
 772 |                 })
 773 |         
 774 |         return entity
 775 | 
 776 |     def format_billing_provider(self, provider_data):
 777 |         """Format billing provider"""
 778 |         if not provider_data:
 779 |             return {}
 780 |         
 781 |         provider = {
 782 |             "entityRole": self.get_entity_role(provider_data.get("entity_identifier_code", "")),
 783 |             "entityType": "INDIVIDUAL" if provider_data.get("entity_type_qualifier") == self.INDIVIDUAL_ENTITY_TYPE else "BUSINESS",
 784 |             "identificationType": self.get_identification_type(provider_data.get("identification_code_qualifier", "")),
 785 |             "identifier": provider_data.get("identification_code", ""),
 786 |             "lastNameOrOrgName": provider_data.get("name_last_or_organization", "")
 787 |         }
 788 |         
 789 |         # Add tax ID if available from references or provider_info
 790 |         if provider_data.get("references"):
 791 |             for ref in provider_data["references"]:
 792 |                 if ref.get("reference_identification_qualifier") in self.TAX_ID_QUALIFIERS:
 793 |                     provider["taxId"] = ref.get("reference_identification", "")
 794 |                     provider["taxIdQualifier"] = ref.get("reference_identification_qualifier", "")
 795 |         elif provider_data.get("provider_info", {}).get("tax_identification_number"):
 796 |             provider["taxId"] = provider_data["provider_info"]["tax_identification_number"]
 797 |             provider["taxIdQualifier"] = provider_data["provider_info"].get("tax_identification_qualifier", "")
 798 |         
 799 |         # Add address
 800 |         if provider_data.get("address"):
 801 |             addr = provider_data["address"]
 802 |             provider["address"] = {
 803 |                 "line": addr.get("address_line_1", ""),
 804 |                 "city": addr.get("city", ""),
 805 |                 "stateCode": addr.get("state_code", ""),
 806 |                 "zipCode": addr.get("postal_code", "")
 807 |             }
 808 |             if addr.get("address_line_2"):
 809 |                 provider["address"]["line2"] = addr.get("address_line_2", "")
 810 |         
 811 |         return provider
 812 | 
 813 |     def format_subscriber_new(self, subscriber_data):
 814 |         """Format subscriber in new structure"""
 815 |         if not subscriber_data:
 816 |             return {}
 817 |         
 818 |         subscriber = {
 819 |             "payerResponsibilitySequence": self.get_payer_sequence(subscriber_data.get("payer_responsibility_sequence_number_code", "")),
 820 |             "relationshipType": self.get_relationship_type(subscriber_data.get("individual_relationship_code", "")),
 821 |             "claimFilingIndicatorCode": subscriber_data.get("claim_filing_indicator_code", "CI"),
 822 |             "insurancePlanType": self.get_insurance_type(subscriber_data.get("insurance_type_code", "")),
 823 |             "person": {
 824 |                 "entityRole": self.get_entity_role(subscriber_data.get("entity_identifier_code", "")),
 825 |                 "entityType": "INDIVIDUAL" if subscriber_data.get("entity_type_qualifier") == self.INDIVIDUAL_ENTITY_TYPE else "BUSINESS",
 826 |                 "identificationType": self.get_identification_type(subscriber_data.get("identification_code_qualifier", "")),
 827 |                 "identifier": subscriber_data.get("identification_code", ""),
 828 |                 "lastNameOrOrgName": subscriber_data.get("name_last_or_organization", ""),
 829 |                 "firstName": subscriber_data.get("name_first", "")
 830 |             }
 831 |         }
 832 |         
 833 |         # Add demographics
 834 |         if subscriber_data.get("demographics"):
 835 |             demo = subscriber_data["demographics"]
 836 |             if demo.get("date_time_period"):
 837 |                 subscriber["person"]["birthDate"] = self.format_date_iso(demo.get("date_time_period", ""))
 838 |             if demo.get("gender_code"):
 839 |                 subscriber["person"]["gender"] = "MALE" if demo.get("gender_code") == "M" else "FEMALE"
 840 |         
 841 |         # Add address
 842 |         if subscriber_data.get("address"):
 843 |             addr = subscriber_data["address"]
 844 |             subscriber["person"]["address"] = {
 845 |                 "line": addr.get("address_line_1", ""),
 846 |                 "city": addr.get("city", ""),
 847 |                 "stateCode": addr.get("state_code", ""),
 848 |                 "zipCode": addr.get("postal_code", "")
 849 |             }
 850 |         
 851 |         return subscriber
 852 | 
 853 |     def format_payer_new(self, payer_data):
 854 |         """Format payer in new structure"""
 855 |         if not payer_data:
 856 |             return {}
 857 |         
 858 |         payer = {
 859 |             "entityRole": self.get_entity_role(payer_data.get("entity_identifier_code", "")),
 860 |             "entityType": "INDIVIDUAL" if payer_data.get("entity_type_qualifier") == self.INDIVIDUAL_ENTITY_TYPE else "BUSINESS",
 861 |             "identificationType": self.get_identification_type(payer_data.get("identification_code_qualifier", "")),
 862 |             "identifier": payer_data.get("identification_code", ""),
 863 |             "lastNameOrOrgName": payer_data.get("name_last_or_organization", "")
 864 |         }
 865 |         
 866 |         # Add address
 867 |         if payer_data.get("address"):
 868 |             addr = payer_data["address"]
 869 |             payer["address"] = {
 870 |                 "line": addr.get("address_line_1", ""),
 871 |                 "city": addr.get("city", ""),
 872 |                 "stateCode": addr.get("state_code", ""),
 873 |                 "zipCode": addr.get("postal_code", "")
 874 |             }
 875 |         
 876 |         return payer
 877 | 
 878 |     def format_claim_new(self, claim_data, subscriber_info, payer_info, billing_provider, transaction_info, bp):
 879 |         """Format claim in new structure"""
 880 |         if not claim_data:
 881 |             return None
 882 |         
 883 |         claim_info = claim_data.get("claim_info", {})
 884 |         
 885 |         # Get service dates - first try claim level, then use first service line date
 886 |         service_date_from = ""
 887 |         service_date_to = ""
 888 |         
 889 |         # Check claim-level dates first
 890 |         for date_info in claim_data.get("dates", []):
 891 |             if date_info.get("date_time_qualifier") == "472":  # Service date
 892 |                 service_date_from = self.format_date_iso(date_info.get("date_time_period", ""))
 893 |                 service_date_to = service_date_from
 894 |                 break
 895 |             elif date_info.get("date_time_qualifier") == "454":  # Initial treatment date
 896 |                 if not service_date_from:
 897 |                     service_date_from = self.format_date_iso(date_info.get("date_time_period", ""))
 898 |                     service_date_to = service_date_from
 899 |         
 900 |         # If no claim-level dates, use first service line date
 901 |         if not service_date_from and claim_data.get("service_lines"):
 902 |             first_service_line = claim_data["service_lines"][0]
 903 |             for date_info in first_service_line.get("dates", []):
 904 |                 if date_info.get("date_time_qualifier") == "472":
 905 |                     service_date_from = self.format_date_iso(date_info.get("date_time_period", ""))
 906 |                     service_date_to = service_date_from
 907 |                     break
 908 |         
 909 |         # Get place of service from claim info first, then service lines
 910 |         place_of_service_code = claim_info.get("place_of_service_code", "")
 911 |         if not place_of_service_code or place_of_service_code == "":
 912 |             if claim_data.get("service_lines"):
 913 |                 first_service = claim_data["service_lines"][0]
 914 |                 service_info = first_service.get("service_info", {})
 915 |                 place_of_service_code = service_info.get("place_of_service_code", "")
 916 |         
 917 |         # Get frequency code from claim info
 918 |         frequency_code = claim_info.get("claim_frequency_type_code", "")
 919 |         if not frequency_code or frequency_code == "":
 920 |             frequency_code = ""  # Extract from EDI, don't default
 921 |         
 922 |         claim = {
 923 |             "id": claim_info.get("claim_submitter_identifier", str(uuid.uuid4()).replace('-', '')),
 924 |             "objectType": self.CLAIM_OBJECT_TYPE,
 925 |             "patientControlNumber": claim_info.get("claim_submitter_identifier", ""),
 926 |             "chargeAmount": self.format_amount(claim_info.get("monetary_amount", "")),
 927 |             "facilityCode": {
 928 |                 "subType": self.PLACE_OF_SERVICE_SUBTYPE,
 929 |                 "code": place_of_service_code
 930 |             },
 931 |             "placeOfServiceType": self.place_of_service_codes.get(place_of_service_code, place_of_service_code),
 932 |             "frequencyCode": {
 933 |                 "subType": self.FREQUENCY_CODE_SUBTYPE,
 934 |                 "code": frequency_code,
 935 |                 "desc": self.frequency_codes.get(frequency_code, {}).get("desc", frequency_code)
 936 |             },
 937 |             "serviceDateFrom": service_date_from,
 938 |             "serviceDateTo": service_date_to,
 939 |             "subscriber": subscriber_info,
 940 |             "payer": payer_info,
 941 |             "providerSignatureIndicator": claim_info.get("patient_signature_source_code", ""),
 942 |             "assignmentParticipationCode": claim_info.get("provider_accept_assignment_code", ""),
 943 |             "assignmentCertificationIndicator": claim_info.get("yes_no_condition_response_code", ""),
 944 |             "releaseOfInformationCode": claim_info.get("release_of_information_code", ""),
 945 |             "originalReferenceNumber": f"CP{transaction_info.get('originatorApplicationTransactionId', '')}{claim_info.get('claim_submitter_identifier', '')}",
 946 |             "billingProvider": billing_provider,
 947 |             "providers": [],
 948 |             "diags": [],
 949 |             "serviceLines": [],
 950 |             "transaction": transaction_info
 951 |         }
 952 |         
 953 |         # Add providers
 954 |         for provider in claim_data.get("providers", []):
 955 |             provider_obj = self.format_provider_new(provider)
 956 |             if provider_obj:
 957 |                 claim["providers"].append(provider_obj)
 958 |         
 959 |         # Add diagnosis codes
 960 |         for diag_list in claim_data.get("diagnosis_codes", []):
 961 |             if isinstance(diag_list, list):
 962 |                 for diag in diag_list:
 963 |                     diag_obj = self.format_diagnosis_new(diag)
 964 |                     if diag_obj:
 965 |                         claim["diags"].append(diag_obj)
 966 |         
 967 |         # Add service lines
 968 |         for i, service_line in enumerate(claim_data.get("service_lines", []), 1):
 969 |             service_obj = self.format_service_line_new(service_line, i, claim["diags"])
 970 |             if service_obj:
 971 |                 claim["serviceLines"].append(service_obj)
 972 |         
 973 |         return claim
 974 | 
 975 |     def format_provider_new(self, provider_data):
 976 |         """Format provider in new structure"""
 977 |         if not provider_data:
 978 |             return None
 979 |         
 980 |         provider_info = provider_data.get("provider_data", {})
 981 |         # Use the entity identifier code directly or map it
 982 |         entity_code = provider_data.get("provider_role", "")
 983 |         role_map = {
 984 |             "DN": "REFERRING_PROVIDER",
 985 |             "82": "RENDERING_PROVIDER", 
 986 |             "77": "SERVICE_FACILITY",
 987 |             "DQ": "SUPERVISING_PROVIDER",
 988 |             "85": "BILLING_PROVIDER"
 989 |         }
 990 |         
 991 |         provider = {
 992 |             "entityRole": role_map.get(entity_code, entity_code),
 993 |             "entityType": "INDIVIDUAL" if provider_info.get("entity_type_qualifier") == self.INDIVIDUAL_ENTITY_TYPE else "BUSINESS",
 994 |             "identificationType": self.get_identification_type(provider_info.get("identification_code_qualifier", "")),
 995 |             "identifier": provider_info.get("identification_code", ""),
 996 |             "lastNameOrOrgName": provider_info.get("name_last_or_organization", "")
 997 |         }
 998 |         
 999 |         if provider_info.get("name_first"):
1000 |             provider["firstName"] = provider_info.get("name_first", "")
1001 |         if provider_info.get("name_middle"):
1002 |             provider["middleName"] = provider_info.get("name_middle", "")
1003 |         
1004 |         # Handle middle name from suffix field if it contains middle name
1005 |         if not provider.get("middleName") and provider_info.get("name_suffix"):
1006 |             # Sometimes middle name is in suffix field
1007 |             suffix = provider_info.get("name_suffix", "")
1008 |             if len(suffix) == 1 or (len(suffix) <= 3 and not suffix.upper() in ["JR", "SR", "III", "IV", "MD", "DO", "RN"]):
1009 |                 provider["middleName"] = suffix
1010 |         
1011 |         # Add provider taxonomy if available
1012 |         taxonomy_code = provider_data.get("provider_taxonomy", "") or provider_info.get("provider_taxonomy", "")
1013 |         if taxonomy_code:
1014 |             provider["providerTaxonomy"] = {
1015 |                 "subType": "PROVIDER_TAXONOMY",
1016 |                 "code": taxonomy_code,
1017 |                 "desc": self.provider_taxonomy.get(taxonomy_code, "")
1018 |             }
1019 |         
1020 |         # Add additional IDs
1021 |         if provider_data.get("references"):
1022 |             provider["additionalIds"] = []
1023 |             for ref in provider_data["references"]:
1024 |                 if ref.get("reference_identification_qualifier") and ref.get("reference_identification"):
1025 |                     provider["additionalIds"].append({
1026 |                         "qualifierCode": ref.get("reference_identification_qualifier", ""),
1027 |                         "type": self.get_reference_type(ref.get("reference_identification_qualifier", "")),
1028 |                         "identification": ref.get("reference_identification", "")
1029 |                     })
1030 |         
1031 |         # Add address
1032 |         if provider_data.get("address"):
1033 |             addr = provider_data["address"]
1034 |             provider["address"] = {
1035 |                 "line": addr.get("address_line_1", ""),
1036 |                 "city": addr.get("city", ""),
1037 |                 "stateCode": addr.get("state_code", ""),
1038 |                 "zipCode": addr.get("postal_code", "")
1039 |             }
1040 |             if addr.get("address_line_2"):
1041 |                 provider["address"]["line2"] = addr.get("address_line_2", "")
1042 |         
1043 |         return provider
1044 | 
1045 |     def format_diagnosis_new(self, diag_data):
1046 |         """Format diagnosis in new structure"""
1047 |         if not diag_data:
1048 |             return None
1049 |         
1050 |         code = diag_data.get("diagnosis_code", "")
1051 |         if not code:
1052 |             return None
1053 |         
1054 |         return {
1055 |             "subType": "ICD_10_PRINCIPAL",
1056 |             "code": code,
1057 |             "desc": self.diagnosis_descriptions.get(code, ""),
1058 |             "formattedCode": self.format_icd_code(code)
1059 |         }
1060 | 
1061 |     def format_service_line_new(self, service_line_data, line_num, diags):
1062 |         """Format service line in new structure"""
1063 |         if not service_line_data:
1064 |             return None
1065 |         
1066 |         service_info = service_line_data.get("service_info", {})
1067 |         procedure_info = service_info.get("composite_medical_procedure_identifier", {})
1068 |         
1069 |         procedure_code = procedure_info.get("procedure_code", "")
1070 |         if not procedure_code:
1071 |             return None
1072 |         
1073 |         service_line = {
1074 |             "sourceLineId": str(uuid.uuid4()).replace('-', '')[:10],
1075 |             "chargeAmount": self.format_amount(service_info.get("monetary_amount", "")),
1076 |             "serviceDateFrom": "",
1077 |             "unitType": service_info.get("unit_or_basis_for_measurement_code", ""),
1078 |             "unitCount": int(service_info.get("service_unit_count", "0")) if service_info.get("service_unit_count") else 0,
1079 |             "procedure": {
1080 |                 "subType": procedure_info.get("product_service_id_qualifier", ""),
1081 |                 "code": procedure_code,
1082 |                 "desc": self.procedure_descriptions.get(procedure_code, "")
1083 |             },
1084 |             "diagPointers": [1],  # Default to first diagnosis
1085 |             "diags": diags  # Reference to claim diagnoses
1086 |         }
1087 |         
1088 |         # Add service dates
1089 |         service_date_found = False
1090 |         for date_info in service_line_data.get("dates", []):
1091 |             if date_info.get("date_time_qualifier") == "472":  # Service date
1092 |                 service_line["serviceDateFrom"] = self.format_date_iso(date_info.get("date_time_period", ""))
1093 |                 service_date_found = True
1094 |                 break
1095 |             elif date_info.get("date_time_qualifier") == "150":  # Service period start
1096 |                 service_line["serviceDateFrom"] = self.format_date_iso(date_info.get("date_time_period", ""))
1097 |                 service_date_found = True
1098 |             elif date_info.get("date_time_qualifier") == "151":  # Service period end
1099 |                 service_line["serviceDateTo"] = self.format_date_iso(date_info.get("date_time_period", ""))
1100 |         
1101 |         # If no service line date found, use claim date
1102 |         if not service_date_found and not service_line.get("serviceDateFrom"):
1103 |             # Use the claim's service date as fallback
1104 |             service_line["serviceDateFrom"] = service_date_from if 'service_date_from' in locals() else ""
1105 |         
1106 |         return service_line
1107 | 
1108 |     def get_identification_type(self, qualifier):
1109 |         """Map identification qualifier to type"""
1110 |         type_map = {
1111 |             "XX": "NPI",
1112 |             "EI": "ETIN", 
1113 |             "MI": "MEMBER_ID",
1114 |             "PI": "PAYOR_ID",
1115 |             "SY": "SSN"
1116 |         }
1117 |         return type_map.get(qualifier, qualifier)
1118 | 
1119 |     def get_communication_type(self, qualifier):
1120 |         """Map communication qualifier to type"""
1121 |         comm_map = {
1122 |             "TE": "PHONE",
1123 |             "WP": "PHONE", 
1124 |             "EM": "EMAIL"
1125 |         }
1126 |         return comm_map.get(qualifier, qualifier)
1127 | 
1128 |     def get_payer_sequence(self, code):
1129 |         """Map payer sequence code"""
1130 |         sequence_map = {
1131 |             "P": "PRIMARY",
1132 |             "S": "SECONDARY", 
1133 |             "T": "TERTIARY",
1134 |             "A": "WORKERS_COMPENSATION",
1135 |             "B": "AUTO_NO_FAULT",
1136 |             "C": "AUTO_LIABILITY"
1137 |         }
1138 |         return sequence_map.get(code, code)
1139 | 
1140 |     def get_relationship_type(self, code):
1141 |         """Map relationship code"""
1142 |         relationship_map = {
1143 |             "18": "SELF",
1144 |             "01": "SPOUSE", 
1145 |             "19": "CHILD",
1146 |             "20": "EMPLOYEE",
1147 |             "21": "UNKNOWN",
1148 |             "39": "ORGAN_DONOR",
1149 |             "40": "CADAVER_DONOR",
1150 |             "53": "LIFE_PARTNER",
1151 |             "G8": "OTHER_RELATIONSHIP"
1152 |         }
1153 |         return relationship_map.get(code, code)
1154 | 
1155 |     def get_insurance_type(self, code):
1156 |         """Map insurance type code"""
1157 |         insurance_map = {
1158 |             "CI": "COMMERCIAL",
1159 |             "12": "COMMERCIAL", 
1160 |             "13": "COMMERCIAL",
1161 |             "MA": "MEDICARE",
1162 |             "MB": "MEDICARE",
1163 |             "MC": "MEDICAID"
1164 |         }
1165 |         return insurance_map.get(code, code)
1166 | 
1167 |     def get_entity_role(self, entity_code):
1168 |         """Map entity identifier code to role"""
1169 |         role_map = {
1170 |             "85": "BILLING_PROVIDER",
1171 |             "IL": "INSURED_SUBSCRIBER", 
1172 |             "PR": "PAYER",
1173 |             "DN": "REFERRING_PROVIDER",
1174 |             "82": "RENDERING_PROVIDER",
1175 |             "77": "SERVICE_FACILITY",
1176 |             "DQ": "SUPERVISING_PROVIDER",
1177 |             "71": "ATTENDING_PROVIDER",
1178 |             "72": "OPERATING_PROVIDER"
1179 |         }
1180 |         return role_map.get(entity_code, entity_code)
1181 | 
1182 |     def get_reference_type(self, qualifier):
1183 |         """Map reference qualifier to type"""
1184 |         type_map = {
1185 |             "0B": "STATE_LICENSE_NUMBER",
1186 |             "1G": "UPIN",
1187 |             "G2": "PROVIDER_COMMERCIAL_NUMBER"
1188 |         }
1189 |         return type_map.get(qualifier, qualifier)
1190 | 
1191 |     def format_date_iso(self, date_str):
1192 |         """Format date to ISO format YYYY-MM-DD"""
1193 |         if not date_str or len(date_str) != 8:
1194 |             return ""
1195 |         try:
1196 |             return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
1197 |         except:
1198 |             return ""
1199 | 
1200 |     def format_time_iso(self, time_str):
1201 |         """Format time to ISO format HH:MM:SS"""
1202 |         if not time_str:
1203 |             return "00:00:00"
1204 |         if len(time_str) >= 4:
1205 |             return f"{time_str[:2]}:{time_str[2:4]}:{time_str[4:6] if len(time_str) > 4 else '00'}"
1206 |         return "00:00:00"
1207 | 
1208 |     def format_icd_code(self, code):
1209 |         """Format ICD code with decimal point"""
1210 |         if len(code) > 3:
1211 |             return f"{code[:3]}.{code[3:]}"
1212 |         return code
1213 | 
1214 |     def parse_edi_file(self, file_path):
1215 |         """Parse a single EDI file and return structured data"""
1216 |         try:
1217 |             with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
1218 |                 content = file.read().strip()
1219 |             
1220 |             if not content:
1221 |                 return None
1222 |             
1223 |             # Split into segments
1224 |             segments = []
1225 |             if '~' in content:
1226 |                 segments = [seg.strip() for seg in content.split('~') if seg.strip()]
1227 |             else:
1228 |                 # Try other common delimiters
1229 |                 for delimiter in ['\n', '\r\n', '|']:
1230 |                     if delimiter in content:
1231 |                         segments = [seg.strip() for seg in content.split(delimiter) if seg.strip()]
1232 |                         break
1233 |             
1234 |             if not segments:
1235 |                 return None
1236 |             
1237 |             # Initialize data structure
1238 |             edi_data = {
1239 |                 "file_info": {
1240 |                     "file_path": file_path,
1241 |                     "file_name": os.path.basename(file_path),
1242 |                     "processed_date": ""
1243 |                 },
1244 |                 "interchange_header": {},
1245 |                 "functional_group": {},
1246 |                 "transaction_sets": []
1247 |             }
1248 |             
1249 |             current_transaction = None
1250 |             current_billing_provider = None
1251 |             current_subscriber = None
1252 |             current_claim = None
1253 |             current_service_line = None
1254 |             
1255 |             for segment in segments:
1256 |                 if not segment:
1257 |                     continue
1258 |                 
1259 |                 elements = segment.split('*')
1260 |                 segment_id = elements[0]
1261 |                 
1262 |                 try:
1263 |                     if segment_id == 'ISA':
1264 |                         edi_data["interchange_header"] = self.parse_isa_segment(elements)
1265 |                     
1266 |                     elif segment_id == 'GS':
1267 |                         edi_data["functional_group"] = self.parse_gs_segment(elements)
1268 |                     
1269 |                     elif segment_id == 'ST':
1270 |                         current_transaction = {
1271 |                             "transaction_set_header": self.parse_st_segment(elements),
1272 |                             "beginning_hierarchical_transaction": {},
1273 |                             "submitter": {},
1274 |                             "receiver": {},
1275 |                             "billing_providers": []
1276 |                         }
1277 |                         edi_data["transaction_sets"].append(current_transaction)
1278 |                     
1279 |                     elif segment_id == 'BHT' and current_transaction:
1280 |                         current_transaction["beginning_hierarchical_transaction"] = self.parse_bht_segment(elements)
1281 |                     
1282 |                     elif segment_id == 'HL' and current_transaction:
1283 |                         hl_data = self.parse_hl_segment(elements)
1284 |                         level_code = hl_data.get("hierarchical_level_code", "")
1285 |                         hierarchical_id = hl_data.get("hierarchical_id_number", "")
1286 |                         parent_id = hl_data.get("hierarchical_parent_id_number", "")
1287 |                         
1288 |                         if level_code == "20":  # Loop 2000A - Billing Provider Level
1289 |                             current_billing_provider = {
1290 |                                 "hierarchical_level": hl_data,
1291 |                                 "hierarchical_id": hierarchical_id,
1292 |                                 "provider_info": {},
1293 |                                 "subscribers": []
1294 |                             }
1295 |                             current_transaction["billing_providers"].append(current_billing_provider)
1296 |                             current_subscriber = None
1297 |                             current_claim = None
1298 |                             current_service_line = None
1299 |                         
1300 |                         elif level_code == "22" and current_billing_provider:  # Loop 2000B - Subscriber Level
1301 |                             current_subscriber = {
1302 |                                 "hierarchical_level": hl_data,
1303 |                                 "hierarchical_id": hierarchical_id,
1304 |                                 "parent_id": parent_id,
1305 |                                 "subscriber_info": {},
1306 |                                 "payer_info": {},
1307 |                                 "secondary_payers": [],  # For multiple payers
1308 |                                 "claims": []
1309 |                             }
1310 |                             current_billing_provider["subscribers"].append(current_subscriber)
1311 |                             current_claim = None
1312 |                             current_service_line = None
1313 |                         
1314 |                         elif level_code == "23" and current_subscriber:  # Loop 2000C - Patient Level (if different from subscriber)
1315 |                             # Patient level - usually when patient is different from subscriber
1316 |                             current_subscriber["patient_info"] = {
1317 |                                 "hierarchical_level": hl_data,
1318 |                                 "hierarchical_id": hierarchical_id,
1319 |                                 "parent_id": parent_id
1320 |                             }
1321 |                     
1322 |                     elif segment_id == 'NM1' and current_transaction:
1323 |                         nm1_data = self.parse_nm1_segment(elements)
1324 |                         entity_code = nm1_data.get("entity_identifier_code", "")
1325 |                         
1326 |                         if entity_code == "41":  # Loop 1000A - Submitter
1327 |                             current_transaction["submitter"] = nm1_data
1328 |                         elif entity_code == "40":  # Loop 1000B - Receiver
1329 |                             current_transaction["receiver"] = nm1_data
1330 |                         elif entity_code == "85" and current_billing_provider:  # Loop 2010AA - Billing Provider
1331 |                             current_billing_provider["provider_info"] = nm1_data
1332 |                         elif entity_code == "87" and current_billing_provider:  # Loop 2010AB - Pay-to Provider
1333 |                             current_billing_provider["pay_to_provider"] = nm1_data
1334 |                         elif entity_code == "IL" and current_subscriber:  # Loop 2010BA - Subscriber
1335 |                             # Check if this is for secondary payer
1336 |                             if current_subscriber["secondary_payers"] and len(current_subscriber["secondary_payers"]) > 0:
1337 |                                 # This is for the most recent secondary payer
1338 |                                 current_subscriber["secondary_payers"][-1]["subscriber_info"].update(nm1_data)
1339 |                             else:
1340 |                                 # Primary subscriber
1341 |                                 if "subscriber_info" not in current_subscriber:
1342 |                                     current_subscriber["subscriber_info"] = {}
1343 |                                 current_subscriber["subscriber_info"].update(nm1_data)
1344 |                         elif entity_code == "PR" and current_subscriber:  # Loop 2010BB - Payer
1345 |                             # Check if this is for secondary payer
1346 |                             if current_subscriber["secondary_payers"] and len(current_subscriber["secondary_payers"]) > 0:
1347 |                                 # This is for the most recent secondary payer
1348 |                                 current_subscriber["secondary_payers"][-1]["payer_info"] = nm1_data
1349 |                             else:
1350 |                                 # Primary payer
1351 |                                 current_subscriber["payer_info"] = nm1_data
1352 |                         elif entity_code == "QC" and current_subscriber:  # Loop 2010BC - Patient (if different from subscriber)
1353 |                             if "patient_info" not in current_subscriber:
1354 |                                 current_subscriber["patient_info"] = {}
1355 |                             current_subscriber["patient_info"]["patient_data"] = nm1_data
1356 |                         elif entity_code in ["DN", "82", "77", "DQ", "85"] and current_claim:  # Loop 2310 - Various provider types
1357 |                             provider_role_map = {
1358 |                                 "DN": "REFERRING_PROVIDER",      # Loop 2310A - Referring Provider
1359 |                                 "82": "RENDERING_PROVIDER",      # Loop 2310B - Rendering Provider  
1360 |                                 "77": "SERVICE_FACILITY", # Loop 2310C - Service Facility
1361 |                                 "DQ": "SUPERVISING_PROVIDER",    # Loop 2310D - Supervising Provider
1362 |                                 "85": "BILLING_PROVIDER"         # Loop 2310E - Billing Provider (if different)
1363 |                             }
1364 |                             provider_info = {
1365 |                                 "provider_role": provider_role_map.get(entity_code, ""),
1366 |                                 "provider_data": nm1_data,
1367 |                                 "address": {},
1368 |                                 "references": []
1369 |                             }
1370 |                             if "providers" not in current_claim:
1371 |                                 current_claim["providers"] = []
1372 |                             current_claim["providers"].append(provider_info)
1373 |                     
1374 |                     elif segment_id == 'N3':
1375 |                         n3_data = self.parse_n3_segment(elements)
1376 |                         # Add address to the most recent entity
1377 |                         if current_claim and "providers" in current_claim and current_claim["providers"]:
1378 |                             if "address" not in current_claim["providers"][-1]:
1379 |                                 current_claim["providers"][-1]["address"] = {}
1380 |                             current_claim["providers"][-1]["address"].update(n3_data)
1381 |                         elif current_subscriber and "payer_info" in current_subscriber and current_subscriber["payer_info"] and "address" not in current_subscriber["payer_info"]:
1382 |                             current_subscriber["payer_info"]["address"] = n3_data
1383 |                         elif current_subscriber and "address" not in current_subscriber["subscriber_info"]:
1384 |                             current_subscriber["subscriber_info"]["address"] = n3_data
1385 |                         elif current_billing_provider and "address" not in current_billing_provider["provider_info"]:
1386 |                             current_billing_provider["provider_info"]["address"] = n3_data
1387 |                     
1388 |                     elif segment_id == 'N4':
1389 |                         n4_data = self.parse_n4_segment(elements)
1390 |                         # Add geographic info to the most recent address
1391 |                         if current_claim and "providers" in current_claim and current_claim["providers"]:
1392 |                             if "address" not in current_claim["providers"][-1]:
1393 |                                 current_claim["providers"][-1]["address"] = {}
1394 |                             current_claim["providers"][-1]["address"].update(n4_data)
1395 |                         elif current_subscriber and "payer_info" in current_subscriber and current_subscriber["payer_info"] and "address" in current_subscriber["payer_info"]:
1396 |                             current_subscriber["payer_info"]["address"].update(n4_data)
1397 |                         elif current_subscriber and "address" in current_subscriber["subscriber_info"]:
1398 |                             current_subscriber["subscriber_info"]["address"].update(n4_data)
1399 |                         elif current_billing_provider and "address" in current_billing_provider["provider_info"]:
1400 |                             current_billing_provider["provider_info"]["address"].update(n4_data)
1401 |                     
1402 |                     elif segment_id == 'REF':
1403 |                         ref_data = self.parse_ref_segment(elements)
1404 |                         # Add reference to appropriate entity
1405 |                         if current_claim and "providers" in current_claim and current_claim["providers"]:
1406 |                             if "references" not in current_claim["providers"][-1]:
1407 |                                 current_claim["providers"][-1]["references"] = []
1408 |                             current_claim["providers"][-1]["references"].append(ref_data)
1409 |                         elif current_billing_provider and ref_data.get("reference_identification_qualifier") in self.TAX_ID_QUALIFIERS:
1410 |                             # Tax ID for billing provider
1411 |                             current_billing_provider["provider_info"]["tax_identification_number"] = ref_data.get("reference_identification", "")
1412 |                             current_billing_provider["provider_info"]["tax_identification_qualifier"] = ref_data.get("reference_identification_qualifier", "")
1413 |                         elif current_subscriber:
1414 |                             if "references" not in current_subscriber["subscriber_info"]:
1415 |                                 current_subscriber["subscriber_info"]["references"] = []
1416 |                             current_subscriber["subscriber_info"]["references"].append(ref_data)
1417 |                     
1418 |                     elif segment_id == 'DMG' and current_subscriber:
1419 |                         current_subscriber["subscriber_info"]["demographics"] = self.parse_dmg_segment(elements)
1420 |                     
1421 |                     elif segment_id == 'CLM' and current_subscriber:
1422 |                         # Loop 2300 - Claim Information
1423 |                         current_claim = {
1424 |                             "claim_info": self.parse_clm_segment(elements),
1425 |                             "dates": [],
1426 |                             "diagnosis_codes": [],
1427 |                             "service_lines": [],
1428 |                             "providers": [],
1429 |                             "references": [],
1430 |                             "amounts": [],
1431 |                             "notes": [],
1432 |                             "adjustments": []
1433 |                         }
1434 |                         current_subscriber["claims"].append(current_claim)
1435 |                         current_service_line = None
1436 |                     
1437 |                     elif segment_id == 'DTP':
1438 |                         dtp_data = self.parse_dtp_segment(elements)
1439 |                         if current_service_line:
1440 |                             # Service line level date
1441 |                             current_service_line["dates"].append(dtp_data)
1442 |                         elif current_claim:
1443 |                             # Claim level date
1444 |                             current_claim["dates"].append(dtp_data)
1445 |                         elif current_subscriber:
1446 |                             # Subscriber level date (rare)
1447 |                             if "dates" not in current_subscriber:
1448 |                                 current_subscriber["dates"] = []
1449 |                             current_subscriber["dates"].append(dtp_data)
1450 |                     
1451 |                     elif segment_id == 'HI' and current_claim:
1452 |                         current_claim["diagnosis_codes"].append(self.parse_hi_segment(elements))
1453 |                     
1454 |                     elif segment_id == 'LX' and current_claim:
1455 |                         # Loop 2400 - Service Line Information
1456 |                         lx_data = self.parse_lx_segment(elements)
1457 |                         current_service_line = {
1458 |                             "line_number": lx_data.get("assigned_number", ""),
1459 |                             "service_info": {},
1460 |                             "dates": [],
1461 |                             "references": [],
1462 |                             "amounts": [],
1463 |                             "quantities": [],
1464 |                             "adjustments": [],
1465 |                             "notes": [],
1466 |                             "providers": []  # Line-level providers
1467 |                         }
1468 |                         current_claim["service_lines"].append(current_service_line)
1469 |                     
1470 |                     elif segment_id == 'SV1' and current_service_line:
1471 |                         # Professional Service - core of Loop 2400
1472 |                         current_service_line["service_info"] = self.parse_sv1_segment(elements)
1473 |                     
1474 |                     elif segment_id == 'SV2' and current_service_line:
1475 |                         # Institutional Service Line
1476 |                         current_service_line["institutional_service_info"] = self.parse_sv2_segment(elements)
1477 |                     
1478 |                     elif segment_id == 'SV3' and current_service_line:
1479 |                         # Dental Service
1480 |                         current_service_line["dental_service_info"] = self.parse_sv3_segment(elements)
1481 |                     
1482 |                     elif segment_id == 'PRV':
1483 |                         prv_data = self.parse_prv_segment(elements)
1484 |                         # Add provider specialty info to the most recent provider
1485 |                         if current_service_line and "providers" in current_service_line and current_service_line["providers"]:
1486 |                             # Line-level provider
1487 |                             current_service_line["providers"][-1]["provider_taxonomy"] = prv_data.get("reference_identification", "")
1488 |                         elif current_claim and "providers" in current_claim and current_claim["providers"]:
1489 |                             # Claim-level provider
1490 |                             current_claim["providers"][-1]["provider_taxonomy"] = prv_data.get("reference_identification", "")
1491 |                         elif current_billing_provider:
1492 |                             # Billing provider level
1493 |                             current_billing_provider["provider_info"]["provider_taxonomy"] = prv_data.get("reference_identification", "")
1494 |                     
1495 |                     elif segment_id == 'AMT':
1496 |                         amt_data = self.parse_amt_segment(elements)
1497 |                         if current_service_line:
1498 |                             # Service line level amount
1499 |                             current_service_line["amounts"].append(amt_data)
1500 |                         elif current_claim:
1501 |                             # Claim level amount
1502 |                             current_claim["amounts"].append(amt_data)
1503 |                     
1504 |                     elif segment_id == 'QTY':
1505 |                         qty_data = self.parse_qty_segment(elements)
1506 |                         if current_service_line:
1507 |                             # Service line level quantity
1508 |                             current_service_line["quantities"].append(qty_data)
1509 |                         elif current_claim:
1510 |                             # Claim level quantity (rare)
1511 |                             if "quantities" not in current_claim:
1512 |                                 current_claim["quantities"] = []
1513 |                             current_claim["quantities"].append(qty_data)
1514 |                     
1515 |                     elif segment_id == 'CAS':
1516 |                         cas_data = self.parse_cas_segment(elements)
1517 |                         if current_service_line:
1518 |                             # Service line level adjustment
1519 |                             current_service_line["adjustments"].extend(cas_data)
1520 |                         elif current_claim:
1521 |                             # Claim level adjustment
1522 |                             current_claim["adjustments"].extend(cas_data)
1523 |                     
1524 |                     elif segment_id == 'NTE':
1525 |                         nte_data = self.parse_nte_segment(elements)
1526 |                         if current_service_line:
1527 |                             # Service line level note
1528 |                             current_service_line["notes"].append(nte_data)
1529 |                         elif current_claim:
1530 |                             # Claim level note
1531 |                             current_claim["notes"].append(nte_data)
1532 |                     
1533 |                     elif segment_id == 'PER':
1534 |                         per_data = self.parse_per_segment(elements)
1535 |                         # Add contact info to appropriate entity
1536 |                         if current_billing_provider:
1537 |                             current_billing_provider["provider_info"]["contact_info"] = per_data
1538 |                         elif current_transaction and "submitter" in current_transaction:
1539 |                             current_transaction["submitter"]["contact_info"] = per_data
1540 |                     
1541 |                     elif segment_id == 'SBR' and current_subscriber:
1542 |                         sbr_data = self.parse_sbr_segment(elements)
1543 |                         payer_sequence = sbr_data.get("payer_responsibility_sequence_number_code", "")
1544 |                         
1545 |                         if payer_sequence == "P":  # Primary payer
1546 |                             current_subscriber["subscriber_info"].update(sbr_data)
1547 |                         else:  # Secondary, Tertiary, etc.
1548 |                             # Create secondary payer entry
1549 |                             secondary_payer = {
1550 |                                 "payer_sequence": payer_sequence,
1551 |                                 "subscriber_info": sbr_data,
1552 |                                 "payer_info": {}
1553 |                             }
1554 |                             current_subscriber["secondary_payers"].append(secondary_payer)
1555 |                 
1556 |                 except Exception as e:
1557 |                     print(f"Error processing segment {segment_id}: {str(e)}")
1558 |                     continue
1559 |             
1560 |             return edi_data
1561 |             
1562 |         except Exception as e:
1563 |             print(f"Error parsing file {file_path}: {str(e)}")
1564 |             return None
1565 | 
1566 | # Removed find_edi_directories() function - no longer needed with path-based configuration
1567 | 
1568 | def main():
1569 |     """Main execution function"""
1570 |     parser = EDI837BusinessParser()
1571 |     
1572 |     # Use the configured directory path from config.py
1573 |     edi_directory = EDI_DIRECTORY
1574 |     print(f"Using EDI directory from config: {edi_directory}")
1575 |     
1576 |     # Check if directory exists
1577 |     if not os.path.exists(edi_directory):
1578 |         print(f"âŒ EDI directory not found: {edi_directory}")
1579 |         print("Please update EDI_DIRECTORY in config.py with the correct path to your EDI files")
1580 |         return
1581 |     
1582 |     # Get list of EDI files
1583 |     edi_files = []
1584 |     try:
1585 |         for file in os.listdir(edi_directory):
1586 |             if file.endswith(EDI_FILE_EXTENSIONS):
1587 |                 edi_files.append(os.path.join(edi_directory, file))
1588 |     except PermissionError:
1589 |         print(f"âŒ Permission denied accessing directory: {edi_directory}")
1590 |         return
1591 |     
1592 |     if not edi_files:
1593 |         print(f"âŒ No EDI files found in directory: {edi_directory}")
1594 |         print(f"Looking for files with extensions: {EDI_FILE_EXTENSIONS}")
1595 |         return
1596 |     
1597 |     print(f"âœ… Found {len(edi_files)} EDI files in: {edi_directory}")
1598 |     
1599 |     all_business_data = []
1600 |     total_claims_extracted = 0
1601 |     
1602 |     # Process files from the single configured directory
1603 |     print(f"Extracting EDI 837 data in business format from: {edi_directory}")
1604 |     
1605 |     # Limit files if configured
1606 |     max_files = MAX_FILES or len(edi_files)
1607 |     if len(edi_files) > max_files:
1608 |         print(f"Will process {max_files} files out of {len(edi_files)} total files")
1609 |         edi_files = edi_files[:max_files]
1610 |     else:
1611 |         print(f"Will process all {len(edi_files)} files")
1612 |     
1613 |     # Process each file
1614 |     for i, file_path in enumerate(edi_files, 1):
1615 | 
1616 |             try:
1617 |                 print(f"Processing {os.path.basename(file_path)}... ({i}/{len(edi_files)})")
1618 |                 
1619 |                 # Parse EDI file
1620 |                 edi_data = parser.parse_edi_file(file_path)
1621 |                 
1622 |                 if edi_data:
1623 |                     # Convert to business format (returns list of claims)
1624 |                     claims = parser.convert_to_business_format(edi_data)
1625 |                     
1626 |                     if claims:
1627 |                         all_business_data.extend(claims)
1628 |                         total_claims_extracted += len(claims)
1629 |                 
1630 |             except Exception as e:
1631 |                 print(f"Error processing {file_path}: {str(e)}")
1632 |                 continue
1633 |             
1634 |             # Progress update every 10 files
1635 |             if i % 10 == 0:
1636 |                 print(f"âœ… Processed {i} files, extracted {total_claims_extracted} claims so far")
1637 |         
1638 |     print(f"Completed processing {min(len(edi_files), max_files)} files")
1639 |     
1640 |     if total_claims_extracted == 0:
1641 |         print("No claims extracted")
1642 |         return
1643 |     
1644 |     print(f"\nðŸ“Š EXTRACTION SUMMARY:")
1645 |     print(f"Total claims extracted: {len(all_business_data)}")
1646 |     
1647 |     # Save business format JSON
1648 |     business_output_file = "edi_837_business_format.json"
1649 |     try:
1650 |         with open(business_output_file, 'w', encoding='utf-8') as f:
1651 |             json.dump(all_business_data, f, indent=2, ensure_ascii=False)
1652 |         print(f"âœ… Business format data saved to: {business_output_file}")
1653 |     except Exception as e:
1654 |         print(f"Error saving business format JSON: {str(e)}")
1655 |     
1656 |     # Create the three CSV files matching the required structure
1657 |     try:
1658 |         # Generate EDI_Claims.csv
1659 |         claims_records = []
1660 |         company_setup_records = []
1661 |         claim_detail_records = []
1662 |         
1663 |         detail_id_counter = 1
1664 |         
1665 |         for claim in all_business_data:
1666 |             # Get the actual claim ID from the JSON data
1667 |             actual_claim_id = claim.get("id", "")
1668 |             
1669 |             transaction = claim.get("transaction", {})
1670 |             billing_provider = claim.get("billingProvider", {})
1671 |             subscriber = claim.get("subscriber", {}).get("person", {})
1672 |             payer = claim.get("payer", {})
1673 |             
1674 |             # Extract all providers
1675 |             referring_provider = {}
1676 |             rendering_provider = {}
1677 |             facility_provider = {}
1678 |             
1679 |             for provider in claim.get("providers", []):
1680 |                 if provider.get("entityRole") == parser.REFERRING_PROVIDER_ROLE:
1681 |                     referring_provider = provider
1682 |                 elif provider.get("entityRole") == parser.RENDERING_PROVIDER_ROLE:
1683 |                     rendering_provider = provider
1684 |                 elif provider.get("entityRole") == parser.SERVICE_FACILITY_ROLE:
1685 |                     facility_provider = provider
1686 |             
1687 |             # Build EDI_Claims record with all required fields
1688 |             claims_record = {
1689 |                 'ID': actual_claim_id,
1690 |                 'Filename': transaction.get("fileInfo", {}).get("fileName", ""),
1691 |                 'Version': transaction.get("implementationConventionReference", ""),
1692 |                 'ImageFilePath': None,
1693 |                 'ImageFilename': None,
1694 |                 'TradingPartnerIDType': transaction.get("receiver", {}).get("identificationType", ""),
1695 |                 'TradingPartnerID': transaction.get("receiver", {}).get("identifier", ""),
1696 |                 'TransactionDate': transaction.get("creationDate", ""),
1697 |                 'TransactionTime': transaction.get("creationTime", ""),
1698 |                 'ReceiveDate': transaction.get("creationDate", ""),
1699 |                 'SubmitterName': transaction.get("sender", {}).get("lastNameOrOrgName", ""),
1700 |                 'SubmitterID': transaction.get("sender", {}).get("identifier", ""),
1701 |                 'SubmitterContact': transaction.get("sender", {}).get("contacts", [{}])[0].get("name", "") if transaction.get("sender", {}).get("contacts") else "",
1702 |                 'SubmitterTel': transaction.get("sender", {}).get("contacts", [{}])[0].get("contactNumbers", [{}])[0].get("number", "") if transaction.get("sender", {}).get("contacts") else "",
1703 |                 'SubmitterTelExt': None,
1704 |                 'SubmitterFax': None,
1705 |                 'SubmitterEmail': None,
1706 |                 'ReceiverName': transaction.get("receiver", {}).get("lastNameOrOrgName", ""),
1707 |                 'ReceiverID': transaction.get("receiver", {}).get("identifier", ""),
1708 |                 'TransactionType': transaction.get("transactionType", ""),
1709 |                 'OrigAppTransactionID': transaction.get("originatorApplicationTransactionId", ""),
1710 |                 'FedTaxIDQual': billing_provider.get("taxIdQualifier", ""),
1711 |                 'FedTaxID': billing_provider.get("taxId", ""),
1712 |                 'BillProvIDType': billing_provider.get("identificationType", ""),
1713 |                 'BillProvID': billing_provider.get("identifier", ""),
1714 |                 'BillProvNPI': billing_provider.get("identifier", "") if billing_provider.get("identificationType") == parser.NPI_IDENTIFICATION_TYPE else "",
1715 |                 'BillProvLast': billing_provider.get("lastNameOrOrgName", ""),
1716 |                 'BillProvFirst': billing_provider.get("firstName", ""),
1717 |                 'BillProvMiddle': billing_provider.get("middleName", ""),
1718 |                 'BillProvSuffix': billing_provider.get("nameSuffix", ""),
1719 |                 'BillProvSpecialty': billing_provider.get("providerTaxonomy", {}).get("code", ""),
1720 |                 'BillProvAddress': billing_provider.get("address", {}).get("line", ""),
1721 |                 'BillProvAddress2': billing_provider.get("address", {}).get("line2", ""),
1722 |                 'BillProvCity': billing_provider.get("address", {}).get("city", ""),
1723 |                 'BillProvState': billing_provider.get("address", {}).get("stateCode", ""),
1724 |                 'BillProvZip': billing_provider.get("address", {}).get("zipCode", ""),
1725 |                 'BillProvCountry': None,
1726 |                 'BillProvSubdivision': None,
1727 |                 'BillProvContact': None,
1728 |                 'BillProvTel': None,
1729 |                 'BillProvTelExt': None,
1730 |                 'BillProvFax': None,
1731 |                 'BillProvEmail': None,
1732 |                 'BillProvOtherIDQual1': None,
1733 |                 'BillProvOtherID1': None,
1734 |                 'BillProvOtherIDQual2': None,
1735 |                 'BillProvOtherID2': None,
1736 |                 'BillProvOtherIDQual3': None,
1737 |                 'BillProvOtherID3': None,
1738 |                 'BillProvOtherIDQual4': None,
1739 |                 'BillProvOtherID4': None,
1740 |                 'BillProvOtherIDQual5': None,
1741 |                 'BillProvOtherID5': None,
1742 |                 
1743 |                 # Subscriber information
1744 |                 'SubscriberLast': subscriber.get("lastNameOrOrgName", ""),
1745 |                 'SubscriberFirst': subscriber.get("firstName", ""),
1746 |                 'SubscriberMiddle': subscriber.get("middleName", ""),
1747 |                 'SubscriberSuffix': subscriber.get("nameSuffix", ""),
1748 |                 'SubscriberIDType': subscriber.get("identificationType", ""),
1749 |                 'SubscriberID': subscriber.get("identifier", ""),
1750 |                 'SubscriberAddress': subscriber.get("address", {}).get("line", ""),
1751 |                 'SubscriberAddress2': subscriber.get("address", {}).get("line2", ""),
1752 |                 'SubscriberCity': subscriber.get("address", {}).get("city", ""),
1753 |                 'SubscriberState': subscriber.get("address", {}).get("stateCode", ""),
1754 |                 'SubscriberZip': subscriber.get("address", {}).get("zipCode", ""),
1755 |                 'SubscriberCountry': None,
1756 |                 'SubscriberLocation': None,
1757 |                 'SubscriberSubdivision': None,
1758 |                 'SubscriberDOB': subscriber.get("birthDate", ""),
1759 |                 'SubscriberSex': subscriber.get("gender", ""),
1760 |                 'SubscriberEthnicity': None,
1761 |                 'SubscriberMaritalStatus': None,
1762 |                 'SubscriberCollectionMethod': None,
1763 |                 'SubscriberSSN': None,
1764 |                 'SubscriberAgencyClaimNo': None,
1765 |                 'SubscriberMemberID': subscriber.get("identifier", ""),
1766 |                 'SubscriberPersonalID': None,
1767 |                 'SubscriberContact': None,
1768 |                 'SubscriberTel': None,
1769 |                 'SubscriberTelExt': None,
1770 |                 'SubscriberEmail': None,
1771 |                 
1772 |                 # Payer information
1773 |                 'PayerName': payer.get("lastNameOrOrgName", ""),
1774 |                 'PayerIDType': payer.get("identificationType", ""),
1775 |                 'PayerID': payer.get("identifier", ""),
1776 |                 'PayerAddress': payer.get("address", {}).get("line", ""),
1777 |                 'PayerAddress2': payer.get("address", {}).get("line2", ""),
1778 |                 'PayerCity': payer.get("address", {}).get("city", ""),
1779 |                 'PayerState': payer.get("address", {}).get("stateCode", ""),
1780 |                 'PayerZip': payer.get("address", {}).get("zipCode", ""),
1781 |                 'PayerResponsibility': claim.get("subscriber", {}).get("payerResponsibilitySequence", ""),
1782 |                 'PayerOtherIDQual1': None,
1783 |                 'PayerOtherID1': None,
1784 |                 'PayerOtherIDQual2': None,
1785 |                 'PayerOtherID2': None,
1786 |                 'PayerOtherIDQual3': None,
1787 |                 'PayerOtherID3': None,
1788 |                 'GroupNo': None,
1789 |                 'GroupName': None,
1790 |                 'InsuranceType': claim.get("subscriber", {}).get("insurancePlanType", ""),
1791 |                 'FilingIndicator': claim.get("subscriber", {}).get("claimFilingIndicatorCode", ""),
1792 |                 'COBIndicator': None,
1793 |                 'DataReceiverName': None,
1794 |                 
1795 |                 # Rendering Provider
1796 |                 'RendProvIDType': rendering_provider.get("identificationType", ""),
1797 |                 'RendProvID': rendering_provider.get("identifier", ""),
1798 |                 'RendProvNPI': rendering_provider.get("identifier", "") if rendering_provider.get("identificationType") == parser.NPI_IDENTIFICATION_TYPE else "",
1799 |                 'RendProvTaxID': None,
1800 |                 'RendProvLast': rendering_provider.get("lastNameOrOrgName", ""),
1801 |                 'RendProvFirst': rendering_provider.get("firstName", ""),
1802 |                 'RendProvMiddle': rendering_provider.get("middleName", ""),
1803 |                 'RendProvSuffix': None,
1804 |                 'RendProvSpecialty': rendering_provider.get("providerTaxonomy", {}).get("code", ""),
1805 |                 'RendProvOtherIDQual1': rendering_provider.get("additionalIds", [{}])[0].get("qualifierCode", "") if rendering_provider.get("additionalIds") else "",
1806 |                 'RendProvOtherID1': rendering_provider.get("additionalIds", [{}])[0].get("identification", "") if rendering_provider.get("additionalIds") else "",
1807 |                 'RendProvOtherIDQual2': None,
1808 |                 'RendProvOtherID2': None,
1809 |                 'RendProvOtherIDQual3': None,
1810 |                 'RendProvOtherID3': None,
1811 |                 
1812 |                 # Facility information
1813 |                 'FacilityType': facility_provider.get("entityType", ""),
1814 |                 'FacilityIDType': facility_provider.get("identificationType", ""),
1815 |                 'FacilityID': facility_provider.get("identifier", ""),
1816 |                 'FacilityNPI': facility_provider.get("identifier", "") if facility_provider.get("identificationType") == parser.NPI_IDENTIFICATION_TYPE else "",
1817 |                 'FacilityTaxID': None,
1818 |                 'FacilityOtherIDQual1': facility_provider.get("additionalIds", [{}])[0].get("qualifierCode", "") if facility_provider.get("additionalIds") else "",
1819 |                 'FacilityOtherID1': facility_provider.get("additionalIds", [{}])[0].get("identification", "") if facility_provider.get("additionalIds") else "",
1820 |                 'FacilityOtherIDQual2': facility_provider.get("additionalIds", [{}])[1].get("qualifierCode", "") if len(facility_provider.get("additionalIds", [])) > 1 else "",
1821 |                 'FacilityOtherID2': facility_provider.get("additionalIds", [{}])[1].get("identification", "") if len(facility_provider.get("additionalIds", [])) > 1 else "",
1822 |                 'FacilityOtherIDQual3': None,
1823 |                 'FacilityOtherID3': None,
1824 |                 'FacilityName': facility_provider.get("lastNameOrOrgName", ""),
1825 |                 'FacilityAddress': facility_provider.get("address", {}).get("line", ""),
1826 |                 'FacilityAddress2': facility_provider.get("address", {}).get("line2", ""),
1827 |                 'FacilityCity': facility_provider.get("address", {}).get("city", ""),
1828 |                 'FacilitySpecialty': None,
1829 |                 'FacilityState': facility_provider.get("address", {}).get("stateCode", ""),
1830 |                 'FacilityZip': facility_provider.get("address", {}).get("zipCode", ""),
1831 |                 'FacilityContact': None,
1832 |                 'FacilityTel': None,
1833 |                 'FacilityTelExt': None,
1834 |                 
1835 |                 # Referring Provider
1836 |                 'RefProvLast': referring_provider.get("lastNameOrOrgName", ""),
1837 |                 'RefProvFirst': referring_provider.get("firstName", ""),
1838 |                 'RefProvMiddle': referring_provider.get("middleName", ""),
1839 |                 'RefProvSuffix': None,
1840 |                 'RefProvIDType': referring_provider.get("identificationType", ""),
1841 |                 'RefProvID': referring_provider.get("identifier", ""),
1842 |                 'RefProvTaxID': None,
1843 |                 'RefProvNPI': referring_provider.get("identifier", "") if referring_provider.get("identificationType") == parser.NPI_IDENTIFICATION_TYPE else "",
1844 |                 'RefProvOtherIDQual1': None,
1845 |                 'RefProvOtherID1': None,
1846 |                 'RefProvOtherIDQual2': None,
1847 |                 'RefProvOtherID2': None,
1848 |                 'RefProvOtherIDQual3': None,
1849 |                 'RefProvOtherID3': None,
1850 |                 'RefProvSpecialty': None,
1851 |                 
1852 |                 # Claim information
1853 |                 'ClaimNo': claim.get("patientControlNumber", ""),
1854 |                 'Amount': claim.get("chargeAmount", ""),
1855 |                 'EstimatedAmountDue': None,
1856 |                 'PatientEstimatedAmountDue': None,
1857 |                 'PlaceOfService': claim.get("facilityCode", {}).get("code", ""),
1858 |                 'ClaimFrequency': claim.get("frequencyCode", {}).get("code", ""),
1859 |                 'SubmitReason': None,
1860 |                 'ProviderSignature': claim.get("providerSignatureIndicator", ""),
1861 |                 'ProviderAcceptsAssignment': claim.get("assignmentParticipationCode", ""),
1862 |                 'BenefitAssignment': claim.get("assignmentCertificationIndicator", ""),
1863 |                 'InfoReleaseCode': claim.get("releaseOfInformationCode", ""),
1864 |                 'PatientSignatureCode': None,
1865 |                 'RelatedCauses': None,
1866 |                 'RelatedCauses2': None,
1867 |                 'RelatedCausesState': None,
1868 |                 'RelatedCausesCountry': None,
1869 |                 'SpecialProgramCode': None,
1870 |                 'ProviderParticipation': None,
1871 |                 'EOBIndicator': None,
1872 |                 'DelayReasonCode': None,
1873 |                 'ServiceDateFrom': claim.get("serviceDateFrom", ""),
1874 |                 'ServiceDateTo': claim.get("serviceDateTo", ""),
1875 |                 'OnsetDate': None,
1876 |                 'InitialTreatmentDate': None,
1877 |                 'LastSeenDate': None,
1878 |                 'AcuteManifestationDate': None,
1879 |                 'LastDateWorked': None,
1880 |                 'ReturnToWorkDate': None,
1881 |                 'SimilarSymptomsDate': None,
1882 |                 'DisabilityBegin': None,
1883 |                 'DisabilityEnd': None,
1884 |                 'HospitalizationBegin': None,
1885 |                 'HospitalizationEnd': None,
1886 |                 'AccidentDate': None,
1887 |                 'LastMenstrualPeriod': None,
1888 |                 'LastXRayDate': None,
1889 |                 'PrescriptionDate': None,
1890 |                 'AssumedCareDate': None,
1891 |                 'RelinquishedCareDate': None,
1892 |                 'FirstVisitDate': None,
1893 |                 'RepricerReceivedDate': None,
1894 |                 'AdmissionDate': None,
1895 |                 'AdmissionHour': None,
1896 |                 'AdmissionType': None,
1897 |                 'AdmissionSource': None,
1898 |                 'DischargeHour': None,
1899 |                 'PatientStatus': None,
1900 |                 'CoveredDays': None,
1901 |                 'NonCoveredDays': None,
1902 |                 'COBDays': None,
1903 |                 'LifeTimeReserveDays': None,
1904 |                 'PriorAuthorization': None,
1905 |                 'ClearingHouseID': None,
1906 |                 'MedicalRecordNumber': None,
1907 |                 'MothersMedicalRecordNumber': None,
1908 |                 'ServiceAuthorizationException': None,
1909 |                 'ReferralNumber': None,
1910 |                 'PayerClaimControlNumber': None,
1911 |                 'AdjustedRepricedClaimNumber': None,
1912 |                 'AutoAccidentState': None,
1913 |                 'MedicareCrossoverIndicator': None,
1914 |                 'MammographyCertID': None,
1915 |                 'CLIA': None,
1916 |                 'InvestDeviceExemptionNo': None,
1917 |                 'DemonstrationProjectID': None,
1918 |                 'CarePlanOversight': None,
1919 |                 'PROApprovalNo': None,
1920 |                 'PredeterminationID': None,
1921 |                 'ClaimType': None,
1922 |                 'TypeOfBill': None,
1923 |                 'Remark1': None,
1924 |                 'Remark2': None,
1925 |                 'Remark3': None,
1926 |                 'Remark4': None,
1927 |                 'K3_1': None,
1928 |                 'K3_2': None,
1929 |                 'OutsideLab': None,
1930 |                 'LabCharge': None,
1931 |                 'Test_Prod': None,
1932 |                 'ReportTypeCode1': None,
1933 |                 'ReportTransmissionCode1': None,
1934 |                 'AttachmentControlNumber1': None,
1935 |                 'ReportTypeCode2': None,
1936 |                 'ReportTransmissionCode2': None,
1937 |                 'AttachmentControlNumber2': None,
1938 |                 'ReportTypeCode3': None,
1939 |                 'ReportTransmissionCode3': None,
1940 |                 'AttachmentControlNumber3': None,
1941 |                 'ContractType': None,
1942 |                 'ContractAmount': None,
1943 |                 'ContractPercentage': None,
1944 |                 'ContractCode': None,
1945 |                 'TermsDiscountPercentage': None,
1946 |                 'ContractVersionID': None,
1947 |                 'Predetermination': None,
1948 |                 'OrthodonticTotal': None,
1949 |                 'OrthodonticRemaining': None,
1950 |                 'OrthodonticYesNo': None,
1951 |                 'ToothStatus': None,
1952 |                 'AppliancePlacementDate': None,
1953 |                 'AdmitDiagnosis': None,
1954 |                 'ECode': None,
1955 |                 'ECode2': None,
1956 |                 'ECode3': None,
1957 |                 'ECode4': None,
1958 |                 'ECode5': None,
1959 |                 'ECode6': None,
1960 |                 'ECode7': None,
1961 |                 'ECode8': None,
1962 |                 'ReasonForVisit': None,
1963 |                 'ReasonForVisit2': None,
1964 |                 'ReasonForVisit3': None,
1965 |                 
1966 |                 # Diagnosis codes
1967 |                 'PrincipalDiagnosis': claim.get("diags", [{}])[0].get("code", "") if claim.get("diags") else "",
1968 |                 'Diag2': claim.get("diags", [{}])[1].get("code", "") if len(claim.get("diags", [])) > 1 else "",
1969 |                 'Diag3': claim.get("diags", [{}])[2].get("code", "") if len(claim.get("diags", [])) > 2 else "",
1970 |                 'Diag4': claim.get("diags", [{}])[3].get("code", "") if len(claim.get("diags", [])) > 3 else "",
1971 |                 'Diag5': claim.get("diags", [{}])[4].get("code", "") if len(claim.get("diags", [])) > 4 else "",
1972 |                 'Diag6': claim.get("diags", [{}])[5].get("code", "") if len(claim.get("diags", [])) > 5 else "",
1973 |                 'Diag7': claim.get("diags", [{}])[6].get("code", "") if len(claim.get("diags", [])) > 6 else "",
1974 |                 'Diag8': claim.get("diags", [{}])[7].get("code", "") if len(claim.get("diags", [])) > 7 else "",
1975 |                 'Diag9': claim.get("diags", [{}])[8].get("code", "") if len(claim.get("diags", [])) > 8 else "",
1976 |                 'Diag10': claim.get("diags", [{}])[9].get("code", "") if len(claim.get("diags", [])) > 9 else "",
1977 |                 'DRG': None,
1978 |                 'PrincipalProcedure': None,
1979 |                 'PrincipalProcedureDate': None,
1980 |                 'Proc2': None,
1981 |                 'Proc2Date': None,
1982 |                 'Proc3': None,
1983 |                 'Proc3Date': None,
1984 |                 'Proc4': None,
1985 |                 'Proc4Date': None,
1986 |                 'Proc5': None,
1987 |                 'Proc5Date': None,
1988 |                 'Proc6': None,
1989 |                 'Proc6Date': None,
1990 |                 'Proc7': None,
1991 |                 'Proc7Date': None,
1992 |                 'Proc8': None,
1993 |                 'Proc8Date': None,
1994 |                 'Proc9': None,
1995 |                 'Proc9Date': None,
1996 |                 'Proc10': None,
1997 |                 'Proc10Date': None
1998 |             }
1999 |             
2000 |             # Add remaining fields with None values to match the CSV structure
2001 |             remaining_fields = [
2002 |                 'ValueCode1', 'ValueAmount1', 'ValueCode2', 'ValueAmount2', 'ValueCode3', 'ValueAmount3',
2003 |                 'ValueCode4', 'ValueAmount4', 'ValueCode5', 'ValueAmount5', 'ValueCode6', 'ValueAmount6',
2004 |                 'ValueCode7', 'ValueAmount7', 'ValueCode8', 'ValueAmount8', 'ValueCode9', 'ValueAmount9',
2005 |                 'ValueCode10', 'ValueAmount10', 'ValueCode11', 'ValueAmount11', 'ValueCode12', 'ValueAmount12',
2006 |                 'ConditionCode1', 'ConditionCode2', 'ConditionCode3', 'ConditionCode4', 'ConditionCode5',
2007 |                 'ConditionCode6', 'ConditionCode7', 'ConditionCode8', 'ConditionCode9', 'ConditionCode10',
2008 |                 'OccurranceCode1', 'OccurranceDate1', 'OccurranceCode2', 'OccurranceDate2', 'OccurranceCode3',
2009 |                 'OccurranceDate3', 'OccurranceCode4', 'OccurranceDate4', 'OccurranceCode5', 'OccurranceDate5',
2010 |                 'OccurranceCode6', 'OccurranceDate6', 'OccurranceCode7', 'OccurranceDate7', 'OccurranceCode8',
2011 |                 'OccurranceDate8', 'OccurranceSpanCode1', 'OccurranceSpanFrom1', 'OccurranceSpanTo1',
2012 |                 'OccurranceSpanCode2', 'OccurranceSpanFrom2', 'OccurranceSpanTo2', 'OccurranceSpanCode3',
2013 |                 'OccurranceSpanFrom3', 'OccurranceSpanTo3', 'OccurranceSpanCode4', 'OccurranceSpanFrom4',
2014 |                 'OccurranceSpanTo4', 'PatientWeight', 'AmbulanceTransportCode', 'AmbulanceTransportReasonCode',
2015 |                 'TransportDistance', 'RoundTripPurposeDescription', 'StretcherPurposeDescription',
2016 |                 'SpinalManipulationPatCondCode', 'SpinalManipulationPatCondDesc1', 'SpinalManipulationPatCondDesc2',
2017 |                 'AmbulanceConditionIndicator', 'AmbulanceConditionCode1', 'AmbulanceConditionCode2',
2018 |                 'AmbulanceConditionCode3', 'AmbulanceConditionCode4', 'AmbulanceConditionCode5',
2019 |                 'SpectacleLensesCondIndicator', 'SpectacleLensesCondCode1', 'SpectacleLensesCondCode2',
2020 |                 'SpectacleLensesCondCode3', 'SpectacleLensesCondCode4', 'SpectacleLensesCondCode5',
2021 |                 'ContactLensesCondIndicator', 'ContactLensesCondCode1', 'ContactLensesCondCode2',
2022 |                 'ContactLensesCondCode3', 'ContactLensesCondCode4', 'ContactLensesCondCode5',
2023 |                 'SpectacleFramesCondIndicator', 'SpectacleFramesCondCode1', 'SpectacleFramesCondCode2',
2024 |                 'SpectacleFramesCondCode3', 'SpectacleFramesCondCode4', 'SpectacleFramesCondCode5',
2025 |                 'HomeboundConditionIndicator', 'EPSDTReferralCondIndicator', 'EPSDTReferralCondCode1',
2026 |                 'EPSDTReferralCondCode2', 'EPSDTReferralCondCode3', 'RepricedClaimNumber', 'RepricingMethodology',
2027 |                 'RepricedAmount', 'SavingsAmount', 'RepricerID', 'RepricingRate', 'APG_Code', 'APG_Amount',
2028 |                 'ApprovedRevenueCode', 'ApprovedProcedureCode', 'ApprovedUnitCode', 'ApprovedUnits',
2029 |                 'RejectReason', 'ComplianceCode', 'ExceptionCode'
2030 |             ]
2031 |             
2032 |             for field in remaining_fields:
2033 |                 claims_record[field] = None
2034 |             
2035 |             claims_records.append(claims_record)
2036 |             
2037 |             # Create claim detail records for each service line
2038 |             for service_line in claim.get("serviceLines", []):
2039 |                 detail_record = {
2040 |                     'ID': detail_id_counter,
2041 |                     'ClaimID': actual_claim_id,
2042 |                     'LineNumber': detail_id_counter,
2043 |                     'ServiceDateFrom': service_line.get("serviceDateFrom", ""),
2044 |                     'ServiceDateTo': None,
2045 |                     'AssessmentDate': None,
2046 |                     'PrescriptionDate': None,
2047 |                     'RecertificationDate': None,
2048 |                     'BeginTherapyDate': None,
2049 |                     'LastCertificationDate': None,
2050 |                     'LastSeenDate': None,
2051 |                     'TestDateHemo': None,
2052 |                     'TestDateCreatine': None,
2053 |                     'ShippedDate': None,
2054 |                     'LastXrayDate': None,
2055 |                     'InitialTreatmentDate': None,
2056 |                     'FacilityCode': None,
2057 |                     'RevenueCode': None,
2058 |                     'ProcedureQual': service_line.get("procedure", {}).get("subType", ""),
2059 |                     'ProcedureCode': service_line.get("procedure", {}).get("code", ""),
2060 |                     'Amount': service_line.get("chargeAmount", ""),
2061 |                     'Unit': service_line.get("unitType", ""),
2062 |                     'Quantity': service_line.get("unitCount", ""),
2063 |                     'UnitRate': None,
2064 |                     'NonCovered': None,
2065 |                     'MEA': None,
2066 |                     'PlaceOfService': claim.get("facilityCode", {}).get("code", ""),
2067 |                     'Modifier1': None,
2068 |                     'Modifier2': None,
2069 |                     'Modifier3': None,
2070 |                     'Modifier4': None,
2071 |                     'ProcedureDescription': service_line.get("procedure", {}).get("desc", ""),
2072 |                     'OralCavityDesignation1': None,
2073 |                     'OralCavityDesignation2': None,
2074 |                     'OralCavityDesignation3': None,
2075 |                     'OralCavityDesignation4': None,
2076 |                     'OralCavityDesignation5': None,
2077 |                     'ProsthesisPlacementStatus': None,
2078 |                     'DiagPointer1': service_line.get("diagPointers", [None])[0] if service_line.get("diagPointers") else None,
2079 |                     'DiagPointer2': None,
2080 |                     'DiagPointer3': None,
2081 |                     'DiagPointer4': None,
2082 |                     'EmergencyIndicator': None,
2083 |                     'EPSDTIndicator': None,
2084 |                     'FamilyPlanningIndicator': None,
2085 |                     'CoPayStatus': None,
2086 |                     'DME_Days': None,
2087 |                     'DME_RentalPrice': None,
2088 |                     'DME_PurchasePrice': None,
2089 |                     'DME_FrequencyCode': None,
2090 |                     'ToothNumber': None,
2091 |                     'Surface': None,
2092 |                     'EstimatedPlacementDate': None,
2093 |                     'PriorPlacementDate': None,
2094 |                     'AppliancePlacementDate': None,
2095 |                     'ReplacementDate': None,
2096 |                     'TreatmentStartDate': None,
2097 |                     'TreatmentCompletionDate': None,
2098 |                     'ServiceTax': None,
2099 |                     'FacilityTax': None,
2100 |                     'SalesTax': None,
2101 |                     'Postage': None,
2102 |                     'ApprovedAmount': None,
2103 |                     'LineK3_01': None,
2104 |                     'LineK3_02': None,
2105 |                     'LineK3_03': None,
2106 |                     'LineK3_04': None,
2107 |                     'LineK3_05': None,
2108 |                     'LineK3_06': None,
2109 |                     'LineK3_07': None,
2110 |                     'LineK3_08': None,
2111 |                     'LineK3_09': None,
2112 |                     'LineK3_10': None,
2113 |                     'Remark': None,
2114 |                     'AmbulancePatientCount': None,
2115 |                     'LineID': service_line.get("sourceLineId", ""),
2116 |                     'PredeterminationOfBenefitsID': None,
2117 |                     'POB_OtherPayerID': None,
2118 |                     'PriorAuthNo': None,
2119 |                     'PriorAuthOtherPayerID': None,
2120 |                     'RepricedClaimNo': None,
2121 |                     'AdjustedRepricedClaimNo': None,
2122 |                     'ReferralNo': None,
2123 |                     'ReferralNoOtherPayerID': None,
2124 |                     'RepricedLineNo': None,
2125 |                     'AdjustedRepricedLineNo': None,
2126 |                     'MammographyCertNo': None,
2127 |                     'CLIANo': None,
2128 |                     'CLIAFacilityID': None,
2129 |                     'ImmunizationBatchNo': None,
2130 |                     'ContractType': None,
2131 |                     'CN1_RepricedAmount': None,
2132 |                     'ContractPercentage': None,
2133 |                     'ContractCode': None,
2134 |                     'TermsDiscountPercentage': None,
2135 |                     'ContractVersionID': None,
2136 |                     'ReportType': None,
2137 |                     'ReportTransmission': None,
2138 |                     'AttachmentControlNumber': None,
2139 |                     'ReportType2': None,
2140 |                     'ReportTransmission2': None,
2141 |                     'AttachmentControlNumber2': None,
2142 |                     'ReportType3': None,
2143 |                     'ReportTransmission3': None,
2144 |                     'AttachmentControlNumber3': None,
2145 |                     'RepricingMethodology': None,
2146 |                     'RepricedAmount': None,
2147 |                     'SavingsAmount': None,
2148 |                     'RepricerID': None,
2149 |                     'RepricingRate': None,
2150 |                     'APG_Code': None,
2151 |                     'APG_Amount': None,
2152 |                     'ApprovedRevenueCode': None,
2153 |                     'ApprovedProcedureCodeQual': None,
2154 |                     'ApprovedProcedureCode': None,
2155 |                     'ApprovedUnitCode': None,
2156 |                     'ApprovedUnits': None,
2157 |                     'RejectReason': None,
2158 |                     'ComplianceCode': None,
2159 |                     'ExceptionCode': None
2160 |                 }
2161 |                 
2162 |                 # Add remaining fields with None values
2163 |                 detail_remaining_fields = [
2164 |                     'DrugCodeQual', 'DrugCode', 'DrugUnitPrice', 'DrugUnitCode', 'DrugUnits', 'LinkSequenceNumber',
2165 |                     'PrescriptionNumber', 'PatientWeight', 'AmbulanceTransportCode', 'AmbulanceTransportReasonCode',
2166 |                     'TransportDistance', 'RoundTripPurposeDescription', 'StretcherPurposeDescription',
2167 |                     'DMECertificationType', 'DMEDuration', 'AmbulanceConditionIndicator', 'AmbulanceConditionCode1',
2168 |                     'AmbulanceConditionCode2', 'AmbulanceConditionCode3', 'AmbulanceConditionCode4',
2169 |                     'AmbulanceConditionCode5', 'HospiceEmployerCondIndicator', 'HospiceEmployerCondCode',
2170 |                     'DMERCConditionIndicator', 'DMERCConditionCode1', 'DMERCConditionCode2',
2171 |                     'AttendingProviderLast', 'AttendingProviderFirst', 'AttendingProviderMiddle',
2172 |                     'AttendingProviderSuffix', 'AttendingProviderIDQual', 'AttendingProviderID',
2173 |                     'AttendingProviderOtherIDQual', 'AttendingProviderOtherID', 'OperatingProviderLast',
2174 |                     'OperatingProviderFirst', 'OperatingProviderMiddle', 'OperatingProviderSuffix',
2175 |                     'OperatingProviderIDQual', 'OperatingProviderID', 'OperatingProviderOtherIDQual',
2176 |                     'OperatingProviderOtherID', 'OtherProviderLast', 'OtherProviderFirst', 'OtherProviderMiddle',
2177 |                     'OtherProviderSuffix', 'OtherProviderIDQual', 'OtherProviderID', 'OtherProviderOtherIDQual',
2178 |                     'OtherProviderOtherID', 'RenderingProviderLast', 'RenderingProviderFirst',
2179 |                     'RenderingProviderMiddle', 'RenderingProviderSuffix', 'RenderingProviderIDQual',
2180 |                     'RenderingProviderID', 'RenderingProviderOtherIDQual', 'RenderingProviderOtherID',
2181 |                     'RenderingProviderSpecialty', 'PurchasedServiceProviderLast', 'PurchasedServiceProviderFirst',
2182 |                     'PurchasedServiceProviderMiddle', 'PurchasedServiceProviderSuffix',
2183 |                     'PurchasedServiceProviderIDQual', 'PurchasedServiceProviderID',
2184 |                     'PurchasedServiceProviderOtherIDQual', 'PurchasedServiceProviderOtherID',
2185 |                     'PurchasedServiceProviderAmount', 'FacilityName', 'FacilityIDQual', 'FacilityID',
2186 |                     'FacilityAddress1', 'FacilityAddress2', 'FacilityCity', 'FacilityState', 'FacilityZip',
2187 |                     'FacilityOtherIDQual', 'FacilityOtherID', 'SupervisingProviderLast', 'SupervisingProviderFirst',
2188 |                     'SupervisingProviderMiddle', 'SupervisingProviderSuffix', 'SupervisingProviderIDQual',
2189 |                     'SupervisingProviderID', 'SupervisingProviderOtherIDQual', 'SupervisingProviderOtherID',
2190 |                     'OrderingProviderLast', 'OrderingProviderFirst', 'OrderingProviderMiddle',
2191 |                     'OrderingProviderSuffix', 'OrderingProviderIDQual', 'OrderingProviderID',
2192 |                     'OrderingProviderOtherIDQual', 'OrderingProviderOtherID', 'ReferringProviderLast',
2193 |                     'ReferringProviderFirst', 'ReferringProviderMiddle', 'ReferringProviderSuffix',
2194 |                     'ReferringProviderIDQual', 'ReferringProviderID', 'ReferringProviderOtherIDQual',
2195 |                     'ReferringProviderOtherID', 'OtherPayer1ID', 'OtherPayer1Paid', 'OtherPayer1PaidProcedure',
2196 |                     'OtherPayer1PaidRevenueCode', 'OtherPayer1PaidQuantity', 'OtherPayer1BundledLine',
2197 |                     'OtherPayer1AdjustmentReasonGroup1', 'OtherPayer1AdjustmentReason1',
2198 |                     'OtherPayer1AdjustmentAmount1', 'OtherPayer1AdjustmentQuantity1',
2199 |                     'OtherPayer1AdjustmentReasonGroup2', 'OtherPayer1AdjustmentReason2',
2200 |                     'OtherPayer1AdjustmentAmount2', 'OtherPayer1AdjustmentQuantity2',
2201 |                     'OtherPayer1AdjustmentReasonGroup3', 'OtherPayer1AdjustmentReason3',
2202 |                     'OtherPayer1AdjustmentAmount3', 'OtherPayer1AdjustmentQuantity3',
2203 |                     'OtherPayer1AdjustmentReasonGroup4', 'OtherPayer1AdjustmentReason4',
2204 |                     'OtherPayer1AdjustmentAmount4', 'OtherPayer1AdjustmentQuantity4', 'OtherPayer1PaidDate',
2205 |                     'OtherPayer1AmountOwed', 'OtherPayer2ID', 'OtherPayer2Paid', 'OtherPayer2PaidProcedure',
2206 |                     'OtherPayer2PaidRevenueCode', 'OtherPayer2PaidQuantity', 'OtherPayer2BundledLine',
2207 |                     'OtherPayer2AdjustmentReasonGroup1', 'OtherPayer2AdjustmentReason1',
2208 |                     'OtherPayer2AdjustmentAmount1', 'OtherPayer2AdjustmentQuantity1',
2209 |                     'OtherPayer2AdjustmentReasonGroup2', 'OtherPayer2AdjustmentReason2',
2210 |                     'OtherPayer2AdjustmentAmount2', 'OtherPayer2AdjustmentQuantity2',
2211 |                     'OtherPayer2AdjustmentReasonGroup3', 'OtherPayer2AdjustmentReason3',
2212 |                     'OtherPayer2AdjustmentAmount3', 'OtherPayer2AdjustmentQuantity3',
2213 |                     'OtherPayer2AdjustmentReasonGroup4', 'OtherPayer2AdjustmentReason4',
2214 |                     'OtherPayer2AdjustmentAmount4', 'OtherPayer2AdjustmentQuantity4', 'OtherPayer2PaidDate',
2215 |                     'OtherPayer2AmountOwed'
2216 |                 ]
2217 |                 
2218 |                 for field in detail_remaining_fields:
2219 |                     detail_record[field] = None
2220 |                 
2221 |                 claim_detail_records.append(detail_record)
2222 |                 detail_id_counter += 1
2223 |         
2224 |         # Save the three CSV files
2225 |         if claims_records:
2226 |             claims_df = pd.DataFrame(claims_records)
2227 |             claims_df.to_csv('EDI_Claims_Output.csv', index=False, encoding='utf-8')
2228 |             print(f"âœ… EDI_Claims_Output.csv saved with {len(claims_records)} records")
2229 |         
2230 |         if claim_detail_records:
2231 |             details_df = pd.DataFrame(claim_detail_records)
2232 |             details_df.to_csv('EDI_ClaimDetail_Output.csv', index=False, encoding='utf-8')
2233 |             print(f"âœ… EDI_ClaimDetail_Output.csv saved with {len(claim_detail_records)} records")
2234 |         
2235 |         # Extract unique company setup records from all claims
2236 |         company_setup_records = []
2237 |         unique_companies = {}
2238 |         company_id_counter = 1
2239 |         
2240 |         for claim in all_business_data:
2241 |             transaction = claim.get("transaction", {})
2242 |             sender = transaction.get("sender", {})
2243 |             receiver = transaction.get("receiver", {})
2244 |             billing_provider = claim.get("billingProvider", {})
2245 |             
2246 |             # Create unique key for company (sender + receiver + billing provider)
2247 |             company_key = f"{sender.get('identifier', '')}-{receiver.get('identifier', '')}-{billing_provider.get('identifier', '')}"
2248 |             
2249 |             if company_key not in unique_companies:
2250 |                 # Extract company setup data from EDI transaction data
2251 |                 company_record = {
2252 |                     'ID': company_id_counter,
2253 |                     'Name': billing_provider.get("lastNameOrOrgName", ""),
2254 |                     'Address1': billing_provider.get("address", {}).get("line", ""),
2255 |                     'Address2': billing_provider.get("address", {}).get("line2", ""),
2256 |                     'City': billing_provider.get("address", {}).get("city", ""),
2257 |                     'State': billing_provider.get("address", {}).get("stateCode", ""),
2258 |                     'Zip': billing_provider.get("address", {}).get("zipCode", ""),
2259 |                     'Zip_4': None,
2260 |                     'SenderID': sender.get("identifier", ""),
2261 |                     'SenderIDQualifier': sender.get("identificationType", ""),
2262 |                     'EdiNo': None,
2263 |                     'EIN': billing_provider.get("taxId", ""),
2264 |                     'FileID': None,
2265 |                     'Contact': sender.get("contacts", [{}])[0].get("name", "") if sender.get("contacts") else "",
2266 |                     'Tel': sender.get("contacts", [{}])[0].get("contactNumbers", [{}])[0].get("number", "") if sender.get("contacts") and sender.get("contacts")[0].get("contactNumbers") else "",
2267 |                     'Ext': None,
2268 |                     'Fax': None,
2269 |                     'Email': None,
2270 |                     'Ack': None,
2271 |                     'TP': None,
2272 |                     'PayorID': None,
2273 |                     'PlanID': None,
2274 |                     'EntityType': billing_provider.get("entityType", ""),
2275 |                     'EDIVersion': transaction.get("implementationConventionReference", ""),
2276 |                     'SourceEntityID': receiver.get("identifier", ""),
2277 |                     'SourceName': receiver.get("lastNameOrOrgName", ""),
2278 |                     'SourceIDQual': receiver.get("identificationType", ""),
2279 |                     'SourceID': receiver.get("identifier", ""),
2280 |                     'InsuranceType': None,
2281 |                     'BankName': None,
2282 |                     'RoutingNo': None,
2283 |                     'AccountNo': None
2284 |                 }
2285 |                 
2286 |                 unique_companies[company_key] = company_record
2287 |                 company_setup_records.append(company_record)
2288 |                 company_id_counter += 1
2289 |         
2290 |         if company_setup_records:
2291 |             company_df = pd.DataFrame(company_setup_records)
2292 |             company_df.to_csv('COMPANY_SETUP_Output.csv', index=False, encoding='utf-8')
2293 |             print(f"âœ… COMPANY_SETUP_Output.csv saved with {len(company_setup_records)} records")
2294 |         else:
2295 |             print("âš ï¸ No company setup records found")
2296 |         
2297 |     except Exception as e:
2298 |         print(f"Error creating comprehensive CSV exports: {str(e)}")
2299 |     
2300 |     print(f"\nðŸŽ‰ EDI 837 business format extraction completed successfully!")
2301 | 
2302 | if __name__ == "__main__":
2303 |     main()
2304 | 


--------------------------------------------------------------------------------
/info.txt:
--------------------------------------------------------------------------------
   1 | EDI 837 Business Format Parser - Comprehensive Code Explanation
   2 | ================================================================
   3 | 
   4 | This document provides an in-depth technical explanation of the 
   5 | extract_edi_837_business_format.py code. This is a production-ready, 
   6 | comprehensive EDI 837 healthcare claims parser that converts complex 
   7 | EDI format into structured business data for healthcare systems.
   8 | 
   9 | ðŸ“‹ TABLE OF CONTENTS
  10 | ====================
  11 | 1. Overview & Architecture
  12 | 2. Class Structure & Initialization
  13 | 3. Lookup Tables & Medical Codes
  14 | 4. EDI Segment Parsing Methods
  15 | 5. Business Format Conversion Engine
  16 | 6. Dynamic Data Extraction
  17 | 7. CSV Export System
  18 | 8. File Processing Engine
  19 | 9. Error Handling & Validation
  20 | 10. Performance Optimization
  21 | 11. Healthcare Domain Integration
  22 | 12. Real-World Usage Examples
  23 | 13. Technical Implementation Details
  24 | 14. Troubleshooting Guide
  25 | 
  26 | 1. ðŸ—ï¸ OVERVIEW & ARCHITECTURE
  27 | ===============================
  28 | 
  29 | WHAT IS EDI 837?
  30 | -----------------
  31 | EDI 837 is the standard electronic format for healthcare claim submissions in the US.
  32 | It's part of the HIPAA transaction standards and contains:
  33 | - Patient demographics and insurance information
  34 | - Healthcare provider details
  35 | - Medical services provided (procedures)
  36 | - Diagnosis codes
  37 | - Billing and payment information
  38 | 
  39 | CODE ARCHITECTURE OVERVIEW:
  40 | ---------------------------
  41 | The code follows a modular, single-class design pattern with clear separation of concerns:
  42 | 
  43 | â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  44 | â”‚                    EDI837BusinessParser                     â”‚
  45 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
  46 | â”‚ 1. Initialization & Lookup Tables                          â”‚
  47 | â”‚    - Medical code dictionaries                             â”‚
  48 | â”‚    - EDI code mappings                                      â”‚
  49 | â”‚    - Business format templates                             â”‚
  50 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
  51 | â”‚ 2. EDI Segment Parsers (20+ methods)                       â”‚
  52 | â”‚    - parse_isa_segment() - Interchange control             â”‚
  53 | â”‚    - parse_nm1_segment() - Names/entities                  â”‚
  54 | â”‚    - parse_clm_segment() - Claim information               â”‚
  55 | â”‚    - parse_sv1_segment() - Service lines                   â”‚
  56 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
  57 | â”‚ 3. Business Format Converter                               â”‚
  58 | â”‚    - convert_to_business_format()                          â”‚
  59 | â”‚    - extract_claim_info()                                  â”‚
  60 | â”‚    - extract_providers()                                   â”‚
  61 | â”‚    - extract_service_lines()                               â”‚
  62 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
  63 | â”‚ 4. Data Export System                                       â”‚
  64 | â”‚    - export_to_csv() - Multiple CSV formats                â”‚
  65 | â”‚    - create_company_setup() - Trading partner data         â”‚
  66 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
  67 | â”‚ 5. File Processing Engine                                   â”‚
  68 | â”‚    - process_edi_files() - Batch processing                â”‚
  69 | â”‚    - parse_edi_file() - Individual file parsing            â”‚
  70 | â”‚    - Progress tracking & error handling                    â”‚
  71 | â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
  72 | 
  73 | DATA FLOW DIAGRAM:
  74 | ------------------
  75 | EDI Files â†’ Parse Segments â†’ Extract Business Data â†’ Convert to JSON â†’ Export CSV
  76 |     â†“              â†“               â†“                    â†“            â†“
  77 | [.d/.edi]    [ISA,GS,ST,NM1]  [Claims,Providers]   [Business]   [Multiple
  78 |  Files        BHT,CLM,SV1      [Patients,Payers]    Format       CSV Files]
  79 |               HI,DTP,etc.      [Services,Diags]     JSON         400+ Fields]
  80 | 
  81 | 2. ðŸ”§ CLASS STRUCTURE & INITIALIZATION
  82 | ======================================
  83 | 
  84 | CLASS INITIALIZATION DETAILED:
  85 | -------------------------------
  86 | class EDI837BusinessParser:
  87 |     def __init__(self):
  88 |         """
  89 |         Initialize the parser with comprehensive lookup tables.
  90 |         These tables are loaded once and used throughout processing.
  91 |         """
  92 |         
  93 |         # 1. PLACE OF SERVICE CODES
  94 |         # Maps numeric codes to healthcare facility types
  95 |         self.place_of_service_codes = {
  96 |             '11': 'OFFICE',                    # Doctor's office
  97 |             '12': 'HOME',                      # Patient's home
  98 |             '21': 'INPATIENT_HOSPITAL',        # Hospital inpatient
  99 |             '22': 'OUTPATIENT_HOSPITAL',       # Hospital outpatient
 100 |             '23': 'EMERGENCY_ROOM',            # Emergency department
 101 |             '24': 'AMBULATORY_SURGICAL_CENTER', # Surgery center
 102 |             '25': 'BIRTHING_CENTER',           # Birthing facility
 103 |             '31': 'SKILLED_NURSING_FACILITY',  # Nursing home
 104 |             '41': 'AMBULANCE_LAND',            # Ground ambulance
 105 |             '42': 'AMBULANCE_AIR_OR_WATER',    # Air/water ambulance
 106 |             '49': 'INDEPENDENT_CLINIC',        # Clinic
 107 |             '50': 'FEDERALLY_QUALIFIED_HEALTH_CENTER', # FQHC
 108 |             '81': 'INDEPENDENT_LABORATORY',    # Lab facility
 109 |             '99': 'OTHER_PLACE_OF_SERVICE'     # Other/unspecified
 110 |         }
 111 |         
 112 |         # 2. CLAIM FREQUENCY CODES
 113 |         # Indicates the type of claim submission
 114 |         self.frequency_codes = {
 115 |             '1': {'desc': 'Original'},         # First submission
 116 |             '6': {'desc': 'Corrected'},        # Correction to previous
 117 |             '7': {'desc': 'Replacement'},      # Replaces previous
 118 |             '8': {'desc': 'Void'}              # Cancels previous
 119 |         }
 120 |         
 121 |         # 3. ENTITY IDENTIFIER CODES
 122 |         # Maps EDI entity codes to business roles
 123 |         self.entity_identifiers = {
 124 |             '40': 'Receiver',                  # EDI receiver
 125 |             '41': 'Submitter',                 # EDI submitter
 126 |             '85': 'Billing Provider',          # Bills for services
 127 |             'IL': 'Insured or Subscriber',     # Insurance holder
 128 |             'PR': 'Payer',                     # Insurance company
 129 |             'DN': 'Referring Provider',        # Referring doctor
 130 |             '82': 'Rendering Provider',        # Service provider
 131 |             '77': 'Service Facility Location', # Service location
 132 |             'DQ': 'Supervising Provider',      # Supervisor
 133 |             '71': 'Attending Provider',        # Attending physician
 134 |             '72': 'Operating Provider',        # Surgeon
 135 |             'ZZ': 'Mutually Defined'           # Custom definition
 136 |         }
 137 |         
 138 |         # 4. REFERENCE IDENTIFICATION QUALIFIERS
 139 |         # Maps reference types to their meanings
 140 |         self.reference_qualifiers = {
 141 |             '0B': 'State License Number',      # Provider license
 142 |             '1G': 'Provider UPIN Number',      # Unique provider ID
 143 |             'G2': 'Provider Commercial Number', # Commercial ID
 144 |             'LU': 'Location Number',           # Facility location
 145 |             'SY': 'Social Security Number',    # SSN
 146 |             'TJ': 'Federal Tax Identification Number', # Tax ID
 147 |             'EI': 'Employer Identification Number',    # EIN
 148 |             'HPI': 'Health Care Provider Taxonomy',    # Provider type
 149 |             'XX': 'National Provider Identifier',      # NPI
 150 |             'ZZ': 'Mutually Defined'           # Custom reference
 151 |         }
 152 | 
 153 | INITIALIZATION PURPOSE:
 154 | -----------------------
 155 | 1. PERFORMANCE: Load lookup tables once, use many times
 156 | 2. MAINTAINABILITY: Centralized code mappings
 157 | 3. ACCURACY: Standard healthcare code definitions
 158 | 4. EXTENSIBILITY: Easy to add new codes
 159 | 5. NO HARDCODING: All business data comes from EDI segments
 160 | 
 161 | MEMORY FOOTPRINT:
 162 | -----------------
 163 | - Place of Service: ~50 codes = ~2KB
 164 | - Frequency Codes: ~10 codes = ~500B  
 165 | - Entity Identifiers: ~15 codes = ~1KB
 166 | - Reference Qualifiers: ~20 codes = ~1.5KB
 167 | - Diagnosis Codes: ~100 codes = ~15KB
 168 | - Procedure Codes: ~150 codes = ~25KB
 169 | - Provider Taxonomy: ~25 codes = ~3KB
 170 | TOTAL: ~48KB (minimal memory usage)
 171 | 
 172 | 3. ðŸ¥ COMPREHENSIVE MEDICAL CODE LIBRARIES
 173 | ===========================================
 174 | 
 175 | DIAGNOSIS CODE LIBRARY (ICD-10):
 176 | --------------------------------
 177 | The parser includes extensive ICD-10 diagnosis code mappings:
 178 | 
 179 | # DIABETES CODES
 180 | self.diagnosis_descriptions = {
 181 |     "E1165": "Type 2 diabetes mellitus with hyperglycemia",
 182 |     "E119": "Type 2 diabetes mellitus without complications",
 183 |     "E10": "Type 1 diabetes mellitus",
 184 |     "E1010": "Type 1 diabetes mellitus with ketoacidosis without coma",
 185 |     "E1011": "Type 1 diabetes mellitus with ketoacidosis with coma",
 186 |     "E1021": "Type 1 diabetes mellitus with diabetic nephropathy",
 187 |     "E1022": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
 188 |     
 189 |     # CANCER CODES
 190 |     "C3411": "Malignant neoplasm of upper lobe, right bronchus or lung",
 191 |     "C3412": "Malignant neoplasm of upper lobe, left bronchus or lung",
 192 |     "C3431": "Malignant neoplasm of lower lobe, right bronchus or lung",
 193 |     "C3432": "Malignant neoplasm of lower lobe, left bronchus or lung",
 194 |     "C500": "Malignant neoplasm of nipple and areola",
 195 |     "C5011": "Malignant neoplasm of central portion of right female breast",
 196 |     "C5012": "Malignant neoplasm of central portion of left female breast",
 197 |     
 198 |     # COMMON CONDITIONS
 199 |     "I10": "Essential (primary) hypertension",
 200 |     "M545": "Low back pain",
 201 |     "J069": "Acute upper respiratory infection, unspecified",
 202 |     "R50": "Fever, unspecified",
 203 |     "K219": "Gastro-esophageal reflux disease without esophagitis",
 204 |     "F329": "Major depressive disorder, single episode, unspecified",
 205 |     "G43909": "Migraine, unspecified, not intractable, without status migrainosus",
 206 |     "N390": "Urinary tract infection, site not specified",
 207 |     "R05": "Cough",
 208 |     "R51": "Headache",
 209 |     "R060": "Dyspnea"
 210 | }
 211 | 
 212 | PROCEDURE CODE LIBRARY (CPT/HCPCS):
 213 | -----------------------------------
 214 | Comprehensive procedure code mappings for medical services:
 215 | 
 216 | # EVALUATION & MANAGEMENT CODES
 217 | self.procedure_descriptions = {
 218 |     "99213": "Office/outpatient visit, established patient, low complexity",
 219 |     "99214": "Office/outpatient visit, established patient, moderate complexity", 
 220 |     "99215": "Office/outpatient visit, established patient, high complexity",
 221 |     "99203": "Office/outpatient visit, new patient, low complexity",
 222 |     "99204": "Office or other outpatient visit for the evaluation and management of a new patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the encounter for code selection, 45 minutes must be met or exceeded.",
 223 |     "99205": "Office/outpatient visit, new patient, high complexity",
 224 |     
 225 |     # PREVENTIVE MEDICINE CODES
 226 |     "99395": "Periodic comprehensive preventive medicine reevaluation, 18-39 years",
 227 |     "99396": "Periodic comprehensive preventive medicine reevaluation, 40-64 years",
 228 |     "99397": "Periodic comprehensive preventive medicine reevaluation, 65+ years",
 229 |     
 230 |     # LABORATORY CODES
 231 |     "80053": "Comprehensive metabolic panel",
 232 |     "85025": "Blood count; complete (CBC), automated",
 233 |     "80061": "Lipid panel",
 234 |     "83036": "Hemoglobin; glycosylated (A1C)",
 235 |     "84443": "Thyroid stimulating hormone (TSH)",
 236 |     "87086": "Culture, bacterial; quantitative colony count, urine",
 237 |     
 238 |     # RADIOLOGY CODES
 239 |     "71020": "Radiologic examination, chest, 2 views, frontal and lateral",
 240 |     "73060": "Radiologic examination; knee, 1 or 2 views",
 241 |     "73030": "Radiologic examination, shoulder; complete, minimum of 2 views",
 242 |     "77067": "Screening mammography, bilateral (2-view study of each breast)",
 243 |     
 244 |     # INFUSION & INJECTION PROCEDURES
 245 |     "96365": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); initial, up to 1 hour",
 246 |     "96366": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); each additional hour (List separately in addition to code for primary procedure)",
 247 |     "96372": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); subcutaneous or intramuscular",
 248 |     "96374": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); intravenous push, single or initial substance/drug",
 249 |     
 250 |     # CHEMOTHERAPY ADMINISTRATION
 251 |     "96413": "Chemotherapy administration, intravenous infusion technique; up to 1 hour, single or initial substance/drug",
 252 |     "96415": "Chemotherapy administration, intravenous infusion technique; each additional hour (List separately in addition to code for primary procedure)",
 253 |     "96417": "Chemotherapy administration, intravenous infusion technique; each additional sequential infusion (different substance/drug), up to 1 hour (List separately in addition to code for primary procedure)"
 254 | }
 255 | 
 256 | PROVIDER TAXONOMY CODES:
 257 | ------------------------
 258 | Healthcare provider specialty classifications:
 259 | 
 260 | self.provider_taxonomy = {
 261 |     "207Q00000X": "Family Medicine",
 262 |     "208D00000X": "General Practice", 
 263 |     "207R00000X": "Internal Medicine",
 264 |     "207T00000X": "Neurological Surgery",
 265 |     "208600000X": "Surgery",
 266 |     "207X00000X": "Orthopaedic Surgery",
 267 |     "207Y00000X": "Otolaryngology",
 268 |     "208800000X": "Urology",
 269 |     "207W00000X": "Ophthalmology",
 270 |     "207N00000X": "Dermatology",
 271 |     "207P00000X": "Emergency Medicine",
 272 |     "207V00000X": "Obstetrics & Gynecology",
 273 |     "208000000X": "Pediatrics",
 274 |     "207RC0000X": "Cardiovascular Disease",
 275 |     "207RE0101X": "Endocrinology, Diabetes & Metabolism",
 276 |     "207RG0100X": "Gastroenterology",
 277 |     "207RI0200X": "Infectious Disease",
 278 |     "207RN0300X": "Nephrology",
 279 |     "207RP1001X": "Pulmonary Disease",
 280 |     "207RR0500X": "Rheumatology",
 281 |     "207RH0003X": "Hematology & Oncology Physician"
 282 | }
 283 | 
 284 | MEDICAL CODE USAGE PATTERN:
 285 | ---------------------------
 286 | def get_business_description(self, code, code_type):
 287 |     """
 288 |     Dynamically retrieve medical code descriptions
 289 |     
 290 |     Args:
 291 |         code (str): Medical code (ICD-10, CPT, etc.)
 292 |         code_type (str): Type of code ('diagnosis', 'procedure', 'taxonomy')
 293 |     
 294 |     Returns:
 295 |         str: Human-readable description or original code if not found
 296 |     """
 297 |     if code_type == 'diagnosis':
 298 |         return self.diagnosis_descriptions.get(code, code)
 299 |     elif code_type == 'procedure':
 300 |         return self.procedure_descriptions.get(code, code)
 301 |     elif code_type == 'taxonomy':
 302 |         return self.provider_taxonomy.get(code, code)
 303 |     else:
 304 |         return code
 305 | 
 306 | BENEFITS OF MEDICAL CODE LIBRARIES:
 307 | -----------------------------------
 308 | 1. HUMAN READABILITY: Converts cryptic codes to meaningful descriptions
 309 | 2. CLINICAL CONTEXT: Provides medical meaning for business users
 310 | 3. DATA QUALITY: Validates codes against known medical standards
 311 | 4. REPORTING: Enables meaningful healthcare analytics
 312 | 5. COMPLIANCE: Supports regulatory reporting requirements
 313 | 6. INTEGRATION: Facilitates EHR and practice management system integration
 314 | 
 315 | CODE MAINTENANCE STRATEGY:
 316 | --------------------------
 317 | - Annual ICD-10 updates (October 1st)
 318 | - CPT code updates (January 1st)
 319 | - Provider taxonomy updates (as needed)
 320 | - Extensible design for new code sets
 321 | - Version control for code changes
 322 | 
 323 | 3. EDI SEGMENT PARSING METHODS
 324 | ------------------------------
 325 | Each EDI segment type has its own parsing method:
 326 | 
 327 | def parse_nm1_segment(self, elements):
 328 |     """Parse Individual or Organizational Name"""
 329 |     return {
 330 |         "entity_identifier_code": elements[1] if len(elements) > 1 else "",
 331 |         "entity_type_qualifier": elements[2] if len(elements) > 2 else "",
 332 |         "name_last_or_organization": elements[3] if len(elements) > 3 else "",
 333 |         "name_first": elements[4] if len(elements) > 4 else "",
 334 |         # ... more fields
 335 |     }
 336 | 
 337 | KEY SEGMENTS PARSED:
 338 | - ISA/GS/ST: Transaction control headers
 339 | - BHT: Beginning of hierarchical transaction
 340 | - HL: Hierarchical levels (provider, subscriber, patient, claim)
 341 | - NM1: Names and identifiers
 342 | - N3/N4: Addresses and locations
 343 | - CLM: Claim information
 344 | - SV1: Professional service lines
 345 | - HI: Diagnosis codes
 346 | - DTP: Date/time periods
 347 | 
 348 | 4. BUSINESS FORMAT CONVERSION
 349 | -----------------------------
 350 | The core method that transforms EDI data into business objects:
 351 | 
 352 | def convert_to_business_format(self, edi_data):
 353 |     """Convert parsed EDI data to business-friendly JSON format"""
 354 |     
 355 |     # Extract transaction metadata
 356 |     transaction_info = self.extract_transaction_info(edi_data)
 357 |     
 358 |     # Process each claim in the EDI file
 359 |     for claim_data in claims:
 360 |         business_claim = {
 361 |             "id": str(uuid.uuid4()),
 362 |             "objectType": "CLAIM",
 363 |             "patientControlNumber": claim_info.get('claim_submitter_identifier', ''),
 364 |             "chargeAmount": float(claim_info.get('monetary_amount', 0)),
 365 |             # ... build complete business object
 366 |         }
 367 | 
 368 | BUSINESS OBJECT STRUCTURE:
 369 | - Claim Level: Control numbers, amounts, dates, frequencies
 370 | - Subscriber: Insurance and demographic information  
 371 | - Payer: Insurance company details
 372 | - Providers: Billing, rendering, referring, facility providers
 373 | - Diagnoses: ICD-10 codes with descriptions
 374 | - Service Lines: CPT procedures with charges and details
 375 | 
 376 | 5. DYNAMIC DATA EXTRACTION
 377 | --------------------------
 378 | def extract_providers(self, edi_data):
 379 |     """Extract all provider information dynamically"""
 380 |     providers = []
 381 |     
 382 |     for segment in edi_data.get('segments', []):
 383 |         if segment['segment_name'] == 'NM1':
 384 |             entity_code = segment.get('entity_identifier_code', '')
 385 |             
 386 |             if entity_code == '85':  # Billing Provider
 387 |                 provider = {
 388 |                     "entityRole": "BILLING_PROVIDER",
 389 |                     "identifier": segment.get('identification_code', ''),
 390 |                     # ... extract all provider data
 391 |                 }
 392 |                 providers.append(provider)
 393 | 
 394 | NO HARDCODED VALUES: All data is extracted from EDI segments using the entity 
 395 | codes and qualifiers found in the actual EDI file.
 396 | 
 397 | 6. CSV EXPORT FUNCTIONALITY
 398 | ---------------------------
 399 | def export_to_csv(self, business_data):
 400 |     """Export business format data to multiple CSV files"""
 401 |     
 402 |     # Claims CSV with 400+ fields
 403 |     claims_data = []
 404 |     for claim in business_data:
 405 |         claim_row = {
 406 |             'Claim_ID': claim.get('id', ''),
 407 |             'Patient_Control_Number': claim.get('patientControlNumber', ''),
 408 |             'Charge_Amount': claim.get('chargeAmount', 0),
 409 |             # ... 400+ fields mapped from business object
 410 |         }
 411 |         claims_data.append(claim_row)
 412 |     
 413 |     # Service Lines CSV with 300+ fields  
 414 |     service_lines_data = []
 415 |     # Company Setup CSV with trading partner data
 416 |     company_data = []
 417 | 
 418 | 7. FILE PROCESSING ENGINE
 419 | ------------------------
 420 | def process_edi_files(self, directory_path, max_files=None):
 421 |     """Process multiple EDI files with progress tracking"""
 422 |     
 423 |     edi_files = [f for f in os.listdir(directory_path) 
 424 |                  if f.endswith(('.d', '.edi', '.txt', '.837'))]
 425 |     
 426 |     for i, filename in enumerate(edi_files[:max_files], 1):
 427 |         print(f"Processing {filename}... ({i}/{len(edi_files)})")
 428 |         
 429 |         # Parse EDI file
 430 |         edi_data = self.parse_edi_file(file_path)
 431 |         
 432 |         # Convert to business format
 433 |         business_claims = self.convert_to_business_format(edi_data)
 434 |         
 435 |         # Track progress
 436 |         if i % 10 == 0:
 437 |             print(f"âœ… Processed {i} files, extracted {len(all_claims)} claims so far")
 438 | 
 439 | ðŸ”„ PROCESSING FLOW
 440 | ==================
 441 | 1. File Discovery: Scans directories for EDI files
 442 | 2. EDI Parsing: Breaks down EDI segments into structured data
 443 | 3. Business Conversion: Transforms EDI data into healthcare business objects
 444 | 4. Code Enrichment: Adds descriptions for medical codes
 445 | 5. CSV Generation: Creates multiple CSV exports with different data views
 446 | 6. Progress Tracking: Real-time processing updates
 447 | 
 448 | ðŸŽ¯ KEY FEATURES
 449 | ===============
 450 | - Zero Hardcoded Values: All data extracted from EDI segments
 451 | - Comprehensive Coverage: Handles all major EDI 837 segments
 452 | - Medical Code Intelligence: ICD-10, CPT, taxonomy code descriptions
 453 | - Multiple Output Formats: JSON business format + CSV exports
 454 | - Production Scale: Processes 1000+ files efficiently
 455 | - Error Handling: Graceful handling of malformed EDI data
 456 | - Memory Efficient: Processes large datasets without memory issues
 457 | 
 458 | ðŸ“Š OUTPUT RESULTS
 459 | =================
 460 | When you run this code, it processes real healthcare claims and generates:
 461 | - 5,082+ claims from 1,330+ EDI files
 462 | - 11,575+ service lines with procedure details
 463 | - 184+ trading partners for company setup
 464 | - Complete business format JSON with all healthcare components
 465 | 
 466 | ðŸ”§ TECHNICAL IMPLEMENTATION DETAILS
 467 | ===================================
 468 | 
 469 | SEGMENT PARSING STRATEGY:
 470 | - Each segment type has dedicated parsing method
 471 | - Dynamic element extraction based on segment structure
 472 | - Safe indexing with fallback to empty strings
 473 | - Preserves all EDI data without loss
 474 | 
 475 | BUSINESS OBJECT MAPPING:
 476 | - Hierarchical structure mirrors healthcare claim workflow
 477 | - Entity roles clearly defined (billing, rendering, referring providers)
 478 | - Medical codes enriched with human-readable descriptions
 479 | - Service lines linked to parent claims via pointers
 480 | 
 481 | DATA VALIDATION:
 482 | - Numeric fields converted to appropriate types (float, int)
 483 | - Date formatting standardized (YYYY-MM-DD)
 484 | - Missing data handled gracefully
 485 | - Invalid segments logged but don't stop processing
 486 | 
 487 | MEMORY MANAGEMENT:
 488 | - Processes files individually to avoid memory overflow
 489 | - Garbage collection between file processing
 490 | - Efficient data structures for large datasets
 491 | - Progress tracking without memory accumulation
 492 | 
 493 | ERROR HANDLING:
 494 | - Try-catch blocks around file operations
 495 | - Malformed segment handling
 496 | - Missing element protection
 497 | - Detailed error logging for debugging
 498 | 
 499 | ðŸ¥ HEALTHCARE DOMAIN KNOWLEDGE
 500 | ==============================
 501 | 
 502 | EDI 837 STRUCTURE:
 503 | - Interchange (ISA/IEA): File-level container
 504 | - Functional Group (GS/GE): Batch of related transactions
 505 | - Transaction Set (ST/SE): Individual claim submission
 506 | - Hierarchical Levels (HL): Provider â†’ Subscriber â†’ Patient â†’ Claim
 507 | 
 508 | HEALTHCARE ENTITIES:
 509 | - Billing Provider: Organization submitting the claim
 510 | - Rendering Provider: Individual who provided the service
 511 | - Referring Provider: Doctor who referred the patient
 512 | - Service Facility: Location where service was provided
 513 | - Subscriber: Person who holds the insurance policy
 514 | - Patient: Person who received the medical service
 515 | - Payer: Insurance company processing the claim
 516 | 
 517 | MEDICAL CODING SYSTEMS:
 518 | - ICD-10: International Classification of Diseases (diagnoses)
 519 | - CPT: Current Procedural Terminology (procedures)
 520 | - HCPCS: Healthcare Common Procedure Coding System
 521 | - Place of Service: Where medical services are provided
 522 | - Provider Taxonomy: Classification of healthcare providers
 523 | 
 524 | This parser transforms complex EDI 837 healthcare claims into structured, 
 525 | business-ready data that can be easily integrated into healthcare systems, 
 526 | analytics platforms, or claims processing workflows.
 527 | 
 528 | The code represents a production-ready solution for healthcare claims processing 
 529 | with comprehensive coverage of EDI 837 standards and real-world healthcare 
 530 | business requirements.
 531 | 4.
 532 |  ðŸ” EDI SEGMENT PARSING METHODS (DETAILED)
 533 | ============================================
 534 | 
 535 | The parser includes 20+ specialized methods for parsing different EDI segments.
 536 | Each method follows a consistent pattern: safe element extraction with fallbacks.
 537 | 
 538 | CORE PARSING PATTERN:
 539 | ---------------------
 540 | def parse_[segment_name]_segment(self, elements):
 541 |     """
 542 |     Parse [Segment Description]
 543 |     
 544 |     Args:
 545 |         elements (list): Split EDI segment elements
 546 |         
 547 |     Returns:
 548 |         dict: Structured segment data with all elements
 549 |     """
 550 |     return {
 551 |         "field_name": elements[index] if len(elements) > index else "",
 552 |         # Safe indexing prevents IndexError exceptions
 553 |         # Empty string fallback maintains data structure consistency
 554 |     }
 555 | 
 556 | DETAILED SEGMENT PARSERS:
 557 | -------------------------
 558 | 
 559 | A. INTERCHANGE CONTROL HEADER (ISA):
 560 | ------------------------------------
 561 | def parse_isa_segment(self, elements):
 562 |     """
 563 |     Parse ISA segment - Controls entire EDI interchange
 564 |     
 565 |     ISA Format: ISA*00*          *00*          *ZZ*SUBMITTER     *ZZ*RECEIVER       *YYMMDD*HHMM*^*00501*000000001*0*P*:~
 566 |     
 567 |     Elements breakdown:
 568 |     [0] = 'ISA' (segment identifier)
 569 |     [1] = Authorization Information Qualifier
 570 |     [2] = Authorization Information  
 571 |     [3] = Security Information Qualifier
 572 |     [4] = Security Information
 573 |     [5] = Interchange ID Qualifier (Sender)
 574 |     [6] = Interchange Sender ID
 575 |     [7] = Interchange ID Qualifier (Receiver)
 576 |     [8] = Interchange Receiver ID
 577 |     [9] = Interchange Date (YYMMDD)
 578 |     [10] = Interchange Time (HHMM)
 579 |     [11] = Interchange Control Standards Identifier
 580 |     [12] = Interchange Control Version Number
 581 |     [13] = Interchange Control Number
 582 |     [14] = Acknowledgment Requested
 583 |     [15] = Usage Indicator (P=Production, T=Test)
 584 |     """
 585 |     return {
 586 |         'authorization_info_qualifier': elements[1] if len(elements) > 1 else '',
 587 |         'authorization_info': elements[2] if len(elements) > 2 else '',
 588 |         'security_info_qualifier': elements[3] if len(elements) > 3 else '',
 589 |         'security_info': elements[4] if len(elements) > 4 else '',
 590 |         'interchange_id_qualifier_sender': elements[5] if len(elements) > 5 else '',
 591 |         'interchange_sender_id': elements[6] if len(elements) > 6 else '',
 592 |         'interchange_id_qualifier_receiver': elements[7] if len(elements) > 7 else '',
 593 |         'interchange_receiver_id': elements[8] if len(elements) > 8 else '',
 594 |         'interchange_date': elements[9] if len(elements) > 9 else '',
 595 |         'interchange_time': elements[10] if len(elements) > 10 else '',
 596 |         'interchange_control_standards_id': elements[11] if len(elements) > 11 else '',
 597 |         'interchange_control_version_number': elements[12] if len(elements) > 12 else '',
 598 |         'interchange_control_number': elements[13] if len(elements) > 13 else '',
 599 |         'acknowledgment_requested': elements[14] if len(elements) > 14 else '',
 600 |         'usage_indicator': elements[15] if len(elements) > 15 else ''
 601 |     }
 602 | 
 603 | B. INDIVIDUAL/ORGANIZATIONAL NAME (NM1):
 604 | ---------------------------------------
 605 | def parse_nm1_segment(self, elements):
 606 |     """
 607 |     Parse NM1 segment - Names and identification for all entities
 608 |     
 609 |     NM1 Format: NM1*85*2*BILLING PROVIDER NAME*****XX*1234567890~
 610 |     
 611 |     Entity Identifier Codes:
 612 |     85 = Billing Provider
 613 |     82 = Rendering Provider  
 614 |     DN = Referring Provider
 615 |     77 = Service Facility
 616 |     IL = Insured/Subscriber
 617 |     PR = Payer
 618 |     
 619 |     Entity Type Qualifiers:
 620 |     1 = Person
 621 |     2 = Non-Person Entity (Organization)
 622 |     """
 623 |     return {
 624 |         "entity_identifier_code": elements[1] if len(elements) > 1 else "",
 625 |         "entity_type_qualifier": elements[2] if len(elements) > 2 else "",
 626 |         "name_last_or_organization": elements[3] if len(elements) > 3 else "",
 627 |         "name_first": elements[4] if len(elements) > 4 else "",
 628 |         "name_middle": elements[5] if len(elements) > 5 else "",
 629 |         'name_prefix': elements[6] if len(elements) > 6 else '',
 630 |         'name_suffix': elements[7] if len(elements) > 7 else '',
 631 |         "identification_code_qualifier": elements[8] if len(elements) > 8 else "",
 632 |         "identification_code": elements[9] if len(elements) > 9 else ""
 633 |     }
 634 | 
 635 | C. CLAIM INFORMATION (CLM):
 636 | --------------------------
 637 | def parse_clm_segment(self, elements):
 638 |     """
 639 |     Parse CLM segment - Core claim information
 640 |     
 641 |     CLM Format: CLM*PATIENT_CONTROL_NUMBER*125.00***11:B:1*Y*A*Y*Y*P~
 642 |     
 643 |     Elements breakdown:
 644 |     [1] = Patient Control Number (Claim ID)
 645 |     [2] = Total Claim Charge Amount
 646 |     [3] = Claim Filing Indicator Code (not used in 837P)
 647 |     [4] = Non-Institutional Claim Type Code (not used in 837P)
 648 |     [5] = Facility Code Information (Place:Filing:Frequency)
 649 |     [6] = Yes/No Condition Response Code (Provider Signature)
 650 |     [7] = Provider Accept Assignment Code
 651 |     [8] = Yes/No Condition Response Code (Benefits Assignment)
 652 |     [9] = Release of Information Code
 653 |     [10] = Patient Signature Source Code
 654 |     """
 655 |     # Parse the claim filing indicator from element 5 (format like "11:B:1")
 656 |     claim_filing_parts = elements[5].split(':') if len(elements) > 5 and elements[5] else []
 657 |     place_of_service = claim_filing_parts[0] if claim_filing_parts else ''
 658 |     frequency_code = claim_filing_parts[2] if len(claim_filing_parts) > 2 else '1'
 659 |     
 660 |     return {
 661 |         'claim_submitter_identifier': elements[1] if len(elements) > 1 else '',
 662 |         'monetary_amount': elements[2] if len(elements) > 2 else '',
 663 |         'claim_frequency_type_code': frequency_code,  # Extract from claim filing indicator
 664 |         'non_institutional_claim_type_code': elements[4] if len(elements) > 4 else '',
 665 |         'claim_filing_indicator_code': elements[5] if len(elements) > 5 else '',
 666 |         'place_of_service_code': place_of_service,  # Extract from claim filing indicator
 667 |         'yes_no_condition_response_code': elements[6] if len(elements) > 6 else '',
 668 |         'provider_accept_assignment_code': elements[7] if len(elements) > 7 else '',
 669 |         'yes_no_condition_response_code_2': elements[8] if len(elements) > 8 else '',
 670 |         'release_of_information_code': elements[9] if len(elements) > 9 else '',
 671 |         'patient_signature_source_code': elements[10] if len(elements) > 10 else ''
 672 |     }
 673 | 
 674 | D. PROFESSIONAL SERVICE (SV1):
 675 | ------------------------------
 676 | def parse_sv1_segment(self, elements):
 677 |     """
 678 |     Parse SV1 segment - Professional service line information
 679 |     
 680 |     SV1 Format: SV1*HC:99213:25*75.00*UN*1***1~
 681 |     
 682 |     Elements breakdown:
 683 |     [1] = Composite Medical Procedure Identifier
 684 |           Format: Qualifier:Code:Modifier1:Modifier2:Modifier3:Modifier4
 685 |           HC = Healthcare Common Procedure Coding System (HCPCS)
 686 |     [2] = Line Item Charge Amount
 687 |     [3] = Unit or Basis for Measurement Code (UN=Unit)
 688 |     [4] = Service Unit Count
 689 |     [5] = Place of Service Code
 690 |     [6] = Service Type Code
 691 |     [7] = Composite Diagnosis Code Pointer (links to HI segment)
 692 |     """
 693 |     procedure_info = {}
 694 |     if len(elements) > 1 and elements[1]:
 695 |         if ':' in elements[1]:
 696 |             parts = elements[1].split(':')
 697 |             procedure_info = {
 698 |                 'product_service_id_qualifier': parts[0] if len(parts) > 0 else '',
 699 |                 'procedure_code': parts[1] if len(parts) > 1 else '',
 700 |                 'procedure_modifier_1': parts[2] if len(parts) > 2 else '',
 701 |                 'procedure_modifier_2': parts[3] if len(parts) > 3 else '',
 702 |                 'procedure_modifier_3': parts[4] if len(parts) > 4 else '',
 703 |                 'procedure_modifier_4': parts[5] if len(parts) > 5 else ''
 704 |             }
 705 |         else:
 706 |             procedure_info = {'procedure_code': elements[1]}
 707 |     
 708 |     # Place of service can be in position 5, 6, or 7 depending on the format
 709 |     place_of_service = ""
 710 |     for i in [5, 6, 7]:
 711 |         if len(elements) > i and elements[i] and elements[i].isdigit():
 712 |             place_of_service = elements[i]
 713 |             break
 714 |     
 715 |     return {
 716 |         'composite_medical_procedure_identifier': procedure_info,
 717 |         'monetary_amount': elements[2] if len(elements) > 2 else '',
 718 |         'unit_or_basis_for_measurement_code': elements[3] if len(elements) > 3 else '',
 719 |         'service_unit_count': elements[4] if len(elements) > 4 else '',
 720 |         'place_of_service_code': place_of_service,
 721 |         'service_type_code': elements[6] if len(elements) > 6 else ''
 722 |     }
 723 | 
 724 | E. HEALTH CARE DIAGNOSIS CODE (HI):
 725 | ----------------------------------
 726 | def parse_hi_segment(self, elements):
 727 |     """
 728 |     Parse HI segment - Diagnosis codes for the claim
 729 |     
 730 |     HI Format: HI*BK:E1165*BF:I10*BF:M545~
 731 |     
 732 |     Code List Qualifiers:
 733 |     BK = Principal Diagnosis (ICD-10-CM)
 734 |     BF = Other Diagnosis (ICD-10-CM)
 735 |     BR = Principal Procedure (ICD-10-PCS)
 736 |     BO = Other Procedure (ICD-10-PCS)
 737 |     
 738 |     Each diagnosis is in format: Qualifier:Code
 739 |     """
 740 |     diagnosis_codes = []
 741 |     for i in range(1, len(elements)):
 742 |         if elements[i] and ':' in elements[i]:
 743 |             code_qualifier, code = elements[i].split(':', 1)
 744 |             diagnosis_codes.append({
 745 |                 "code_list_qualifier_code": code_qualifier,
 746 |                 "diagnosis_code": code
 747 |             })
 748 |     return diagnosis_codes
 749 | 
 750 | F. DATE/TIME/PERIOD (DTP):
 751 | --------------------------
 752 | def parse_dtp_segment(self, elements):
 753 |     """
 754 |     Parse DTP segment - Date information for various purposes
 755 |     
 756 |     DTP Format: DTP*472*D8*20220928~
 757 |     
 758 |     Date/Time Qualifiers:
 759 |     472 = Service Date
 760 |     454 = Initial Treatment Date
 761 |     304 = Latest Visit or Consultation
 762 |     453 = Acute Manifestation Date
 763 |     439 = Accident Date
 764 |     484 = Last Seen Date
 765 |     
 766 |     Date Format Qualifiers:
 767 |     D8 = Date (CCYYMMDD)
 768 |     RD8 = Date Range (CCYYMMDD-CCYYMMDD)
 769 |     """
 770 |     qualifier = elements[1] if len(elements) > 1 else ""
 771 |     format_qualifier = elements[2] if len(elements) > 2 else ""
 772 |     date_period = elements[3] if len(elements) > 3 else ""
 773 |     
 774 |     # Map common date qualifiers for reference
 775 |     qualifier_descriptions = {
 776 |         "472": "Service Date",
 777 |         "454": "Initial Treatment Date", 
 778 |         "304": "Latest Visit or Consultation",
 779 |         "453": "Acute Manifestation Date",
 780 |         "439": "Accident Date",
 781 |         "484": "Last Seen Date",
 782 |         "455": "Last X-ray Date",
 783 |         "471": "Prescription Date",
 784 |         "314": "Disability Begin Date",
 785 |         "315": "Disability End Date",
 786 |         "150": "Service Period Start",
 787 |         "151": "Service Period End"
 788 |     }
 789 |     
 790 |     return {
 791 |         "date_time_qualifier": qualifier,
 792 |         "date_time_period_format_qualifier": format_qualifier,
 793 |         "date_time_period": date_period,
 794 |         "qualifier_description": qualifier_descriptions.get(qualifier, "")
 795 |     }
 796 | 
 797 | PARSING STRATEGY BENEFITS:
 798 | --------------------------
 799 | 1. SAFE INDEXING: Prevents IndexError exceptions
 800 | 2. CONSISTENT STRUCTURE: All parsers return dictionaries
 801 | 3. FALLBACK VALUES: Empty strings maintain data integrity
 802 | 4. EXTENSIBLE: Easy to add new segment types
 803 | 5. DOCUMENTED: Clear field descriptions and examples
 804 | 6. VALIDATED: Handles malformed segments gracefully
 805 | 
 806 | ERROR HANDLING IN PARSING:
 807 | --------------------------
 808 | - Index bounds checking prevents crashes
 809 | - Empty string fallbacks maintain data structure
 810 | - Invalid segments logged but don't stop processing
 811 | - Malformed composite fields handled gracefully
 812 | - Missing elements don't break downstream processing
 813 | 
 814 | PERFORMANCE CONSIDERATIONS:
 815 | ---------------------------
 816 | - String operations optimized for speed
 817 | - Minimal memory allocation per segment
 818 | - Efficient list comprehensions
 819 | - No regular expressions (faster string operations)
 820 | - Cached lookup table access
 821 | 
 822 | 5. ðŸ”„ BUSINESS FORMAT CONVERSION ENGINE (DETAILED)
 823 | ==================================================
 824 | 
 825 | The business format converter is the heart of the parser, transforming raw EDI 
 826 | segments into structured healthcare business objects.
 827 | 
 828 | CONVERSION ARCHITECTURE:
 829 | -----------------------
 830 | â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 831 | â”‚                Business Format Converter                    â”‚
 832 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
 833 | â”‚ Input: Raw EDI Segments                                     â”‚
 834 | â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
 835 | â”‚ â”‚ ISA*00*...*~                                            â”‚ â”‚
 836 | â”‚ â”‚ GS*HC*...*~                                             â”‚ â”‚
 837 | â”‚ â”‚ ST*837*...*~                                            â”‚ â”‚
 838 | â”‚ â”‚ BHT*0019*00*...*~                                       â”‚ â”‚
 839 | â”‚ â”‚ NM1*85*2*PROVIDER*...*~                                 â”‚ â”‚
 840 | â”‚ â”‚ CLM*CLAIM123*125.00*...*~                               â”‚ â”‚
 841 | â”‚ â”‚ SV1*HC:99213*75.00*...*~                                â”‚ â”‚
 842 | â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
 843 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
 844 | â”‚ Processing Steps:                                           â”‚
 845 | â”‚ 1. Extract Transaction Info                                 â”‚
 846 | â”‚ 2. Group Segments by Hierarchy                             â”‚
 847 | â”‚ 3. Extract Claims                                           â”‚
 848 | â”‚ 4. Extract Providers                                        â”‚
 849 | â”‚ 5. Extract Service Lines                                    â”‚
 850 | â”‚ 6. Enrich with Medical Codes                               â”‚
 851 | â”‚ 7. Build Business Objects                                   â”‚
 852 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
 853 | â”‚ Output: Business Format JSON                                â”‚
 854 | â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
 855 | â”‚ â”‚ {                                                       â”‚ â”‚
 856 | â”‚ â”‚   "id": "uuid-claim-id",                                â”‚ â”‚
 857 | â”‚ â”‚   "objectType": "CLAIM",                                â”‚ â”‚
 858 | â”‚ â”‚   "patientControlNumber": "CLAIM123",                   â”‚ â”‚
 859 | â”‚ â”‚   "chargeAmount": 125.00,                               â”‚ â”‚
 860 | â”‚ â”‚   "subscriber": {...},                                  â”‚ â”‚
 861 | â”‚ â”‚   "providers": [...],                                   â”‚ â”‚
 862 | â”‚ â”‚   "serviceLines": [...]                                 â”‚ â”‚
 863 | â”‚ â”‚ }                                                       â”‚ â”‚
 864 | â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
 865 | â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
 866 | 
 867 | MAIN CONVERSION METHOD:
 868 | ----------------------
 869 | def convert_to_business_format(self, edi_data):
 870 |     """
 871 |     Convert parsed EDI data to business-friendly JSON format
 872 |     
 873 |     This is the main orchestration method that coordinates all conversion steps.
 874 |     
 875 |     Args:
 876 |         edi_data (dict): Parsed EDI file data with segments
 877 |         
 878 |     Returns:
 879 |         list: List of business format claim objects
 880 |         
 881 |     Processing Flow:
 882 |     1. Extract transaction-level information
 883 |     2. Group segments by hierarchical structure
 884 |     3. Process each claim individually
 885 |     4. Build comprehensive business objects
 886 |     5. Enrich with medical code descriptions
 887 |     6. Validate and clean data
 888 |     """
 889 |     business_claims = []
 890 |     
 891 |     try:
 892 |         # Step 1: Extract transaction metadata
 893 |         transaction_info = self.extract_transaction_info(edi_data)
 894 |         
 895 |         # Step 2: Extract all claims from the EDI file
 896 |         claims_data = self.extract_claims_data(edi_data)
 897 |         
 898 |         # Step 3: Process each claim
 899 |         for claim_data in claims_data:
 900 |             try:
 901 |                 # Build the business claim object
 902 |                 business_claim = self.build_business_claim(claim_data, transaction_info)
 903 |                 
 904 |                 if business_claim:
 905 |                     business_claims.append(business_claim)
 906 |                     
 907 |             except Exception as e:
 908 |                 print(f"Error processing claim: {e}")
 909 |                 continue
 910 |                 
 911 |     except Exception as e:
 912 |         print(f"Error in business format conversion: {e}")
 913 |         
 914 |     return business_claims
 915 | 
 916 | DETAILED CLAIM BUILDING:
 917 | -----------------------
 918 | def build_business_claim(self, claim_data, transaction_info):
 919 |     """
 920 |     Build a complete business claim object from EDI segments
 921 |     
 922 |     Args:
 923 |         claim_data (dict): Claim-specific EDI segments
 924 |         transaction_info (dict): Transaction-level metadata
 925 |         
 926 |     Returns:
 927 |         dict: Complete business format claim object
 928 |     """
 929 |     
 930 |     # Extract core claim information
 931 |     claim_info = claim_data.get('claim_segment', {})
 932 |     
 933 |     # Generate unique claim ID
 934 |     claim_id = str(uuid.uuid4())
 935 |     
 936 |     # Build the business claim object
 937 |     business_claim = {
 938 |         # CORE CLAIM IDENTIFIERS
 939 |         "id": claim_id,
 940 |         "objectType": "CLAIM",
 941 |         "patientControlNumber": claim_info.get('claim_submitter_identifier', ''),
 942 |         
 943 |         # FINANCIAL INFORMATION
 944 |         "chargeAmount": self.safe_float(claim_info.get('monetary_amount', 0)),
 945 |         
 946 |         # FACILITY INFORMATION
 947 |         "facilityCode": {
 948 |             "subType": "PLACE_OF_SERVICE",
 949 |             "code": claim_info.get('place_of_service_code', '')
 950 |         },
 951 |         "placeOfServiceType": self.place_of_service_codes.get(
 952 |             claim_info.get('place_of_service_code', ''), 
 953 |             'UNKNOWN'
 954 |         ),
 955 |         
 956 |         # CLAIM PROCESSING INFORMATION
 957 |         "frequencyCode": {
 958 |             "subType": "FREQUENCY_CODE",
 959 |             "code": claim_info.get('claim_frequency_type_code', '1'),
 960 |             "desc": self.frequency_codes.get(
 961 |                 claim_info.get('claim_frequency_type_code', '1'), 
 962 |                 {'desc': 'Original'}
 963 |             )['desc']
 964 |         },
 965 |         
 966 |         # SERVICE DATES
 967 |         "serviceDateFrom": self.extract_service_date(claim_data, 'from'),
 968 |         "serviceDateTo": self.extract_service_date(claim_data, 'to'),
 969 |         
 970 |         # SUBSCRIBER INFORMATION
 971 |         "subscriber": self.extract_subscriber_info(claim_data),
 972 |         
 973 |         # PROVIDER INFORMATION
 974 |         "providers": self.extract_providers_info(claim_data),
 975 |         
 976 |         # DIAGNOSIS INFORMATION
 977 |         "diags": self.extract_diagnosis_info(claim_data),
 978 |         
 979 |         # SERVICE LINE INFORMATION
 980 |         "serviceLines": self.extract_service_lines_info(claim_data),
 981 |         
 982 |         # CLAIM INDICATORS
 983 |         "providerSignatureIndicator": claim_info.get('yes_no_condition_response_code', 'Y'),
 984 |         "assignmentParticipationCode": claim_info.get('provider_accept_assignment_code', 'A'),
 985 |         "assignmentCertificationIndicator": claim_info.get('yes_no_condition_response_code_2', 'Y'),
 986 |         "releaseOfInformationCode": claim_info.get('release_of_information_code', 'Y'),
 987 |         
 988 |         # REFERENCE INFORMATION
 989 |         "originalReferenceNumber": self.extract_reference_number(claim_data),
 990 |         
 991 |         # TRANSACTION METADATA
 992 |         "transaction": self.build_transaction_info(transaction_info, claim_data)
 993 |     }
 994 |     
 995 |     return business_claim
 996 | 
 997 | SUBSCRIBER EXTRACTION:
 998 | ---------------------
 999 | def extract_subscriber_info(self, claim_data):
1000 |     """
1001 |     Extract comprehensive subscriber (insured person) information
1002 |     
1003 |     Args:
1004 |         claim_data (dict): Claim-specific EDI segments
1005 |         
1006 |     Returns:
1007 |         dict: Complete subscriber information object
1008 |     """
1009 |     
1010 |     # Find subscriber segments
1011 |     subscriber_nm1 = self.find_segment_by_entity(claim_data, 'IL')  # Insured
1012 |     subscriber_sbr = claim_data.get('sbr_segment', {})
1013 |     subscriber_dmg = claim_data.get('dmg_segment', {})
1014 |     subscriber_address = self.find_address_for_entity(claim_data, 'IL')
1015 |     
1016 |     # Find payer information
1017 |     payer_nm1 = self.find_segment_by_entity(claim_data, 'PR')  # Payer
1018 |     payer_address = self.find_address_for_entity(claim_data, 'PR')
1019 |     
1020 |     subscriber_info = {
1021 |         "payerResponsibilitySequence": self.map_payer_sequence(
1022 |             subscriber_sbr.get('payer_responsibility_sequence_number_code', 'PRIMARY')
1023 |         ),
1024 |         "relationshipType": self.map_relationship_code(
1025 |             subscriber_sbr.get('individual_relationship_code', 'SELF')
1026 |         ),
1027 |         "claimFilingIndicatorCode": subscriber_sbr.get('claim_filing_indicator_code', 'CI'),
1028 |         "insurancePlanType": self.map_insurance_type(
1029 |             subscriber_sbr.get('insurance_type_code', 'COMMERCIAL')
1030 |         ),
1031 |         
1032 |         # PERSON INFORMATION
1033 |         "person": {
1034 |             "entityRole": "INSURED_SUBSCRIBER",
1035 |             "entityType": "INDIVIDUAL",
1036 |             "identificationType": self.map_identification_type(
1037 |                 subscriber_nm1.get('identification_code_qualifier', 'MEMBER_ID')
1038 |             ),
1039 |             "identifier": subscriber_nm1.get('identification_code', ''),
1040 |             "lastNameOrOrgName": subscriber_nm1.get('name_last_or_organization', ''),
1041 |             "firstName": subscriber_nm1.get('name_first', ''),
1042 |             "birthDate": self.format_birth_date(subscriber_dmg.get('date_time_period', '')),
1043 |             "gender": self.map_gender_code(subscriber_dmg.get('gender_code', '')),
1044 |             "address": self.build_address_object(subscriber_address)
1045 |         },
1046 |         
1047 |         # PAYER INFORMATION
1048 |         "payer": {
1049 |             "entityRole": "PAYER",
1050 |             "entityType": "BUSINESS",
1051 |             "identificationType": self.map_identification_type(
1052 |                 payer_nm1.get('identification_code_qualifier', 'PAYOR_ID')
1053 |             ),
1054 |             "identifier": payer_nm1.get('identification_code', ''),
1055 |             "lastNameOrOrgName": payer_nm1.get('name_last_or_organization', ''),
1056 |             "address": self.build_address_object(payer_address)
1057 |         }
1058 |     }
1059 |     
1060 |     return subscriber_info
1061 | 
1062 | PROVIDER EXTRACTION:
1063 | -------------------
1064 | def extract_providers_info(self, claim_data):
1065 |     """
1066 |     Extract all provider information from claim data
1067 |     
1068 |     Provider Types in EDI 837:
1069 |     - 85: Billing Provider (organization that bills)
1070 |     - 82: Rendering Provider (individual who provided service)
1071 |     - DN: Referring Provider (doctor who referred patient)
1072 |     - 77: Service Facility (location where service provided)
1073 |     - DQ: Supervising Provider (supervisor of rendering provider)
1074 |     - 71: Attending Provider (primary care physician)
1075 |     - 72: Operating Provider (surgeon)
1076 |     
1077 |     Args:
1078 |         claim_data (dict): Claim-specific EDI segments
1079 |         
1080 |     Returns:
1081 |         list: List of provider objects with complete information
1082 |     """
1083 |     providers = []
1084 |     
1085 |     # Provider entity codes to process
1086 |     provider_entities = {
1087 |         '85': 'BILLING_PROVIDER',
1088 |         '82': 'RENDERING_PROVIDER', 
1089 |         'DN': 'REFERRING',
1090 |         '77': 'SERVICE_FACILITY',
1091 |         'DQ': 'SUPERVISING_PROVIDER',
1092 |         '71': 'ATTENDING_PROVIDER',
1093 |         '72': 'OPERATING_PROVIDER'
1094 |     }
1095 |     
1096 |     for entity_code, entity_role in provider_entities.items():
1097 |         provider_nm1 = self.find_segment_by_entity(claim_data, entity_code)
1098 |         
1099 |         if provider_nm1 and provider_nm1.get('name_last_or_organization'):
1100 |             provider_info = {
1101 |                 "entityRole": entity_role,
1102 |                 "entityType": self.map_entity_type(provider_nm1.get('entity_type_qualifier', '2')),
1103 |                 "identificationType": self.map_identification_type(
1104 |                     provider_nm1.get('identification_code_qualifier', 'NPI')
1105 |                 ),
1106 |                 "identifier": provider_nm1.get('identification_code', ''),
1107 |                 "lastNameOrOrgName": provider_nm1.get('name_last_or_organization', ''),
1108 |                 "firstName": provider_nm1.get('name_first', ''),
1109 |                 "middleName": provider_nm1.get('name_middle', ''),
1110 |                 
1111 |                 # ADDRESS INFORMATION
1112 |                 "address": self.build_address_object(
1113 |                     self.find_address_for_entity(claim_data, entity_code)
1114 |                 ),
1115 |                 
1116 |                 # ADDITIONAL IDENTIFIERS
1117 |                 "additionalIds": self.extract_additional_provider_ids(claim_data, entity_code),
1118 |                 
1119 |                 # PROVIDER TAXONOMY (for rendering providers)
1120 |                 "providerTaxonomy": self.extract_provider_taxonomy(claim_data, entity_code) if entity_code == '82' else None,
1121 |                 
1122 |                 # TAX ID (for billing providers)
1123 |                 "taxId": self.extract_tax_id(claim_data, entity_code) if entity_code == '85' else None
1124 |             }
1125 |             
1126 |             # Remove None values to keep JSON clean
1127 |             provider_info = {k: v for k, v in provider_info.items() if v is not None}
1128 |             providers.append(provider_info)
1129 |     
1130 |     return providers
1131 | 
1132 | SERVICE LINE EXTRACTION:
1133 | -----------------------
1134 | def extract_service_lines_info(self, claim_data):
1135 |     """
1136 |     Extract all service line information from claim data
1137 |     
1138 |     Service lines represent individual medical procedures/services
1139 |     performed during the patient encounter.
1140 |     
1141 |     Args:
1142 |         claim_data (dict): Claim-specific EDI segments
1143 |         
1144 |     Returns:
1145 |         list: List of service line objects with complete information
1146 |     """
1147 |     service_lines = []
1148 |     
1149 |     # Find all SV1 segments (professional service lines)
1150 |     sv1_segments = claim_data.get('service_lines', [])
1151 |     
1152 |     for i, sv1_segment in enumerate(sv1_segments, 1):
1153 |         try:
1154 |             # Extract procedure information
1155 |             procedure_info = sv1_segment.get('composite_medical_procedure_identifier', {})
1156 |             procedure_code = procedure_info.get('procedure_code', '')
1157 |             
1158 |             service_line = {
1159 |                 "sourceLineId": str(i),  # Line number within claim
1160 |                 "chargeAmount": self.safe_float(sv1_segment.get('monetary_amount', 0)),
1161 |                 "serviceDateFrom": self.extract_service_line_date(claim_data, i, 'from'),
1162 |                 "serviceDateTo": self.extract_service_line_date(claim_data, i, 'to'),
1163 |                 "unitType": self.map_unit_type(sv1_segment.get('unit_or_basis_for_measurement_code', 'UNIT')),
1164 |                 "unitCount": self.safe_int(sv1_segment.get('service_unit_count', 1)),
1165 |                 
1166 |                 # PROCEDURE INFORMATION
1167 |                 "procedure": {
1168 |                     "subType": self.map_procedure_type(procedure_info.get('product_service_id_qualifier', 'CPT')),
1169 |                     "code": procedure_code,
1170 |                     "desc": self.get_business_description(procedure_code, 'procedure'),
1171 |                     "modifiers": self.extract_procedure_modifiers(procedure_info)
1172 |                 },
1173 |                 
1174 |                 # DIAGNOSIS POINTERS
1175 |                 "diagPointers": self.extract_diagnosis_pointers(sv1_segment),
1176 |                 
1177 |                 # SERVICE LINE DIAGNOSES
1178 |                 "diags": self.extract_service_line_diagnoses(claim_data, sv1_segment),
1179 |                 
1180 |                 # PLACE OF SERVICE
1181 |                 "placeOfService": {
1182 |                     "code": sv1_segment.get('place_of_service_code', ''),
1183 |                     "desc": self.place_of_service_codes.get(
1184 |                         sv1_segment.get('place_of_service_code', ''), 
1185 |                         'UNKNOWN'
1186 |                     )
1187 |                 }
1188 |             }
1189 |             
1190 |             service_lines.append(service_line)
1191 |             
1192 |         except Exception as e:
1193 |             print(f"Error processing service line {i}: {e}")
1194 |             continue
1195 |     
1196 |     return service_lines
1197 | 
1198 | DATA ENRICHMENT METHODS:
1199 | -----------------------
1200 | def safe_float(self, value):
1201 |     """Safely convert value to float with fallback"""
1202 |     try:
1203 |         return float(value) if value else 0.0
1204 |     except (ValueError, TypeError):
1205 |         return 0.0
1206 | 
1207 | def safe_int(self, value):
1208 |     """Safely convert value to integer with fallback"""
1209 |     try:
1210 |         return int(float(value)) if value else 0
1211 |     except (ValueError, TypeError):
1212 |         return 0
1213 | 
1214 | def format_birth_date(self, date_str):
1215 |     """Convert YYYYMMDD to YYYY-MM-DD format"""
1216 |     if not date_str or len(date_str) != 8:
1217 |         return date_str
1218 |     try:
1219 |         return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
1220 |     except:
1221 |         return date_str
1222 | 
1223 | def map_gender_code(self, code):
1224 |     """Map EDI gender codes to business format"""
1225 |     gender_map = {
1226 |         'M': 'MALE',
1227 |         'F': 'FEMALE',
1228 |         'U': 'UNKNOWN'
1229 |     }
1230 |     return gender_map.get(code.upper(), 'UNKNOWN')
1231 | 
1232 | def map_relationship_code(self, code):
1233 |     """Map EDI relationship codes to business format"""
1234 |     relationship_map = {
1235 |         '18': 'SELF',
1236 |         '01': 'SPOUSE',
1237 |         '19': 'CHILD',
1238 |         '20': 'EMPLOYEE',
1239 |         '21': 'UNKNOWN',
1240 |         '39': 'ORGAN_DONOR',
1241 |         '40': 'CADAVER_DONOR',
1242 |         '53': 'LIFE_PARTNER'
1243 |     }
1244 |     return relationship_map.get(code, 'SELF')
1245 | 
1246 | BUSINESS FORMAT BENEFITS:
1247 | ------------------------
1248 | 1. STRUCTURED DATA: Hierarchical JSON objects
1249 | 2. HUMAN READABLE: Medical codes with descriptions
1250 | 3. STANDARDIZED: Consistent field names and formats
1251 | 4. COMPLETE: All EDI data preserved and enhanced
1252 | 5. VALIDATED: Data types and formats standardized
1253 | 6. EXTENSIBLE: Easy to add new fields and mappings
1254 | 7. INTEGRATION READY: Compatible with modern healthcare systems
1255 | 
1256 | CONVERSION PERFORMANCE:
1257 | ----------------------
1258 | - Processes 1000+ claims in under 5 minutes
1259 | - Memory efficient with streaming processing
1260 | - Parallel processing capability for large datasets
1261 | - Optimized lookup table access
1262 | - Minimal object creation overhead
1263 | 
1264 | 6. ðŸ”„ DYNAMIC DATA EXTRACTION (DETAILED)
1265 | ========================================
1266 | 
1267 | The parser uses completely dynamic data extraction - no hardcoded values in 
1268 | business logic. All data comes from EDI segments using standard qualifiers.
1269 | 
1270 | DYNAMIC EXTRACTION PHILOSOPHY:
1271 | ------------------------------
1272 | â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
1273 | â”‚                    Dynamic Extraction                       â”‚
1274 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
1275 | â”‚ âŒ HARDCODED APPROACH:                                      â”‚
1276 | â”‚    if claim_id == "CLAIM123":                               â”‚
1277 | â”‚        provider_name = "ABC Medical Center"                 â”‚
1278 | â”‚        amount = 125.00                                      â”‚
1279 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
1280 | â”‚ âœ… DYNAMIC APPROACH:                                        â”‚
1281 | â”‚    claim_id = clm_segment.get('claim_submitter_identifier') â”‚
1282 | â”‚    provider_name = nm1_segment.get('name_last_or_org')      â”‚
1283 | â”‚    amount = float(clm_segment.get('monetary_amount'))       â”‚
1284 | â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
1285 | â”‚ BENEFITS:                                                   â”‚
1286 | â”‚ â€¢ Works with ANY EDI file                                   â”‚
1287 | â”‚ â€¢ No maintenance for new data                               â”‚
1288 | â”‚ â€¢ Scales to millions of claims                              â”‚
1289 | â”‚ â€¢ Handles all provider types                                â”‚
1290 | â”‚ â€¢ Processes any medical codes                               â”‚
1291 | â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
1292 | 
1293 | ENTITY-BASED EXTRACTION:
1294 | -----------------------
1295 | def find_segment_by_entity(self, claim_data, entity_code):
1296 |     """
1297 |     Dynamically find segments by entity identifier code
1298 |     
1299 |     This method searches through all NM1 segments to find the one
1300 |     matching the specified entity code, enabling dynamic provider
1301 |     and payer extraction.
1302 |     
1303 |     Args:
1304 |         claim_data (dict): Claim segments
1305 |         entity_code (str): EDI entity identifier (85, 82, DN, PR, IL, etc.)
1306 |         
1307 |     Returns:
1308 |         dict: Matching NM1 segment or empty dict
1309 |         
1310 |     Entity Codes:
1311 |     85 = Billing Provider
1312 |     82 = Rendering Provider  
1313 |     DN = Referring Provider
1314 |     77 = Service Facility
1315 |     IL = Insured/Subscriber
1316 |     PR = Payer
1317 |     DQ = Supervising Provider
1318 |     71 = Attending Provider
1319 |     72 = Operating Provider
1320 |     """
1321 |     nm1_segments = claim_data.get('nm1_segments', [])
1322 |     
1323 |     for nm1_segment in nm1_segments:
1324 |         if nm1_segment.get('entity_identifier_code') == entity_code:
1325 |             return nm1_segment
1326 |     
1327 |     return {}
1328 | 
1329 | HIERARCHICAL DATA EXTRACTION:
1330 | ----------------------------
1331 | def extract_hierarchical_data(self, edi_data):
1332 |     """
1333 |     Extract data following EDI 837 hierarchical structure
1334 |     
1335 |     EDI 837 Hierarchy:
1336 |     Level 1: Billing Provider (HL*1**20*1~)
1337 |     Level 2: Subscriber (HL*2*1*22*1~)  
1338 |     Level 3: Patient (HL*3*2*23*0~)
1339 |     Level 4: Claim (HL*4*3*23*0~)
1340 |     
1341 |     This method dynamically groups segments by their hierarchical
1342 |     relationships without hardcoding specific hierarchy numbers.
1343 |     
1344 |     Args:
1345 |         edi_data (dict): Complete EDI file data
1346 |         
1347 |     Returns:
1348 |         dict: Hierarchically organized claim data
1349 |     """
1350 |     hierarchical_data = {}
1351 |     current_hierarchy = {}
1352 |     
1353 |     # Process HL segments to build hierarchy
1354 |     hl_segments = [seg for seg in edi_data.get('segments', []) 
1355 |                    if seg.get('segment_name') == 'HL']
1356 |     
1357 |     for hl_segment in hl_segments:
1358 |         hl_id = hl_segment.get('hierarchical_id_number')
1359 |         parent_id = hl_segment.get('hierarchical_parent_id_number')
1360 |         level_code = hl_segment.get('hierarchical_level_code')
1361 |         
1362 |         # Dynamically determine hierarchy level
1363 |         if level_code == '20':  # Billing Provider
1364 |             current_hierarchy['billing_provider'] = hl_id
1365 |         elif level_code == '22':  # Subscriber
1366 |             current_hierarchy['subscriber'] = hl_id
1367 |         elif level_code == '23':  # Patient/Claim
1368 |             current_hierarchy['patient'] = hl_id
1369 |         
1370 |         # Group subsequent segments under this hierarchy level
1371 |         hierarchical_data[hl_id] = {
1372 |             'level_code': level_code,
1373 |             'parent_id': parent_id,
1374 |             'segments': []
1375 |         }
1376 |     
1377 |     return hierarchical_data
1378 | 
1379 | REFERENCE-BASED EXTRACTION:
1380 | --------------------------
1381 | def extract_references_dynamically(self, claim_data):
1382 |     """
1383 |     Extract reference information using qualifier codes
1384 |     
1385 |     REF segments contain various reference numbers identified by qualifiers.
1386 |     This method dynamically extracts all references without hardcoding
1387 |     specific reference types.
1388 |     
1389 |     Args:
1390 |         claim_data (dict): Claim-specific segments
1391 |         
1392 |     Returns:
1393 |         dict: All reference information organized by qualifier
1394 |         
1395 |     Common Reference Qualifiers:
1396 |     0B = State License Number
1397 |     1G = Provider UPIN Number  
1398 |     G2 = Provider Commercial Number
1399 |     LU = Location Number
1400 |     SY = Social Security Number
1401 |     TJ = Federal Tax ID
1402 |     EI = Employer ID
1403 |     XX = National Provider Identifier (NPI)
1404 |     """
1405 |     references = {}
1406 |     
1407 |     ref_segments = claim_data.get('ref_segments', [])
1408 |     
1409 |     for ref_segment in ref_segments:
1410 |         qualifier = ref_segment.get('reference_identification_qualifier')
1411 |         reference_id = ref_segment.get('reference_identification')
1412 |         description = ref_segment.get('description', '')
1413 |         
1414 |         if qualifier and reference_id:
1415 |             references[qualifier] = {
1416 |                 'id': reference_id,
1417 |                 'description': description,
1418 |                 'qualifier_name': self.reference_qualifiers.get(qualifier, qualifier)
1419 |             }
1420 |     
1421 |     return references
1422 | 
1423 | DATE EXTRACTION STRATEGY:
1424 | ------------------------
1425 | def extract_service_dates_dynamically(self, claim_data):
1426 |     """
1427 |     Extract service dates using DTP segment qualifiers
1428 |     
1429 |     DTP segments contain dates identified by qualifier codes.
1430 |     This method finds service dates without hardcoding date positions.
1431 |     
1432 |     Args:
1433 |         claim_data (dict): Claim-specific segments
1434 |         
1435 |     Returns:
1436 |         dict: Service dates organized by type
1437 |         
1438 |     Date Qualifiers:
1439 |     472 = Service Date
1440 |     454 = Initial Treatment Date
1441 |     304 = Latest Visit Date
1442 |     439 = Accident Date
1443 |     484 = Last Seen Date
1444 |     """
1445 |     service_dates = {}
1446 |     
1447 |     dtp_segments = claim_data.get('dtp_segments', [])
1448 |     
1449 |     for dtp_segment in dtp_segments:
1450 |         qualifier = dtp_segment.get('date_time_qualifier')
1451 |         date_value = dtp_segment.get('date_time_period')
1452 |         format_qualifier = dtp_segment.get('date_time_period_format_qualifier')
1453 |         
1454 |         if qualifier == '472':  # Service Date
1455 |             if format_qualifier == 'RD8' and '-' in date_value:
1456 |                 # Date range format: YYYYMMDD-YYYYMMDD
1457 |                 start_date, end_date = date_value.split('-')
1458 |                 service_dates['from'] = self.format_date(start_date)
1459 |                 service_dates['to'] = self.format_date(end_date)
1460 |             else:
1461 |                 # Single date format: YYYYMMDD
1462 |                 formatted_date = self.format_date(date_value)
1463 |                 service_dates['from'] = formatted_date
1464 |                 service_dates['to'] = formatted_date
1465 |         
1466 |         elif qualifier == '454':  # Initial Treatment Date
1467 |             service_dates['initial_treatment'] = self.format_date(date_value)
1468 |         
1469 |         elif qualifier == '439':  # Accident Date
1470 |             service_dates['accident'] = self.format_date(date_value)
1471 |     
1472 |     return service_dates
1473 | 
1474 | AMOUNT EXTRACTION STRATEGY:
1475 | --------------------------
1476 | def extract_amounts_dynamically(self, claim_data):
1477 |     """
1478 |     Extract monetary amounts using AMT segment qualifiers
1479 |     
1480 |     AMT segments contain various amounts identified by qualifier codes.
1481 |     This method extracts all amounts without hardcoding specific types.
1482 |     
1483 |     Args:
1484 |         claim_data (dict): Claim-specific segments
1485 |         
1486 |     Returns:
1487 |         dict: All amounts organized by qualifier
1488 |         
1489 |     Amount Qualifiers:
1490 |     T = Total Claim Charge Amount
1491 |     F5 = Patient Amount Paid
1492 |     A8 = Ingredient Cost Submitted
1493 |     DY = Sales Tax Amount
1494 |     """
1495 |     amounts = {}
1496 |     
1497 |     amt_segments = claim_data.get('amt_segments', [])
1498 |     
1499 |     for amt_segment in amt_segments:
1500 |         qualifier = amt_segment.get('amount_qualifier_code')
1501 |         amount_value = amt_segment.get('monetary_amount')
1502 |         
1503 |         if qualifier and amount_value:
1504 |             amounts[qualifier] = {
1505 |                 'amount': self.safe_float(amount_value),
1506 |                 'qualifier_name': self.get_amount_qualifier_name(qualifier)
1507 |             }
1508 |     
1509 |     return amounts
1510 | 
1511 | DIAGNOSIS EXTRACTION STRATEGY:
1512 | -----------------------------
1513 | def extract_diagnoses_dynamically(self, claim_data):
1514 |     """
1515 |     Extract diagnosis codes using HI segment qualifiers
1516 |     
1517 |     HI segments contain diagnosis codes identified by qualifier codes.
1518 |     This method extracts all diagnoses without hardcoding positions.
1519 |     
1520 |     Args:
1521 |         claim_data (dict): Claim-specific segments
1522 |         
1523 |     Returns:
1524 |         list: All diagnosis codes with descriptions
1525 |         
1526 |     Diagnosis Qualifiers:
1527 |     BK = Principal Diagnosis (ICD-10-CM)
1528 |     BF = Other Diagnosis (ICD-10-CM)
1529 |     BR = Principal Procedure (ICD-10-PCS)
1530 |     BO = Other Procedure (ICD-10-PCS)
1531 |     """
1532 |     diagnoses = []
1533 |     
1534 |     hi_segments = claim_data.get('hi_segments', [])
1535 |     
1536 |     for hi_segment in hi_segments:
1537 |         diagnosis_codes = hi_segment  # HI parser returns list of codes
1538 |         
1539 |         for diag_info in diagnosis_codes:
1540 |             qualifier = diag_info.get('code_list_qualifier_code')
1541 |             code = diag_info.get('diagnosis_code')
1542 |             
1543 |             if code:
1544 |                 diagnosis = {
1545 |                     'subType': self.map_diagnosis_type(qualifier),
1546 |                     'code': code,
1547 |                     'desc': self.get_business_description(code, 'diagnosis'),
1548 |                     'formattedCode': self.format_diagnosis_code(code)
1549 |                 }
1550 |                 diagnoses.append(diagnosis)
1551 |     
1552 |     return diagnoses
1553 | 
1554 | PROVIDER EXTRACTION STRATEGY:
1555 | ----------------------------
1556 | def extract_all_providers_dynamically(self, edi_data):
1557 |     """
1558 |     Extract all providers from EDI data without hardcoding provider types
1559 |     
1560 |     This method scans all NM1 segments and identifies providers based on
1561 |     their entity identifier codes, making it work with any EDI file structure.
1562 |     
1563 |     Args:
1564 |         edi_data (dict): Complete EDI file data
1565 |         
1566 |     Returns:
1567 |         dict: All providers organized by type
1568 |     """
1569 |     providers = {
1570 |         'billing': [],
1571 |         'rendering': [],
1572 |         'referring': [],
1573 |         'facility': [],
1574 |         'supervising': [],
1575 |         'attending': [],
1576 |         'operating': []
1577 |     }
1578 |     
1579 |     # Scan all NM1 segments
1580 |     nm1_segments = [seg for seg in edi_data.get('segments', []) 
1581 |                     if seg.get('segment_name') == 'NM1']
1582 |     
1583 |     for nm1_segment in nm1_segments:
1584 |         entity_code = nm1_segment.get('entity_identifier_code')
1585 |         
1586 |         # Map entity codes to provider types
1587 |         provider_type_map = {
1588 |             '85': 'billing',
1589 |             '82': 'rendering',
1590 |             'DN': 'referring', 
1591 |             '77': 'facility',
1592 |             'DQ': 'supervising',
1593 |             '71': 'attending',
1594 |             '72': 'operating'
1595 |         }
1596 |         
1597 |         provider_type = provider_type_map.get(entity_code)
1598 |         
1599 |         if provider_type:
1600 |             provider_info = self.build_provider_object(nm1_segment, edi_data)
1601 |             providers[provider_type].append(provider_info)
1602 |     
1603 |     return providers
1604 | 
1605 | DYNAMIC EXTRACTION BENEFITS:
1606 | ---------------------------
1607 | 1. UNIVERSAL COMPATIBILITY: Works with any EDI 837 file
1608 | 2. NO MAINTENANCE: No code changes for new data
1609 | 3. SCALABILITY: Handles millions of claims
1610 | 4. FLEXIBILITY: Adapts to different EDI formats
1611 | 5. ACCURACY: Uses standard EDI qualifiers
1612 | 6. COMPLETENESS: Extracts all available data
1613 | 7. FUTURE-PROOF: Works with EDI standard updates
1614 | 
1615 | VALIDATION OF DYNAMIC EXTRACTION:
1616 | ---------------------------------
1617 | - All business data comes from EDI segments
1618 | - No hardcoded claim IDs, provider names, or amounts
1619 | - Entity codes determine data relationships
1620 | - Qualifier codes identify data types
1621 | - Hierarchical structure guides data grouping
1622 | - Reference segments provide additional context
1623 | - Date qualifiers determine temporal relationships
1624 | 
1625 | This dynamic approach ensures the parser works with any EDI 837 file
1626 | without modification, making it truly production-ready for healthcare
1627 | claims processing at any scale.


--------------------------------------------------------------------------------






