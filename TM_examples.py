# Carnegie Mellon University 15-251 Great Ideas in Theoretical Computer Science
# Homework 3 Programming Assignment
# Starter code for TM_examples
# TODO Define a TuringMachine object that solves the given problems

from TM_classes import State, TuringMachine

def TM1():
    """Define and then return a Turing Machine with the following behavior:

    Input alphabet is {0, 1}.
    The tape alphabet is a superset of {0, 1, _}, where _ is the blank symbol.
    (It is up to you if you want the tape alphabet to contain more symbols.)
    If the input has equal number of 0s and 1s, accept.
    Otherwise, reject.
    """
    return TuringMachine(
        {
            State("checkFirst"),
            State("find0"),
            State("find1"),
            State("goFirst"),
            State("qacc"),
            State("qrej")},
        ['0', '1'],
        ['0', '1', '_', 'X'],
        {
            # X marks an eliminated symbol.
            (State("checkFirst"), '1'): (State("find0"), 'X', 'R'),
            (State("checkFirst"), '0'): (State("find1"), 'X', 'R'),
            (State("checkFirst"), 'X'): (State("checkFirst"), 'X', 'R'),
            (State("checkFirst"), '_'): (State("qacc"), '_', 'R'),

            (State("find0"), '1'): (State("find0"), '1', 'R'),
            (State("find0"), '0'): (State("goFirst"), 'X', 'L'),
            (State("find0"), 'X'): (State("find0"), 'X', 'R'),
            (State("find0"), '_'): (State("qrej"), '_', 'L'),

            (State("find1"), '1'): (State("goFirst"), 'X', 'L'),
            (State("find1"), '0'): (State("find1"), '0', 'R'),
            (State("find1"), 'X'): (State("find1"), 'X', 'R'),
            (State("find1"), '_'): (State("qrej"), '_', 'L'),

            (State("goFirst"), '1'): (State("goFirst"), '1', 'L'),
            (State("goFirst"), '0'): (State("goFirst"), '0', 'L'),
            (State("goFirst"), 'X'): (State("goFirst"), 'X', 'L'),
            (State("goFirst"), '_'): (State("checkFirst"), '_', 'R'),
        },
        State("checkFirst"),
        State("qacc"),
        State("qrej"),
    )

def TM2():
    """Define and then return a Turing Machine with the following behavior:

    Input alphabet is {0, 1}.
    The tape alphabet is a superset of {0, 1, _}, where _ is the blank symbol.
    (It is up to you if you want the tape alphabet to contain more symbols.)
    If the input does not correspond to the usual binary encoding of a natural number,
    output the empty string.
    Otherwise, output x + 1 in binary, where x is the input number.
    """
    return TuringMachine(
        {
            State("checkFirst"),
            State("checkSecond"),
            State("moveR"),
            State("add1"),
            State("done"),
            State("qacc"),
            State("qrej"),
            State("clear"),
            State("goFirst")},
        ['0', '1'],
        ['0', '1', '_'],
        {
            (State("checkFirst"), '1'): (State("moveR"), '1', 'R'),
            (State("checkFirst"), '0'): (State("checkSecond"), '0', 'R'),
            (State("checkFirst"), '_'): (State("qrej"), '_', 'L'),

            (State("checkSecond"), '1'): (State("goFirst"), '1', 'L'),
            (State("checkSecond"), '0'): (State("goFirst"), '0', 'L'),
            (State("checkSecond"), '_'): (State("add1"), '_', 'L'),

            (State("moveR"), '1'): (State("moveR"), '1', 'R'),
            (State("moveR"), '0'): (State("moveR"), '0', 'R'),
            (State("moveR"), '_'): (State("add1"), '_', 'L'),

            (State("add1"), '1'): (State("add1"), '0', 'L'),
            (State("add1"), '0'): (State("done"), '1', 'L'),
            (State("add1"), '_'): (State("done"), '1', 'L'),

            (State("done"), '1'): (State("done"), '1', 'L'),
            (State("done"), '0'): (State("done"), '0', 'L'),
            (State("done"), '_'): (State("qacc"), '_', 'R'),

            (State("clear"), '1'): (State("clear"), '_', 'R'),
            (State("clear"), '0'): (State("clear"), '_', 'R'),
            (State("clear"), '_'): (State("qrej"), '_', 'R'),

            (State("goFirst"), '1'): (State("goFirst"), '1', 'L'),
            (State("goFirst"), '0'): (State("goFirst"), '0', 'L'),
            (State("goFirst"), '_'): (State("clear"), '_', 'R'),
        },
        State("checkFirst"),
        State("qacc"),
        State("qrej"),
    )

