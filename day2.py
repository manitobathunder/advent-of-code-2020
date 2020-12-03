import re
with open('twoinput.txt') as f:
	content = f.readlines()

#Organizing and cleaning our passwords and policies:
inputlist = [x.strip() for x in content]
splitlist = [x.split(':') for x in inputlist]
keys = [x[0] for x in splitlist]
values = [x[1] for x in splitlist]
split_keys = [x.split(' ') for x in keys]
nums = [x[0] for x in split_keys]
low_high = [x.split('-') for x in nums]

#Password Policies and Password inputs for checking:
low = [x[0] for x in low_high]
high = [x[1] for x in low_high]
chars = [x[1] for x in split_keys]
passwords = [x.strip() for x in values]

#Check passwords:
def verify_pass_count(passwords):
	counter = 0
	for i in range(len(passwords)):
		char_count = 0
		for letter in passwords[i]:
			if chars[i] == letter:
				char_count += 1
		if char_count >= int(low[i]) and char_count <= int(high[i]):
			counter += 1
	return counter

def new_verify_pass_count(passwords):
	counter = 0
	for i in range(len(passwords)):
		char_count = 0
		if (chars[i] == passwords[i][int(low[i])-1] and not chars[i] == passwords[i][int(high[i])-1]) or (not chars[i] == passwords[i][int(low[i])-1] and chars[i] == passwords[i][int(high[i])-1]):
			char_count += 1
		if char_count == 1:
			counter += 1
	return counter

verified_old = verify_pass_count(passwords)
verified_new = new_verify_pass_count(passwords)

print('The amount of passwords verified under the old policy is {}, however, the amount of verified passwords under the new standards are {}.'.format(verified_old, verified_new))