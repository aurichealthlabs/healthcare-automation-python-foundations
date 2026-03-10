# HIPAA Code Review Checklist

A practical checklist for reviewing healthcare intelligence code before committing. Use this to ensure HIPAA compliance at every layer.

**Created:** February 2026 by Auric Health Labs  
**Updated:** March 2026 (v1.1 - Healthcare Intelligence focus)  
**Purpose:** Validate code for HIPAA compliance before pushing to repository  
**Used by:** Auric Health Labs in all healthcare intelligence projects

---

## How to Use This Checklist

Run through ALL sections before committing code that handles healthcare data. Even if you're using synthetic data for learning, build the habit of HIPAA-aware development.

**When to use:**
- Before every Git commit
- After AI generates code (Claude, Cursor, Copilot, etc.)
- When reviewing your own code
- Before sharing code examples
- When querying healthcare databases
- When analyzing patient datasets
- When investigating security incidents

---

## Layer 1: Prevention (Design)

**Principle:** Don't collect PHI if you don't need it (Minimum Necessary)

- [ ] Am I collecting only the minimum necessary data for this function?
- [ ] Could this work with just an ID instead of a full patient record?
- [ ] Have I documented WHY this specific PHI is needed?
- [ ] Are there alternative approaches that require less PHI?
- [ ] For analytics: Can I aggregate before accessing individual records?
- [ ] For fraud detection: Can I use de-identified data for pattern analysis?

**Example Check:**
```python
# ❌ BAD - Collects unnecessary PHI
def process_claim(patient_name, dob, ssn, address, claim_id):
    return claim_status(claim_id)  # Only needs claim_id!

# ✅ GOOD - Minimum necessary
def process_claim(claim_id):
    return claim_status(claim_id)

# ✅ GOOD - Analytics use case
def analyze_denial_patterns(claim_ids):
    """Analyze denial patterns using only claim identifiers.
    Patient details not needed for pattern recognition."""
    return aggregate_denial_stats(claim_ids)
```

---

## Layer 2: Detection (Input Validation)

**Principle:** Validate inputs for PHI before processing

- [ ] Do I validate/sanitize inputs that might contain PHI?
- [ ] Are there checks for common PHI patterns (SSN format, phone format, etc.)?
- [ ] Do error messages avoid revealing PHI?
- [ ] Are test cases using ONLY synthetic data?
- [ ] For SQL queries: Am I preventing PHI in WHERE clauses from being logged?
- [ ] For API calls: Are PHI parameters properly secured/encrypted?

**Example Check:**
```python
# ❌ BAD - No validation, might process real PHI
def log_patient_activity(patient_info):
    print(f"Activity: {patient_info}")

# ✅ GOOD - Validates and strips PHI before logging
def log_patient_activity(patient_id):
    if contains_phi(patient_id):
        raise ValueError("PHI detected in input")
    print(f"Activity for patient: {hash(patient_id)}")

# ✅ GOOD - Database query with validation
def query_claims_by_provider(provider_id):
    """Query claims WITHOUT logging PHI."""
    # Log the query pattern, not the data
    logger.info(f"Querying claims for provider (ID hashed)")
    return execute_query(provider_id)  # Results contain PHI - handle carefully
```

---

## Layer 3: Filtering (Output Sanitization)

**Principle:** Remove PHI before displaying or logging

- [ ] Are all print statements free of PHI?
- [ ] Are all log messages free of PHI?
- [ ] Are error messages generic (no patient-specific details)?
- [ ] Are debug outputs sanitized?
- [ ] Are return values checked for PHI leakage?
- [ ] For analytics: Are aggregated results checked for small cell sizes (<11 patients)?
- [ ] For fraud investigation: Are case summaries de-identified before sharing?

**Example Check:**
```python
# ❌ BAD - Logs PHI
logger.info(f"Processing patient {patient_name}, DOB: {dob}")

# ✅ GOOD - Logs without PHI
logger.info(f"Processing patient record {patient_id}")

# ✅ GOOD - Analytics output sanitized
def report_denial_stats(stats):
    """Report denial statistics with small cell suppression."""
    for category, count in stats.items():
        if count < 11:
            print(f"{category}: <11 (suppressed for privacy)")
        else:
            print(f"{category}: {count}")
```

---

## Layer 4: Warning (Alerting)

**Principle:** Alert when PHI is detected inappropriately

- [ ] Do I alert/warn when PHI is detected in unexpected places?
- [ ] Are warnings clear about WHAT was caught (without revealing actual PHI)?
- [ ] Do warnings explain WHY this is a compliance issue?
- [ ] Is there a mechanism to prevent continued processing if PHI detected?
- [ ] For investigation tools: Do they warn when accessing sensitive audit logs?
- [ ] For analytics: Do they alert when query returns identifiable data?

