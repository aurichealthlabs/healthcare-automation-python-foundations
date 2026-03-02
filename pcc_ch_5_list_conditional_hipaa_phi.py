# HIPAA Compliance Note: This program uses no PHI.
# All examples are synthetic/educational.



# HIPAA Safe Harbor de-identification of PHI 18 Identifiers
# Changed to a tuple = immutable
# Tuples use () instead of [] to surround the list.

phi = ('names', 'all geographic subdivisions smaller than state', 'all elements of dates except year', 'telephone numbers', 'fax numbers', 'electronic mail address', 'social security numbers', 'medical records numbers', 'health plan beneficiary numbers', 'account numbers', 'certificate and/or license numbers', 'vehicle identifiers and serial numbers', 'device identifiers and serial numbers', 'web universal resource locators (url)', 'internet protocol address numbers (ip)', 'biometric identifiers', 'full face photographic images and any comparable images', 'any other unique identifying number, characteristic, or code')
# Source p. 97 hipaa-simplification-201303.pdf

print()
print('PHI labels in this file are only recognition of the 18 identifiers.')
print('Any one identifier, alone, is not PHI.')
print()

print(f'Age as PHI: {phi[2]}')
print(f'Conditional: {phi[-1]}')
print()

# NOT PHI
# DOB is PHI, yet int(age) alone does not specify DOB
    # Exception to research: YEAR of birth, alone, is not PHI either
    # Age / Year alone are similar data points, so it does make sense
# Age alone outside of Covered Entity / Business Associate is not PHI

# IS PHI
# Age combined with other health data is PHI
# See conditions for 1. minors, 2. age 18 full rights, 3. 90+, etc
# See conditions for 1. law, 2. select states, 3. education admission, etc

# TO DO
# More Research: Year as acceptable de-identifier

# COMPLIANCE SOLUTION
# Minimum necessary rule
# Data Use Agreement if/when applicable
# Aggregate ages, ex. 20-29. 30-39, ... 70-79, etc

age = 74
if age <= 89:
    print(f'\tAge {age} alone is not PHI.')
print()

year = 2026
if year > 1936: # 90+ age rule
    print(f'\tYear {year} alone is not PHI and under 90 years of age.')
print()

dob = '02/27/2026'
month = 2
day = 27
print(f'Date of birth: {dob}')
print('\tMonth is ' + str(type(month)) + ' and PHI.')
print('\tDay is ' + str(type(day)) + ' and PHI.')
print('Changed str Day and Month to int for recognition and de-identification.')
print()

# isinstance is beyond the current lesson, so I tried to figure it out first.
# Eventually I had to look it up. This will be important soon enough.
if isinstance(month, int):
    print(f'Specifying a month, {month}, is PHI.')
    print(f'See: {phi[2]}')
print()

if isinstance(day, int):
    print(f'Specifying a day, {day}, is PHI.')
    print(f'See: {phi[2]}')
print()

# Elif test for only one condition
test_age = 91
print(f'== Testing elif statements ==\nAge is {test_age}')
if test_age < 18:
    print('Patient is a minor. PHI allowed with parents.')
elif test_age < 90:
    print('Patient is an adult with full rights to PHI.')
elif test_age >= 90:
    print('Patient is 90 or older, full PHI rights; do not specify age.')
print()

# Multiple if statements = testing for more than one condition
print(f'== Testing for PHI in list/tuple with multiple "if" statements ==')
if 'names' in phi:
    print(f'{phi[0].title()} are protected. De-identification needed.')
if 'time' not in phi:
    print('Time is not PHI.\n\t[This uses a "if, not in" statement]')
    print('\tCondition was ignored as "if, in"')

print('\n// Find index number: Social security numbers')
find_index_num = phi.index('social security numbers')
print(f'\tLocation is index {find_index_num} in "phi" tuple.')
if 'social security numbers' in phi:
    print(f'{phi[6].title()} are protected. De-identification needed.')

print('\n// Find index number: Telephone numbers')
find_index_num = phi.index('telephone numbers')
print(f'\tLocation is index {find_index_num} in "phi" tuple.')
if 'telephone numbers' in phi:
    print(f'{phi[3].title()} are protected. De-identification needed.')

if 'weather' in phi:
    print('Weather is not PHI. [Left to show ignored "if, in" statement.]')
print()

# PHI conditions* and exceptions* (*not Python code)
# Copy list/tuple isn't this lesson, but included as relevant to this lesson
print('== Conditional PHI ==')
phi_add_exception = list(phi)
phi_add_exception.append('emancipated minor')
# print(phi_add_exception) # Test append

conditional_phi = ['emancipated minor', 'legal court order']

for phi_exception in conditional_phi:
    if phi_exception in phi_add_exception:
        print(phi_exception.title())
        print(f'PHI exception as {conditional_phi[0]}. Parents unauthorized.')
print()