def Bonus():
    """Define and then return a Turing Machine with the following behavior: (BONUS)

    Input alphabet is {0, 1, $}.
    The tape alphabet is a superset of {0, 1, $, _}, where _ is the blank symbol.
    (It is up to you if you want the tape alphabet to contain more symbols.)
    If the input is not of form x$y where x and y are binary encodings of natural numbers,
    output the empty string.
    Otherwise, output the sum of x and y in binary.
    """
    return TuringMachine(
        {
            State("checkFirstX"),
            State("checkSecondX"),
            State("moveX"),
            State("checkFirstY"),
            State("checkSecondY"),
            State("moveR"),
            State("sub1"),
            State("goDollar"),
            State("add1"),
            State("moveY"),
            State("checkZero"),
            State("clearY"),
            State("done"),
            State("goFirst"),
            State("clear"),
            State("qacc"),
            State("qrej")},
        ['0', '1', '$'],
        ['0', '1', '$', '_'],
        {
            # Check that both numbers are nonempty and have no leading zeros.
            (State("checkFirstX"), '1'): (State("moveX"), '1', 'R'),
            (State("checkFirstX"), '0'): (State("checkSecondX"), '0', 'R'),
            (State("checkFirstX"), '$'): (State("goFirst"), '$', 'L'),
            (State("checkFirstX"), '_'): (State("qrej"), '_', 'L'),

            (State("checkSecondX"), '1'): (State("goFirst"), '1', 'L'),
            (State("checkSecondX"), '0'): (State("goFirst"), '0', 'L'),
            (State("checkSecondX"), '$'): (State("checkFirstY"), '$', 'R'),
            (State("checkSecondX"), '_'): (State("goFirst"), '_', 'L'),

            (State("moveX"), '1'): (State("moveX"), '1', 'R'),
            (State("moveX"), '0'): (State("moveX"), '0', 'R'),
            (State("moveX"), '$'): (State("checkFirstY"), '$', 'R'),
            (State("moveX"), '_'): (State("goFirst"), '_', 'L'),

            (State("checkFirstY"), '1'): (State("moveR"), '1', 'R'),
            (State("checkFirstY"), '0'): (State("checkSecondY"), '0', 'R'),
            (State("checkFirstY"), '$'): (State("goFirst"), '$', 'L'),
            (State("checkFirstY"), '_'): (State("goFirst"), '_', 'L'),

            (State("checkSecondY"), '1'): (State("goFirst"), '1', 'L'),
            (State("checkSecondY"), '0'): (State("goFirst"), '0', 'L'),
            (State("checkSecondY"), '$'): (State("goFirst"), '$', 'L'),
            (State("checkSecondY"), '_'): (State("clearY"), '_', 'L'),

            # Move to the end of a nonzero y, then subtract one with borrowing.
            (State("moveR"), '1'): (State("moveR"), '1', 'R'),
            (State("moveR"), '0'): (State("moveR"), '0', 'R'),
            (State("moveR"), '$'): (State("goFirst"), '$', 'L'),
            (State("moveR"), '_'): (State("sub1"), '_', 'L'),

            (State("sub1"), '1'): (State("goDollar"), '0', 'L'),
            (State("sub1"), '0'): (State("sub1"), '1', 'L'),
            (State("sub1"), '$'): (State("goFirst"), '$', 'L'),
            (State("sub1"), '_'): (State("goFirst"), '_', 'L'),

            (State("goDollar"), '1'): (State("goDollar"), '1', 'L'),
            (State("goDollar"), '0'): (State("goDollar"), '0', 'L'),
            (State("goDollar"), '$'): (State("add1"), '$', 'L'),
            (State("goDollar"), '_'): (State("goFirst"), '_', 'L'),

            # Add one to x, allowing a carry to extend it to the left.
            (State("add1"), '1'): (State("add1"), '0', 'L'),
            (State("add1"), '0'): (State("moveY"), '1', 'R'),
            (State("add1"), '$'): (State("goFirst"), '$', 'L'),
            (State("add1"), '_'): (State("moveY"), '1', 'R'),

            (State("moveY"), '1'): (State("moveY"), '1', 'R'),
            (State("moveY"), '0'): (State("moveY"), '0', 'R'),
            (State("moveY"), '$'): (State("checkZero"), '$', 'R'),
            (State("moveY"), '_'): (State("goFirst"), '_', 'L'),

            # Leading zeros in y are kept during subtraction.
            (State("checkZero"), '1'): (State("moveR"), '1', 'R'),
            (State("checkZero"), '0'): (State("checkZero"), '0', 'R'),
            (State("checkZero"), '$'): (State("goFirst"), '$', 'L'),
            (State("checkZero"), '_'): (State("clearY"), '_', 'L'),

            # Once y is zero, erase y and the separator, leaving only the sum.
            (State("clearY"), '1'): (State("clearY"), '_', 'L'),
            (State("clearY"), '0'): (State("clearY"), '_', 'L'),
            (State("clearY"), '$'): (State("done"), '_', 'L'),
            (State("clearY"), '_'): (State("goFirst"), '_', 'L'),

            (State("done"), '1'): (State("done"), '1', 'L'),
            (State("done"), '0'): (State("done"), '0', 'L'),
            (State("done"), '$'): (State("goFirst"), '$', 'L'),
            (State("done"), '_'): (State("qacc"), '_', 'R'),

            # Invalid inputs are erased completely.
            (State("goFirst"), '1'): (State("goFirst"), '1', 'L'),
            (State("goFirst"), '0'): (State("goFirst"), '0', 'L'),
            (State("goFirst"), '$'): (State("goFirst"), '$', 'L'),
            (State("goFirst"), '_'): (State("clear"), '_', 'R'),

            (State("clear"), '1'): (State("clear"), '_', 'R'),
            (State("clear"), '0'): (State("clear"), '_', 'R'),
            (State("clear"), '$'): (State("clear"), '_', 'R'),
            (State("clear"), '_'): (State("qrej"), '_', 'R'),
        },
        State("checkFirstX"),
        State("qacc"),
        State("qrej"),
    )
