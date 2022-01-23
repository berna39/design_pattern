from abc import ABCMeta, abstractstaticmethod

class ICloudService(meta=ABCMeta):

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
    @abstractstaticmethod
    def auth():
        print('Auth to Azure')

    @abstractstaticmethod
    def deploy():
        print('Deploy to Azure')

    @abstractstaticmethod
    def scale():
        print('Scale my app to Azure')

class CloudServiceFactory:
     
    @staticmethod
    def get_instance(provider):
        if provider == 'Azure':
            pass
        elif provider == 'Aws':
            pass
        elif provider == 'Gcp':
            pass
        else:
            return -1 
