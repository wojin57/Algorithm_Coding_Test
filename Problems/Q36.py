s1 = input()
s2 = input()
# Step 1. find longest co-subseq.
i1 = i2 = 0
cosubseq = ''
while i1 < len(s1) and i2 < len(s2):
    if s1[i1] == s2[i2]:
        cosubseq += (s1[i1])
        i1 += 1

    i2 += 1
# Step 2. add longer remaining seq.
print(cosubseq)
print(max(len(s1), len(s2)) - len(cosubseq))