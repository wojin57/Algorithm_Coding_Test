str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)
edit_dist = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    edit_dist[i][0] = i
for j in range(1, len2 + 1):
    edit_dist[0][j] = j

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            edit_dist[i][j] = edit_dist[i - 1][j - 1]
        else:
            edit_dist[i][j] = 1 + min(edit_dist[i][j - 1], edit_dist[i - 1][j], edit_dist[i - 1][j - 1])

print(edit_dist[len1][len2])
