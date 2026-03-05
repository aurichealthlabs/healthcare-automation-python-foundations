# THE 18 HIPAA PHI IDENTIFIERS (COMPLETE)

### Overview
Per 45 CFR §164.514(b)(2), the following 18 identifiers must be removed to properly de-identify protected health information. This portfolio addresses each identifier with synthetic data practices.

---

### 1. **Names**
**What qualifies:** Any name (patient, relative, employer, household member)

**Portfolio Practice:**
- ✅ Test data uses: `"TestPatient_001"`, `"Sample_Patient_A"`, `"Demo_John_Smith"`
- ✅ Clearly synthetic prefixes (Test, Sample, Demo, Mock)
- ✅ Sequential numbering for uniqueness
- ❌ Never use: Real names, common names without synthetic prefix

**Code Example:**
```python
# CORRECT - Obviously synthetic
patient_name = "TestPatient_001"
physician_name = "Dr_Sample_Provider"

# INCORRECT - Could be real person
patient_name = "John Smith"  # Too realistic, avoid
```

---

### 2. **Geographic Subdivisions Smaller Than State**
**What qualifies:** Street address, city, county, precinct, ZIP code, equivalent geocodes (except first 3 digits of ZIP if area >20,000 people)

**Portfolio Practice:**
- ✅ State-level only: `"IL"`, `"California"`, `"TX"`
- ✅ First 3 ZIP digits if population >20,000: `"606XX"` (Chicago area)
- ✅ Generic location references: `"Metropolitan area"`, `"Rural region"`
- ❌ Never use: Full addresses, cities, specific ZIP codes

**Code Example:**
```python
# CORRECT - State level only
patient_location = {
    'state': 'Illinois',
    'region': 'Midwest',
    'zip_prefix': '606XX'  # Chicago area (>20k population)
}

# INCORRECT - Too specific
patient_address = "123 Main St, Springfield, IL 62704"  # AVOID
```

---

### 3. **Dates (Except Year)**
**What qualifies:** 
- All dates directly related to individual (birth, admission, discharge, death)
- All ages over 89 (must be aggregated to "90 or older")
- Elements of dates (month/day) that could identify individual

**Portfolio Practice:**
- ✅ Birth dates: Randomized, clearly synthetic
  - Format: `"YYYY-01-01"` (January 1st placeholder)
  - Or: Random dates ensuring patient would be 18-89 years old
- ✅ Service dates: Generic or offset from real calendar
  - Use: `"2025-XX-XX"` or relative dates "30 days ago"
- ✅ Ages: 18-89 only (aggregate 90+ as "90+")
- ❌ Never use: Real birth dates, specific service dates, ages >89

**Code Example:**
```python
from datetime import datetime, timedelta
import random

# CORRECT - Synthetic date generation
def generate_synthetic_dob():
    """Generate random DOB for patient aged 18-89."""
    current_year = datetime.now().year
    age = random.randint(18, 89)
    birth_year = current_year - age
    # Use Jan 1 placeholder or random month/day
    return f"{birth_year}-01-01"

# CORRECT - Age handling
def display_age(age):
    """Display age with HIPAA aggregation."""
    if age >= 90:
        return "90+"  # Required aggregation
    return str(age)

# INCORRECT - Specific real dates
patient_dob = "1975-03-15"  # Too specific, avoid
admission_date = "2024-11-23"  # Real calendar date, avoid
```

---

### 4. **Telephone Numbers**
**What qualifies:** Any telephone or fax number

**Portfolio Practice:**
- ✅ Use: `"555-0100"` through `"555-0199"` (reserved for fictional use)
- ✅ Use: `"(555) 555-XXXX"` pattern
- ✅ Use: `"XXX-XXX-XXXX"` placeholder format
- ❌ Never use: Real phone numbers, 1-800 numbers, actual area codes with real exchanges

**Code Example:**
```python
# CORRECT - Fictional 555 exchange
patient_phone = "555-0123"
fax_number = "(555) 555-0187"
emergency_contact = "555-0145"

# CORRECT - Placeholder format
phone_placeholder = "XXX-XXX-XXXX"

# INCORRECT - Could be real number
patient_phone = "312-555-1234"  # Real Chicago area code, avoid
```

---