**Example Check:**
```python
# ✅ GOOD - Warns without revealing PHI
def validate_input(data):
    if contains_phi(data):
        warnings.warn(
            "HIPAA Warning: PHI detected in input. "
            "Use synthetic data only for testing.",
            category=HIPAAComplianceWarning
        )
        return False
    return True

# ✅ GOOD - Analytics warning
def analyze_patient_outcomes(patient_records):
    """Analyze outcomes with PHI detection."""
    if len(patient_records) < 11:
        warnings.warn(
            "HIPAA Warning: Small cell size (<11). "
            "Results may be identifiable. Consider aggregating.",
            category=StatisticalDisclosureWarning
        )
    # Continue with analysis...
```

---

## Layer 5: Stripping (De-identification)

**Principle:** If de-identifying data, remove ALL 18 PHI identifiers

- [ ] If de-identifying, are ALL 18 identifiers removed or generalized?
- [ ] Are dates generalized (to year only, or removed)?
- [ ] Are geographic areas larger than state level?
- [ ] Are ages over 89 aggregated to "90+"?
- [ ] Have I documented the de-identification method used?
- [ ] Is the resulting dataset truly non-identifiable?
- [ ] For analytics: Have I applied Safe Harbor or Expert Determination?
- [ ] For fraud detection: Can I use de-identified data for pattern training?

**18 PHI Identifiers Checklist:**
- [ ] Names (including nicknames, aliases)
- [ ] Geographic subdivisions smaller than state
- [ ] Dates (except year) - including birth, admission, discharge, death
- [ ] Telephone numbers
- [ ] Fax numbers
- [ ] Email addresses
- [ ] Social Security numbers
- [ ] Medical record numbers
- [ ] Health plan beneficiary numbers
- [ ] Account numbers
- [ ] Certificate/license numbers
- [ ] Vehicle identifiers and serial numbers
- [ ] Device identifiers and serial numbers
- [ ] Web URLs
- [ ] IP addresses
- [ ] Biometric identifiers (fingerprints, retinal scans)
- [ ] Full-face photographs
- [ ] Any other unique identifying number, characteristic, or code

---

## Healthcare Intelligence Contexts

**Additional considerations for fraud detection, analytics, and security investigation:**

### Fraud Detection & Pattern Analysis

**Principle:** Detect fraud patterns without exposing individual PHI

- [ ] Can fraud patterns be identified using aggregated/de-identified data first?
- [ ] Is individual PHI access limited to confirmed fraud cases only?
- [ ] Are anomaly detection models trained on de-identified datasets?
- [ ] Are investigation reports sanitized before sharing outside compliance team?
- [ ] Is access to fraud case PHI logged and auditable?

**Example:**
```python
# ✅ GOOD - Two-stage fraud detection
def detect_billing_fraud():
    """Stage 1: Aggregate analysis (no PHI)"""
    suspicious_providers = analyze_billing_patterns()  # Uses aggregates only
    
    """Stage 2: Individual investigation (controlled PHI access)"""
    for provider_id in suspicious_providers:
        # Log PHI access for audit
        log_phi_access(user="fraud_analyst", reason="investigation", provider=provider_id)
        # Access individual claims only for confirmed suspicious cases
        claims = get_provider_claims(provider_id)
        investigate_claims(claims)
```

### Clinical Analytics & Outcomes Analysis

**Principle:** Analyze population health while protecting individual privacy

- [ ] Are results aggregated to prevent re-identification?
- [ ] Are small cell sizes (<11 patients) suppressed?
- [ ] Are indirect identifiers (rare conditions + demographics) considered?
- [ ] Is statistical disclosure risk assessed before releasing results?
- [ ] Are limited datasets properly defined and documented?

**Example:**
```python
# ✅ GOOD - Population analysis with privacy protection
def analyze_readmission_rates(patient_cohort):
    """Analyze readmissions with privacy protection."""
    results = {}
    for demographic_group, patients in patient_cohort.items():
        count = len(patients)
        if count < 11:
            # Suppress small cells
            results[demographic_group] = "Suppressed (<11)"
        else:
            rate = calculate_readmission_rate(patients)
            results[demographic_group] = f"{rate:.1f}%"
    return results
```

### Security Investigation & Incident Response

**Principle:** Investigate breaches while minimizing further PHI exposure

