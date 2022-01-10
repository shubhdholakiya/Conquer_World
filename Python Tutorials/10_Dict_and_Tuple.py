result = {"anand": {"fs":9.2, "ss": 9.5}, "dev": 8.9, "jay": 8.5}

# print(result["dev"])

result["vishnu"] = 8.4

# print(result["anand"]["ss"])

del result["anand"]
# print(result)

dev_result = result.get("anand")
# print(dev_result)

result.clear()
# print(result)


# Tuples

vowel = ("a", "e", "i")
print(vowel)

# vowel[3] = "o" it won't work as tuple is immutable


fv, sv, tv = vowel
print(tv)




