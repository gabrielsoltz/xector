import whois

class NetworkModule:
    
    def __init__(self, url):
        whois = self.get_whois(url)
        self.domain_name = whois.domain_name
        self.name_servers = whois.name_servers
        self.registrar = whois.registrar
        self.registrar_url = whois.registrar_url
        self.status = whois.status
        self.registrant_name = whois.registrant_name
        self.creation_date = str(whois.creation_date)
        self.expiration_date = str(whois.expiration_date)
        self.updated_date = str(whois.updated_date)
        self.emails = whois.emails
    
    def get_whois(self, url):
        whois_info = whois.whois(url)
        return whois_info