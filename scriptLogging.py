import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def extended_welcome(firstname, lastname):
    logging.info("Hello %s %s!" % (firstname, lastname))

if __name__ == "__main__":
    logging.debug("This program was called with parameters %s" % sys.argv[1:])      
    logging.debug("First parameter is %s" % sys.argv[1])
    firstname = sys.argv[1]
    lastname = sys.argv[2]
    extended_welcome(firstname,lastname)




"""

import sys

def customized_hello(first_name, last_name, prefix):
    print("Hello %s %s %s!" % (prefix, first_name, last_name ))

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    prefix = sys.argv[3]
    customized_hello(first_name, last_name, prefix)
"""    