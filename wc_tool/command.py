from wc_tool.cli import get_user_input
from wc_tool.utils import count_bytes,count_words,count_lines, count_characters
from io import BytesIO, TextIOWrapper

def get_file_stream(file_name):
    try:
       stream = open(file_name,'r')
       return stream
    except Exception as e:
       print(f"Unable to open file due to {e}")



def process_command(args,file_stream):
    result=[]
    
    if args.c:
        result.append(count_bytes(file_stream))
    elif args.w:
        result.append(count_words(file_stream))
    elif args.l:
        result.append(count_lines(file_stream))
    elif args.m:
        result.append(count_characters(file_stream))
    else:
        result.append(count_lines(file_stream))
        result.append(count_words(file_stream))
        result.append(count_characters(file_stream))               
    return result
           


def execute(args):
    if not args.files:
        # take input from the terminal and convert it into it into an in memory byte stream
         with BytesIO(get_user_input().encode()) as stream:
            result = process_command(args,TextIOWrapper(stream))
    else:
        for file in args.files:
            try:
                with open(file) as stream:
                    result = process_command(args,stream)
                    result.append(file) 
            except FileNotFoundError:
                result = f"File {file} doesn't exists"
    return result            
               
   