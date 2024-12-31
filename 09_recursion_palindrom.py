def palindrome(word, index):
    mid_index = len(word)//2
    left = word[index:mid_index]
    right = word[mid_index+1:]
    if left == right[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))