#!/usr/bin/python

# global requirements
import sys
import getopt
import logging

# local requirements
from lib.utils import *
from lib.Simulation import *
from lib.Configuration import *


# main
if __name__ == "__main__":

    #####################################################
    #
    # create a logger
    #
    #####################################################
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("Medslik")
    logger.info("Medslik started!")

    
    #####################################################
    #
    # read input arguments
    #
    #####################################################
    
    # initialization
    configFile = None
    
    # read input params
    try:
        options, rem = getopt.getopt(sys.argv[1:], 'hc:', ['config=', 'help'])
    
        for opt, arg in options:
            if opt in ('-c', '--config'):
                configFile = arg
            elif opt in ('-h', '--help'):
                showHelp(logger)
                sys.exit(0)
    
    except getopt.GetoptError:
        showHelp(logger)
        sys.exit(1)

    # check if mandatory arguments are present
    if not(configFile):
        logger.error("Missing mandatory argument!")
        showHelp(logger)
        sys.exit(1)

        
    #####################################################
    #
    # read configuration file
    #
    #####################################################
        
    try:
        c = Configuration(configFile, logger)
    except ConfigurationException as e:
        logger.error(e.message)
        sys.exit(1)

    if c.debug:
        logger.setLevel(logging.DEBUG)


    #####################################################
    #
    # init and run the simulation
    #
    #####################################################

    s = Simulation(c, logger)

    # print debug information
    if c.debug:
        c.getInfoInputFiles()

    # run the simulation
    s.run()


    #####################################################
    #
    # exit gracefully
    #
    #####################################################

    logger.info("Simulation finished")
    sys.exit(0)
