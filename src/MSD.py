#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-05-29
# file: MSD.py
##########################################################################################

import math
import numpy as np

def MSD1d(x):
    '''
    Calculates the 1d MSD of a 1d trajectory vector x
    '''
    nTimepoints = len(x)
    nLagTimes = nTimepoints - 1
    lagIndices = np.arange(1, nLagTimes + 1, 1) # i.e. the indicies to account for
    # the different lagTimes
    msd = np.zeros((nLagTimes,))
    # loop through the different lag times (lag indices)
    counter = 0
    for lag in lagIndices:
        dx = x[0 + lag:] - x[0:-lag]
        msd[counter] = np.mean(np.square(dx))
        counter += 1
    return msd

    
    
    
    
    
    
        
        