import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii
1234567891 , 1010101010, 1111111111'''

# findall, search, split, sub, finditer


# ye jo finditer hai ye match object return kr ta hai 



print(r'\n')# this is a raw string .. 
# patt = re.compile(r'fass')
# patt = re.compile(r'.')  # ye jo hota hai vo any character hota hai mtlb ye sare character ko hi print kr denga...
# patt = re.compile(r'.aadm')
# patt = re.compile(r'^Tata')   # starts with
# patt = re.compile(r'Tata$')   # Ends with

# patt = re.compile(r'ai*')     # iss ka mtlb hai ki ek a ho aur kitne bhi i ho
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{2}')    # aapne ko kuch specific hona ki aii hi hona to i ke aage kuch iss tarah laga dena 
# patt = re.compile(r'(ai){2}')   # iss se aapne ko 2 ai milenge . 

# patt = re.compile(r'ai{2}|t')    # iss se ye hota hai ek to ye hona ye phir ye hona




# speial  sequence


# patt = re.compile(r'\ATata')  # starts with
# patt = re.compile(r'Fax\b')   # khi pr bhi 

# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\d{10}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
print(mystr[448:452]) # on line no 23


