#!/usr/bin/env python3

DESIREDCONCENTRATION = 0.3 # this value is a percentage, decimal wise, it would be 0.003
CHEMICALNAME = 'Povidone-Iodine' #placeholder 

def concentration_calc(cPVI: int, desired_volume : int):
    return (DESIREDCONCENTRATION*desired_volume)/cPVI

def convert_ml_oz():
    pass

def convert_oz_ml():
    pass

def getNonZeroValue():
    pass

def checkForYesorNo():
    pass

def main():
    userConcentration = int(input(f'input the percent concentration of your {CHEMICALNAME} solution (for example, if it is listed as 10%, input just "10")'))
    print(f"The program will interpret this as a {userConcentration}% solution is this correct?")
    #if yes, continue, if no, loop above line of code
    userDesiredVolume = int(input(f'input the amount of water you will be using in ml: '))
    print(f'The program will now calculate the amount of {CHEMICALNAME} concentrate at {userConcentration}%, you need to add to your {userDesiredVolume} of water...')
    print(f"{concentration_calc(userConcentration, userDesiredVolume)} ml")



if __name__ == "__main__":
    main()
