'''
 * User: Noman Kabeer
 * Date: 30-Oct-2019
 * Time: 1:12 AM
 * Print the longest word from string
'''

def LongestWord(sen):
    longestword = None
    longestwordcount = 0
    words = sen.split(' ')
    totalwords = len(words)
    for i in range(totalwords):
        if (longestwordcount < len(words[i])):
            longestwordcount = len(words[i])
            longestword = words[i]
    return longestword


print(LongestWord('I am a php programmer'))
print(LongestWord('longest word will print in this string'))
