from abc import ABCMeta, abstractstaticmethod

class Iperson(metaclass=ABCMeta):

    @abstractstaticmethod
    def speak():
        print('i\'m the real person')

class person(Iperson):

    def speak(self):
        print('i\'m the real person')


class PersonProxy(Iperson):
    def __init__(self):
        self.person = person()

    def speak(self):
        print('I\'m the proxy person')
        self.person.speak()

p = PersonProxy()
p.speak()
        
