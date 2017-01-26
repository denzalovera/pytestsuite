import os

'''
    created by: denz alovera
    1/24/2017
    place  configuration here for webdrivers
    import to python script to use.
'''


class Config(object):

    def __init__(self):
        # add path for webdrivers
        # create a directory named webdrivers and save corresponding files here
        # self.testcase = os.path.abspath(os.path.dirname(__file__))
        self.chromeWebdriver = os.path.abspath('..' + '/webdrivers' + '/chromedriver')
        self.firefoxWebdriver = os.path.abspath('..' + '/webdrivers' + '/geckodriver')
        self.ieWebdriver = os.path.abspath('..' + '/webdrivers' + '/IEDriverServer')
        self.operaWebdriver = ('PATH TO WEBDRIVER')
        self.phantomjsWebdriver = ('PATH TO WEBDRIVER')

# call path to webdriver from testscripts
    def get_ChromeWebdriver(self):
        return self.chromeWebdriver

    def get_FirefoxWebdriver(self):
        return self.firefoxWebdriver

    def get_IeWebdriver(self):
        return self.ieWebdriver

    def get_OperaWebdriver(self):
        return self.operaWebdriver

    def get_PhantomjsWebdriver(self):
        return self.phantomjsWebdriver
