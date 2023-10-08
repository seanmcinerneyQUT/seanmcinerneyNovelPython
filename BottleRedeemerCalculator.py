# Bottle Redeemer Calculator

# This script calculates how much money a person attempting to redeem recyclable bottles and cans will receive:
# INPUTS:
#   number of bottle and cans collected
#   if there is a place you can return the bottles and cans

import sys

print(f'Welcome to the Bottle Redeemer Calculator!')

responseA = str(input('Would like to calculate the money you will make? Type Y for Yes, N for No. Any other key will exit.'))
if responseA != 'Y' and responseA != 'N':
    print(f'Have a nice day!')
    sys.exit()
elif responseA == 'N':
    responseB = str(input('Are you sure you want to exit? Type Y for Yes, anything else for No'))
    if responseB == 'Y':
        print('Thank you for your time!')
        sys.exit()
    print(f'So you want to calculate the money you will make from returning bottles?')
    responseC = str(input(f'Type Y for Yes, N for No. Any other key will exit.'))
    if responseC != 'Y':
        print(f'That is okay! Thank you for your time!')
        sys.exit()

bottleNumber = int(input('How many bottles and cans are you going to return?'))
responseE = str(input('Do you have a place to return it to? Type Y for Yes, anything else for No.'))

if responseE != 'Y':
    print(f'If you are able to find somewhere to return it to, you would receive ${bottleNumber*0.1}0. Good luck!')
else:
    print(f'Great! Once you return the bottles and cans, you will receive ${bottleNumber*0.1}0. Well done!')