- [ ] Is access to breach-related PHI limited to investigation team only?
- [ ] Are audit logs reviewed without exposing underlying PHI?
- [ ] Are investigation findings de-identified before broader reporting?
- [ ] Is all investigative PHI access documented for breach notification?
- [ ] Are security tools configured to alert without logging PHI?

**Example:**
```python
# ✅ GOOD - Security investigation with minimal PHI exposure
def investigate_unauthorized_access(access_log_entry):
    """Investigate security incident without exposing PHI unnecessarily."""
    # Log contains PHI access metadata, not PHI itself
    user_id = access_log_entry['user_id']
    record_id = access_log_entry['record_id']  # ID only, not patient data
    timestamp = access_log_entry['timestamp']
    
    # Determine if access was authorized WITHOUT pulling actual patient record
    if not is_authorized_access(user_id, record_id, timestamp):
        # Flag for investigation, log the INCIDENT not the PHI
        logger.warn(f"Unauthorized access attempt: User {user_id}, Time {timestamp}")
        # Only access actual PHI if investigation requires it
        # And log that access separately
```

### Database Queries & Data Analysis

**Principle:** Query healthcare data responsibly

- [ ] Are SQL queries parameterized (prevent PHI in WHERE clauses from logging)?
- [ ] Are query results checked for PHI before printing/logging?
- [ ] Are connection strings and credentials secured (separate from code)?
- [ ] Are result set sizes validated (prevent accidental mass PHI export)?
- [ ] Are temporary tables/files cleaned up after analysis?

**Example:**
```python
# ✅ GOOD - Database query with HIPAA awareness
def query_high_cost_claims(threshold):
    """Query high-cost claims without logging PHI."""
    query = """
        SELECT claim_id, provider_id, total_cost
        FROM claims
        WHERE total_cost > ?
        ORDER BY total_cost DESC
    """
    # Parameterized query prevents PHI logging
    # Query result contains IDs only (not patient names/DOB/etc.)
    results = execute_query(query, params=[threshold])
    
    # Log the QUERY PATTERN, not results
    logger.info(f"Queried {len(results)} claims above threshold")
    
    return results  # Return value contains limited PHI - handle carefully
```

---

## Synthetic Data Validation

**Principle:** All test/example data must be clearly synthetic

**My Synthetic Data Patterns:**
- Patient names: `TestPatient_001`, `SAMPLE-PATIENT-A`, `John_Doe_Test`
- MRNs: `99990001` and higher (outside real MRN ranges)
- Phone numbers: `555-0100` to `555-0199` (reserved for fiction)
- Emails: `test@example.com`, `patient001@example.com` (example.com reserved)
- Dates of birth: `1900-01-01`, `2000-01-01` (clearly non-real)
- SSNs: `000-00-0000`, `123-45-6789` (invalid formats)
- Addresses: `123 Test Street`, `000 Sample Avenue`
- Provider IDs: `TEST-PROV-001`, `99999` (clearly synthetic)
- Claim amounts: Round numbers like `1000.00`, `5000.00` (not realistic variation)

**Checklist:**
- [ ] All patient names are clearly synthetic/fake
- [ ] All MRNs are in synthetic range (99990001+)
- [ ] All phone numbers use 555 prefix
- [ ] All emails use example.com or clearly fake domains
- [ ] All dates are obviously synthetic
- [ ] No realistic combinations that could match real patients
- [ ] README/comments state: "All data is synthetic"
- [ ] Synthetic datasets large enough to demonstrate patterns (100+ records)

---

## AI-Generated Code Review

**Principle:** AI tools don't understand HIPAA - YOU must validate

**When using AI (Claude Code, Cursor, Copilot) for healthcare code:**

- [ ] Did AI log PHI anywhere? (Check print/logger statements)
- [ ] Did AI use realistic patient data? (Should be synthetic only)
- [ ] Did AI follow minimum necessary principle? (Or collect excessive data?)
- [ ] Did AI include PHI in error messages?
- [ ] Did AI include PHI in function names or comments?
- [ ] Did AI create test data that looks too realistic?
- [ ] Have I reviewed EVERY line AI generated?
- [ ] Did AI generate SQL queries that might log PHI?
- [ ] Did AI create analytics code without small cell suppression?

**Example AI Review Pattern:**
```
1. AI generates code
2. Search for: print(), logger., raise Exception
3. Check each for PHI content
4. Search for: patient_name, ssn, dob, phone, email
5. Verify each is handled compliantly
6. Check database queries for PHI logging
7. Check analytics for small cell suppression
8. Run through full checklist above
9. Only then commit
```

