""" Name: Isaac A. Olmedo
    Date: 18 Aug 2021
    File Name: lab1_Olmedo_Isaac
    This is a voter registration
    application for Lab 1.
"""
import sys

WELCOME = str("*********************************************************\n"
              "Welcome to the Python Voter Registration Application.")
print(str(WELCOME))
CONTINUE_STATEMENT = str(input("Do you want to continue with Voter Registration?: "))
TRUE = str("yes")
FALSE = str("no")
while CONTINUE_STATEMENT == TRUE:
    VOTER_FIRST_NAME = str(input("What is your first name?: "))
    CONTINUE_STATEMENT = str(input("Do you want to continue with Voter Registration?: "))
    if CONTINUE_STATEMENT == TRUE:
        VOTER_LAST_NAME = str(input("What is your last name?: "))
        CONTINUE_STATEMENT = str(input("Do you want to continue with Voter Registration?: "))
    if CONTINUE_STATEMENT == TRUE:
        VOTER_AGE = int(input("What is your age?: "))
        while VOTER_AGE:
            if VOTER_AGE > 120:
                print("This age is not reasonable, please re-enter an age between 18 and 120: ")
                VOTER_AGE = int(input("What is your age?: "))
            if VOTER_AGE < 18:
                print("You are not old enough to vote, please try again when"
                      " you turn 18 years old!")
                print("Thanks for trying the Voter Registration Application.")
                sys.exit()
            else:
                CONTINUE_STATEMENT = str(input("Do you want to continue with Voter"
                                               " Registration?: "))
                break
    if CONTINUE_STATEMENT == TRUE:
        VOTER_CITIZENSHIP = str(input("Are you a U.S. Citizen? (Enter 'yes' or 'no'): "))
        if VOTER_CITIZENSHIP == FALSE:
            print("You must be a U.S. Citizen to vote!")
            print("Thanks for trying the Voter Registration Application.")
            sys.exit()
        CONTINUE_STATEMENT = str(input("Do you want to continue with "
                                       "Voter Registration?: "))
    if CONTINUE_STATEMENT == TRUE:
        VOTER_STATE = str(input("What State do you live in? "
                                "(State Abbreviation 'ALL CAPS'): "))
        REGISTERED_STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
                             "DE", "FL", "GA", "HI", "ID", "IL",
                             "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                             "MA", "MI", "MN", "MS", "MO",
                             "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
                             "NC", "ND", "OH", "OK", "OR", "PA",
                             "RI", "SC", "SD", "TN", "TX", "UT", "VT",
                             "VA", "WA", "WV", "WI", "WY"]
        while VOTER_STATE:
            if VOTER_STATE in REGISTERED_STATES:
                break
            if VOTER_STATE not in REGISTERED_STATES:
                print("Please enter a valid State.")
                VOTER_STATE = str(input("What State do you live in?"
                                        "(State Abbreviation 'ALL CAPS'): "))
            else:
                CONTINUE_STATEMENT = str(input("Do you want to continue with "
                                               "Voter Registration?: "))
                break
    if CONTINUE_STATEMENT == TRUE:
        VOTER_ZIP = input("What is your 5 digit zip code?: ")
        while VOTER_ZIP:
            if len(VOTER_ZIP) != 5:
                print("Invalid zip code!")
                VOTER_ZIP = input("What is your 5 digit "
                                  "zip code?: ")
            if len(VOTER_ZIP) == 5:
                print("Thanks for registering to vote. Here "
                      "is the information we received: "
                      "\nName (First Last):", VOTER_FIRST_NAME, VOTER_LAST_NAME,
                      "\nAge:", VOTER_AGE, "\nU.S. Citizen:", VOTER_CITIZENSHIP +
                      "\nState:", VOTER_STATE + "\nZipcode:", VOTER_ZIP,
                      "\nThanks for trying the Voter "
                      "Registration Application."
                      "\nYour voter registration card should "
                      "be shipped within 3 weeks.")
                END_LINE = str("******************************"
                               "****************************************")
                print(END_LINE)
            sys.exit()
    else:
        if CONTINUE_STATEMENT == FALSE:
            print("Thanks for trying the Voter Registration Application.")
            sys.exit()
    break
else:
    if CONTINUE_STATEMENT == FALSE:
        print("Thanks for trying the Voter Registration Application.")
        sys.exit()
