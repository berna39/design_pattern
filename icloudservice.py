from abc import ABCMeta, abstractstaticmethod

class ICloudService(meta=ABCMeta):

    @abstractstaticmethod
    def auth():
        pass
