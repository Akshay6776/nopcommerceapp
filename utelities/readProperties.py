import configparser

config=configparser.RawConfigParser()
config.read('C:\\akshay python projects\\nopcommerceApp\\Configuration\\congig.ini')


class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url=config.get('comman info','base_url')
        return url

    @staticmethod
    def getemail():
        email=config.get('comman info','email')
        return email

    @staticmethod
    def getpassword():
        password=config.get('comman info','password')
        return password