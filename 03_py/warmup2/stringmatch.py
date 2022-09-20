#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    count = 0
    if len(a) <= len(b):
        for n in range (0, len(a)-1):
            if a[n:n+2] == b[n:n+2]:
                count += 1
        return count
    else:
        for n in range (0, len(b)-1):
            if a[n:n+2] == b[n:n+2]:
                count += 1
        return count

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))