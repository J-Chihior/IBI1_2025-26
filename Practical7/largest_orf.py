# import the module re
# create a string variable
# use findall to find all the sequences that meet the demand
#find the largest one

import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
#find all the sequences that meet the demand
ORF=re.findall(r'AUG(?:...)*?(?:UAA|UAG|UGA)', seq)
#get the longest one
if ORF:
    largest_orf=max(ORF,key=len)
    print("the largest ORF :",largest_orf)
    print("the length:",len(largest_orf))
else:
    print("No ORF found")# in case that no sequence meets the demand