o = urlparse(request)
    path_name = o.path
    arguments = parse_qs(o.query)


    termcolor.cprint(req_line, "green")

    print("Resource requested:", path_name)
    print("Parameters:", arguments)
    print("Request", request)

try:
    parameters = request.split("?")[1]
    o = urlparse(req_line.split(" ")[1])
    query = parse_qs(o.query)
    print(o)
    print(query)
except IndexError:
    pass
print("Resource requested:", path_name)