def longestCommonPrefix(strs):
    strs.sort()
    result = 0
    n = 0

    if len(strs) < 2:
        return strs[0]

    while True:
        if len(strs[0]) > n and len(strs[-1]) > n:
            if strs[0][n] == strs[-1][n]:
                n += 1
                result += 1
                continue
            else:
                break
        else:
            break
    
    if result < 1:
        return ''
    else:
        return strs[0][:n]
