"""
ABSPY.PROJECT.1.1 
Extract phone numbers and emails from copied text in clipboard using regular expressions
1. Copy some text to clipboard
2. Run this program
3. Paste your text somewhere to get all extracted phone numbers and emails
"""

import pyperclip, re

# Create regex for phone number
regexPhone = re.compile(r"""
(\d\{3}|\(\d{3}\))?     # Areacode
(\s|-|\.)?              # Separator
(\d{3})                 # First 3 digits
(\s|-|\.)               # Separator
(\d{4})                 # Last 4 digits
(\s|-|\.)
(\s*(ext|x|ext.)\s*(\d{2,5}))?
""", re.VERBOSE)

# Create regex for email address
regexEmail = re.compile(r"""
[a-zA-Z0-9_%.+-]+     # Username
@
[a-zA-Z0-9.-]+        # Domain
(\.[a-zA-Z]{2,4})       # Top Level Domain (TLD)
""", re.VERBOSE)

# Find and format all emails and phone numbers
text = str(pyperclip.paste())
matches = []
for groups in regexPhone.findall(text):
    phoneNo = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNo += " x" + groups[8]
    matches.append(phoneNo)
for groups in regexEmail.findall(text):
    matches.append(groups[0])

# Paste text to clipboard
if len(matches) > 0:
    result = "\n".join(matches)
    pyperclip.copy(result)
    print("Copied to clipboard")
    print(result)    
else:
    print("No phone numbers or email addresses found.")
