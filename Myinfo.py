class Myinfo:
    def __init__(self):
        self.mykey = "myApiKey"

    @property
    def myapikey(self):
        return self.mykey

    @myapikey.setter
    def myapikey(self, value):
        self.mykey = value
