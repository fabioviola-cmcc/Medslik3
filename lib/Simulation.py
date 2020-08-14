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

        # store input files
        currentsTFiles = []
        currentsUFiles = []
        currentsVFiles = []
        windsFiles = []
        bathymetryFile = []
        coastlineFile = []


    # read input currents file
    def readCurrentFile(self, filename):
        pass

    
    # read input wind file
    def readWindFile(self, filename):
        pass


    # read bathymetry file
    def readBathymetryFile(self, filename):
        pass


    # read coastline file
    def readCoastlineFile(self, filename):
        pass
    
        
    # the main method
    def run(self):

        # read input files


        # 
        self.logger.error("Not yet implemented!")
