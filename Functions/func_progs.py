# we are given two lists of numbers and we need to find total of each of these list.
tom_exp_list = [100,200,4800,900]
joe_exp_list = [1000,780,888,1098]

total = 0
for item in tom_exp_list:
    total = item + total
print("Toms exp list:", total)

total = 0
for item in joe_exp_list:
    total = item + total
print("Joe's exp list:",total)



# using functions :
def calculate_total_exp(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp_list = [100, 200, 4800, 900]
joe_exp_list = [1000, 780, 888, 1098]

toms_total = calculate_total_exp(tom_exp_list)
joes_total = calculate_total_exp(joe_exp_list)

print("Tom's total expenses:", toms_total)
print("Joe's total expenses:", joes_total)


def sum(a,b):
 total = a + b
 return total

n = sum(5,6)
print("Total:", n)