#!/usr/bin/python3

# global requirements
import os

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


    # check input files
    def checkInputFiles(self):

        errors = False
        missingFiles = []
        
        for f in self.config.currentsTFiles + self.config.currentsUFiles + self.config.currentsVFiles:
            if not(os.path.isfile(f)):
                self.logger.error("Missing currents file %s" % f)
                missingFiles.append(f)
                errors = True
                
        for f in self.config.windsFiles:
            if not(os.path.isfile(f)):
                self.logger.error("Missing winds file %s" % f)
                missingFiles.append(f)
                errors = True
                
        if not(os.path.isfile(self.config.coastlineFile)):
            self.logger.error("Missing coastline file %s" % self.config.coastlineFile)
            missingFiles.append(self.config.coastlineFile)
            errors = True

        if not(os.path.isfile(self.config.bathymetryFile)):
            self.logger.error("Missing bathymetry file %s" % self.config.bathymetryFile)
            missingFiles.append(self.config.bathymetryFile)
            errors = True

        if errors:
            raise SimulationException("Missing input files: %s" % ",".join(missingFiles))
        
    
        
    # the main method
    def run(self):

        # debug
        self.logger.error("Not yet implemented!")
