#The basic struture of Container and Pod execution on backend.
**Explaination**
There are two files one is a container.py file whihc runs on background untill killed.
And the other is monitor_pod file which monitors the number of processes running for a particular container with port number,to make sure if the container is killed it can be restarted automatically.

**Technical Explaination**
Subprocess: It is a module in Python is used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It allows you to execute shell commands directly from your Python code, offering control over their execution and the ability to capture thier output.

check_out: captures the standard output (stdout) and standard error (stderr) of the subprocess and stores them in the CompletedProcess object.
shell=True: means the command passed is a shell command

Popen:It is a class in the subprocess module that allows you to create a new process by executing a command.

**Testing**
You can test the code by running the container.py file in the background and then running the monitor_pod file. You can also test it by killing the container.py process and see if it gets restarted automatically.
python container.py port_number &
python monitor_pod.py 
kill porocess_id 
Once the process is killed there is another process which starts with the same port number.



