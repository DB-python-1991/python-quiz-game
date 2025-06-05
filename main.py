# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 11:37:41 2025

@author: Dhara
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from quiz import run_quiz

print("🎮 Welcome to the Python Quiz Game!")
run_quiz()