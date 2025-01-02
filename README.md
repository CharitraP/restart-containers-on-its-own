#The basic struture of Container and Pod execution on backend.
**Explaination**
There are two files one is a container.py file whihc runs on background untill killed.
And the other is monitor_pod file which monitors the number of processes running for a particular container with port number,to make sure if the container is killed it can be restarted automatically.

**Technical Explaination**
Subprocess: It is a module in Python is used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It allows you to execute shell commands directly from your Python code, offering control over their execution and the ability to capture thier output.
