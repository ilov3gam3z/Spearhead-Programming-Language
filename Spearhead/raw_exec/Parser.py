def parse(parsed_data):
    parsed_data = parsed_data.replace(parsed_data[:3], '')
    parsed_data = parsed_data.replace('\"', '')
    c = open(parsed_data, "r")
    cl = c.readlines()
    for ln in cl:
        print(ln)
    return c