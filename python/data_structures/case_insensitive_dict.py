class CaseInsensitiveDict(dict):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self[key.lower()] = value
        
    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(key.lower())
    
    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())
    
    def __setitem__(self, key, value):
        return super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)
    
d = CaseInsensitiveDict(SpAm='eggs')
print 'spam' in d
print d['SPAM']
d['sPaM'] = 'burger'
print d['SpaM']
