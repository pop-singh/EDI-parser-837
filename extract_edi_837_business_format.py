#!/usr/bin/env python3
"""
Complete EDI 837 data extraction script that converts to business-friendly JSON format
Includes dynamic parsing, CSV conversion, and comprehensive business format output
"""

import os
import json
import uuid
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import configuration
try:
    from config import EDI_DIRECTORY, MAX_FILES, EDI_FILE_EXTENSIONS
except ImportError:
    print("Warning: config.py not found. Using default settings.")
    EDI_DIRECTORY = None
    MAX_FILES = 1000
    EDI_FILE_EXTENSIONS = ('.d', '.edi', '.txt', '.x12')
    EDI_FILE_EXTENSIONS = ('.d', '.edi', '.txt', '.x12')

class EDI837BusinessParser:
    def __init__(self):
        # Lookup tables for business format conversion
        self.place_of_service_codes = {
            '11': 'OFFICE',
            '12': 'HOME',
            '21': 'INPATIENT_HOSPITAL',
            '22': 'OUTPATIENT_HOSPITAL',
            '23': 'EMERGENCY_ROOM',
            '24': 'AMBULATORY_SURGICAL_CENTER',
            '25': 'BIRTHING_CENTER',
            '26': 'MILITARY_TREATMENT_FACILITY',
            '31': 'SKILLED_NURSING_FACILITY',
            '32': 'NURSING_FACILITY',
            '33': 'CUSTODIAL_CARE_FACILITY',
            '34': 'HOSPICE',
            '41': 'AMBULANCE_LAND',
            '42': 'AMBULANCE_AIR_OR_WATER',
            '49': 'INDEPENDENT_CLINIC',
            '50': 'FEDERALLY_QUALIFIED_HEALTH_CENTER',
            '51': 'INPATIENT_PSYCHIATRIC_FACILITY',
            '52': 'PSYCHIATRIC_FACILITY_PARTIAL_HOSPITALIZATION',
            '53': 'COMMUNITY_MENTAL_HEALTH_CENTER',
            '54': 'INTERMEDIATE_CARE_FACILITY_MENTALLY_RETARDED',
            '55': 'RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY',
            '56': 'PSYCHIATRIC_RESIDENTIAL_TREATMENT_CENTER',
            '57': 'NON_RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY',
            '60': 'MASS_IMMUNIZATION_CENTER',
            '61': 'COMPREHENSIVE_INPATIENT_REHABILITATION_FACILITY',
            '62': 'COMPREHENSIVE_OUTPATIENT_REHABILITATION_FACILITY',
            '65': 'END_STAGE_RENAL_DISEASE_TREATMENT_FACILITY',
            '71': 'PUBLIC_HEALTH_CLINIC',
            '72': 'RURAL_HEALTH_CLINIC',
            '81': 'INDEPENDENT_LABORATORY',
            '99': 'OTHER_PLACE_OF_SERVICE'
        }
        
        self.frequency_codes = {
            '1': {'desc': 'Original'},
            '6': {'desc': 'Corrected'},
            '7': {'desc': 'Replacement'},
            '8': {'desc': 'Void'}
        }
        
        # Comprehensive ICD-10 Diagnosis Code Descriptions
        self.diagnosis_descriptions = {
            # Common diagnosis codes
            "E1165": "Type 2 diabetes mellitus with hyperglycemia",
            "E119": "Type 2 diabetes mellitus without complications",
            "I10": "Essential (primary) hypertension",
            "Z00121": "Encounter for routine child health examination with abnormal findings",
            "Z0000": "Encounter for general adult medical examination without abnormal findings",
            "M545": "Low back pain",
            "J069": "Acute upper respiratory infection, unspecified",
            "R50": "Fever, unspecified",
            "K219": "Gastro-esophageal reflux disease without esophagitis",
            "F329": "Major depressive disorder, single episode, unspecified",
            "G43909": "Migraine, unspecified, not intractable, without status migrainosus",
            "M25551": "Pain in right hip",
            "M25552": "Pain in left hip",
            "N390": "Urinary tract infection, site not specified",
            "R05": "Cough",
            "R51": "Headache",
            "R060": "Dyspnea",
            "Z1231": "Encounter for screening mammogram for malignant neoplasm of breast",
            
            # Blood disorders
            "D500": "Iron deficiency anemia, unspecified",
            "D501": "Iron deficiency anemia secondary to blood loss (chronic)",
            "D509": "Iron deficiency anemia, unspecified",
            "D510": "Vitamin B12 deficiency anemia due to intrinsic factor deficiency",
            "D519": "Vitamin B12 deficiency anemia, unspecified",
            "D520": "Dietary folate deficiency anemia",
            "D529": "Folate deficiency anemia, unspecified",
            
            # Neoplasms
            "C3411": "Malignant neoplasm of upper lobe, right bronchus or lung",
            "C3412": "Malignant neoplasm of upper lobe, left bronchus or lung",
            "C3431": "Malignant neoplasm of lower lobe, right bronchus or lung",
            "C3432": "Malignant neoplasm of lower lobe, left bronchus or lung",
            "C500": "Malignant neoplasm of nipple and areola",
            "C5011": "Malignant neoplasm of central portion of right female breast",
            "C5012": "Malignant neoplasm of central portion of left female breast",
            
            # Diabetes
            "E10": "Type 1 diabetes mellitus",
            "E1010": "Type 1 diabetes mellitus with ketoacidosis without coma",
            "E1011": "Type 1 diabetes mellitus with ketoacidosis with coma",
            "E1021": "Type 1 diabetes mellitus with diabetic nephropathy",
            "E1022": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
            
            # Mental health
            "F329": "Major depressive disorder, single episode, unspecified",
            "F4321": "Adjustment disorder with mixed anxiety and depressed mood",
            "F411": "Generalized anxiety disorder",
            
            # Musculoskeletal
            "M545": "Low back pain",
            "M25551": "Pain in right hip",
            "M25552": "Pain in left hip",
            "M7960": "Pain in limb, unspecified",
            "M25561": "Pain in right knee",
            "M25562": "Pain in left knee"
        }
        
        # CPT/HCPCS Procedure Code Descriptions
        self.procedure_descriptions = {
            # Evaluation and Management
            "99213": "Office/outpatient visit, established patient, low complexity",
            "99214": "Office/outpatient visit, established patient, moderate complexity", 
            "99215": "Office/outpatient visit, established patient, high complexity",
            "99203": "Office/outpatient visit, new patient, low complexity",
            "99204": "Office or other outpatient visit for the evaluation and management of a new patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the encounter for code selection, 45 minutes must be met or exceeded.",
            "99205": "Office/outpatient visit, new patient, high complexity",
            "99212": "Office/outpatient visit, established patient, straightforward",
            "99202": "Office/outpatient visit, new patient, straightforward",
            "99211": "Office/outpatient visit, established patient, minimal",
            "99201": "Office/outpatient visit, new patient, minimal",
            
            # Preventive Medicine
            "99395": "Periodic comprehensive preventive medicine reevaluation, 18-39 years",
            "99396": "Periodic comprehensive preventive medicine reevaluation, 40-64 years",
            "99397": "Periodic comprehensive preventive medicine reevaluation, 65+ years",
            "99385": "Initial comprehensive preventive medicine evaluation, 18-39 years",
            "99386": "Initial comprehensive preventive medicine evaluation, 40-64 years",
            "99387": "Initial comprehensive preventive medicine evaluation, 65+ years",
            
            # Laboratory
            "80053": "Comprehensive metabolic panel",
            "85025": "Blood count; complete (CBC), automated",
            "80061": "Lipid panel",
            "83036": "Hemoglobin; glycosylated (A1C)",
            "84443": "Thyroid stimulating hormone (TSH)",
            "87086": "Culture, bacterial; quantitative colony count, urine",
            
            # Radiology
            "71020": "Radiologic examination, chest, 2 views, frontal and lateral",
            "73060": "Radiologic examination; knee, 1 or 2 views",
            "73030": "Radiologic examination, shoulder; complete, minimum of 2 views",
            "77067": "Screening mammography, bilateral (2-view study of each breast)",
            
            # Infusion and Injection Procedures
            "96365": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); initial, up to 1 hour",
            "96366": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); each additional hour (List separately in addition to code for primary procedure)",
            "96367": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); additional sequential infusion of a new drug/substance, up to 1 hour (List separately in addition to code for primary procedure)",
            "96368": "Intravenous infusion, for therapy, prophylaxis, or diagnosis (specify substance or drug); concurrent infusion (List separately in addition to code for primary procedure)",
            "96372": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); subcutaneous or intramuscular",
            "96373": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); intra-arterial",
            "96374": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); intravenous push, single or initial substance/drug",
            "96375": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); each additional sequential intravenous push of a new substance/drug (List separately in addition to code for primary procedure)",
            "96376": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); each additional sequential intravenous push of the same substance/drug provided in a facility (List separately in addition to code for primary procedure)",
            "96377": "Application of on-body injector (includes cannula insertion) for timed subcutaneous injection",
            
            # Procedures
            "12001": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities (including hands and feet); 2.5 cm or less",
            "11042": "Debridement, subcutaneous tissue (includes epidermis and dermis, if performed); first 20 sq cm or less",
            "90471": "Immunization administration (includes percutaneous, intradermal, subcutaneous, or intramuscular injections); 1 vaccine (single or combination vaccine/toxoid)",
            "90715": "Tetanus, diphtheria toxoids and acellular pertussis vaccine (Tdap), when administered to individuals 7 years or older, for intramuscular use",
            
            # Chemotherapy Administration
            "96413": "Chemotherapy administration, intravenous infusion technique; up to 1 hour, single or initial substance/drug",
            "96415": "Chemotherapy administration, intravenous infusion technique; each additional hour (List separately in addition to code for primary procedure)",
            "96417": "Chemotherapy administration, intravenous infusion technique; each additional sequential infusion (different substance/drug), up to 1 hour (List separately in addition to code for primary procedure)"
        }
        
        # Provider Taxonomy Codes
        self.provider_taxonomy = {
            "207Q00000X": "Family Medicine",
            "208D00000X": "General Practice", 
            "207R00000X": "Internal Medicine",
            "207T00000X": "Neurological Surgery",
            "208600000X": "Surgery",
            "207X00000X": "Orthopaedic Surgery",
            "207Y00000X": "Otolaryngology",
            "208800000X": "Urology",
            "207W00000X": "Ophthalmology",
            "207N00000X": "Dermatology",
            "207P00000X": "Emergency Medicine",
            "207V00000X": "Obstetrics & Gynecology",
            "208000000X": "Pediatrics",
            "207RC0000X": "Cardiovascular Disease",
            "207RE0101X": "Endocrinology, Diabetes & Metabolism",
            "207RG0100X": "Gastroenterology",
            "207RI0200X": "Infectious Disease",
            "207RN0300X": "Nephrology",
            "207RP1001X": "Pulmonary Disease",
            "207RR0500X": "Rheumatology"
        }
        
        # Entity Identifier Codes
        self.entity_identifiers = {
            '40': 'Receiver',
            '41': 'Submitter', 
            '85': 'Billing Provider',
            'IL': 'Insured or Subscriber',
            'PR': 'Payer',
            'DN': 'Referring Provider',
            '82': 'Rendering Provider',
            '77': 'Service Facility Location',
            'DQ': 'Supervising Provider',
            'PW': 'Pickup Address',
            '71': 'Attending Provider',
            '72': 'Operating Provider',
            'ZZ': 'Mutually Defined'
        }
        
        # Reference Identification Qualifiers
        self.reference_qualifiers = {
            '0B': 'State License Number',
            '1G': 'Provider UPIN Number',
            'G2': 'Provider Commercial Number',
            'LU': 'Location Number',
            'SY': 'Social Security Number',
            'TJ': 'Federal Tax Identification Number',
            'EI': 'Employer Identification Number',
            'HPI': 'Health Care Provider Taxonomy',
            'XX': 'Health Care Financing Administration National Provider Identifier',
            'ZZ': 'Mutually Defined'
        }

    def parse_isa_segment(self, elements):
        """Parse Interchange Control Header"""
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
        """Parse Functional Group Header"""
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

    def parse_st_segment(self, elements):
        """Parse Transaction Set Header"""
        return {
            "transaction_set_identifier_code": elements[1] if len(elements) > 1 else "",
            "transaction_set_control_number": elements[2] if len(elements) > 2 else "",
            'implementation_convention_reference': elements[3] if len(elements) > 3 else ''
        }

    def parse_bht_segment(self, elements):
        """Parse Beginning of Hierarchical Transaction"""
        return {
            "hierarchical_structure_code": elements[1] if len(elements) > 1 else "",
            "transaction_set_purpose_code": elements[2] if len(elements) > 2 else "",
            "reference_identification": elements[3] if len(elements) > 3 else "",
            "date": elements[4] if len(elements) > 4 else "",
            "time": elements[5] if len(elements) > 5 else "",
            'transaction_type_code': elements[6] if len(elements) > 6 else ''
        }

    def parse_hl_segment(self, elements):
        """Parse Hierarchical Level"""
        return {
            "hierarchical_id_number": elements[1] if len(elements) > 1 else "",
            "hierarchical_parent_id_number": elements[2] if len(elements) > 2 else "",
            "hierarchical_level_code": elements[3] if len(elements) > 3 else "",
            "hierarchical_child_code": elements[4] if len(elements) > 4 else ""
        }

    def parse_nm1_segment(self, elements):
        """Parse Individual or Organizational Name"""
        return {
            "entity_identifier_code": elements[1] if len(elements) > 1 else "",
            "entity_type_qualifier": elements[2] if len(elements) > 2 else "",
            "name_last_or_organization": elements[3] if len(elements) > 3 else "",
            "name_first": elements[4] if len(elements) > 4 else "",
            "name_middle": elements[5] if len(elements) > 5 else "",
            'name_prefix': elements[6] if len(elements) > 6 else '',
            'name_suffix': elements[7] if len(elements) > 7 else '',
            "identification_code_qualifier": elements[8] if len(elements) > 8 else "",
            "identification_code": elements[9] if len(elements) > 9 else ""
        }

    def parse_n3_segment(self, elements):
        """Parse Party Location"""
        return {
            "address_line_1": elements[1] if len(elements) > 1 else "",
            "address_line_2": elements[2] if len(elements) > 2 else ""
        }

    def parse_n4_segment(self, elements):
        """Parse Geographic Location"""
        return {
            "city": elements[1] if len(elements) > 1 else "",
            "state_code": elements[2] if len(elements) > 2 else "",
            "postal_code": elements[3] if len(elements) > 3 else "",
            'country_code': elements[4] if len(elements) > 4 else ''
        }

    def parse_ref_segment(self, elements):
        """Parse Reference Information"""
        return {
            "reference_identification_qualifier": elements[1] if len(elements) > 1 else "",
            "reference_identification": elements[2] if len(elements) > 2 else "",
            'description': elements[3] if len(elements) > 3 else ''
        }

    def parse_dmg_segment(self, elements):
        """Parse Demographic Information"""
        return {
            "date_time_period_format_qualifier": elements[1] if len(elements) > 1 else "",
            "date_time_period": elements[2] if len(elements) > 2 else "",
            "gender_code": elements[3] if len(elements) > 3 else "",
            'marital_status_code': elements[4] if len(elements) > 4 else ''
        }

    def parse_dtp_segment(self, elements):
        """Parse Date or Time or Period"""
        qualifier = elements[1] if len(elements) > 1 else ""
        format_qualifier = elements[2] if len(elements) > 2 else ""
        date_period = elements[3] if len(elements) > 3 else ""
        
        # Map common date qualifiers for reference
        qualifier_descriptions = {
            "472": "Service Date",
            "454": "Initial Treatment Date", 
            "304": "Latest Visit or Consultation",
            "453": "Acute Manifestation Date",
            "439": "Accident Date",
            "484": "Last Seen Date",
            "455": "Last X-ray Date",
            "471": "Prescription Date",
            "314": "Disability Begin Date",
            "315": "Disability End Date",
            "150": "Service Period Start",
            "151": "Service Period End"
        }
        
        return {
            "date_time_qualifier": qualifier,
            "date_time_period_format_qualifier": format_qualifier,
            "date_time_period": date_period,
            "qualifier_description": qualifier_descriptions.get(qualifier, "")
        }

    def parse_clm_segment(self, elements):
        """Parse Claim Information"""
        # Parse the claim filing indicator from element 5 (format like "11:B:1")
        claim_filing_parts = elements[5].split(':') if len(elements) > 5 and elements[5] else []
        place_of_service = claim_filing_parts[0] if claim_filing_parts else ''
        frequency_code = claim_filing_parts[2] if len(claim_filing_parts) > 2 else '1'
        
        return {
            'claim_submitter_identifier': elements[1] if len(elements) > 1 else '',
            'monetary_amount': elements[2] if len(elements) > 2 else '',
            'claim_frequency_type_code': frequency_code,  # Extract from claim filing indicator
            'non_institutional_claim_type_code': elements[4] if len(elements) > 4 else '',
            'claim_filing_indicator_code': elements[5] if len(elements) > 5 else '',
            'place_of_service_code': place_of_service,  # Extract from claim filing indicator
            'yes_no_condition_response_code': elements[6] if len(elements) > 6 else '',
            'provider_accept_assignment_code': elements[7] if len(elements) > 7 else '',
            'yes_no_condition_response_code_2': elements[8] if len(elements) > 8 else '',
            'release_of_information_code': elements[9] if len(elements) > 9 else '',
            'patient_signature_source_code': elements[10] if len(elements) > 10 else ''
        }

    def parse_sv1_segment(self, elements):
        """Parse Professional Service"""
        procedure_info = {}
        if len(elements) > 1 and elements[1]:
            if ':' in elements[1]:
                parts = elements[1].split(':')
                procedure_info = {
                    'product_service_id_qualifier': parts[0] if len(parts) > 0 else '',
                    'procedure_code': parts[1] if len(parts) > 1 else '',
                    'procedure_modifier_1': parts[2] if len(parts) > 2 else '',
                    'procedure_modifier_2': parts[3] if len(parts) > 3 else '',
                    'procedure_modifier_3': parts[4] if len(parts) > 4 else '',
                    'procedure_modifier_4': parts[5] if len(parts) > 5 else ''
                }
            else:
                procedure_info = {'procedure_code': elements[1]}
        
        # Place of service can be in position 5, 6, or 7 depending on the format
        place_of_service = ""
        for i in [5, 6, 7]:
            if len(elements) > i and elements[i] and elements[i].isdigit():
                place_of_service = elements[i]
                break
        
        return {
            'composite_medical_procedure_identifier': procedure_info,
            'monetary_amount': elements[2] if len(elements) > 2 else '',
            'unit_or_basis_for_measurement_code': elements[3] if len(elements) > 3 else '',
            'service_unit_count': elements[4] if len(elements) > 4 else '',
            'place_of_service_code': place_of_service,
            'service_type_code': elements[6] if len(elements) > 6 else ''
        }

    def parse_per_segment(self, elements):
        """Parse Administrative Communications Contact"""
        return {
            'contact_function_code': elements[1] if len(elements) > 1 else '',
            'name': elements[2] if len(elements) > 2 else '',
            'communication_number_qualifier_1': elements[3] if len(elements) > 3 else '',
            'communication_number_1': elements[4] if len(elements) > 4 else '',
            'communication_number_qualifier_2': elements[5] if len(elements) > 5 else '',
            'communication_number_2': elements[6] if len(elements) > 6 else ''
        }

    def parse_sbr_segment(self, elements):
        """Parse Subscriber Information"""
        return {
            'payer_responsibility_sequence_number_code': elements[1] if len(elements) > 1 else '',
            'individual_relationship_code': elements[2] if len(elements) > 2 else '',
            'reference_identification': elements[3] if len(elements) > 3 else '',
            'name': elements[4] if len(elements) > 4 else '',
            'insurance_type_code': elements[5] if len(elements) > 5 else '',
            'coordination_of_benefits_code': elements[6] if len(elements) > 6 else '',
            'yes_no_condition_response_code': elements[7] if len(elements) > 7 else '',
            'employment_status_code': elements[8] if len(elements) > 8 else '',
            'claim_filing_indicator_code': elements[9] if len(elements) > 9 else ''
        }

    def parse_hi_segment(self, elements):
        """Parse Health Care Diagnosis Code"""
        diagnosis_codes = []
        for i in range(1, len(elements)):
            if elements[i] and ':' in elements[i]:
                code_qualifier, code = elements[i].split(':', 1)
                diagnosis_codes.append({
                    "code_list_qualifier_code": code_qualifier,
                    "diagnosis_code": code
                })
        return diagnosis_codes

    def parse_prv_segment(self, elements):
        """Parse Provider Information"""
        return {
            'provider_code': elements[1] if len(elements) > 1 else '',
            'reference_identification_qualifier': elements[2] if len(elements) > 2 else '',
            'reference_identification': elements[3] if len(elements) > 3 else ''
        }

    def parse_lx_segment(self, elements):
        """Parse Service Line Number"""
        return {
            'assigned_number': elements[1] if len(elements) > 1 else ''
        }

    def parse_sv2_segment(self, elements):
        """Parse Institutional Service Line"""
        return {
            'revenue_code': elements[1] if len(elements) > 1 else '',
            'monetary_amount': elements[2] if len(elements) > 2 else '',
            'unit_or_basis_for_measurement_code': elements[3] if len(elements) > 3 else '',
            'service_unit_count': elements[4] if len(elements) > 4 else ''
        }

    def parse_sv3_segment(self, elements):
        """Parse Dental Service"""
        procedure_info = {}
        if len(elements) > 1 and elements[1]:
            if ':' in elements[1]:
                parts = elements[1].split(':')
                procedure_info = {
                    'product_service_id_qualifier': parts[0] if len(parts) > 0 else '',
                    'procedure_code': parts[1] if len(parts) > 1 else ''
                }
            else:
                procedure_info = {'procedure_code': elements[1]}
        
        return {
            'composite_medical_procedure_identifier': procedure_info,
            'monetary_amount': elements[2] if len(elements) > 2 else '',
            'place_of_service_code': elements[3] if len(elements) > 3 else '',
            'oral_cavity_designation': elements[4] if len(elements) > 4 else '',
            'prosthesis_crown_or_inlay_code': elements[5] if len(elements) > 5 else '',
            'quantity': elements[6] if len(elements) > 6 else ''
        }

    def parse_cas_segment(self, elements):
        """Parse Claim Adjustment"""
        adjustments = []
        i = 1
        while i < len(elements):
            if i + 2 < len(elements):
                adjustments.append({
                    'claim_adjustment_group_code': elements[i] if i < len(elements) else '',
                    'claim_adjustment_reason_code': elements[i+1] if i+1 < len(elements) else '',
                    'monetary_amount': elements[i+2] if i+2 < len(elements) else '',
                    'quantity': elements[i+3] if i+3 < len(elements) else ''
                })
                i += 4
            else:
                break
        return adjustments

    def parse_amt_segment(self, elements):
        """Parse Monetary Amount Information"""
        return {
            'amount_qualifier_code': elements[1] if len(elements) > 1 else '',
            'monetary_amount': elements[2] if len(elements) > 2 else ''
        }

    def parse_qty_segment(self, elements):
        """Parse Quantity Information"""
        return {
            'quantity_qualifier': elements[1] if len(elements) > 1 else '',
            'quantity': elements[2] if len(elements) > 2 else ''
        }

    def parse_nte_segment(self, elements):
        """Parse Note/Special Instruction"""
        return {
            'note_reference_code': elements[1] if len(elements) > 1 else '',
            'description': elements[2] if len(elements) > 2 else ''
        }

    def format_date(self, date_str):
        """Format date from YYYYMMDD to readable format"""
        if not date_str or len(date_str) != 8:
            return date_str
        try:
            year = date_str[:4]
            month = date_str[4:6]
            day = date_str[6:8]
            return f"{month}/{day}/{year}"
        except:
            return date_str

    def format_time(self, time_str):
        """Format time from HHMM to readable format"""
        if not time_str or len(time_str) < 4:
            return time_str
        try:
            hour = time_str[:2]
            minute = time_str[2:4]
            return f"{hour}:{minute}"
        except:
            return time_str

    def get_business_description(self, code, code_type):
        """Get business-friendly description for codes"""
        lookup_tables = {
            'place_of_service': self.place_of_service_codes,
            'diagnosis': self.diagnosis_descriptions,
            'procedure': self.procedure_descriptions,
            'provider_taxonomy': self.provider_taxonomy,
            'entity_identifier': self.entity_identifiers,
            'reference_qualifier': self.reference_qualifiers,
            'frequency': self.frequency_codes
        }
        
        if code_type in lookup_tables:
            return lookup_tables[code_type].get(code, code)
        return code

    def convert_to_business_format(self, edi_data):
        """Convert parsed EDI data to the specified JSON format"""
        claims = []
        
        # Process transaction sets to extract claims
        for ts in edi_data.get("transaction_sets", []):
            transaction_info = self.format_transaction_info(ts, edi_data)
            
            # Process billing providers
            for bp in ts.get("billing_providers", []):
                billing_provider = self.format_billing_provider(bp.get("provider_info", {}))
                
                # Process subscribers
                for sub in bp.get("subscribers", []):
                    subscriber_info = self.format_subscriber_new(sub.get("subscriber_info", {}))
                    payer_info = self.format_payer_new(sub.get("payer_info", {}))
                    
                    # Process claims
                    for claim in sub.get("claims", []):
                        claim_obj = self.format_claim_new(claim, subscriber_info, payer_info, billing_provider, transaction_info, bp)
                        if claim_obj:
                            claims.append(claim_obj)
        
        return claims

    def format_entity_info(self, entity_data):
        """Format entity information for business use"""
        if not entity_data:
            return {}
        
        return {
            "entity_type": self.get_business_description(entity_data.get("entity_identifier_code", ""), "entity_identifier"),
            "organization_name": entity_data.get("name_last_or_organization", ""),
            "contact_info": entity_data.get("contact_info", {}),
            "address": entity_data.get("address", {}),
            "identification": {
                "qualifier": self.get_business_description(entity_data.get("identification_code_qualifier", ""), "reference_qualifier"),
                "id": entity_data.get("identification_code", "")
            }
        }

    def format_provider_info(self, provider_data):
        """Format provider information for business use"""
        if not provider_data:
            return {}
        
        return {
            "provider_name": provider_data.get("name_last_or_organization", ""),
            "provider_type": self.get_business_description(provider_data.get("entity_identifier_code", ""), "entity_identifier"),
            "npi": provider_data.get("identification_code", "") if provider_data.get("identification_code_qualifier") == "XX" else "",
            "tax_id": provider_data.get("tax_identification_number", ""),
            "address": provider_data.get("address", {}),
            "contact_info": provider_data.get("contact_info", {}),
            "specialty": self.get_business_description(provider_data.get("provider_taxonomy", ""), "provider_taxonomy")
        }

    def format_subscriber_info(self, subscriber_data):
        """Format subscriber information for business use"""
        if not subscriber_data:
            return {}
        
        return {
            "member_id": subscriber_data.get("identification_code", ""),
            "name": {
                "last": subscriber_data.get("name_last_or_organization", ""),
                "first": subscriber_data.get("name_first", ""),
                "middle": subscriber_data.get("name_middle", "")
            },
            "address": subscriber_data.get("address", {}),
            "demographics": {
                "date_of_birth": self.format_date(subscriber_data.get("demographics", {}).get("date_time_period", "")),
                "gender": subscriber_data.get("demographics", {}).get("gender_code", "")
            },
            "relationship_to_patient": subscriber_data.get("individual_relationship_code", "")
        }

    def format_payer_info(self, payer_data):
        """Format payer information for business use"""
        if not payer_data:
            return {}
        
        return {
            "payer_name": payer_data.get("name_last_or_organization", ""),
            "payer_id": payer_data.get("identification_code", ""),
            "address": payer_data.get("address", {}),
            "responsibility_sequence": payer_data.get("payer_responsibility_sequence_number_code", "")
        }

    def format_transaction_info(self, ts, edi_data):
        """Format transaction information"""
        bht = ts.get("beginning_hierarchical_transaction", {})
        st = ts.get("transaction_set_header", {})
        submitter = ts.get("submitter", {})
        receiver = ts.get("receiver", {})
        
        return {
            "id": str(uuid.uuid4()).replace('-', ''),
            "controlNumber": st.get("transaction_set_control_number", ""),
            "transactionType": "PROF",
            "hierarchicalStructureCode": bht.get("hierarchical_structure_code", ""),
            "purposeCode": bht.get("transaction_set_purpose_code", ""),
            "originatorApplicationTransactionId": bht.get("reference_identification", ""),
            "creationDate": self.format_date_iso(bht.get("date", "")),
            "creationTime": self.format_time_iso(bht.get("time", "")),
            "claimOrEncounterIdentifierType": "CHARGEABLE",
            "transactionSetIdentifierCode": st.get("transaction_set_identifier_code", ""),
            "implementationConventionReference": st.get("implementation_convention_reference", ""),
            "fileInfo": {"fileType": "EDI"},
            "sender": self.format_entity_new(submitter, "SUBMITTER"),
            "receiver": self.format_entity_new(receiver, "RECEIVER"),
            "creationDateTime": f"{self.format_date_iso(bht.get('date', ''))}T{self.format_time_iso(bht.get('time', ''))}"
        }

    def format_entity_new(self, entity_data, role):
        """Format entity in new structure"""
        if not entity_data:
            return {}
        
        entity = {
            "entityRole": role,
            "entityType": "INDIVIDUAL" if entity_data.get("entity_type_qualifier") == "1" else "BUSINESS",
            "identificationType": self.get_identification_type(entity_data.get("identification_code_qualifier", "")),
            "identifier": entity_data.get("identification_code", ""),
            "lastNameOrOrgName": entity_data.get("name_last_or_organization", "")
        }
        
        if entity_data.get("name_first"):
            entity["firstName"] = entity_data.get("name_first", "")
        if entity_data.get("name_middle"):
            entity["middleName"] = entity_data.get("name_middle", "")
        
        # Add contacts if available
        if entity_data.get("contact_info"):
            contact = entity_data["contact_info"]
            entity["contacts"] = [{
                "functionCode": contact.get("contact_function_code", ""),
                "name": contact.get("name", ""),
                "contactNumbers": []
            }]
            
            if contact.get("communication_number_1"):
                entity["contacts"][0]["contactNumbers"].append({
                    "type": self.get_communication_type(contact.get("communication_number_qualifier_1", "")),
                    "number": contact.get("communication_number_1", "")
                })
        
        return entity

    def format_billing_provider(self, provider_data):
        """Format billing provider"""
        if not provider_data:
            return {}
        
        provider = {
            "entityRole": "BILLING_PROVIDER",
            "entityType": "INDIVIDUAL" if provider_data.get("entity_type_qualifier") == "1" else "BUSINESS",
            "identificationType": self.get_identification_type(provider_data.get("identification_code_qualifier", "")),
            "identifier": provider_data.get("identification_code", ""),
            "lastNameOrOrgName": provider_data.get("name_last_or_organization", "")
        }
        
        # Add tax ID if available from references
        if provider_data.get("references"):
            for ref in provider_data["references"]:
                if ref.get("reference_identification_qualifier") == "EI":
                    provider["taxId"] = ref.get("reference_identification", "")
        
        # Add address
        if provider_data.get("address"):
            addr = provider_data["address"]
            provider["address"] = {
                "line": addr.get("address_line_1", ""),
                "city": addr.get("city", ""),
                "stateCode": addr.get("state_code", ""),
                "zipCode": addr.get("postal_code", "")
            }
            if addr.get("address_line_2"):
                provider["address"]["line2"] = addr.get("address_line_2", "")
        
        return provider

    def format_subscriber_new(self, subscriber_data):
        """Format subscriber in new structure"""
        if not subscriber_data:
            return {}
        
        subscriber = {
            "payerResponsibilitySequence": self.get_payer_sequence(subscriber_data.get("payer_responsibility_sequence_number_code", "")),
            "relationshipType": self.get_relationship_type(subscriber_data.get("individual_relationship_code", "")),
            "claimFilingIndicatorCode": subscriber_data.get("claim_filing_indicator_code", "CI"),
            "insurancePlanType": self.get_insurance_type(subscriber_data.get("insurance_type_code", "")),
            "person": {
                "entityRole": "INSURED_SUBSCRIBER",
                "entityType": "INDIVIDUAL",
                "identificationType": self.get_identification_type(subscriber_data.get("identification_code_qualifier", "")),
                "identifier": subscriber_data.get("identification_code", ""),
                "lastNameOrOrgName": subscriber_data.get("name_last_or_organization", ""),
                "firstName": subscriber_data.get("name_first", "")
            }
        }
        
        # Add demographics
        if subscriber_data.get("demographics"):
            demo = subscriber_data["demographics"]
            if demo.get("date_time_period"):
                subscriber["person"]["birthDate"] = self.format_date_iso(demo.get("date_time_period", ""))
            if demo.get("gender_code"):
                subscriber["person"]["gender"] = "MALE" if demo.get("gender_code") == "M" else "FEMALE"
        
        # Add address
        if subscriber_data.get("address"):
            addr = subscriber_data["address"]
            subscriber["person"]["address"] = {
                "line": addr.get("address_line_1", ""),
                "city": addr.get("city", ""),
                "stateCode": addr.get("state_code", ""),
                "zipCode": addr.get("postal_code", "")
            }
        
        return subscriber

    def format_payer_new(self, payer_data):
        """Format payer in new structure"""
        if not payer_data:
            return {}
        
        payer = {
            "entityRole": "PAYER",
            "entityType": "BUSINESS",
            "identificationType": self.get_identification_type(payer_data.get("identification_code_qualifier", "")),
            "identifier": payer_data.get("identification_code", ""),
            "lastNameOrOrgName": payer_data.get("name_last_or_organization", "")
        }
        
        # Add address
        if payer_data.get("address"):
            addr = payer_data["address"]
            payer["address"] = {
                "line": addr.get("address_line_1", ""),
                "city": addr.get("city", ""),
                "stateCode": addr.get("state_code", ""),
                "zipCode": addr.get("postal_code", "")
            }
        
        return payer

    def format_claim_new(self, claim_data, subscriber_info, payer_info, billing_provider, transaction_info, bp):
        """Format claim in new structure"""
        if not claim_data:
            return None
        
        claim_info = claim_data.get("claim_info", {})
        
        # Get service dates - first try claim level, then use first service line date
        service_date_from = ""
        service_date_to = ""
        
        # Check claim-level dates first
        for date_info in claim_data.get("dates", []):
            if date_info.get("date_time_qualifier") == "472":  # Service date
                service_date_from = self.format_date_iso(date_info.get("date_time_period", ""))
                service_date_to = service_date_from
                break
            elif date_info.get("date_time_qualifier") == "454":  # Initial treatment date
                if not service_date_from:
                    service_date_from = self.format_date_iso(date_info.get("date_time_period", ""))
                    service_date_to = service_date_from
        
        # If no claim-level dates, use first service line date
        if not service_date_from and claim_data.get("service_lines"):
            first_service_line = claim_data["service_lines"][0]
            for date_info in first_service_line.get("dates", []):
                if date_info.get("date_time_qualifier") == "472":
                    service_date_from = self.format_date_iso(date_info.get("date_time_period", ""))
                    service_date_to = service_date_from
                    break
        
        # Get place of service from claim info first, then service lines
        place_of_service_code = claim_info.get("place_of_service_code", "11")
        if not place_of_service_code or place_of_service_code == "":
            if claim_data.get("service_lines"):
                first_service = claim_data["service_lines"][0]
                service_info = first_service.get("service_info", {})
                place_of_service_code = service_info.get("place_of_service_code", "11")
        
        # Get frequency code from claim info
        frequency_code = claim_info.get("claim_frequency_type_code", "1")
        if not frequency_code or frequency_code == "":
            frequency_code = "1"  # Default to original
        
        claim = {
            "id": str(uuid.uuid4()).replace('-', ''),
            "objectType": "CLAIM",
            "patientControlNumber": claim_info.get("claim_submitter_identifier", ""),
            "chargeAmount": float(claim_info.get("monetary_amount", "0")) if claim_info.get("monetary_amount") else 0.0,
            "facilityCode": {
                "subType": "PLACE_OF_SERVICE",
                "code": place_of_service_code
            },
            "placeOfServiceType": self.place_of_service_codes.get(place_of_service_code, "OFFICE"),
            "frequencyCode": {
                "subType": "FREQUENCY_CODE",
                "code": frequency_code,
                "desc": self.frequency_codes.get(frequency_code, {}).get("desc", "Original")
            },
            "serviceDateFrom": service_date_from,
            "serviceDateTo": service_date_to,
            "subscriber": subscriber_info,
            "payer": payer_info,
            "providerSignatureIndicator": "Y" if claim_info.get("patient_signature_source_code") else "N",
            "assignmentParticipationCode": claim_info.get("provider_accept_assignment_code", ""),
            "assignmentCertificationIndicator": "Y" if claim_info.get("yes_no_condition_response_code") == "Y" else "N",
            "releaseOfInformationCode": "Y" if claim_info.get("release_of_information_code") == "Y" else "N",
            "originalReferenceNumber": f"CP{transaction_info.get('originatorApplicationTransactionId', '')}{claim_info.get('claim_submitter_identifier', '')}",
            "billingProvider": billing_provider,
            "providers": [],
            "diags": [],
            "serviceLines": [],
            "transaction": transaction_info
        }
        
        # Add providers
        for provider in claim_data.get("providers", []):
            provider_obj = self.format_provider_new(provider)
            if provider_obj:
                claim["providers"].append(provider_obj)
        
        # Add diagnosis codes
        for diag_list in claim_data.get("diagnosis_codes", []):
            if isinstance(diag_list, list):
                for diag in diag_list:
                    diag_obj = self.format_diagnosis_new(diag)
                    if diag_obj:
                        claim["diags"].append(diag_obj)
        
        # Add service lines
        for i, service_line in enumerate(claim_data.get("service_lines", []), 1):
            service_obj = self.format_service_line_new(service_line, i, claim["diags"])
            if service_obj:
                claim["serviceLines"].append(service_obj)
        
        return claim

    def format_provider_new(self, provider_data):
        """Format provider in new structure"""
        if not provider_data:
            return None
        
        provider_info = provider_data.get("provider_data", {})
        role_map = {
            "REFERRING": "REFERRING",
            "RENDERING": "RENDERING", 
            "SERVICE_FACILITY": "SERVICE_FACILITY"
        }
        
        provider = {
            "entityRole": role_map.get(provider_data.get("provider_role", ""), "RENDERING"),
            "entityType": "INDIVIDUAL" if provider_info.get("entity_type_qualifier") == "1" else "BUSINESS",
            "identificationType": self.get_identification_type(provider_info.get("identification_code_qualifier", "")),
            "identifier": provider_info.get("identification_code", ""),
            "lastNameOrOrgName": provider_info.get("name_last_or_organization", "")
        }
        
        if provider_info.get("name_first"):
            provider["firstName"] = provider_info.get("name_first", "")
        if provider_info.get("name_middle"):
            provider["middleName"] = provider_info.get("name_middle", "")
        
        # Handle middle name from suffix field if it contains middle name
        if not provider.get("middleName") and provider_info.get("name_suffix"):
            # Sometimes middle name is in suffix field
            suffix = provider_info.get("name_suffix", "")
            if len(suffix) == 1 or (len(suffix) <= 3 and not suffix.upper() in ["JR", "SR", "III", "IV", "MD", "DO", "RN"]):
                provider["middleName"] = suffix
        
        # Add provider taxonomy if available
        taxonomy_code = provider_data.get("provider_taxonomy", "") or provider_info.get("provider_taxonomy", "")
        if taxonomy_code:
            provider["providerTaxonomy"] = {
                "subType": "PROVIDER_TAXONOMY",
                "code": taxonomy_code,
                "desc": self.provider_taxonomy.get(taxonomy_code, "")
            }
        
        # Add additional IDs
        if provider_data.get("references"):
            provider["additionalIds"] = []
            for ref in provider_data["references"]:
                if ref.get("reference_identification_qualifier") and ref.get("reference_identification"):
                    provider["additionalIds"].append({
                        "qualifierCode": ref.get("reference_identification_qualifier", ""),
                        "type": self.get_reference_type(ref.get("reference_identification_qualifier", "")),
                        "identification": ref.get("reference_identification", "")
                    })
        
        # Add address
        if provider_data.get("address"):
            addr = provider_data["address"]
            provider["address"] = {
                "line": addr.get("address_line_1", ""),
                "city": addr.get("city", ""),
                "stateCode": addr.get("state_code", ""),
                "zipCode": addr.get("postal_code", "")
            }
            if addr.get("address_line_2"):
                provider["address"]["line2"] = addr.get("address_line_2", "")
        
        return provider

    def format_diagnosis_new(self, diag_data):
        """Format diagnosis in new structure"""
        if not diag_data:
            return None
        
        code = diag_data.get("diagnosis_code", "")
        if not code:
            return None
        
        return {
            "subType": "ICD_10_PRINCIPAL",
            "code": code,
            "desc": self.diagnosis_descriptions.get(code, ""),
            "formattedCode": self.format_icd_code(code)
        }

    def format_service_line_new(self, service_line_data, line_num, diags):
        """Format service line in new structure"""
        if not service_line_data:
            return None
        
        service_info = service_line_data.get("service_info", {})
        procedure_info = service_info.get("composite_medical_procedure_identifier", {})
        
        procedure_code = procedure_info.get("procedure_code", "")
        if not procedure_code:
            return None
        
        service_line = {
            "sourceLineId": str(uuid.uuid4()).replace('-', '')[:10],
            "chargeAmount": float(service_info.get("monetary_amount", "0")) if service_info.get("monetary_amount") else 0.0,
            "serviceDateFrom": "",
            "unitType": "UNIT",
            "unitCount": int(service_info.get("service_unit_count", "1")) if service_info.get("service_unit_count") else 1,
            "procedure": {
                "subType": "CPT",
                "code": procedure_code,
                "desc": self.procedure_descriptions.get(procedure_code, "")
            },
            "diagPointers": [1],  # Default to first diagnosis
            "diags": diags  # Reference to claim diagnoses
        }
        
        # Add service dates
        service_date_found = False
        for date_info in service_line_data.get("dates", []):
            if date_info.get("date_time_qualifier") == "472":  # Service date
                service_line["serviceDateFrom"] = self.format_date_iso(date_info.get("date_time_period", ""))
                service_date_found = True
                break
            elif date_info.get("date_time_qualifier") == "150":  # Service period start
                service_line["serviceDateFrom"] = self.format_date_iso(date_info.get("date_time_period", ""))
                service_date_found = True
            elif date_info.get("date_time_qualifier") == "151":  # Service period end
                service_line["serviceDateTo"] = self.format_date_iso(date_info.get("date_time_period", ""))
        
        # If no service line date found, use claim date
        if not service_date_found and not service_line.get("serviceDateFrom"):
            # Use the claim's service date as fallback
            service_line["serviceDateFrom"] = service_date_from if 'service_date_from' in locals() else ""
        
        return service_line

    def get_identification_type(self, qualifier):
        """Map identification qualifier to type"""
        type_map = {
            "XX": "NPI",
            "EI": "ETIN", 
            "MI": "MEMBER_ID",
            "PI": "PAYOR_ID",
            "SY": "SSN"
        }
        return type_map.get(qualifier, qualifier)

    def get_communication_type(self, qualifier):
        """Map communication qualifier to type"""
        return "PHONE" if qualifier in ["TE", "WP"] else "EMAIL" if qualifier == "EM" else "PHONE"

    def get_payer_sequence(self, code):
        """Map payer sequence code"""
        sequence_map = {
            "P": "PRIMARY",
            "S": "SECONDARY", 
            "T": "TERTIARY",
            "A": "WORKERS_COMPENSATION",
            "B": "AUTO_NO_FAULT",
            "C": "AUTO_LIABILITY"
        }
        return sequence_map.get(code, "PRIMARY")

    def get_relationship_type(self, code):
        """Map relationship code"""
        relationship_map = {
            "18": "SELF",
            "01": "SPOUSE", 
            "19": "CHILD",
            "20": "EMPLOYEE",
            "21": "UNKNOWN",
            "39": "ORGAN_DONOR",
            "40": "CADAVER_DONOR",
            "53": "LIFE_PARTNER",
            "G8": "OTHER_RELATIONSHIP"
        }
        return relationship_map.get(code, "SELF")

    def get_insurance_type(self, code):
        """Map insurance type code"""
        return "COMMERCIAL" if code in ["CI", "12", "13"] else "MEDICARE" if code == "MA" else "MEDICAID" if code == "MC" else "COMMERCIAL"

    def get_reference_type(self, qualifier):
        """Map reference qualifier to type"""
        type_map = {
            "0B": "STATE_LICENSE_NUMBER",
            "1G": "UPIN",
            "G2": "PROVIDER_COMMERCIAL_NUMBER"
        }
        return type_map.get(qualifier, qualifier)

    def format_date_iso(self, date_str):
        """Format date to ISO format YYYY-MM-DD"""
        if not date_str or len(date_str) != 8:
            return ""
        try:
            return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        except:
            return ""

    def format_time_iso(self, time_str):
        """Format time to ISO format HH:MM:SS"""
        if not time_str:
            return "00:00:00"
        if len(time_str) >= 4:
            return f"{time_str[:2]}:{time_str[2:4]}:{time_str[4:6] if len(time_str) > 4 else '00'}"
        return "00:00:00"

    def format_icd_code(self, code):
        """Format ICD code with decimal point"""
        if len(code) > 3:
            return f"{code[:3]}.{code[3:]}"
        return code

    def parse_edi_file(self, file_path):
        """Parse a single EDI file and return structured data"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read().strip()
            
            if not content:
                return None
            
            # Split into segments
            segments = []
            if '~' in content:
                segments = [seg.strip() for seg in content.split('~') if seg.strip()]
            else:
                # Try other common delimiters
                for delimiter in ['\n', '\r\n', '|']:
                    if delimiter in content:
                        segments = [seg.strip() for seg in content.split(delimiter) if seg.strip()]
                        break
            
            if not segments:
                return None
            
            # Initialize data structure
            edi_data = {
                "file_info": {
                    "file_path": file_path,
                    "file_name": os.path.basename(file_path),
                    "processed_date": datetime.now().isoformat()
                },
                "interchange_header": {},
                "functional_group": {},
                "transaction_sets": []
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
                    if segment_id == 'ISA':
                        edi_data["interchange_header"] = self.parse_isa_segment(elements)
                    
                    elif segment_id == 'GS':
                        edi_data["functional_group"] = self.parse_gs_segment(elements)
                    
                    elif segment_id == 'ST':
                        current_transaction = {
                            "transaction_set_header": self.parse_st_segment(elements),
                            "beginning_hierarchical_transaction": {},
                            "submitter": {},
                            "receiver": {},
                            "billing_providers": []
                        }
                        edi_data["transaction_sets"].append(current_transaction)
                    
                    elif segment_id == 'BHT' and current_transaction:
                        current_transaction["beginning_hierarchical_transaction"] = self.parse_bht_segment(elements)
                    
                    elif segment_id == 'HL' and current_transaction:
                        hl_data = self.parse_hl_segment(elements)
                        level_code = hl_data.get("hierarchical_level_code", "")
                        hierarchical_id = hl_data.get("hierarchical_id_number", "")
                        parent_id = hl_data.get("hierarchical_parent_id_number", "")
                        
                        if level_code == "20":  # Loop 2000A - Billing Provider Level
                            current_billing_provider = {
                                "hierarchical_level": hl_data,
                                "hierarchical_id": hierarchical_id,
                                "provider_info": {},
                                "subscribers": []
                            }
                            current_transaction["billing_providers"].append(current_billing_provider)
                            current_subscriber = None
                            current_claim = None
                            current_service_line = None
                        
                        elif level_code == "22" and current_billing_provider:  # Loop 2000B - Subscriber Level
                            current_subscriber = {
                                "hierarchical_level": hl_data,
                                "hierarchical_id": hierarchical_id,
                                "parent_id": parent_id,
                                "subscriber_info": {},
                                "payer_info": {},
                                "secondary_payers": [],  # For multiple payers
                                "claims": []
                            }
                            current_billing_provider["subscribers"].append(current_subscriber)
                            current_claim = None
                            current_service_line = None
                        
                        elif level_code == "23" and current_subscriber:  # Loop 2000C - Patient Level (if different from subscriber)
                            # Patient level - usually when patient is different from subscriber
                            current_subscriber["patient_info"] = {
                                "hierarchical_level": hl_data,
                                "hierarchical_id": hierarchical_id,
                                "parent_id": parent_id
                            }
                    
                    elif segment_id == 'NM1' and current_transaction:
                        nm1_data = self.parse_nm1_segment(elements)
                        entity_code = nm1_data.get("entity_identifier_code", "")
                        
                        if entity_code == "41":  # Loop 1000A - Submitter
                            current_transaction["submitter"] = nm1_data
                        elif entity_code == "40":  # Loop 1000B - Receiver
                            current_transaction["receiver"] = nm1_data
                        elif entity_code == "85" and current_billing_provider:  # Loop 2010AA - Billing Provider
                            current_billing_provider["provider_info"] = nm1_data
                        elif entity_code == "87" and current_billing_provider:  # Loop 2010AB - Pay-to Provider
                            current_billing_provider["pay_to_provider"] = nm1_data
                        elif entity_code == "IL" and current_subscriber:  # Loop 2010BA - Subscriber
                            # Check if this is for secondary payer
                            if current_subscriber["secondary_payers"] and len(current_subscriber["secondary_payers"]) > 0:
                                # This is for the most recent secondary payer
                                current_subscriber["secondary_payers"][-1]["subscriber_info"].update(nm1_data)
                            else:
                                # Primary subscriber
                                if "subscriber_info" not in current_subscriber:
                                    current_subscriber["subscriber_info"] = {}
                                current_subscriber["subscriber_info"].update(nm1_data)
                        elif entity_code == "PR" and current_subscriber:  # Loop 2010BB - Payer
                            # Check if this is for secondary payer
                            if current_subscriber["secondary_payers"] and len(current_subscriber["secondary_payers"]) > 0:
                                # This is for the most recent secondary payer
                                current_subscriber["secondary_payers"][-1]["payer_info"] = nm1_data
                            else:
                                # Primary payer
                                current_subscriber["payer_info"] = nm1_data
                        elif entity_code == "QC" and current_subscriber:  # Loop 2010BC - Patient (if different from subscriber)
                            if "patient_info" not in current_subscriber:
                                current_subscriber["patient_info"] = {}
                            current_subscriber["patient_info"]["patient_data"] = nm1_data
                        elif entity_code in ["DN", "82", "77", "DQ", "85"] and current_claim:  # Loop 2310 - Various provider types
                            provider_role_map = {
                                "DN": "REFERRING",      # Loop 2310A - Referring Provider
                                "82": "RENDERING",      # Loop 2310B - Rendering Provider  
                                "77": "SERVICE_FACILITY", # Loop 2310C - Service Facility
                                "DQ": "SUPERVISING",    # Loop 2310D - Supervising Provider
                                "85": "BILLING"         # Loop 2310E - Billing Provider (if different)
                            }
                            provider_info = {
                                "provider_role": provider_role_map.get(entity_code, ""),
                                "provider_data": nm1_data,
                                "address": {},
                                "references": []
                            }
                            if "providers" not in current_claim:
                                current_claim["providers"] = []
                            current_claim["providers"].append(provider_info)
                    
                    elif segment_id == 'N3':
                        n3_data = self.parse_n3_segment(elements)
                        # Add address to the most recent entity
                        if current_claim and "providers" in current_claim and current_claim["providers"]:
                            if "address" not in current_claim["providers"][-1]:
                                current_claim["providers"][-1]["address"] = {}
                            current_claim["providers"][-1]["address"].update(n3_data)
                        elif current_subscriber and "payer_info" in current_subscriber and current_subscriber["payer_info"] and "address" not in current_subscriber["payer_info"]:
                            current_subscriber["payer_info"]["address"] = n3_data
                        elif current_subscriber and "address" not in current_subscriber["subscriber_info"]:
                            current_subscriber["subscriber_info"]["address"] = n3_data
                        elif current_billing_provider and "address" not in current_billing_provider["provider_info"]:
                            current_billing_provider["provider_info"]["address"] = n3_data
                    
                    elif segment_id == 'N4':
                        n4_data = self.parse_n4_segment(elements)
                        # Add geographic info to the most recent address
                        if current_claim and "providers" in current_claim and current_claim["providers"]:
                            if "address" not in current_claim["providers"][-1]:
                                current_claim["providers"][-1]["address"] = {}
                            current_claim["providers"][-1]["address"].update(n4_data)
                        elif current_subscriber and "payer_info" in current_subscriber and current_subscriber["payer_info"] and "address" in current_subscriber["payer_info"]:
                            current_subscriber["payer_info"]["address"].update(n4_data)
                        elif current_subscriber and "address" in current_subscriber["subscriber_info"]:
                            current_subscriber["subscriber_info"]["address"].update(n4_data)
                        elif current_billing_provider and "address" in current_billing_provider["provider_info"]:
                            current_billing_provider["provider_info"]["address"].update(n4_data)
                    
                    elif segment_id == 'REF':
                        ref_data = self.parse_ref_segment(elements)
                        # Add reference to appropriate entity
                        if current_claim and "providers" in current_claim and current_claim["providers"]:
                            if "references" not in current_claim["providers"][-1]:
                                current_claim["providers"][-1]["references"] = []
                            current_claim["providers"][-1]["references"].append(ref_data)
                        elif current_billing_provider and ref_data.get("reference_identification_qualifier") == "EI":
                            # Tax ID for billing provider
                            current_billing_provider["provider_info"]["tax_identification_number"] = ref_data.get("reference_identification", "")
                        elif current_subscriber:
                            if "references" not in current_subscriber["subscriber_info"]:
                                current_subscriber["subscriber_info"]["references"] = []
                            current_subscriber["subscriber_info"]["references"].append(ref_data)
                    
                    elif segment_id == 'DMG' and current_subscriber:
                        current_subscriber["subscriber_info"]["demographics"] = self.parse_dmg_segment(elements)
                    
                    elif segment_id == 'CLM' and current_subscriber:
                        # Loop 2300 - Claim Information
                        current_claim = {
                            "claim_info": self.parse_clm_segment(elements),
                            "dates": [],
                            "diagnosis_codes": [],
                            "service_lines": [],
                            "providers": [],
                            "references": [],
                            "amounts": [],
                            "notes": [],
                            "adjustments": []
                        }
                        current_subscriber["claims"].append(current_claim)
                        current_service_line = None
                    
                    elif segment_id == 'DTP':
                        dtp_data = self.parse_dtp_segment(elements)
                        if current_service_line:
                            # Service line level date
                            current_service_line["dates"].append(dtp_data)
                        elif current_claim:
                            # Claim level date
                            current_claim["dates"].append(dtp_data)
                        elif current_subscriber:
                            # Subscriber level date (rare)
                            if "dates" not in current_subscriber:
                                current_subscriber["dates"] = []
                            current_subscriber["dates"].append(dtp_data)
                    
                    elif segment_id == 'HI' and current_claim:
                        current_claim["diagnosis_codes"].append(self.parse_hi_segment(elements))
                    
                    elif segment_id == 'LX' and current_claim:
                        # Loop 2400 - Service Line Information
                        lx_data = self.parse_lx_segment(elements)
                        current_service_line = {
                            "line_number": lx_data.get("assigned_number", ""),
                            "service_info": {},
                            "dates": [],
                            "references": [],
                            "amounts": [],
                            "quantities": [],
                            "adjustments": [],
                            "notes": [],
                            "providers": []  # Line-level providers
                        }
                        current_claim["service_lines"].append(current_service_line)
                    
                    elif segment_id == 'SV1' and current_service_line:
                        # Professional Service - core of Loop 2400
                        current_service_line["service_info"] = self.parse_sv1_segment(elements)
                    
                    elif segment_id == 'SV2' and current_service_line:
                        # Institutional Service Line
                        current_service_line["institutional_service_info"] = self.parse_sv2_segment(elements)
                    
                    elif segment_id == 'SV3' and current_service_line:
                        # Dental Service
                        current_service_line["dental_service_info"] = self.parse_sv3_segment(elements)
                    
                    elif segment_id == 'PRV':
                        prv_data = self.parse_prv_segment(elements)
                        # Add provider specialty info to the most recent provider
                        if current_service_line and "providers" in current_service_line and current_service_line["providers"]:
                            # Line-level provider
                            current_service_line["providers"][-1]["provider_taxonomy"] = prv_data.get("reference_identification", "")
                        elif current_claim and "providers" in current_claim and current_claim["providers"]:
                            # Claim-level provider
                            current_claim["providers"][-1]["provider_taxonomy"] = prv_data.get("reference_identification", "")
                        elif current_billing_provider:
                            # Billing provider level
                            current_billing_provider["provider_info"]["provider_taxonomy"] = prv_data.get("reference_identification", "")
                    
                    elif segment_id == 'AMT':
                        amt_data = self.parse_amt_segment(elements)
                        if current_service_line:
                            # Service line level amount
                            current_service_line["amounts"].append(amt_data)
                        elif current_claim:
                            # Claim level amount
                            current_claim["amounts"].append(amt_data)
                    
                    elif segment_id == 'QTY':
                        qty_data = self.parse_qty_segment(elements)
                        if current_service_line:
                            # Service line level quantity
                            current_service_line["quantities"].append(qty_data)
                        elif current_claim:
                            # Claim level quantity (rare)
                            if "quantities" not in current_claim:
                                current_claim["quantities"] = []
                            current_claim["quantities"].append(qty_data)
                    
                    elif segment_id == 'CAS':
                        cas_data = self.parse_cas_segment(elements)
                        if current_service_line:
                            # Service line level adjustment
                            current_service_line["adjustments"].extend(cas_data)
                        elif current_claim:
                            # Claim level adjustment
                            current_claim["adjustments"].extend(cas_data)
                    
                    elif segment_id == 'NTE':
                        nte_data = self.parse_nte_segment(elements)
                        if current_service_line:
                            # Service line level note
                            current_service_line["notes"].append(nte_data)
                        elif current_claim:
                            # Claim level note
                            current_claim["notes"].append(nte_data)
                    
                    elif segment_id == 'PER':
                        per_data = self.parse_per_segment(elements)
                        # Add contact info to appropriate entity
                        if current_billing_provider:
                            current_billing_provider["provider_info"]["contact_info"] = per_data
                        elif current_transaction and "submitter" in current_transaction:
                            current_transaction["submitter"]["contact_info"] = per_data
                    
                    elif segment_id == 'SBR' and current_subscriber:
                        sbr_data = self.parse_sbr_segment(elements)
                        payer_sequence = sbr_data.get("payer_responsibility_sequence_number_code", "")
                        
                        if payer_sequence == "P":  # Primary payer
                            current_subscriber["subscriber_info"].update(sbr_data)
                        else:  # Secondary, Tertiary, etc.
                            # Create secondary payer entry
                            secondary_payer = {
                                "payer_sequence": payer_sequence,
                                "subscriber_info": sbr_data,
                                "payer_info": {}
                            }
                            current_subscriber["secondary_payers"].append(secondary_payer)
                
                except Exception as e:
                    print(f"Error processing segment {segment_id}: {str(e)}")
                    continue
            
            return edi_data
            
        except Exception as e:
            print(f"Error parsing file {file_path}: {str(e)}")
            return None

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

def main():
    """Main execution function"""
    parser = EDI837BusinessParser()
    
    # Find EDI directories
    edi_directories = find_edi_directories()
    
    if not edi_directories:
        print("No EDI directories found in current directory")
        return
    
    all_business_data = []
    total_claims_extracted = 0
    
    for edi_dir in edi_directories:
        print(f"Found TOIH directory: {edi_dir['path']} with {edi_dir['file_count']} EDI files")
        print(f"Extracting EDI 837 data in business format from: {edi_dir['name']}")
        
        # Get list of EDI files
        edi_files = []
        try:
            for file in os.listdir(edi_dir['path']):
                if file.endswith(('.d', '.edi', '.txt', '.x12')):
                    edi_files.append(os.path.join(edi_dir['path'], file))
        except PermissionError:
            print(f"Permission denied accessing {edi_dir['path']}")
            continue
        
        print(f"Found {len(edi_files)} EDI files to process")
        
        # Process 1000 files as requested
        max_files = 1000
        if len(edi_files) > max_files:
            print(f"Will process {max_files} files out of {len(edi_files)} total files")
            edi_files = edi_files[:max_files]
        else:
            print(f"Will process all {len(edi_files)} files")
        
        # Process each file
        for i, file_path in enumerate(edi_files, 1):
            try:
                print(f"Processing {os.path.basename(file_path)}... ({i}/{len(edi_files)})")
                
                # Parse EDI file
                edi_data = parser.parse_edi_file(file_path)
                
                if edi_data:
                    # Convert to business format (returns list of claims)
                    claims = parser.convert_to_business_format(edi_data)
                    
                    if claims:
                        all_business_data.extend(claims)
                        total_claims_extracted += len(claims)
                
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
                continue
            
            # Progress update every 10 files
            if i % 10 == 0:
                print(f"✅ Processed {i} files, extracted {total_claims_extracted} claims so far")
        
        print(f"Completed processing {min(len(edi_files), max_files)} files")
    
    if total_claims_extracted == 0:
        print("No claims extracted")
        return
    
    print(f"\n📊 EXTRACTION SUMMARY:")
    print(f"Total claims extracted: {len(all_business_data)}")
    
    # Save business format JSON
    business_output_file = "edi_837_business_format.json"
    try:
        with open(business_output_file, 'w', encoding='utf-8') as f:
            json.dump(all_business_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Business format data saved to: {business_output_file}")
    except Exception as e:
        print(f"Error saving business format JSON: {str(e)}")
    
    # Create the three CSV files matching the required structure
    try:
        # Generate EDI_Claims.csv
        claims_records = []
        company_setup_records = []
        claim_detail_records = []
        
        claim_id_counter = 1
        detail_id_counter = 1
        
        for claim in all_business_data:
            transaction = claim.get("transaction", {})
            billing_provider = claim.get("billingProvider", {})
            subscriber = claim.get("subscriber", {}).get("person", {})
            payer = claim.get("payer", {})
            
            # Extract all providers
            referring_provider = {}
            rendering_provider = {}
            facility_provider = {}
            
            for provider in claim.get("providers", []):
                if provider.get("entityRole") == "REFERRING":
                    referring_provider = provider
                elif provider.get("entityRole") == "RENDERING":
                    rendering_provider = provider
                elif provider.get("entityRole") == "SERVICE_FACILITY":
                    facility_provider = provider
            
            # Build EDI_Claims record with all required fields
            claims_record = {
                'ID': claim_id_counter,
                'Filename': transaction.get("fileInfo", {}).get("fileType", "") + "-" + str(claim_id_counter) + ".d",
                'Version': transaction.get("implementationConventionReference", ""),
                'ImageFilePath': None,
                'ImageFilename': None,
                'TradingPartnerIDType': transaction.get("receiver", {}).get("identificationType", ""),
                'TradingPartnerID': transaction.get("receiver", {}).get("identifier", ""),
                'TransactionDate': transaction.get("creationDate", ""),
                'TransactionTime': transaction.get("creationTime", ""),
                'ReceiveDate': datetime.now().strftime("%Y-%m-%d"),
                'SubmitterName': transaction.get("sender", {}).get("lastNameOrOrgName", ""),
                'SubmitterID': transaction.get("sender", {}).get("identifier", ""),
                'SubmitterContact': transaction.get("sender", {}).get("contacts", [{}])[0].get("name", "") if transaction.get("sender", {}).get("contacts") else "",
                'SubmitterTel': transaction.get("sender", {}).get("contacts", [{}])[0].get("contactNumbers", [{}])[0].get("number", "") if transaction.get("sender", {}).get("contacts") else "",
                'SubmitterTelExt': None,
                'SubmitterFax': None,
                'SubmitterEmail': None,
                'ReceiverName': transaction.get("receiver", {}).get("lastNameOrOrgName", ""),
                'ReceiverID': transaction.get("receiver", {}).get("identifier", ""),
                'TransactionType': transaction.get("transactionType", ""),
                'OrigAppTransactionID': transaction.get("originatorApplicationTransactionId", ""),
                'FedTaxIDQual': "EI",
                'FedTaxID': billing_provider.get("taxId", ""),
                'BillProvIDType': billing_provider.get("identificationType", ""),
                'BillProvID': billing_provider.get("identifier", ""),
                'BillProvNPI': billing_provider.get("identifier", "") if billing_provider.get("identificationType") == "NPI" else "",
                'BillProvLast': billing_provider.get("lastNameOrOrgName", ""),
                'BillProvFirst': billing_provider.get("firstName", ""),
                'BillProvMiddle': billing_provider.get("middleName", ""),
                'BillProvSuffix': None,
                'BillProvSpecialty': None,
                'BillProvAddress': billing_provider.get("address", {}).get("line", ""),
                'BillProvAddress2': billing_provider.get("address", {}).get("line2", ""),
                'BillProvCity': billing_provider.get("address", {}).get("city", ""),
                'BillProvState': billing_provider.get("address", {}).get("stateCode", ""),
                'BillProvZip': billing_provider.get("address", {}).get("zipCode", ""),
                'BillProvCountry': None,
                'BillProvSubdivision': None,
                'BillProvContact': None,
                'BillProvTel': None,
                'BillProvTelExt': None,
                'BillProvFax': None,
                'BillProvEmail': None,
                'BillProvOtherIDQual1': None,
                'BillProvOtherID1': None,
                'BillProvOtherIDQual2': None,
                'BillProvOtherID2': None,
                'BillProvOtherIDQual3': None,
                'BillProvOtherID3': None,
                'BillProvOtherIDQual4': None,
                'BillProvOtherID4': None,
                'BillProvOtherIDQual5': None,
                'BillProvOtherID5': None,
                
                # Subscriber information
                'SubscriberLast': subscriber.get("lastNameOrOrgName", ""),
                'SubscriberFirst': subscriber.get("firstName", ""),
                'SubscriberMiddle': None,
                'SubscriberSuffix': None,
                'SubscriberIDType': subscriber.get("identificationType", ""),
                'SubscriberID': subscriber.get("identifier", ""),
                'SubscriberAddress': subscriber.get("address", {}).get("line", ""),
                'SubscriberAddress2': None,
                'SubscriberCity': subscriber.get("address", {}).get("city", ""),
                'SubscriberState': subscriber.get("address", {}).get("stateCode", ""),
                'SubscriberZip': subscriber.get("address", {}).get("zipCode", ""),
                'SubscriberCountry': None,
                'SubscriberLocation': None,
                'SubscriberSubdivision': None,
                'SubscriberDOB': subscriber.get("birthDate", ""),
                'SubscriberSex': subscriber.get("gender", ""),
                'SubscriberEthnicity': None,
                'SubscriberMaritalStatus': None,
                'SubscriberCollectionMethod': None,
                'SubscriberSSN': None,
                'SubscriberAgencyClaimNo': None,
                'SubscriberMemberID': subscriber.get("identifier", ""),
                'SubscriberPersonalID': None,
                'SubscriberContact': None,
                'SubscriberTel': None,
                'SubscriberTelExt': None,
                'SubscriberEmail': None,
                
                # Payer information
                'PayerName': payer.get("lastNameOrOrgName", ""),
                'PayerIDType': payer.get("identificationType", ""),
                'PayerID': payer.get("identifier", ""),
                'PayerAddress': payer.get("address", {}).get("line", ""),
                'PayerAddress2': None,
                'PayerCity': payer.get("address", {}).get("city", ""),
                'PayerState': payer.get("address", {}).get("stateCode", ""),
                'PayerZip': payer.get("address", {}).get("zipCode", ""),
                'PayerResponsibility': claim.get("subscriber", {}).get("payerResponsibilitySequence", ""),
                'PayerOtherIDQual1': None,
                'PayerOtherID1': None,
                'PayerOtherIDQual2': None,
                'PayerOtherID2': None,
                'PayerOtherIDQual3': None,
                'PayerOtherID3': None,
                'GroupNo': None,
                'GroupName': None,
                'InsuranceType': claim.get("subscriber", {}).get("insurancePlanType", ""),
                'FilingIndicator': claim.get("subscriber", {}).get("claimFilingIndicatorCode", ""),
                'COBIndicator': None,
                'DataReceiverName': None,
                
                # Rendering Provider
                'RendProvIDType': rendering_provider.get("identificationType", ""),
                'RendProvID': rendering_provider.get("identifier", ""),
                'RendProvNPI': rendering_provider.get("identifier", "") if rendering_provider.get("identificationType") == "NPI" else "",
                'RendProvTaxID': None,
                'RendProvLast': rendering_provider.get("lastNameOrOrgName", ""),
                'RendProvFirst': rendering_provider.get("firstName", ""),
                'RendProvMiddle': rendering_provider.get("middleName", ""),
                'RendProvSuffix': None,
                'RendProvSpecialty': rendering_provider.get("providerTaxonomy", {}).get("code", ""),
                'RendProvOtherIDQual1': rendering_provider.get("additionalIds", [{}])[0].get("qualifierCode", "") if rendering_provider.get("additionalIds") else "",
                'RendProvOtherID1': rendering_provider.get("additionalIds", [{}])[0].get("identification", "") if rendering_provider.get("additionalIds") else "",
                'RendProvOtherIDQual2': None,
                'RendProvOtherID2': None,
                'RendProvOtherIDQual3': None,
                'RendProvOtherID3': None,
                
                # Facility information
                'FacilityType': facility_provider.get("entityType", ""),
                'FacilityIDType': facility_provider.get("identificationType", ""),
                'FacilityID': facility_provider.get("identifier", ""),
                'FacilityNPI': facility_provider.get("identifier", "") if facility_provider.get("identificationType") == "NPI" else "",
                'FacilityTaxID': None,
                'FacilityOtherIDQual1': facility_provider.get("additionalIds", [{}])[0].get("qualifierCode", "") if facility_provider.get("additionalIds") else "",
                'FacilityOtherID1': facility_provider.get("additionalIds", [{}])[0].get("identification", "") if facility_provider.get("additionalIds") else "",
                'FacilityOtherIDQual2': facility_provider.get("additionalIds", [{}])[1].get("qualifierCode", "") if len(facility_provider.get("additionalIds", [])) > 1 else "",
                'FacilityOtherID2': facility_provider.get("additionalIds", [{}])[1].get("identification", "") if len(facility_provider.get("additionalIds", [])) > 1 else "",
                'FacilityOtherIDQual3': None,
                'FacilityOtherID3': None,
                'FacilityName': facility_provider.get("lastNameOrOrgName", ""),
                'FacilityAddress': facility_provider.get("address", {}).get("line", ""),
                'FacilityAddress2': facility_provider.get("address", {}).get("line2", ""),
                'FacilityCity': facility_provider.get("address", {}).get("city", ""),
                'FacilitySpecialty': None,
                'FacilityState': facility_provider.get("address", {}).get("stateCode", ""),
                'FacilityZip': facility_provider.get("address", {}).get("zipCode", ""),
                'FacilityContact': None,
                'FacilityTel': None,
                'FacilityTelExt': None,
                
                # Referring Provider
                'RefProvLast': referring_provider.get("lastNameOrOrgName", ""),
                'RefProvFirst': referring_provider.get("firstName", ""),
                'RefProvMiddle': referring_provider.get("middleName", ""),
                'RefProvSuffix': None,
                'RefProvIDType': referring_provider.get("identificationType", ""),
                'RefProvID': referring_provider.get("identifier", ""),
                'RefProvTaxID': None,
                'RefProvNPI': referring_provider.get("identifier", "") if referring_provider.get("identificationType") == "NPI" else "",
                'RefProvOtherIDQual1': None,
                'RefProvOtherID1': None,
                'RefProvOtherIDQual2': None,
                'RefProvOtherID2': None,
                'RefProvOtherIDQual3': None,
                'RefProvOtherID3': None,
                'RefProvSpecialty': None,
                
                # Claim information
                'ClaimNo': claim.get("patientControlNumber", ""),
                'Amount': claim.get("chargeAmount", ""),
                'EstimatedAmountDue': None,
                'PatientEstimatedAmountDue': None,
                'PlaceOfService': claim.get("facilityCode", {}).get("code", ""),
                'ClaimFrequency': claim.get("frequencyCode", {}).get("code", ""),
                'SubmitReason': None,
                'ProviderSignature': claim.get("providerSignatureIndicator", ""),
                'ProviderAcceptsAssignment': claim.get("assignmentParticipationCode", ""),
                'BenefitAssignment': claim.get("assignmentCertificationIndicator", ""),
                'InfoReleaseCode': claim.get("releaseOfInformationCode", ""),
                'PatientSignatureCode': None,
                'RelatedCauses': None,
                'RelatedCauses2': None,
                'RelatedCausesState': None,
                'RelatedCausesCountry': None,
                'SpecialProgramCode': None,
                'ProviderParticipation': None,
                'EOBIndicator': None,
                'DelayReasonCode': None,
                'ServiceDateFrom': claim.get("serviceDateFrom", ""),
                'ServiceDateTo': claim.get("serviceDateTo", ""),
                'OnsetDate': None,
                'InitialTreatmentDate': None,
                'LastSeenDate': None,
                'AcuteManifestationDate': None,
                'LastDateWorked': None,
                'ReturnToWorkDate': None,
                'SimilarSymptomsDate': None,
                'DisabilityBegin': None,
                'DisabilityEnd': None,
                'HospitalizationBegin': None,
                'HospitalizationEnd': None,
                'AccidentDate': None,
                'LastMenstrualPeriod': None,
                'LastXRayDate': None,
                'PrescriptionDate': None,
                'AssumedCareDate': None,
                'RelinquishedCareDate': None,
                'FirstVisitDate': None,
                'RepricerReceivedDate': None,
                'AdmissionDate': None,
                'AdmissionHour': None,
                'AdmissionType': None,
                'AdmissionSource': None,
                'DischargeHour': None,
                'PatientStatus': None,
                'CoveredDays': None,
                'NonCoveredDays': None,
                'COBDays': None,
                'LifeTimeReserveDays': None,
                'PriorAuthorization': None,
                'ClearingHouseID': None,
                'MedicalRecordNumber': None,
                'MothersMedicalRecordNumber': None,
                'ServiceAuthorizationException': None,
                'ReferralNumber': None,
                'PayerClaimControlNumber': None,
                'AdjustedRepricedClaimNumber': None,
                'AutoAccidentState': None,
                'MedicareCrossoverIndicator': None,
                'MammographyCertID': None,
                'CLIA': None,
                'InvestDeviceExemptionNo': None,
                'DemonstrationProjectID': None,
                'CarePlanOversight': None,
                'PROApprovalNo': None,
                'PredeterminationID': None,
                'ClaimType': None,
                'TypeOfBill': None,
                'Remark1': None,
                'Remark2': None,
                'Remark3': None,
                'Remark4': None,
                'K3_1': None,
                'K3_2': None,
                'OutsideLab': None,
                'LabCharge': None,
                'Test_Prod': None,
                'ReportTypeCode1': None,
                'ReportTransmissionCode1': None,
                'AttachmentControlNumber1': None,
                'ReportTypeCode2': None,
                'ReportTransmissionCode2': None,
                'AttachmentControlNumber2': None,
                'ReportTypeCode3': None,
                'ReportTransmissionCode3': None,
                'AttachmentControlNumber3': None,
                'ContractType': None,
                'ContractAmount': None,
                'ContractPercentage': None,
                'ContractCode': None,
                'TermsDiscountPercentage': None,
                'ContractVersionID': None,
                'Predetermination': None,
                'OrthodonticTotal': None,
                'OrthodonticRemaining': None,
                'OrthodonticYesNo': None,
                'ToothStatus': None,
                'AppliancePlacementDate': None,
                'AdmitDiagnosis': None,
                'ECode': None,
                'ECode2': None,
                'ECode3': None,
                'ECode4': None,
                'ECode5': None,
                'ECode6': None,
                'ECode7': None,
                'ECode8': None,
                'ReasonForVisit': None,
                'ReasonForVisit2': None,
                'ReasonForVisit3': None,
                
                # Diagnosis codes
                'PrincipalDiagnosis': claim.get("diags", [{}])[0].get("code", "") if claim.get("diags") else "",
                'Diag2': claim.get("diags", [{}])[1].get("code", "") if len(claim.get("diags", [])) > 1 else "",
                'Diag3': claim.get("diags", [{}])[2].get("code", "") if len(claim.get("diags", [])) > 2 else "",
                'Diag4': claim.get("diags", [{}])[3].get("code", "") if len(claim.get("diags", [])) > 3 else "",
                'Diag5': claim.get("diags", [{}])[4].get("code", "") if len(claim.get("diags", [])) > 4 else "",
                'Diag6': claim.get("diags", [{}])[5].get("code", "") if len(claim.get("diags", [])) > 5 else "",
                'Diag7': claim.get("diags", [{}])[6].get("code", "") if len(claim.get("diags", [])) > 6 else "",
                'Diag8': claim.get("diags", [{}])[7].get("code", "") if len(claim.get("diags", [])) > 7 else "",
                'Diag9': claim.get("diags", [{}])[8].get("code", "") if len(claim.get("diags", [])) > 8 else "",
                'Diag10': claim.get("diags", [{}])[9].get("code", "") if len(claim.get("diags", [])) > 9 else "",
                'DRG': None,
                'PrincipalProcedure': None,
                'PrincipalProcedureDate': None,
                'Proc2': None,
                'Proc2Date': None,
                'Proc3': None,
                'Proc3Date': None,
                'Proc4': None,
                'Proc4Date': None,
                'Proc5': None,
                'Proc5Date': None,
                'Proc6': None,
                'Proc6Date': None,
                'Proc7': None,
                'Proc7Date': None,
                'Proc8': None,
                'Proc8Date': None,
                'Proc9': None,
                'Proc9Date': None,
                'Proc10': None,
                'Proc10Date': None
            }
            
            # Add remaining fields with None values to match the CSV structure
            remaining_fields = [
                'ValueCode1', 'ValueAmount1', 'ValueCode2', 'ValueAmount2', 'ValueCode3', 'ValueAmount3',
                'ValueCode4', 'ValueAmount4', 'ValueCode5', 'ValueAmount5', 'ValueCode6', 'ValueAmount6',
                'ValueCode7', 'ValueAmount7', 'ValueCode8', 'ValueAmount8', 'ValueCode9', 'ValueAmount9',
                'ValueCode10', 'ValueAmount10', 'ValueCode11', 'ValueAmount11', 'ValueCode12', 'ValueAmount12',
                'ConditionCode1', 'ConditionCode2', 'ConditionCode3', 'ConditionCode4', 'ConditionCode5',
                'ConditionCode6', 'ConditionCode7', 'ConditionCode8', 'ConditionCode9', 'ConditionCode10',
                'OccurranceCode1', 'OccurranceDate1', 'OccurranceCode2', 'OccurranceDate2', 'OccurranceCode3',
                'OccurranceDate3', 'OccurranceCode4', 'OccurranceDate4', 'OccurranceCode5', 'OccurranceDate5',
                'OccurranceCode6', 'OccurranceDate6', 'OccurranceCode7', 'OccurranceDate7', 'OccurranceCode8',
                'OccurranceDate8', 'OccurranceSpanCode1', 'OccurranceSpanFrom1', 'OccurranceSpanTo1',
                'OccurranceSpanCode2', 'OccurranceSpanFrom2', 'OccurranceSpanTo2', 'OccurranceSpanCode3',
                'OccurranceSpanFrom3', 'OccurranceSpanTo3', 'OccurranceSpanCode4', 'OccurranceSpanFrom4',
                'OccurranceSpanTo4', 'PatientWeight', 'AmbulanceTransportCode', 'AmbulanceTransportReasonCode',
                'TransportDistance', 'RoundTripPurposeDescription', 'StretcherPurposeDescription',
                'SpinalManipulationPatCondCode', 'SpinalManipulationPatCondDesc1', 'SpinalManipulationPatCondDesc2',
                'AmbulanceConditionIndicator', 'AmbulanceConditionCode1', 'AmbulanceConditionCode2',
                'AmbulanceConditionCode3', 'AmbulanceConditionCode4', 'AmbulanceConditionCode5',
                'SpectacleLensesCondIndicator', 'SpectacleLensesCondCode1', 'SpectacleLensesCondCode2',
                'SpectacleLensesCondCode3', 'SpectacleLensesCondCode4', 'SpectacleLensesCondCode5',
                'ContactLensesCondIndicator', 'ContactLensesCondCode1', 'ContactLensesCondCode2',
                'ContactLensesCondCode3', 'ContactLensesCondCode4', 'ContactLensesCondCode5',
                'SpectacleFramesCondIndicator', 'SpectacleFramesCondCode1', 'SpectacleFramesCondCode2',
                'SpectacleFramesCondCode3', 'SpectacleFramesCondCode4', 'SpectacleFramesCondCode5',
                'HomeboundConditionIndicator', 'EPSDTReferralCondIndicator', 'EPSDTReferralCondCode1',
                'EPSDTReferralCondCode2', 'EPSDTReferralCondCode3', 'RepricedClaimNumber', 'RepricingMethodology',
                'RepricedAmount', 'SavingsAmount', 'RepricerID', 'RepricingRate', 'APG_Code', 'APG_Amount',
                'ApprovedRevenueCode', 'ApprovedProcedureCode', 'ApprovedUnitCode', 'ApprovedUnits',
                'RejectReason', 'ComplianceCode', 'ExceptionCode'
            ]
            
            for field in remaining_fields:
                claims_record[field] = None
            
            claims_records.append(claims_record)
            
            # Create claim detail records for each service line
            for service_line in claim.get("serviceLines", []):
                detail_record = {
                    'ID': detail_id_counter,
                    'ClaimID': claim_id_counter,
                    'LineNumber': detail_id_counter,
                    'ServiceDateFrom': service_line.get("serviceDateFrom", ""),
                    'ServiceDateTo': None,
                    'AssessmentDate': None,
                    'PrescriptionDate': None,
                    'RecertificationDate': None,
                    'BeginTherapyDate': None,
                    'LastCertificationDate': None,
                    'LastSeenDate': None,
                    'TestDateHemo': None,
                    'TestDateCreatine': None,
                    'ShippedDate': None,
                    'LastXrayDate': None,
                    'InitialTreatmentDate': None,
                    'FacilityCode': None,
                    'RevenueCode': None,
                    'ProcedureQual': service_line.get("procedure", {}).get("subType", ""),
                    'ProcedureCode': service_line.get("procedure", {}).get("code", ""),
                    'Amount': service_line.get("chargeAmount", ""),
                    'Unit': service_line.get("unitType", ""),
                    'Quantity': service_line.get("unitCount", ""),
                    'UnitRate': None,
                    'NonCovered': None,
                    'MEA': None,
                    'PlaceOfService': claim.get("facilityCode", {}).get("code", ""),
                    'Modifier1': None,
                    'Modifier2': None,
                    'Modifier3': None,
                    'Modifier4': None,
                    'ProcedureDescription': service_line.get("procedure", {}).get("desc", ""),
                    'OralCavityDesignation1': None,
                    'OralCavityDesignation2': None,
                    'OralCavityDesignation3': None,
                    'OralCavityDesignation4': None,
                    'OralCavityDesignation5': None,
                    'ProsthesisPlacementStatus': None,
                    'DiagPointer1': service_line.get("diagPointers", [None])[0] if service_line.get("diagPointers") else None,
                    'DiagPointer2': None,
                    'DiagPointer3': None,
                    'DiagPointer4': None,
                    'EmergencyIndicator': None,
                    'EPSDTIndicator': None,
                    'FamilyPlanningIndicator': None,
                    'CoPayStatus': None,
                    'DME_Days': None,
                    'DME_RentalPrice': None,
                    'DME_PurchasePrice': None,
                    'DME_FrequencyCode': None,
                    'ToothNumber': None,
                    'Surface': None,
                    'EstimatedPlacementDate': None,
                    'PriorPlacementDate': None,
                    'AppliancePlacementDate': None,
                    'ReplacementDate': None,
                    'TreatmentStartDate': None,
                    'TreatmentCompletionDate': None,
                    'ServiceTax': None,
                    'FacilityTax': None,
                    'SalesTax': None,
                    'Postage': None,
                    'ApprovedAmount': None,
                    'LineK3_01': None,
                    'LineK3_02': None,
                    'LineK3_03': None,
                    'LineK3_04': None,
                    'LineK3_05': None,
                    'LineK3_06': None,
                    'LineK3_07': None,
                    'LineK3_08': None,
                    'LineK3_09': None,
                    'LineK3_10': None,
                    'Remark': None,
                    'AmbulancePatientCount': None,
                    'LineID': service_line.get("sourceLineId", ""),
                    'PredeterminationOfBenefitsID': None,
                    'POB_OtherPayerID': None,
                    'PriorAuthNo': None,
                    'PriorAuthOtherPayerID': None,
                    'RepricedClaimNo': None,
                    'AdjustedRepricedClaimNo': None,
                    'ReferralNo': None,
                    'ReferralNoOtherPayerID': None,
                    'RepricedLineNo': None,
                    'AdjustedRepricedLineNo': None,
                    'MammographyCertNo': None,
                    'CLIANo': None,
                    'CLIAFacilityID': None,
                    'ImmunizationBatchNo': None,
                    'ContractType': None,
                    'CN1_RepricedAmount': None,
                    'ContractPercentage': None,
                    'ContractCode': None,
                    'TermsDiscountPercentage': None,
                    'ContractVersionID': None,
                    'ReportType': None,
                    'ReportTransmission': None,
                    'AttachmentControlNumber': None,
                    'ReportType2': None,
                    'ReportTransmission2': None,
                    'AttachmentControlNumber2': None,
                    'ReportType3': None,
                    'ReportTransmission3': None,
                    'AttachmentControlNumber3': None,
                    'RepricingMethodology': None,
                    'RepricedAmount': None,
                    'SavingsAmount': None,
                    'RepricerID': None,
                    'RepricingRate': None,
                    'APG_Code': None,
                    'APG_Amount': None,
                    'ApprovedRevenueCode': None,
                    'ApprovedProcedureCodeQual': None,
                    'ApprovedProcedureCode': None,
                    'ApprovedUnitCode': None,
                    'ApprovedUnits': None,
                    'RejectReason': None,
                    'ComplianceCode': None,
                    'ExceptionCode': None
                }
                
                # Add remaining fields with None values
                detail_remaining_fields = [
                    'DrugCodeQual', 'DrugCode', 'DrugUnitPrice', 'DrugUnitCode', 'DrugUnits', 'LinkSequenceNumber',
                    'PrescriptionNumber', 'PatientWeight', 'AmbulanceTransportCode', 'AmbulanceTransportReasonCode',
                    'TransportDistance', 'RoundTripPurposeDescription', 'StretcherPurposeDescription',
                    'DMECertificationType', 'DMEDuration', 'AmbulanceConditionIndicator', 'AmbulanceConditionCode1',
                    'AmbulanceConditionCode2', 'AmbulanceConditionCode3', 'AmbulanceConditionCode4',
                    'AmbulanceConditionCode5', 'HospiceEmployerCondIndicator', 'HospiceEmployerCondCode',
                    'DMERCConditionIndicator', 'DMERCConditionCode1', 'DMERCConditionCode2',
                    'AttendingProviderLast', 'AttendingProviderFirst', 'AttendingProviderMiddle',
                    'AttendingProviderSuffix', 'AttendingProviderIDQual', 'AttendingProviderID',
                    'AttendingProviderOtherIDQual', 'AttendingProviderOtherID', 'OperatingProviderLast',
                    'OperatingProviderFirst', 'OperatingProviderMiddle', 'OperatingProviderSuffix',
                    'OperatingProviderIDQual', 'OperatingProviderID', 'OperatingProviderOtherIDQual',
                    'OperatingProviderOtherID', 'OtherProviderLast', 'OtherProviderFirst', 'OtherProviderMiddle',
                    'OtherProviderSuffix', 'OtherProviderIDQual', 'OtherProviderID', 'OtherProviderOtherIDQual',
                    'OtherProviderOtherID', 'RenderingProviderLast', 'RenderingProviderFirst',
                    'RenderingProviderMiddle', 'RenderingProviderSuffix', 'RenderingProviderIDQual',
                    'RenderingProviderID', 'RenderingProviderOtherIDQual', 'RenderingProviderOtherID',
                    'RenderingProviderSpecialty', 'PurchasedServiceProviderLast', 'PurchasedServiceProviderFirst',
                    'PurchasedServiceProviderMiddle', 'PurchasedServiceProviderSuffix',
                    'PurchasedServiceProviderIDQual', 'PurchasedServiceProviderID',
                    'PurchasedServiceProviderOtherIDQual', 'PurchasedServiceProviderOtherID',
                    'PurchasedServiceProviderAmount', 'FacilityName', 'FacilityIDQual', 'FacilityID',
                    'FacilityAddress1', 'FacilityAddress2', 'FacilityCity', 'FacilityState', 'FacilityZip',
                    'FacilityOtherIDQual', 'FacilityOtherID', 'SupervisingProviderLast', 'SupervisingProviderFirst',
                    'SupervisingProviderMiddle', 'SupervisingProviderSuffix', 'SupervisingProviderIDQual',
                    'SupervisingProviderID', 'SupervisingProviderOtherIDQual', 'SupervisingProviderOtherID',
                    'OrderingProviderLast', 'OrderingProviderFirst', 'OrderingProviderMiddle',
                    'OrderingProviderSuffix', 'OrderingProviderIDQual', 'OrderingProviderID',
                    'OrderingProviderOtherIDQual', 'OrderingProviderOtherID', 'ReferringProviderLast',
                    'ReferringProviderFirst', 'ReferringProviderMiddle', 'ReferringProviderSuffix',
                    'ReferringProviderIDQual', 'ReferringProviderID', 'ReferringProviderOtherIDQual',
                    'ReferringProviderOtherID', 'OtherPayer1ID', 'OtherPayer1Paid', 'OtherPayer1PaidProcedure',
                    'OtherPayer1PaidRevenueCode', 'OtherPayer1PaidQuantity', 'OtherPayer1BundledLine',
                    'OtherPayer1AdjustmentReasonGroup1', 'OtherPayer1AdjustmentReason1',
                    'OtherPayer1AdjustmentAmount1', 'OtherPayer1AdjustmentQuantity1',
                    'OtherPayer1AdjustmentReasonGroup2', 'OtherPayer1AdjustmentReason2',
                    'OtherPayer1AdjustmentAmount2', 'OtherPayer1AdjustmentQuantity2',
                    'OtherPayer1AdjustmentReasonGroup3', 'OtherPayer1AdjustmentReason3',
                    'OtherPayer1AdjustmentAmount3', 'OtherPayer1AdjustmentQuantity3',
                    'OtherPayer1AdjustmentReasonGroup4', 'OtherPayer1AdjustmentReason4',
                    'OtherPayer1AdjustmentAmount4', 'OtherPayer1AdjustmentQuantity4', 'OtherPayer1PaidDate',
                    'OtherPayer1AmountOwed', 'OtherPayer2ID', 'OtherPayer2Paid', 'OtherPayer2PaidProcedure',
                    'OtherPayer2PaidRevenueCode', 'OtherPayer2PaidQuantity', 'OtherPayer2BundledLine',
                    'OtherPayer2AdjustmentReasonGroup1', 'OtherPayer2AdjustmentReason1',
                    'OtherPayer2AdjustmentAmount1', 'OtherPayer2AdjustmentQuantity1',
                    'OtherPayer2AdjustmentReasonGroup2', 'OtherPayer2AdjustmentReason2',
                    'OtherPayer2AdjustmentAmount2', 'OtherPayer2AdjustmentQuantity2',
                    'OtherPayer2AdjustmentReasonGroup3', 'OtherPayer2AdjustmentReason3',
                    'OtherPayer2AdjustmentAmount3', 'OtherPayer2AdjustmentQuantity3',
                    'OtherPayer2AdjustmentReasonGroup4', 'OtherPayer2AdjustmentReason4',
                    'OtherPayer2AdjustmentAmount4', 'OtherPayer2AdjustmentQuantity4', 'OtherPayer2PaidDate',
                    'OtherPayer2AmountOwed'
                ]
                
                for field in detail_remaining_fields:
                    detail_record[field] = None
                
                claim_detail_records.append(detail_record)
                detail_id_counter += 1
            
            claim_id_counter += 1
        
        # Save the three CSV files
        if claims_records:
            claims_df = pd.DataFrame(claims_records)
            claims_df.to_csv('EDI_Claims_Output.csv', index=False, encoding='utf-8')
            print(f"✅ EDI_Claims_Output.csv saved with {len(claims_records)} records")
        
        if claim_detail_records:
            details_df = pd.DataFrame(claim_detail_records)
            details_df.to_csv('EDI_ClaimDetail_Output.csv', index=False, encoding='utf-8')
            print(f"✅ EDI_ClaimDetail_Output.csv saved with {len(claim_detail_records)} records")
        
        # Extract unique company setup records from all claims
        company_setup_records = []
        unique_companies = {}
        company_id_counter = 1
        
        for claim in all_business_data:
            transaction = claim.get("transaction", {})
            sender = transaction.get("sender", {})
            receiver = transaction.get("receiver", {})
            billing_provider = claim.get("billingProvider", {})
            
            # Create unique key for company (sender + receiver + billing provider)
            company_key = f"{sender.get('identifier', '')}-{receiver.get('identifier', '')}-{billing_provider.get('identifier', '')}"
            
            if company_key not in unique_companies:
                # Extract company setup data from EDI transaction data
                company_record = {
                    'ID': company_id_counter,
                    'Name': billing_provider.get("lastNameOrOrgName", ""),
                    'Address1': billing_provider.get("address", {}).get("line", ""),
                    'Address2': billing_provider.get("address", {}).get("line2", ""),
                    'City': billing_provider.get("address", {}).get("city", ""),
                    'State': billing_provider.get("address", {}).get("stateCode", ""),
                    'Zip': billing_provider.get("address", {}).get("zipCode", ""),
                    'Zip_4': None,
                    'SenderID': sender.get("identifier", ""),
                    'SenderIDQualifier': sender.get("identificationType", ""),
                    'EdiNo': None,
                    'EIN': billing_provider.get("taxId", ""),
                    'FileID': None,
                    'Contact': sender.get("contacts", [{}])[0].get("name", "") if sender.get("contacts") else "",
                    'Tel': sender.get("contacts", [{}])[0].get("contactNumbers", [{}])[0].get("number", "") if sender.get("contacts") and sender.get("contacts")[0].get("contactNumbers") else "",
                    'Ext': None,
                    'Fax': None,
                    'Email': None,
                    'Ack': None,
                    'TP': None,
                    'PayorID': None,
                    'PlanID': None,
                    'EntityType': billing_provider.get("entityType", ""),
                    'EDIVersion': transaction.get("implementationConventionReference", ""),
                    'SourceEntityID': receiver.get("identifier", ""),
                    'SourceName': receiver.get("lastNameOrOrgName", ""),
                    'SourceIDQual': receiver.get("identificationType", ""),
                    'SourceID': receiver.get("identifier", ""),
                    'InsuranceType': None,
                    'BankName': None,
                    'RoutingNo': None,
                    'AccountNo': None
                }
                
                unique_companies[company_key] = company_record
                company_setup_records.append(company_record)
                company_id_counter += 1
        
        if company_setup_records:
            company_df = pd.DataFrame(company_setup_records)
            company_df.to_csv('COMPANY_SETUP_Output.csv', index=False, encoding='utf-8')
            print(f"✅ COMPANY_SETUP_Output.csv saved with {len(company_setup_records)} records")
        else:
            print("⚠️ No company setup records found")
        
    except Exception as e:
        print(f"Error creating comprehensive CSV exports: {str(e)}")
    
    print(f"\n🎉 EDI 837 business format extraction completed successfully!")

if __name__ == "__main__":
    main()