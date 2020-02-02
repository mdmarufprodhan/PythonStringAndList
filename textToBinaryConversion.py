
test_str = "Rangpur"
print("The Orginal String :" + str(test_str))
res = ''.join(format(ord(i), 'b') for i in test_str)

print("The String after conversion: " +str(res))