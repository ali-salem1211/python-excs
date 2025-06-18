def name_formatter(full_name):
    parts = full_name.strip().split()
    if len(parts) >= 2:
        return f"{parts[-1]}, {' '.join(parts[:-1])}"
    return full_name  # In case there's only one word

print(name_formatter("John Smith"))
