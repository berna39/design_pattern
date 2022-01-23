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

class Aws(ICloudService):
    def __init__(self):
        pass

    def auth(self):
        print('Auth to Aws')

    def deploy(self):
        print('Deploy to Aws')

    def scale(self):
        print('Scale my app to Aws')


class Gcp(ICloudService):
    def __init__(self):
        pass

    def auth(self):
        print('Auth to Gcp')

    def deploy(self):
        print('Deploy to Gcp')

    def scale(self):
        print('Scale my app to Gcp')

class CloudServiceFactory:
     
    @staticmethod
    def get_instance(provider):
        if provider == 'Azure':
            return Azure()
        elif provider == 'Aws':
            return Aws()
        elif provider == 'Gcp':
            return Gcp()
        else:
            return -1 

azure = CloudServiceFactory.get_instance('Azure')
azure.deploy()

aws = CloudServiceFactory.get_instance('Aws')
aws.auth()

gcp = CloudServiceFactory.get_instance('Gcp')
gcp.scale()