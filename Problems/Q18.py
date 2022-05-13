def reverse(s):
    result = ""
    for c in s:
        if c == "(":
            result += ")"
        else:
            result += "("

    return result
        

def correct(s):
    if not s:
        return s
    
    s = reverse(s[1:-1])
    return s


def is_valid(s):
    count = 0

    for c in s:
        if c == '(':
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                return False

    if count == 0:
        return True
    else:
        return False


def split(s):
    num_in = 0
    num_out = 0
    
    for i, c in enumerate(s):
        if c == "(":
            num_in += 1
        else:
            num_out += 1
        
        if num_in == num_out:
            return s[:i + 1], s[i + 1:]


def solution(s):
    if is_valid(s):
        return s
    
    answer = ""
    while not is_valid(s):
        u, v = split(s)
        if is_valid(u):
            answer += u
            s = v
        else:
            answer += ("(" + solution(v) +")")
            s = correct(u)

    answer += s
    return answer


if __name__ == '__main__':
    p = input()
    print(solution(p))
