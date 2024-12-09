def format_to_graphql_string(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        formatted_list = [format_to_graphql_string(v) for v in value]
        return f"[{', '.join(formatted_list)}]"
    elif isinstance(value, dict):
        formatted_dict = {k: format_to_graphql_string(v) for k, v in value.items()}
        return f"{{{', '.join(f'{k}: {v}' for k, v in formatted_dict.items())}}}"
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")