### 5. **Fax Numbers**
**What qualifies:** Any fax number (same rules as telephone)

**Portfolio Practice:**
- ✅ Same as telephone numbers: `"555-0100"` series
- ✅ Clearly marked as synthetic: `"Fax: 555-0150"`

**Code Example:**
```python
# CORRECT
provider_fax = "555-0167"
facility_fax = "(555) 555-0188"

# INCORRECT
provider_fax = "847-555-9876"  # Real area code, avoid
```

---

### 6. **Email Addresses**
**What qualifies:** Any electronic mail address

**Portfolio Practice:**
- ✅ Use: `example.com`, `test.com`, `sample.org` domains
- ✅ Use: Obviously synthetic usernames
- ✅ Format: `testpatient001@example.com`
- ❌ Never use: Real domains (gmail.com, yahoo.com), realistic email patterns

**Code Example:**
```python
# CORRECT - Reserved domains
patient_email = "testpatient001@example.com"
provider_email = "dr.sample@test.org"
facility_contact = "billing@sample-clinic.example"

# INCORRECT - Real domain
patient_email = "john.smith@gmail.com"  # Real domain, avoid
```

---

### 7. **Social Security Numbers (SSN)**
**What qualifies:** Full or partial SSN

**Portfolio Practice:**
- ✅ Use: `"XXX-XX-XXXX"` placeholder
- ✅ Use: `"000-00-0000"` (invalid SSN format)
- ✅ Use: `"999-99-9999"` (clearly synthetic)
- ❌ Never use: Real SSN patterns, even if randomized

**Code Example:**
```python
# CORRECT - Obviously invalid/synthetic
patient_ssn = "XXX-XX-XXXX"  # Placeholder
patient_ssn = "000-00-0000"  # Invalid format
patient_ssn = "999-99-9999"  # Clearly synthetic

# INCORRECT
patient_ssn = "123-45-6789"  # Could be real, avoid
```

---

### 8. **Medical Record Numbers (MRN)**
**What qualifies:** Medical record number, health plan beneficiary number, account number

**Portfolio Practice:**
- ✅ Use: High-range synthetic sequences `99990001-99999999`
- ✅ Use: Alpha-numeric with clear prefix: `TEST-MRN-001`, `DEMO-12345`
- ✅ Use: Sequential test IDs: `MRN-00001`, `MRN-00002`
- ❌ Never use: Realistic MRN ranges that could overlap with real systems

**Code Example:**
```python
# CORRECT - High-range synthetic
patient_mrn = "99990001"
patient_mrn = "99995432"

# CORRECT - Prefixed test IDs
patient_mrn = "TEST-MRN-001"
patient_mrn = "DEMO-12345"
account_number = "SAMPLE-ACCT-9999"

# INCORRECT - Low range could overlap with real IDs
patient_mrn = "00012345"  # Too realistic, avoid
```

---

### 9. **Health Plan Beneficiary Numbers**
**What qualifies:** Insurance member ID, subscriber number, policy number

**Portfolio Practice:**
- ✅ Use: `"PLAN-TEST-001"`, `"SAMPLE-99999"`
- ✅ Use: Obviously synthetic patterns
- ❌ Never use: Real insurance ID formats

**Code Example:**
```python
# CORRECT
insurance_id = "PLAN-TEST-001"
member_number = "SAMPLE-99999"
subscriber_id = "DEMO-SUBSCRIBER-123"

# INCORRECT
insurance_id = "XYZ123456789"  # Realistic format, avoid
```

---

### 10. **Certificate/License Numbers**
**What qualifies:** Professional license numbers, vehicle IDs, device serial numbers

**Portfolio Practice:**
- ✅ Use: `"LICENSE-SAMPLE-001"`, `"CERT-TEST-999"`
- ✅ Use: Generic placeholders: `"LICENSE-XXXXXXX"`
- ❌ Never use: Real license number formats

**Code Example:**
```python
# CORRECT
physician_license = "LICENSE-SAMPLE-IL-001"
device_serial = "DEVICE-TEST-999"
certificate_number = "CERT-DEMO-ABC123"

# INCORRECT
physician_license = "IL123456789"  # Realistic state license, avoid
```

---

### 11. **Vehicle Identifiers and Serial Numbers**
**What qualifies:** License plates, VINs, any vehicle identifying number

