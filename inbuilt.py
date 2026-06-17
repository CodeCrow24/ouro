def handle_print(line, crudel, i):
    output = ""
    firstChar = line[1][0]
    if firstChar == "\"":
        output = get_string_from_tokens(line, crudel)
    elif firstChar.isnumeric():
        print(line[1])
    
    print(output)

def handle_input(line, crudel, i):
    return

def handle_var(line, crudel, i):
    return

def handle_if(line, crudel, i):
    return

def handle_for(line, crudel, i):
    return

def handle_stop(line, crudel, i):
    return

def handle_verbose(line, crudel, i):
    return

def get_string_from_tokens(line, crudel):
    prefix = line[0] + ' "'

    if crudel.startswith(prefix):
        text = crudel[len(prefix):]

        end = text.find('"')
        if end != -1:
            return text[:end]

    return ""