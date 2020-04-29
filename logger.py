import log_file

# Create and configure logger
log_file.basicConfig(filename="newfile.log",
                     format='%(asctime)s %(message)s',
                     filemode='w')

# Creating an object
logger = log_file.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(log_file.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
