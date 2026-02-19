import string 


def count_character_length(domain):

    return len(domain) 


def count_hyphens(domain):
    domain = domain.replace('.', '')

    return domain.count('-')
    

def find_main_domain_length(domain):
    # make list of domains by splitting domain string dotwise
    domains = domain.strip().split('.')
    
    # if there is only one domain it has to be TLD so there is no main domain
    if len(domains) < 2:
        return 0

    # gets the length of the main domain (just before the TLD)
    return len(domains[-2]) 