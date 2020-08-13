#!/usr/bin/python3

# local requirements
from lib.SimulationException import *


# the class
class Simulation:

    # constructor
    def __init__(self, configuration, logger):

        # store the arguments
        self.config = configuration
        self.logger = logger


    # the main method
    def run(self):
        self.logger.error("Not yet implemented!")
