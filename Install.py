import subprocess
import sys

class Install:

    # Methods
    def InstallPackage(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def InstallAllPackagesLoop(packageList):
        for package in packageList:
            Install.InstallPackage(package)

    def LoadPackages():
        f = open("packages", "r")

        packageList = f.readlines()

        f.close()

        i = 0

        for package in packageList:
            package.replace('\n', '', -1)
            packageList[i] = package
            i += 1
        
        return packageList

    def InstallPackages():
        Install.InstallAllPackagesLoop( Install.LoadPackages() )



if __name__ == "__main__":
    Install.InstallPackages()