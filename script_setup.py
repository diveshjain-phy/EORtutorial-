import subprocess
import sys
import os
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# install packages required for script: "fftw3","matplotlib","numpy"


wget("matplotlib")
wget("numpy")



# Install script
subprocess.call("apt-get install git", shell=True)
subprocess.call('git clone https://bitbucket.org/rctirthankar/script', shell = True)


cwd = os.getcwd()
os.chdir(cwd+'/script')

subprocess.call('python2 setup.py install --user',shell=True)

os.chdir('/root')

print("installation complete!")
