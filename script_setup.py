import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# Install Conda
install("wget")
import wget
url="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh"
wget.download(url)

import os
os.system("sha256sum Miniconda3-latest-Linux-x86.sh")
# install packages required for script: "fftw3","matplotlib","numpy"
import conda.cli.python_api as Conda
import sys

(stdout_str, stderr_str, return_code_int) = Conda.run_command(
    Conda.Commands.INSTALL,
    '-c', 'eumetsat',
    'fftw3',
    use_exception_handler=True, stdout=sys.stdout, stderr=sys.stderr
)



(stdout_str, stderr_str, return_code_int) = Conda.run_command(Conda.Commands.INSTALL,[ 'numpy', 'matplotlib', 'ipykernel' ],use_exception_handler=True,stdout=sys.stdout,stderr=sys.stderr,search_path=Conda.SEARCH_PATH)
# Install script
subprocess.call("apt-get install git", shell=True)
subprocess.call('git clone https://bitbucket.org/rctirthankar/script', shell = True)


cwd = os.getcwd()
os.chdir(cwd+'/script')

subprocess.call('python setup.py install --user',shell=True)

os.chdir('/root')

print("installation complete!")