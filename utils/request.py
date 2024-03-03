def unparse_request(connection: str) -> str:
    return connection.splitlines()[0].split()[1][1:]
