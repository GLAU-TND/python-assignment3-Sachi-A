def isPalindrome(string,k):
    list01 = []
    for i in string:
        if i not in list01:
            list01.append(i)
        else:
            list01.remove(i)
    if len(list01) - k <= 1:
        print(True)
    else:
        print(False)


str_in =input()
k_in=int(input())
isPalindrome(str_in,k_in)