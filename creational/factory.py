from abc import ABCMeta, abstractmethod
# Concrete product classes for sections

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

# Abstract creator(factory) class
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)
    
    def describeSections(self):
        for section in self.sections:
            section.describe()

#Concrete creator class for a linkedIn type profile
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

#Concrete creator class for a facebook type profile
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

if __name__ == '__main__':
    profile_type = input("which profile would you like to create? [linkedin or facebook]")
    profile = eval(profile_type.lower())()
    print("creating profile ... ", type(profile).__name__)
    print("profile has sections -- ")
    profile.describeSections()