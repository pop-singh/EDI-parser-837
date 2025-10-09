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






