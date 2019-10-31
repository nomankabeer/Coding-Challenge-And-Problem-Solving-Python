'''
 * User: Noman Kabeer
 * Date: 30-Oct-2019
 * Time: 1:12 AM
 * Palindrome string
'''


def PalindromeString(sen):
    stringLength = len(sen) - 1
    stringLengthCount = stringLength
    ans = "Given String is Palindrome"
    for i in range(stringLength):
        if (sen[i] != sen[stringLengthCount]):
            ans = "Not Palindrome"
            break
        stringLengthCount = stringLengthCount - 1
    return ans


print(PalindromeString('abbcbba'))