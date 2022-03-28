import functions_from_class

def cutout(text, skip_header):
    """
    
    """

    fp = open(text, encoding='UTF8')

    for line in fp:
        line = line.strip()
        if line.startswith('*** START OF THE PROJECT'):
            break
        