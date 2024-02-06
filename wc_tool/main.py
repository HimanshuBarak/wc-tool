
from wc_tool.cli import parse_arguments
from wc_tool.command import execute

def main():
    args = parse_arguments()
    result = execute(args)
    return "  ".join([str(item) for item in result]) 
