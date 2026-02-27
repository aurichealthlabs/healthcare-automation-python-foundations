# HIPAA Compliance Note: This program uses no PHI.
# All examples are synthetic/educational.



# HIPAA Safe Harbor de-identification of PHI 18 Identifiers
# Changed to a tuple
# Tuples use () instead of [] to surround the list.

phi = ('names', 'all geographic subdivisions smaller than state', 'all elements of dates except year', 'telephone numbers', 'fax numbers', 'electronic mail address', 'social security numbers', 'medical records numbers', 'health plan beneficiary numbers', 'account numbers', 'certificate and/or license numbers', 'vehicle identifiers and serial numbers', 'device identifiers and serial numbers', 'web universal resource locators (url)', 'internet protocol address numbers (ip)', 'biometric identifiers', 'full face photographic images and any comparable images', 'any other unique identifying number, characteristic, or code')
# Source p. 97 hipaa-simplification-201303.pdf

print()
print(f'List index total: {len(phi)}')
print(f'This list contains ' + str(len(phi)) + ' total identifiers to be de-identified.\n')

print('This list is now a tuple, i.e. immutable\n')
for info in phi:
    print(info)
print()