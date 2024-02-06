import argparse



def parse_arguments():
    """
    Returns the list of command line arguments 
    """
    parser = argparse.ArgumentParser(
        description="This is a cli tool to retreive information about your file text")

    parser.add_argument("-c", action="store_true",
                        help="Returns the number of bytes in the provided file")
    parser.add_argument("-l", action="store_true",
                        help="Returns the number of lines in the provided file")
    parser.add_argument("-w", action="store_true",
                        help="Returns the number of words in the provided file")
    parser.add_argument("-m", action="store_true",
                        help="Returns the number of characters in the provided file")
    # this basically means there may be one or more than one arguments present
    parser.add_argument('files', nargs='*', help="The file to process")
    args = parser.parse_args()
    return args


def get_user_input():
    """
    to take the input from the terminal when file name is not specified 
    """
    content = []
    while 1:
        try:
            content.append(input())
        except EOFError:
            break

    return "\n".join(content)