<!--  TO BE INCLUDED IF AND WHEN APPLICABLE:
**Common AI Mistakes I've Caught:**
- Logging full patient records for "debugging"
- Using realistic patient names in examples
- Including PHI in error messages
- Not following minimum necessary in function parameters
- SQL queries that log PHI in WHERE clauses
- Analytics results without small cell suppression
- No warnings when accessing sensitive data 
-->

---

## Comments and Documentation

**Principle:** Comments should explain HIPAA considerations

- [ ] Do my comments explain WHY HIPAA-specific decisions were made?
- [ ] Are HIPAA compliance notes included where relevant?
- [ ] Do function docstrings note PHI handling approach?
- [ ] Is it clear to future readers (including me) what data is PHI?
- [ ] Are de-identification methods documented?
- [ ] Are data access restrictions documented?

**Example:**
```python
def analyze_claim_denials(claim_ids):
    """
    Analyze claim denial patterns using aggregated data.
    
    HIPAA Note: Uses claim_ids only (not patient identifiers) following
    minimum necessary principle. Analysis performed on aggregated data
    to prevent individual patient identification. Results suppress counts
    <11 to prevent statistical disclosure.
    
    Args:
        claim_ids: List of claim identifiers (not PHI)
    
    Returns:
        Aggregated denial statistics (no PHI, small cells suppressed)
    """
    pass
```

---

## File and Repository Checks

**Principle:** Repository should never contain real PHI

- [ ] Is my .gitignore configured to exclude data files? (*.csv, *.xlsx, *.db)
- [ ] Are there any accidentally committed data files?
- [ ] Are test data files clearly marked as synthetic?
- [ ] Is README clear that all data is synthetic?
- [ ] Are there any API keys or credentials in the code? (separate concern but critical)
- [ ] Are SQL dumps excluded? (*.sql, *.dump)
- [ ] Are analysis outputs excluded? (*.xlsx, *.pdf reports)

**My .gitignore includes:**
```
# Healthcare data - never commit
*.csv
*.xlsx
*.db
*.sqlite
**/patient_data/
**/phi_data/
**/claims_data/
*.log
*.sql
*.dump
**/analysis_outputs/
**/investigation_reports/
```

---

## Before Committing - Final Check

**Run through this final checklist before `git commit`:**

1. [ ] All 5 layers reviewed (Prevention, Detection, Filtering, Warning, Stripping)
2. [ ] All synthetic data validated (clearly fake)
3. [ ] All AI-generated code reviewed line-by-line
4. [ ] All comments/documentation include HIPAA notes where relevant
5. [ ] No PHI in logs, prints, or error messages
6. [ ] Minimum necessary principle followed throughout
7. [ ] Healthcare Intelligence contexts considered (if applicable)
8. [ ] Database queries don't log PHI
9. [ ] Analytics include small cell suppression
10. [ ] I can explain WHY each HIPAA decision was made

**If ALL checked:** Safe to commit ✅

**If ANY unchecked:** Review that section before committing ❌

---

## Learning and Evolution

**This checklist evolves as I learn more about HIPAA compliance.**

**Version History:**
- v1.0 (February 2026): Initial checklist based on learning Healthcare Automation focus
- v1.1 (March 2026): Updated for Healthcare Intelligence focus - added fraud detection, analytics, and security investigation contexts

**Discoveries to add:**
- New pitfalls I encounter
- Additional AI mistakes I catch
- Better validation patterns I develop
- Edge cases I discover
- Intelligence-specific scenarios

---

## Resources

**Where I learned these patterns:**
- HHS.gov HIPAA resources
- HIPAA Privacy Rule (45 CFR Part 164)
- Safe Harbor de-identification method
- Statistical disclosure control principles
- Partnership with Claude AI (framework development)
- Practical application during Python learning

**Related Documentation:**
- See `HIPAA_COMPLIANCE.md` for full PHI identifier reference
- See `README.md` for healthcare intelligence project overview

---

## Notes

**This is a LEARNING tool.**

I'm building HIPAA-aware development habits from day one, even while learning Python fundamentals. This checklist helps me:

1. Think about compliance BEFORE writing code (not after)
2. Catch issues in AI-generated code (validate, don't blindly trust)
3. Build professional habits (that will matter in employment)
4. Document my process (for portfolio review)
5. Understand healthcare intelligence contexts (fraud, analytics, security)

**For employers reviewing this:**

This checklist demonstrates:
- HIPAA awareness from day one of learning
- Systematic approach to compliance across contexts (automation, analytics, investigation)
- AI partnership with validation (not blind trust)
- Professional discipline in code review
- Understanding of healthcare intelligence requirements
- Commitment to building compliant systems

---

*Last updated: March 2026*  
*Living document - updated as I learn more about HIPAA compliance in healthcare intelligence*
