import whois

class NetworkModule:
    
    def __init__(self, url):
        whois = self.get_whois(url)
        self.domain_name = whois.domain_name
        self.name_servers = self.get_name_servers(whois)
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
    
    def get_name_servers(self, whois):
        if '\n' in whois.name_servers:
            name_servers = []
            for line in whois.name_servers.splitlines():
                line = line.strip()
                if line != "":
                    name_servers.append(line)
        else:
            return whois.name_servers
        return name_servers