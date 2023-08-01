try:
    import pip
except ImportError:
    from pip._internal import main as pip
print(
'''A program written by AetherYT, to use basic Python commands without Command Prompt/Shell/Root/Administrator access. A-CLIP stands for:

Alternative
Command
Line
Interface
for
Python

''')
def install_apcli():
    package = input("Enter the name of the package you want to install:")
    pip.main(["install", "--user", package])
def remove_apcli():
    package = input("Enter the name of the package you want to uninstall:")
    pip.main(["uninstall", package])
def update_apcli():
    package = input("Enter the name of the package you want to update:")
    pip.main(["install", "--user", "--upgrade", package])
def list_apcli():
    print("List of all Pip packages installed.")
    pip.main(["list"])
def check_apcli():
    print("Checks compatibility of all Pip packages installed.")
    pip.main(["check"])
def optionmenu():
    option = ''
    option = input('''
    Available commands:
    update
    install
    uninstall
    list
    check

    Note that pressing 'Ctrl' and 'C' at the same time will kill the Pip process.
    Doing so while in the main menu will kill A-CLIP.
    Enter a command:
    ''')
    if option == 'update':
        update_apcli()
    elif option == 'install':
        install_apcli()
    elif option == 'uninstall':
        remove_apcli()
    elif option == 'list':
        list_apcli()
    elif option == 'check':
        check_apcli()
    else:
        print('Unknown command.')
while True:
    optionmenu()
    
