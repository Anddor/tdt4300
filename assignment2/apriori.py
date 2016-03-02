import getopt
import sys


def frequent_itemset(transactions, minsup):
    """Generate frequent itemset from transactions
    :param minsup: The threshold for support count, number (0, 1)
    """
    pass


def rule_generation(items, minconf):
    """Generate rules from frequent items"""
    pass


def main(argv):
    inputfile = False
    minsup = False
    minconf = False
    try:
        opts, args = getopt.getopt(argv, "f:s:c:", ["file=", "minsup=", "minconf="])
    except getopt.GetoptError:
        print('Usage: apriori.py -f <file> -s <minsup> [-c <minconf>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: apriori.py -f <inputfile> -s <minsup> [-c <minconf>]')
            sys.exit()
        elif opt in ("-f", "--file"):
            inputfile = arg
        elif opt in ("-s", "--minsup"):
            minsup = arg
        elif opt in ("-c", "--minconf"):
            minconf = arg

    if not inputfile or not minsup:
        print('Usage: apriori.py -f <inputfile> -s <minsup> [-c <minconf>]')
        sys.exit(2)

    with open(inputfile, 'r') as f:
        data = f.read()

    lines = data.split('\n')
    items = dict()
    for line in lines[1:]:
        basket = line.split(';')[1]
        print(basket)

main(sys.argv[1:])
