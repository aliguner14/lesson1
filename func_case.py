import random
def is_more_then_five(number):
    if number > 5:
        print('more 5')
    else:
        print('les 5')
rand_num = random.randint(1, 10)
is_more_then_five(rand_num)
print(rand_num)
x = 0
while x < 10:
    print(x)
x = x + 1