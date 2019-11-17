def isPalindrome(string,k):
    temp= []
    for i in string:
        if i not in temp:
            temp.append(i)
        else:
            temp.remove(i)
    if len() - k <= 1:
        print(True)
    else:
        print(False)


str =input()
k=int(input())
isPalindrome(str,k)