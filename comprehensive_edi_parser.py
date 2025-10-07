#!/usr/bin/env python3
"""
Comprehensive EDI 837 parser that extracts all fields to match the three CSV structures:
- EDI_Claims.csv (claim-level data)
- COMPANY_SETUP.csv (company/trading partner setup)
- EDI_ClaimDetail.csv (service line details)
"""

import os
import json
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime

class ComprehensiveEDIParser:
    def __init__(self):
        # Initialize data containers
        self.claims_data = []
        self.company_setup_data = []
        self.claim_details_data = []
        
        # Counters for IDs
        self.claim_id_counter = 1
        self.detail_id_counter = 1
        self.company_id_counter = 1
        
        # Lookup tables
        self.init_lookup_tables()
    
    def init_lookup_tables(self):
        """Initialize lookup tables for code mappings"""
        self.place_of_service_codes = {
            '11': 'Office', '12': 'Home', '21': 'Inpatient Hospital',
            '22': 'Outpatient Hospital', '23': 'Emergency Room'
        }
        
        self.entity_identifiers = {
            '40': 'Receiver', '41': 'Submitter', '85': 'Billing Provider',
            'IL': 'Insured or Subscriber', 'PR': 'Payer', 'DN': 'Referring Provider',
            '82': 'Rendering Provider', '77': 'Service Facility Location'
        }
    
    def parse_edi_file(self, file_path):
        """Parse a single EDI file and extract all data"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read().strip()
            
            if not content:
                return None
            
            # Split into segments
            segments = [seg.strip() for seg in content.split('~') if seg.strip()]
            
            if not segments:
                return None
            
            # Parse segments and build data structure
            return self.parse_segments(segments, file_path)
            
        except Exception as e:
            print(f"Error parsing file {file_path}: {str(e)}")
            return None
    
    def parse_segments(self, segments, file_path):
        """Parse EDI segments and build structured data"""
        # Initialize data structure
        edi_data = {
            'file_info': {
                'filename': os.path.basename(file_path),
                'file_path': file_path
            },
            'interchange_header': {},
            'functional_group': {},
            'transaction_sets': []
        }
        
        current_transaction = None
        current_billing_provider = None
        current_subscriber = None
        current_claim = None
        current_service_line = None
        
        for segment in segments:
            if not segment:
                continue
            
            elements = segment.split('*')
            segment_id = elements[0]
            
            try:
                # Parse each segment type
                if segment_id == 'ISA':
                    edi_data['interchange_header'] = self.parse_isa_segment(elements)
                elif segment_id == 'GS':
                    edi_data['functional_group'] = self.parse_gs_segment(elements)
                elif segment_id == 'ST':
                    current_transaction = self.init_transaction(elements)
                    edi_data['transaction_sets'].append(current_transaction)
                # Add more segment parsing here...
                
            except Exception as e:
                print(f"Error processing segment {segment_id}: {str(e)}")
                continue
        
        return edi_data 
   def parse_isa_segment(self, elements):
        """Parse ISA - Interchange Control Header"""
        return {
            'authorization_info_qualifier': elements[1] if len(elements) > 1 else '',
            'authorization_info': elements[2] if len(elements) > 2 else '',
            'security_info_qualifier': elements[3] if len(elements) > 3 else '',
            'security_info': elements[4] if len(elements) > 4 else '',
            'interchange_id_qualifier_sender': elements[5] if len(elements) > 5 else '',
            'interchange_sender_id': elements[6] if len(elements) > 6 else '',
            'interchange_id_qualifier_receiver': elements[7] if len(elements) > 7 else '',
            'interchange_receiver_id': elements[8] if len(elements) > 8 else '',
            'interchange_date': elements[9] if len(elements) > 9 else '',
            'interchange_time': elements[10] if len(elements) > 10 else '',
            'interchange_control_standards_id': elements[11] if len(elements) > 11 else '',
            'interchange_control_version_number': elements[12] if len(elements) > 12 else '',
            'interchange_control_number': elements[13] if len(elements) > 13 else '',
            'acknowledgment_requested': elements[14] if len(elements) > 14 else '',
            'usage_indicator': elements[15] if len(elements) > 15 else ''
        }
    
    def parse_gs_segment(self, elements):
        """Parse GS - Functional Group Header"""
        return {
            'functional_identifier_code': elements[1] if len(elements) > 1 else '',
            'application_sender_code': elements[2] if len(elements) > 2 else '',
            'application_receiver_code': elements[3] if len(elements) > 3 else '',
            'date': elements[4] if len(elements) > 4 else '',
            'time': elements[5] if len(elements) > 5 else '',
            'group_control_number': elements[6] if len(elements) > 6 else '',
            'responsible_agency_code': elements[7] if len(elements) > 7 else '',
            'version_release_identifier': elements[8] if len(elements) > 8 else ''
        }
    
    def init_transaction(self, elements):
        """Initialize transaction set"""
        return {
            'transaction_set_header': {
                'transaction_set_identifier_code': elements[1] if len(elements) > 1 else '',
                'transaction_set_control_number': elements[2] if len(elements) > 2 else '',
                'implementation_convention_reference': elements[3] if len(elements) > 3 else ''
            },
            'beginning_hierarchical_transaction': {},
            'submitter': {},
            'receiver': {},
            'billing_providers': []
        }
    
    def extract_to_csv_format(self, edi_data_list):
        """Extract data to the three CSV formats"""
        for edi_data in edi_data_list:
            if not edi_data:
                continue
            
            # Extract company setup data
            self.extract_company_setup(edi_data)
            
            # Extract claims and claim details
            self.extract_claims_and_details(edi_data)
    
    def extract_company_setup(self, edi_data):
        """Extract company setup data"""
        # This would be extracted from ISA, GS segments and submitter/receiver info
        pass
    
    def extract_claims_and_details(self, edi_data):
        """Extract claims and claim detail data"""
        # This would extract all the claim-level and service line data
        pass
    
    def save_csv_files(self):
        """Save the three CSV files"""
        # Save EDI_Claims.csv
        if self.claims_data:
            claims_df = pd.DataFrame(self.claims_data)
            claims_df.to_csv('EDI_Claims_Output.csv', index=False)
            print(f"✅ EDI_Claims_Output.csv saved with {len(self.claims_data)} records")
        
        # Save COMPANY_SETUP.csv
        if self.company_setup_data:
            company_df = pd.DataFrame(self.company_setup_data)
            company_df.to_csv('COMPANY_SETUP_Output.csv', index=False)
            print(f"✅ COMPANY_SETUP_Output.csv saved with {len(self.company_setup_data)} records")
        
        # Save EDI_ClaimDetail.csv
        if self.claim_details_data:
            details_df = pd.DataFrame(self.claim_details_data)
            details_df.to_csv('EDI_ClaimDetail_Output.csv', index=False)
            print(f"✅ EDI_ClaimDetail_Output.csv saved with {len(self.claim_details_data)} records")

def main():
    """Main execution function"""
    parser = ComprehensiveEDIParser()
    
    # Find EDI directories (reuse the logic from previous script)
    edi_directories = find_edi_directories()
    
    if not edi_directories:
        print("No EDI directories found")
        return
    
    all_edi_data = []
    
    for edi_dir in edi_directories:
        print(f"Processing directory: {edi_dir['name']} with {edi_dir['file_count']} files")
        
        # Get EDI files
        edi_files = []
        try:
            for file in os.listdir(edi_dir['path']):
                if file.endswith(('.d', '.edi', '.txt', '.x12')):
                    edi_files.append(os.path.join(edi_dir['path'], file))
        except PermissionError:
            continue
        
        # Process limited number of files for testing
        max_files = 10
        if len(edi_files) > max_files:
            edi_files = edi_files[:max_files]
        
        for i, file_path in enumerate(edi_files, 1):
            print(f"Processing {os.path.basename(file_path)}... ({i}/{len(edi_files)})")
            
            edi_data = parser.parse_edi_file(file_path)
            if edi_data:
                all_edi_data.append(edi_data)
    
    # Extract to CSV format
    parser.extract_to_csv_format(all_edi_data)
    
    # Save CSV files
    parser.save_csv_files()
    
    print(f"\n🎉 Comprehensive EDI extraction completed!")

def find_edi_directories():
    """Find directories containing EDI files"""
    current_dir = os.getcwd()
    edi_directories = []
    
    # Look for directories with "TOIH" or "837" in the name in current dir and subdirs
    search_dirs = [current_dir]
    
    # Add subdirectories to search
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            search_dirs.append(item_path)
    
    for search_dir in search_dirs:
        try:
            for item in os.listdir(search_dir):
                item_path = os.path.join(search_dir, item)
                if os.path.isdir(item_path):
                    if "TOIH" in item or "837" in item:
                        # Count EDI files in directory
                        edi_files = []
                        try:
                            for file in os.listdir(item_path):
                                if file.endswith(('.d', '.edi', '.txt', '.x12')):
                                    edi_files.append(file)
                            
                            if edi_files:
                                edi_directories.append({
                                    'path': item_path,
                                    'name': item,
                                    'file_count': len(edi_files)
                                })
                        except PermissionError:
                            continue
        except PermissionError:
            continue
    
    return edi_directories

if __name__ == "__main__":
    main()