from slugify import slugify_de


def slugify(value):
    return slugify_de(value, to_lower=True)
