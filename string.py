#name = "venkataramana"
#print(name.lower())
#port = "8888"
#arm = "arm:iam::123456789012:role/vvr"
#print(arm.split("/")[0])

#string1 = "Hello, World!"
#string2 = "Python is awesome."

#result = string1 + " " + string2
#print(result)
#length = len(result)
#print("Length of the concatenated string:", length)
#print(result.upper())
#print(result.lower())

# num1 = 5.8
# num2 = 3.0
# sum_result = num1 + num2
'''print("Sum of", num1, "and", num2, "is:", sum_result)

sub_result = num1 - num2
print("Subtraction of", num1, "and", num2, "is:", sub_result)

mult_result = num1 * num2
print("Multiplication of", num1, "and", num2, "is:", mult_result)   

div_result = num1 / num2
print("Division of", num1, "and", num2, "is:", div_result)      

round_result = round(num1, 2)

print("Rounded value of", num1, "is:", round_result)

num3 = -10 

abs_result = abs(num3)
print("Absolute value of", num3, "is:", abs_result)'''

'''text = "Python is awesome"
new_text = text.replace("awe", "great")
print("Modified text:", new_text)'''

import re

'''text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found") '''


'''import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
'''

'''import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)'''