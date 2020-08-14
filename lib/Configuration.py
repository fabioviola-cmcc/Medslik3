#!/usr/bin/python3

# global requirements
import traceback
import configparser
from datetime import datetime
from datetime import timedelta

# local requirements
from lib.ConfigurationException import *

class Configuration:

    # attributes
    currentsTFiles = []
    currentsUFiles = []
    currentsVFiles = []
    windsFiles = []

    # constructor
    def __init__(self, configFile, logger):        

        """Constructor for the Configuration class"""
        
        # store attributes
        self.configFile = configFile
        self.logger = logger
        
        # try to read the config file
        try:
            self.configFileDesc = configparser.ConfigParser()
            self.configFileDesc.read(configFile)
        except:
            print(traceback.print_exc())
            raise ConfigurationException("Error opening file!")

        # read values from section Medslik
        try:
            self.debug = self.configFileDesc.getboolean("Medslik", "Debug")
        except:
            print(traceback.print_exc())
            raise ConfigurationException("Error in section Medslik of the config file")
        
        # read values from section Simulation
        try:
            self.simLength = self.configFileDesc.getint("Simulation", "Length")
            self.startDateTimeString = self.configFileDesc.get("Simulation", "StartDateTime")
            self.continuousSpill = self.configFileDesc.getboolean("Simulation", "ContinuousSpill")
            self.areaRadiusDeg = self.configFileDesc.getfloat("Simulation", "AreaRadiusDeg")
        except:
            print(traceback.print_exc())
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
            self.coastlineFile = self.configFileDesc.get("InputFiles", "CoastlineFile")
            self.bathymetryFile = self.configFileDesc.get("InputFiles", "BathymetryFile")
        except:
            raise ConfigurationException("Error in section InputFiles of the config file")
        
        # create the datetime object
        self.startDateTime = datetime.strptime(self.startDateTimeString, "%Y/%m/%d %H:%M")

        # determine the list of files needed for the simulation
        currDayObject = self.startDateTime
        for hour in range(self.simLength):

            # determine current timestamp
            currDay = currDayObject.strftime("%Y%m%d")
            
            # build the filename
            filenameT = "MDK_ocean_%s_T.nc" % currDay
            filenameU = "MDK_ocean_%s_U.nc" % currDay
            filenameV = "MDK_ocean_%s_V.nc" % currDay
            filenameWind = "%s.nc" % currDay

            # check if the filenames are already in the lists
            if not(filenameT in self.currentsTFiles):
                self.currentsTFiles.append(filenameT)
            if not(filenameU in self.currentsUFiles):
                self.currentsUFiles.append(filenameU)
            if not(filenameV in self.currentsVFiles):
                self.currentsVFiles.append(filenameV)
            if not(filenameWind in self.windsFiles):
                self.windsFiles.append(filenameWind)

            # increment date
            currDayObject += timedelta(hours=1)
                

    def getInfoInputFiles(self):

        """This is a method mainly used for debug purposes. It
        shows a list of the input files needed to run the simulation."""
        
        self.logger.debug("Currents files:")
        for f in self.currentsTFiles + self.currentsUFiles + self.currentsVFiles:
            self.logger.debug(" - %s" % f)
            
        self.logger.debug("Wind files:")
        for f in self.windsFiles:
            self.logger.debug(" - %s" % f)

        self.logger.debug("Coastline file:")
        self.logger.debug(" - %s" % self.coastlineFile)
        
        self.logger.debug("Bathymetry file:")
        self.logger.debug(" - %s" % self.bathymetryFile)
