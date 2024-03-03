import os
import zlib


def parse_response(path, headers = "header: value"):
    response = f"{headers}\n"
    
    for file in os.listdir(f"./files/{path}"):
        response += f"{file}:{zlib.compress(open(f"./files/{path}" + f"/{file}", 'rb').read())}\n"
    return response.splitlines()


