# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

import re
def domain_name(url):
    pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w\.-]+\.\w+)(/\S*)?"
    match = re.match(pattern, url)
    if match:
        domain = match.group("domain")
        return domain.split(".")[0]
    else:
        return None
