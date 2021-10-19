#4-3
for number in range(1,21):
    print(number)

#4-5
nums = []
for num in range(1,100001):
    nums.append(num)
print(nums)
print(sum(nums))

#4-6
a = range(1,21,2)
for aa in a:
    print(aa)

#4-8
lifang = [value**3 for value in range(1,11)]
for i in lifang:
    print(i)

#
for i in lifang[2:]:
    print(i)

ali = lifang[:]

