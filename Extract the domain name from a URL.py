import re
def domain_name(url):
    pattern = re.compile(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?')
    domain = pattern.sub(r'\3', url)
    return domain