#!/usr/bin/env python
#encoding: UTF-8

"""
This project is an agent-based simulation of interbank lending, to asses systemic risk. It is created in partial
fulfillment of the Capstone thesis project of the Amsterdam University College, towards the Bachelor of Science degree.
"""

__author__ = "Reinier Maat"
__copyright__ = "Copyright 2014, AUC Capstone Project Reinier Maat"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "reinier.maat@student.auc.nl"
__status__ = "Development"


import bank
import controller
import time


def main():
    """
    Runs the simulation with parameters set in the if-statement below.
    """

    clock = time.TimeStepper(STEPSIZE)

if __name__ == '__main__':
    STEPSIZE = 1
    NUMBEROFBANKS = 30
    main()