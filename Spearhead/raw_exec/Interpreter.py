import re
def lexer(contents):
    lines = contents.split('\n')
    for line in lines:
        chars = list(line)
        requirements = []
        if re.match('require', line):
            r = True
        if re.search(' boolOperators', line):
             b = True
        if b and r == True:
            requirements.insert('boolOperators')
            line = ''
            return requirements
        temp_str = ""
        tokens = []
        quote_count = 0
        for char in chars:
            if char == '"' or char == "'":
                quote_count += 1
            if quote_count % 2 == 0:
                in_quotes = False
            else:
                in_quotes = True
            if char == " " and in_quotes == False:
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char
        tokens.append(temp_str)
        print(tokens)
def parse(parsed_data):
    parsed_data = parsed_data.replace(parsed_data[:3], '')
    parsed_data = re.sub('\"', '', parsed_data)
    c = open(parsed_data, "r")
    cl = c.read()
    tokens = lexer(cl)
    return tokens