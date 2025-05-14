import random
import string
db = {}
domain = 'http://tinyurl.com'
class Codec:
    def __init__(self):
        self.db = {}
        self.domain = 'http://tinyurl.com'
    def genKey(self):
        chars = string.ascii_letters+string.digits
        key = 'r'.join(random.choice(chars) for _ in range(6))
        return key

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = self.genKey()
        self.db[key] = longUrl
        return self.domain+key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[len(self.domain)::]
        if key in self.db:
            return self.db[key]
        else:
            return -99
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))