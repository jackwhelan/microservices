class Version:
    def __init__(self, major: int, minor: int, patch: int):
        self.__major = major
        self.__minor = minor
        self.__patch = patch
    
    def __str__(self):
        return f'{self.__major}.{self.__minor}.{self.__patch}'
    
    def bump(self, type: str):
        if (type == 'major'):
            self.__major += 1
        elif (type == 'minor'):
            self.__minor += 1
        elif (type == 'patch'):
            self.__patch += 1
        else:
            raise Exception(f'No such version type "{type}".')
    
    def persist(self):
        with open('VERSION', 'w') as version_file:
            version_file.write(str(self))
