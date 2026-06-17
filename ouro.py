import sys
import inbuilt

#error types
class OuroError(Exception):
    pass

#global memory variables
filename = sys.argv[1]
file_content = open(filename)

name = ""
version = ""

VARS = {}

#Interpreter Constants
base_statements = ["out", "in", "set", "if", "for", "stop", "verbose"]

#primary header parsing
def parse_file(file):
    global name, version, source

    lines = file.splitlines()

    try:
        name = lines[0]
        version = lines[1]
    except IndexError:
        raise OuroError("[CRITICAL 100] Header not found")

#Line to Tokens:
def tokenize(line, i):
    valid_tokens = base_statements
    tokens = line.split(" ")
    if tokens[0] not in valid_tokens:
        raise OuroError(f'[CRITICAL ERROR] Invalid statement on line {i+1}')
    return tokens

#line handler:
def handle_line(line, i):
    tokens = tokenize(line, i)
    print(tokens) #TODO remove debug print later

    # Handle Token 0
    match tokens[0]:
        case "out":
            inbuilt.handle_print(tokens, line, i)
        case "in":
            inbuilt.handle_input(tokens, line, i)
        case "set":
            inbuilt.handle_var(tokens, line, i)
        case "if":
            inbuilt.handle_if(tokens, line, i)
        case "for":
            inbuilt.handle_for(tokens, line, i)
        case "stop":
            inbuilt.handle_stop(tokens, line, i)
        case "verbose":
            inbuilt.handle_verbose(tokens, line, i)


#main environment:
def main(file):

    #parse for global vars
    content = file.read()
    parse_file(content)

    #user friendlieness
    print("Executing", name, "version", version)

    #split source by lines
    lines = content.splitlines()

    #interpret content
    i = 0
    for line in lines[3:]:  # skip header lines
        handle_line(line, i)
        i += 1
    i = "EoF"

    #user friendlieness
    print("Finished executing with zero critical errors.")



try:
    main(file_content)
    input("\nPress Enter to exit...")
except OuroError as e:
    print(e)
    input("\nPress Enter to exit...")