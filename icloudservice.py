from abc import ABCMeta, abstractstaticmethod

class ICloudService(metaclass=ABCMeta):

    @abstractstaticmethod
    def auth():
        pass

    @abstractstaticmethod
    def deploy():
        pass

    @abstractstaticmethod
    def scale():
        pass

class Azure(ICloudService):
    def __init__(self):
        pass

    def auth(self):
        print('Auth to Azure')

    def deploy(self):
        print('Deploy to Azure')

    def scale(self):
        print('Scale my app to Azure')

class CloudServiceFactory:
     
    @staticmethod
    def get_instance(provider):
        if provider == 'Azure':
            return Azure()
        elif provider == 'Aws':
            pass
        elif provider == 'Gcp':
            pass
        else:
            return -1 

azure = CloudServiceFactory.get_instance('Azure')
azure.deploy()