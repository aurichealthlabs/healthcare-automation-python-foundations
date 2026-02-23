# HIPAA Compliance Note: This program uses no PHI.
# All examples are synthetic/educational.



# Variables and Strings
#patient_name = 'Patient name: Smith, John' # PHI identifier #1

# String with Method .title()
#patient_name = 'smith, john' # PHI identifier #1

# Whitespace added to Name on purpose to strip; important in future
# Constants are CAPITALIZED; this makes sense for most PHI
FIRST_NAME = " john" # PHI identifier #1
LAST_NAME = "   smith   " # PHI identifier #1
DOB = 'DOB: 2026-02-23' # PHI identifier #2
# MRN is organization specific
patient_mrn = 'MRN: SYN-9999-0001' # PHI identifier #3
diagnosis_code = 'Diagnosis: E11.9' # NOT PHI (code only)

print()
print('___Example Patient Data___')
#print(patient_name.title()) #store data lowercase; format when called

# Variables in Strings
# f string (format string)
print(f'Patient name: {LAST_NAME.title().strip()}, {FIRST_NAME.title().strip()}')
print(DOB)
print(patient_mrn)
print(diagnosis_code)
print()

phi = 'PHI = Protected Health Information'
requirement = 'PHI cannot be used or disclosed unless specifically permitted'

# Tabs and Newlines
print(phi)
print('\t3 inputs are PHI (name, DOB, MRN)\n\t1 input is not PHI (diagnosis code)')
print(requirement)
print()
