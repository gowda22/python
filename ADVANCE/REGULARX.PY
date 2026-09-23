# import re
# text="python is power full"
# result=re.match(r'python',text)
# if result:
#     print("match found:",result.group())
# else:
#     print("no match")


# import re
# text=" the  in python"
# res=re.search(r'python',text)
# if res:
#     print("match found:",res.group())
# else:
#     print("not found")


#re.findall() all occurence
# import re
# text="i have 2 _ _apples @@@@#$% nd 3 banana"
# num=re.findall(r'\W+',text)
# if num:
#     print(f"yess found {num}")
# else:
#     print("not present")

import re

n = ["1234567890", "1234567890"]

for number in n:
    res = re.findall(r"^\d{10}$", number)

    if res:
        print(f"yes valid {res}")
    else:
        print("invalid")




