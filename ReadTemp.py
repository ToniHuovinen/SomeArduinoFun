# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:56:05 2018

@author: Toni Huovinen
"""

from pyfirmata import Arduino, util
import time

# Determine the board and the COM-port it uses. You can check this through Arduino IDE
board = Arduino('COM5')

iterator = util.Iterator(board)
iterator.start()

    
userInput = input("Read temperature (y/n): ")
    
if userInput == "y":
    
    print("Please wait, reading temperature...")
    print("")
    # Read Analog Pin A0
    measureVoltage = board.get_pin('a:0:i')
        
    # Wait for 1 second for script to get the reading
    time.sleep(1.0)
        
    # Convert the measurement into degrees
    convertToDegree = (measureVoltage.read() * 5000.0 - 500.0) / 10.0
        
    print("Temperature in Celsius:")
    print(convertToDegree)
        
    board.exit()
        
elif userInput == "n":
    print("Shutting down..")
    board.exit()