#!/usr/bin/env python3.10
# from typing import Tuple


DESIREDCONCENTRATION = 0.3  # this value is a percentage, decimal wise, it would be 0.003
CHEMICALNAME = 'Povidone-Iodine'  # placeholder


def concentration_calc(stockConcentration: float, desired_volume: float, desiredConcentration: float) -> float:
    """
    Calculate the final concentration of the solutions.

    This function calculates the final concentration of a solution
    based on a current
    """

    return (desiredConcentration*desired_volume)/stockConcentration


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


def getConcentration(concMessage):
    """
    Determine the concentration of stock solution or final solution.

    input "ogConcentrate" for stock conc message
    input "finalConcentration" for final conc message
    """
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
    while True:

        match concMessage:
            case "ogConcentrate":
                concentrate = getNonZeroValue(CONCENTRATEMessage)

            case "finalConcentration":
                concentrate = getNonZeroValue(FINALConcentrationMessage)

            case _:
                print("Error, getConcentration() received an unintended value.")

        print(f'The program will interpret this as a {concentrate}% solution, is this correct?')

        if checkForYesorNo():
            break
        else:
            print("Sorry! Let's try again\n")

    return concentrate


def display_procedure(stockConcentration, desiredCon, desiredVolume, unit):
    """Print procedure for user to follow based on their parameters.
    """
    displayMessage = f"""
                  The program will now calculate the amount of {CHEMICALNAME} concentrate at {stockConcentration}%,
                  you need to add to your {desiredVolume} {unit} of water to acheive a {desiredCon}% concentration..."""
    print(displayMessage)


def runCalc():
    """Runs the full calulation of one stock solution to desired solution.
    """
    unitMode = get_ml_or_oz()

    # grab the stock concentration (store bought)
    userConcentration = getConcentration("ogConcentrate")

    # grab the desired final concentration
    finalConcentration = getConcentration("finalConcentration")

    # grab the amount of solvent
    userDesiredVolume = getNonZeroValue(f'input the amount of water you will be using in {unitMode}: ')

    # print final amount
    display_procedure(userConcentration, finalConcentration, userDesiredVolume, unitMode)

    additiveAmount = concentration_calc(userConcentration, userDesiredVolume, finalConcentration)

    match unitMode:
        case "ml":
            print(f"""
                {additiveAmount} {unitMode}
                or, you can add
                {convert_ml_oz(additiveAmount)} oz""")

        case "oz":
            print(f"""
                {additiveAmount} {unitMode}
                or, you can add
                {convert_oz_ml(additiveAmount)} ml""")

        case _:
            print("unit mode not determined")


def main():
    print("Welcome to the concentration calculator!!!")
    runCalc()


if __name__ == "__main__":
    main()
