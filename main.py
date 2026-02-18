# ML Driven Phishing Domain Classifier

# from extract_features import is_ip_address, extract_features

def main():
    while True:
        # get domain string input and strip whitespace characters
        domain = input("Enter a domain to extract its features: ").strip()

        # basic domain validation: must contain at least one dot, no spaces, not be an IP address
        # if ' ' in domain or '.' not in domain or is_ip_address(domain):
        #     print("Invalid domain.  Please enter a valid domain name (e.g., example.com).")

        #     continue

        # EXTRACT FEATURES (14 non-database dependent features, 1 WHOIS lookup (creation date))

        # extract_features(domain)

# check whether script is run directly and not imported as a library module
# this is so main will not run when it is imported elsewhere
if __name__ == "__main__":
    main()


"""

LENGTH - Longer domain length corresponds with likely phishing
    Example: thisisaverylongandunusuallylengthyphishingdomainexample.com
DOMAIN CREATION DATE - Older domain creation date corresponds with likely legitimate
    Example: newlyregistereddomain123.com (registered today)
CHARACTER ENTROPY (RANDOMNESS) - Greater domain character entropy corresponds with likely phishing
    Example: x7k9q2w8zv3b1n.com
SUBDOMAIN COUNT - More subdomains corresponds with likely phishing
    Example: login.verify.account.security.bank.example.com
DIGIT COUNT - More digits in domain corresponds with likely phishing
    Example: secure1234567890login.com
SPECIAL CHARACTER COUNT - More special characters in domain corresponds with likely phishing
    Example: secure-login_update!verify@account.com
LONGEST SUBDOMAIN LENGTH - Longer subdomain length corresponds with likely phishing
    Example: thisisaverylongsubdomain.example.com
VOWEL TO CONSONANT RATIO - Lower vowel to consonant ratio corresponds with likely phishing
    Example: xjklmnqz.com
HYPHEN COUNT - More hyphens in domain corresponds with likely phishing
    Example: secure-login-update-verify-account.com
UPPERCASE COUNT - Presence of uppercase letters corresponds with likely phishing
    Example: PayPalSECURELogin.com
CYRILLIC VOWEL SUBSTITUTION - Presence of Cyrillic vowel substitutions corresponds with likely phishing
    Example: раураl.com (uses Cyrillic 'а' and 'у')
NON-LATIN CHARACTER - Presence of non-Latin characters corresponds with likely phishing
    Example: exámple.com or xn--exmple-cua.com
MAIN DOMAIN LENGTH - Unusually short or long main domain length corresponds with likely phishing
    Example: averyveryverylongmaindomain.com or a.co
MOST CONSECUTIVELY REPEATED CHARACTER COUNT - Higher count of consecutively repeated characters corresponds with likely phishing
    Example: paypallll.com

TODO:
BLACKLISTS - Domain listed on blacklist corresponds with likely phishing

"""