**Portfolio Practice:**
- ✅ Use: `"PLATE-TEST-001"`, `"VIN-SAMPLE-XXX"`
- ✅ Not typically used in healthcare automation portfolio
- ❌ Never use: Realistic plate or VIN formats

**Code Example:**
```python
# CORRECT (if ever needed)
vehicle_plate = "TEST-PLATE-001"
vehicle_vin = "VIN-SAMPLE-XXXXXXXXXXXXX"

# Note: Rarely needed in healthcare automation projects
```

---

### 12. **Device Identifiers and Serial Numbers**
**What qualifies:** Medical device serial numbers, implant IDs

**Portfolio Practice:**
- ✅ Use: `"DEVICE-SAMPLE-001"`, `"SERIAL-TEST-999"`
- ✅ Use: Generic format: `"SERIAL-XXXXXXX"`
- ❌ Never use: Real device serial numbers

**Code Example:**
```python
# CORRECT
pacemaker_serial = "DEVICE-SAMPLE-001"
implant_id = "IMPLANT-TEST-999"
equipment_serial = "SERIAL-DEMO-ABC123"

# INCORRECT
device_serial = "PM2024-123456"  # Realistic format, avoid
```

---

### 13. **Web URLs**
**What qualifies:** Any web universal resource locator

**Portfolio Practice:**
- ✅ Use: `example.com`, `test.org`, `sample.net` (reserved domains)
- ✅ Use: `https://example.com/patient/portal`
- ❌ Never use: Real healthcare organization URLs

**Code Example:**
```python
# CORRECT - Reserved domains
patient_portal = "https://example.com/portal"
provider_website = "https://sample-clinic.test"
emr_url = "https://test-emr.example.org"

# INCORRECT
clinic_website = "https://chicagoclinic.com"  # Could be real, avoid
```

---

### 14. **IP Addresses**
**What qualifies:** Internet protocol address

**Portfolio Practice:**
- ✅ Use: `192.0.2.0/24` (TEST-NET-1, reserved)
- ✅ Use: `198.51.100.0/24` (TEST-NET-2, reserved)
- ✅ Use: `203.0.113.0/24` (TEST-NET-3, reserved)
- ✅ Use: `10.0.0.0/8` (private, safe for examples)
- ❌ Never use: Public IP ranges that could be real systems

**Code Example:**
```python
# CORRECT - Reserved test ranges
server_ip = "192.0.2.100"  # TEST-NET-1
workstation_ip = "198.51.100.50"  # TEST-NET-2
device_ip = "203.0.113.25"  # TEST-NET-3
internal_ip = "10.0.0.100"  # Private range, safe

# INCORRECT
server_ip = "8.8.8.8"  # Real Google DNS, avoid
clinic_ip = "72.14.207.99"  # Could be real, avoid
```

---

### 15. **Biometric Identifiers**
**What qualifies:** Fingerprints, retinal scans, voiceprints, facial photographs

**Portfolio Practice:**
- ✅ Use: Text descriptions only: `"Biometric data placeholder"`
- ✅ Use: Generic references: `"Fingerprint scan required"`
- ✅ Never include actual biometric data files
- ❌ Never use: Real photos, actual biometric scans

**Code Example:**
```python
# CORRECT - Text placeholder only
biometric_auth = {
    'type': 'fingerprint',
    'status': 'SAMPLE_BIOMETRIC_DATA',
    'note': 'Placeholder for production biometric validation'
}

# CORRECT - Generic reference
facial_recognition = "Biometric verification placeholder"

# Note: Never include actual biometric files in portfolio
```

---

### 16. **Full-Face Photographs**
**What qualifies:** Any photograph or comparable image of full face or identifying features

**Portfolio Practice:**
- ✅ Use: Text placeholders: `"Patient photo placeholder"`
- ✅ Use: Generic avatar images (non-identifiable clipart)
- ✅ Use: Solid color blocks with text: `[PATIENT PHOTO]`
- ❌ Never use: Real photographs, even with permission

