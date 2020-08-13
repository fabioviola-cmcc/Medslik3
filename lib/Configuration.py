#!/usr/bin/python3

# local requirements
from lib.ConfigurationException import *

class Configuration:

    def __init__(self, configFile):

        # store attributes
        self.configFile = configFile
        
        # try to read the config file
        try:
            self.configFileDesc = open(configFile)
        except:
            raise ConfigurationException("Error opening file!")

        # read values from section Simulation
        try:
            self.simLength = self.configFileDesc.get("Simulation", "Length")
            self.startDateTime = self.configFileDesc.get("Simulation", "StartDateTime")
            self.continuousSpill = self.configFileDesc.getBoolean("Simulation", "ContinuousSpill")
            self.areaRadiusDeg = self.configFileDesc.getfloat("Simulation", "AreaRadiusDeg")
        except:
            raise ConfigurationException("Error in section Simulation of the config file")

        # read values from section SpillLocation
        try:
            self.spillLocationLatDeg = self.configFileDesc.getfloat("SpillLocation", "SpillLocationLatDeg")
            self.spillLocationLatMin = self.configFileDesc.getfloat("SpillLocation", "SpillLocationLatMin")
            self.spillLocationLonDeg = self.configFileDesc.getfloat("SpillLocation", "SpillLocationLonDeg")
            self.spillLocationLonMin = self.configFileDesc.getfloat("SpillLocation", "SpillLocationLonMin")
        except:
            raise ConfigurationException("Error in section SpillLocation of the config file")

        # read values from section InputFiles
        try:
            self.currentsFilesPath = self.configFileDesc.get("InputFiles", "CurrentsFilesPath")
            self.windsFilesPath = self.configFileDesc.get("InputFiles", "WindsFilesPath")
            self.coastlinePath = self.configFileDesc.get("InputFiles", "CoastlinePath")
            self.bathymetryPath = self.configFileDesc.get("InputFiles", "BathymetryPath")
        except:
            raise ConfigurationException("Error in section InputFiles of the config file")
            
        # close the file
        self.configDesc.close()
        
