# Carnegie Mellon University 15-251 Great Ideas in Theoretical Computer Science
# Homework 3 Programming Assignment
# Defines classes: State, Configuration, Result, and TuringMachine

import enum

class State:
    """
    We define the State of a TM as a string representing its name, which is a string type in Python.
    We consider two State objects to be equal if their names are the same.
    ex)
        q0 = State("q0")
        q1 = State("q1")
        q0' = State("q0")
        q0 == q0' # evaluates to True
        q0 == q1 # evaluates to False
    """
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, State):
            return self.name == other.name
        return False

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.__repr__())

class Configuration:
    """
    A configuration consists of (u, q, v) where
        - q: current state
        - u: tape alphabet string on the tape left of the current tape head
        - v: tape alphabet string on the tape right of the current tape head (including current tape head location)
    Refer to the textbook for the exact definition.
    """
    def __init__(self, u, q, v):
        self.u = u
        self.q = q
        self.v = v

    def __eq__(self, other):
        if isinstance(other, Configuration):
            return self.u == other.u and self.q == other.q and self.v == other.v
        return False

    def __repr__(self):
        return "(" + self.u + "," + self.q.name + "," + self.v + ")"

    def __hash__(self):
        return hash(self.__repr__())

class Result(enum.Enum):
    ACCEPT = enum.auto()
    REJECT = enum.auto()
    UNDETERMINED = enum.auto()

class TuringMachine:
    """
    A Turing Machine can be defined with the 7-tuple (Q, Sigma, Gamma, delta, q0, q_acc, q_rej)
        - Q: set of states; we represent this using a Python set containing objects of class State
        - Sigma: input alphabet; we represent this using a Python set containing strings (which will be of length 1 corresponding to a symbol)
        - Gamma: tape alphabet; we represent this using a Python set containing strings (again, of length 1, i.e. a symbol) where '_' is the blank symbol
        - delta: transition function; we represent this using a Python dictionary mapping a tuple (State, str) as key to tuple (State, str, str) as value
            - Key (q, s) represents reading tape symbol s from state q
            - Value (q', s', d) represents transitioning to state q', writing tape symbol s', and moving in direction d ('L' or 'R')
        - q0: initial state; we represent this using class State
        - q_acc: accepting state; we represent this using class State
        - q_rej: rejecting state; we represent this using class State
    """
    def __init__(self, Q, Sigma, Gamma, delta, q0, q_acc, q_rej):
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma
        self.delta = delta
        self.q0 = q0
        self.q_acc = q_acc
        self.q_rej = q_rej
