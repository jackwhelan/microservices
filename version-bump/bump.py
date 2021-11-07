import sys

from version import Version

if __name__ == '__main__':
    version_strs = None
    with open('microservice/VERSION', 'r') as version_file:
        version_strs = version_file.readline().split('.')
    
    version = Version(
        int(version_strs[0]),
        int(version_strs[1]),
        int(version_strs[2])
    )

    version.bump(sys.argv[1])
    version.persist()
