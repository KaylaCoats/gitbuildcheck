from sys import argv

action = True

if argv > 3:
    print('Usage: gitbuildcheck user/repo --shame or gitbuildcheck --shame user/repo')
    exit(1)

if argv[1] == '--shame':
    repo = argv[2]
else:
    repo = argv[1]

if '--shame' in argv:
    if action is not True:
        with open('runsiren.sh'):
            exec(f.read())



