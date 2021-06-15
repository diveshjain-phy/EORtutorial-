import subprocess
import sys
import os
import wget
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# install packages required for script: "fftw3","matplotlib","numpy"
import conda.cli.python_api as Conda

(stdout_str, stderr_str, return_code_int) = Conda.run_command(
    Conda.Commands.INSTALL,
    '-c', 'eumetsat',
    'fftw3',
    use_exception_handler=True, stdout=sys.stdout, stderr=sys.stderr
)


subprocess.call('conda install matplotlib',shell=True)
subprocess.call('conda install numpy',shell=True)
subprocess.call('conda install ipykernel',shell=True)

# Install script
subprocess.call("apt-get install git", shell=True)
subprocess.call('git clone https://bitbucket.org/rctirthankar/script', shell = True)


cwd = os.getcwd()
os.chdir(cwd+'/script')

subprocess.call('python setup.py install --user',shell=True)

os.chdir('/root')

print("installation complete!")
