#!/usr/bin/env python3

DESIREDCONCENTRATION = 0.3  # this value is a percentage, decimal wise, it would be 0.003
CHEMICALNAME = 'Povidone-Iodine'  #placeholder


def concentration_calc(cPVI: int, desired_volume : int) -> float:
    return (DESIREDCONCENTRATION*desired_volume)/cPVI


def convert_ml_oz(milliters: float) -> float:
    return milliters/29.574


def convert_oz_ml(ounces: float) -> float:
    return 29.574*ounces


def getNonZeroValue(uInput):
        while True:
        try:
            conc_pct = float(input('Please input your desired concentration percentage as a positive decimal '
                                   '(ex. \'28.6\').\n'))
            if conc_pct > 0:
                return conc_pct
            else:
                print('Please try again. Input a positive number.')

        except ValueError:
            print('The value you entered could not be recognized as a percentage. '
                  'Please use the same formatting as the example.')
    return 33


def checkForYesorNo():
    boolMessage = ('Yes or no?\n')
    boolValid = ['y', 'yes', 'n', 'no']
    boolInput = ""
    while boolInput not in boolValid:
        boolInput = input(boolMessage).lower()
    if 'y' in boolInput:
        boolInput = True
    else:
        boolInput = False
    return boolInput
    pass


def get_ml_or_oz() -> str:

    greeting = '''Hello!
                  Will you be doing your calculations in fluid ounces or ml?
                  Please type your response and then hit enter.
                  Mililiters are recommended.
                  1) Mililiters
                  2) Ounces
                  : '''
    valid_inputs = ['1', '2']
    reply = ""
    while reply not in valid_inputs:
        reply = input(greeting).lower()
    return reply

def getConcentration() -> int:
    concMessage = f'''Input the percent concentration of your {CHEMICALNAME}
                      solution
                      (for example, if it is listed as 10%, input just "10") '''
    return getNonZeroValue(concMessage)


def main():
    get_ml_or_oz()
    userConcentration = getConcentration()
    print(f"The program will interpret this as a {userConcentration}% solution is this correct?")

    # if yes, continue, if no, loop above line of code
    userDesiredVolume = int(input(f'input the amount of water you will be using in ml: '))
    print(f'The program will now calculate the amount of {CHEMICALNAME} concentrate at {userConcentration}%, you need to add to your {userDesiredVolume} of water...')
    print(f"{concentration_calc(userConcentration, userDesiredVolume)} ml")


if __name__ == "__main__":
    main()
