import subprocess

def get_process():
    current={}
    try:
      lines=subprocess.check_output('ps -ef | grep container', text=True, shell=True).splitlines()
    except subprocess.CalledProcessError:
      lines=[]
    for line in lines:
      process=line.split(" ")
      pid=int(process[3])
      cmd_line=process[4:]
      if "container.py" in cmd_line:
        ind=cmd_line.index("container.py")
        if (ind+1)<len(cmd_line):
          arg=cmd_line[ind+1]
          current[arg]=pid
    return current

def main():
  # forever_name=sys.argv[1]
  print("the processors of the program container.py")
  known_processors={}
  while True:
    print("current processes",known_processors.items())
    current=get_process()
    for arg,pid in current.items():
      if arg not in known_processors:
        known_processors[arg]=pid
    dead_arg=[]
    for arg,pid in list(known_processors.items()):
      if arg not in current:
        print("The process has been killed for argument ",arg)
        dead_arg.append(arg)
        del known_processors[arg]
    print("--------------",dead_arg)
    for arg in dead_arg:
      print("Starting the process for the argument",arg)
      subprocess.Popen(["python",'container.py',arg])
      new_process=get_process()
      if arg in new_process:
        new_pid=new_process[arg]
        known_processors[arg]=new_pid
        print("the process has started successfully for ",arg)
      else:
        print("The process has not been started for the argument",arg)
  
    time.sleep(2)
if __name__=="__main__":
  main()
