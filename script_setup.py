import subprocess
import sys
import os
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# install packages required for script: "fftw3","matplotlib","numpy"

subprocess.call("apt-get install fftw3 fftw3-dev", shell=True)
subprocess.call("apt-get install libfftw3-dev libfftw3-doc", shell=True)
install("matplotlib")
install("numpy")
install("cosmolopy")
install("scipy")



# Install script
subprocess.call("apt-get install git", shell=True)
subprocess.call('git clone https://bitbucket.org/rctirthankar/script', shell = True)


cwd = os.getcwd()
os.chdir(cwd+'/script')

subprocess.call('python setup.py install --user',shell=True)

os.chdir('/root')

print("installation complete!")
