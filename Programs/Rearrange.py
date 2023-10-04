"""
Input: text = "Keep calm and code on"
Output: "On and keep calm code"
"""


def rearrange(str1):
    str1_lst = str1.split(" ")
    str1_lst = [i.lower() for i in str1_lst]
    str_lst = sorted(str1_lst, key=len)
    temp = " ".join(str_lst)
    return temp.capitalize()


s = "Keep calm and code on"
print(rearrange(s))
