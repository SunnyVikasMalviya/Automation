import logging
logging.basicConfig(filename="newLog.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
#logging.disable(logging.INFO)
logging.debug("Start of program.")

def factorial(n):
    logging.debug("Start of factorial {}.".format(n))
    total = 1
    for i in range(n+1):
        if i == 0:
            logging.warning("i is {}, total is {}".format(i, total))
        total *= i
        logging.debug("i is {}, total is {}.".format(i, total))
    logging.debug("End of factorial {}.".format(n))
    return total

if __name__ == "__main__":
    n = 5
    print(factorial(n))
    logging.debug("End of program.")