**Code Example:**
```python
# CORRECT - Placeholder reference
patient_photo = {
    'type': 'image/placeholder',
    'description': 'Patient photo - not included in test data',
    'display': '[PHOTO PLACEHOLDER]'
}

# CORRECT - Generic avatar reference
profile_image = "generic_avatar_001.png"  # Non-identifiable clipart

# INCORRECT
patient_photo = "john_smith_photo.jpg"  # Never use real photos
```

---

### 17. **Other Unique Identifying Numbers**
**What qualifies:** Any other unique identifying characteristic or code (not previously listed)

**Portfolio Practice:**
- ✅ Use: Generic prefixed codes: `"UNIQUE-TEST-001"`
- ✅ Use: Obviously synthetic patterns
- ❌ Never use: Real identifying codes specific to individuals

**Code Example:**
```python
# CORRECT
unique_identifier = "UNIQUE-TEST-001"
patient_code = "SAMPLE-IDENTIFIER-999"
tracking_number = "DEMO-TRACK-ABC123"

# Examples of "other" identifiers this covers:
# - Employee ID numbers
# - Student ID numbers
# - Unique case numbers
# All should use synthetic/test prefixes
```

---

### 18. **Any Other Information That Could Identify Individual**
**What qualifies:** Catchall - any characteristic or combination that could identify individual

**Portfolio Practice:**
- ✅ Avoid: Rare diagnoses + specific location combinations
- ✅ Avoid: Unusual occupations + demographic details
- ✅ Think: "Could these combined details identify someone?"
- ✅ Use: Generic combinations that couldn't pinpoint individual
- ❌ Never use: Specific combinations that create unique fingerprint

**Code Example:**
```python
# CORRECT - Generic enough to not identify
patient_profile = {
    'age_range': '45-50',
    'occupation': 'Office worker',  # Common
    'diagnosis': 'Hypertension',  # Common (affects 47% of US adults)
    'location': 'Midwest'  # Broad region
}

# QUESTIONABLE - Too specific combination
patient_profile = {
    'age': 47,
    'occupation': 'Underwater welder',  # Rare profession
    'diagnosis': 'Fibrodysplasia ossificans progressiva',  # Extremely rare
    'location': 'Small town in rural Montana'  # Specific
}
# This combination could potentially identify individual - AVOID
```

**Examples of combinations to avoid:**
```python
# TOO SPECIFIC - Likely identifiable
{
    'diagnosis': 'Rare genetic disorder X',
    'treatment_location': 'Only hospital in state offering treatment',
    'age': 'One of 3 known cases in age group'
}

# SAFE - Generic combination
{
    'diagnosis_category': 'Chronic condition',
    'treatment_type': 'Outpatient',
    'age_range': '40-60'
}
```

---
---
---

## COMPLETE SUMMARY TABLE

| # | Identifier | Portfolio Practice | Example |
|---|------------|-------------------|---------|
| 1 | Names | Synthetic prefixes | `TestPatient_001` |
| 2 | Geographic < State | State-level only | `Illinois`, `606XX` |
| 3 | Dates (except year) | Randomized, 18-89 ages | `YYYY-01-01` |
| 4 | Telephone | 555-0100 to 555-0199 | `555-0123` |
| 5 | Fax | Same as telephone | `555-0167` |
| 6 | Email | Reserved domains | `test@example.com` |
| 7 | SSN | Invalid/placeholder | `XXX-XX-XXXX` |
| 8 | MRN | High-range synthetic | `99990001` |
| 9 | Health Plan # | Prefixed test IDs | `PLAN-TEST-001` |
| 10 | License # | Generic placeholders | `LICENSE-SAMPLE-001` |
| 11 | Vehicle IDs | Test placeholders | `PLATE-TEST-001` |
| 12 | Device Serials | Sample IDs | `DEVICE-SAMPLE-001` |
| 13 | URLs | Reserved domains | `example.com` |
| 14 | IP Addresses | Test ranges | `192.0.2.100` |
| 15 | Biometric | Text placeholders | `Biometric placeholder` |
| 16 | Photos | No actual images | `[PHOTO PLACEHOLDER]` |
| 17 | Other Unique # | Synthetic codes | `UNIQUE-TEST-001` |
| 18 | Any Identifying | Generic combinations | Avoid rare + specific |

---
*This is a learning repository demonstrating Python fundamentals applied to healthcare automation with HIPAA compliance awareness. All data is synthetic.*