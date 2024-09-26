#!/usr/bin/env python3
# from typing import Tuple


DESIREDCONCENTRATION = 0.3  # this value is a percentage, decimal wise, it would be 0.003
CHEMICALNAME = 'Povidone-Iodine'  # placeholder

CONCENTRATEMessage = f'''
                  Input the percent concentration of your {CHEMICALNAME}
                  solution
                  (for example, if it is listed as 10%, input just "10")
                  : '''

FINALConcentrationMessage = f'''
                  Input the desired percent concentration of your {CHEMICALNAME}
                  solution after dilution.
                  (for example, if it is listed as 10%, input just "10")
                  : '''


def concentration_calc(cPVI: float, desired_volume: float, desiredConcentration: float) -> float:
    """
    Calculate the final concentration of the solutions.

    This function calculates the final concentration of a solution
    based on a current
    """
    # return ((DESIREDCONCENTRATION*desired_volume)/cPVI , mode)
    return (desiredConcentration*desired_volume)/cPVI


def convert_ml_oz(milliters: float) -> float:
    """Convert an input in milliliters to ounces."""
    return milliters/29.574


def convert_oz_ml(ounces: float) -> float:
    """Convert an input in ounces to milliliters."""
    return 29.574*ounces


def getNonZeroValue(message: str) -> float:
    """
    Grab a positive value from the user, while prompting them a custom message.

    Only allows a positive number to be returned, and reprompts the user.
    """
    while True:
        try:
            conc_pct = float(input(message))
            if conc_pct > 0:
                return conc_pct
            else:
                print('Please try again. Input a positive number.')

        except ValueError:
            print('The value you entered could not be recognized as a number. '
                  'Please use the same formatting as the example.')


def checkForYesorNo():
    """
    Ask user for a yes or no, returns True if yes.

    Checks for yes or no, and only give a true value
    """
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


def get_ml_or_oz() -> str:
    """
    Ask user for ml or oz.

    Greets user, and asks if the user will be doing calculations in
    millilters or ounces. It then asks for a "1" of "2" as input.
    It is not case sensitive. If the user says 1, then it returns 'ml'.
    If the user says 2, then it returns 'oz'
    If the user gives any other input, it reprompts, only returning "ml"/"oz".
    """
    greeting = '''
                  Hello!
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
    if reply == '1':
        return 'ml'
    else:
        return 'oz'


def getConcentration(concMessage) -> float:
    """Get a positive value to be used as an original concentration percentage."""
    CONCENTRATEMessage = f'''
                  Input the percent concentration of your {CHEMICALNAME}
                  solution
                  (for example, if it is listed as 10%, input just "10")
                  : '''
    return getNonZeroValue(concMessage)


def display_procedure(userConcentration, desiredCon, desiredVolume, unit) -> None:
    """Print procedure for user to follow based on their parameters.

    """
    displayMessage = f"""
                  The program will now calculate the amount of {CHEMICALNAME} concentrate at {userConcentration}%,
                  you need to add to your {desiredVolume} {unit} of water to acheive a {desiredCon}% concentration..."""
    print(displayMessage)


def runCalc():
    unitMode = get_ml_or_oz()

    while True:
        # grab the concentrate concentration (store bought)
        userConcentration = getConcentration(CONCENTRATEMessage)
        print(f"The program will interpret this as a {userConcentration}% solution is this correct?")

        if checkForYesorNo():
            break
        else:
            print('Sorry! lets try again\n')
            continue

    while True:
        # grab the desired final concentration
        finalConcentration = getConcentration(FINALConcentrationMessage)
        print(f"The program will interpret this as a {finalConcentration}% solution, is this correct?")

        if checkForYesorNo():
            break
        else:
            print('Sorry! lets try again\n')
            continue

    userDesiredVolume = getNonZeroValue(f'input the amount of water you will be using in {unitMode}: ')

    display_procedure(userConcentration, finalConcentration, userDesiredVolume, unitMode)

    print(f"{concentration_calc(userConcentration, userDesiredVolume, finalConcentration)} {unitMode}")


def main():
    runCalc()


if __name__ == "__main__":
    main()
