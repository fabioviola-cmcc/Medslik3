#!/usr/bin/python

class SimulationException(Exception):

    def __init__(self, message):
        
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # store the message
        self.message = message
