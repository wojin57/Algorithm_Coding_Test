def slice_nwords(s, n):
    arr = []
    cur_idx = 0
    s_len = len(s)
    while cur_idx + n <= s_len:
        arr.append(s[cur_idx: cur_idx + n])
        cur_idx += n
    arr.append(s[cur_idx:])
    return arr
    

if __name__ == '__main__':
    s = input()
    shortest_zip_len = len(s)

    if len(s) == 1:
        shortest_zip_len = 1

    for length in range(1, len(s) // 2 + 1):
        words = slice_nwords(s, length)
        zip = ""
        prev = words[0]
        cnt = 1
        for i, word in enumerate(words[1:]):
            if word == prev:
                cnt += 1
            else:
                if cnt != 1:
                    zip += (str(cnt) + prev)
                else:
                    zip += prev
                prev = word
                cnt = 1

        if cnt != 1:
            zip += (str(cnt) + words[-1])
        else:
            zip += words[-1]
        
        if len(zip) < shortest_zip_len:
            shortest_zip_len = len(zip)
            print(zip)

    print(shortest_zip_len)
