#  * --------------------------------------------------------------------------
#  * File: SD_obs_modular.py
#  * ---------------------------------------------------------------------------
#  * Copyright (c) 2018 The University of Southern California.
#  * All rights reserved.
#  *
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions
#  * are met:
#  * 1. Redistributions of source code must retain the above copyright
#  *    notice, this list of conditions and the following disclaimer.
#  * 2. Redistributions in binary form must reproduce the above
#  *    copyright notice, this list of conditions and the following
#  *    disclaimer in the documentation and/or other materials provided
#  *    with the distribution.
#  * 3. All advertising materials mentioning features or use of this
#  *    software must display the following acknowledgement:
#  *       This product includes software developed by NSL at USC.
#  * 4. Neither the name of the University nor that of the Laboratory
#  *    may be used to endorse or promote products derived from this
#  *    software without specific prior written permission.
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
#  * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#  * PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS
#  * OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
#  * USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
#  * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
#  * SUCH DAMAGE.
#  *
#  * Developed by: Pradipta Ghosh
#  */

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

import sys
import z3 as z3

from sympy import Matrix


import scipy as sci
from scipy.io import loadmat
from scipy.linalg import expm

import timeit
import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


import scipy as sci
from scipy.io import loadmat
from scipy.linalg import expm

import sys

import numpy as np
from pprint import *
import cplex as cplex
from cplex.exceptions import CplexError

import random as rand

import signal
import itertools



def keyboard_handler(signal, frame):
    print 'You pressed Ctrl+C! --- Keep pressing more until you exit'
    sys.exit(0)

#***************************************************************************************************
#***************************************************************************************************
#
#         SCALABILITY Test - SMC
#
#***************************************************************************************************
#***************************************************************************************************


def connectivity_placement_adjacency_conn_subgraph(dim, router_count, 
            existing_sensor_count, comm_thr_dist, Y, scenario, strategy, subgraph = None):
    """[summary]
    
    [description]
    
    Parameters
    ----------
    dim : {[type]}
        [description]
    router_count : {[type]}
        [description]
    existing_sensor_count : {[type]}
        [description]
    comm_thr_dist : {[type]}
        [description]
    Y : {[type]}
        [description]
    scenario : {[type]}
        [description]
    strategy : {[type]}
        [description]
    subgraph : {[type]}, optional
        [description] (the default is None, which [default_description])
    
    Returns
    -------
    [type]
        [description]
    """
    


   
    
    return time_smt_SMC, sensor_location



def bla(temp):
    """[summary]
    
    [description]
    
    Parameters
    ----------
    temp : {[type]}
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    return None



