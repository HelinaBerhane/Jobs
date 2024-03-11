class Parameter:
    def __init__(self, value):
        self.value = value


def compile_sql(sql, n=0):
    query = []
    parameters = []

    for part in sql:
        if isinstance(part, list):
            sub_query, sub_parameters = compile_sql(part)
            sub_val = ', '.join(sub_query.split(" "))
            query.append(f"({sub_val})")
            parameters.extend(sub_parameters)
        elif isinstance(part, str):
            query.append(part)
        elif isinstance(part, Parameter):
            query.append("?")
            parameters.append(part.value)

    query_string = " ".join(str(x) for x in query)

    return query_string, parameters, n
