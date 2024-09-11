# amino acid counter

peptide="Ala-Gly-Ala-Gly-Ala-Gly-Ala-Gly"
# converting the peptide into a list

pep_list=peptide.split("-")

# variable count
count=0
target="Ala"

for i in pep_list:
    if target == i:
        count=count+1
    else:
        continue

print(f"Ala is present {count} times")