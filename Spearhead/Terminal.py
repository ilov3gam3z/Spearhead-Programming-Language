import subprocess
import sys
import os
errorCaught = ""
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + "\\Y_frontend.py"
def run_c(c):
    global errorCaught
    try:
        #start terminal and get output
        output = subprocess.check_output(c, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        #incase i need to handle errors later
        return e.output.decode()
def main():
    while True:
        #get user input and check if it is "exit"
        u_i = input("cmd< ")
        if u_i.lower() == "exit":
            break
        #get user input and check if it is "+r"
        elif u_i[:2] == "+r":
            try:
                subprocess.run(["python", dir_path, u_i])
            except FileNotFoundError:
                print("Directory invalid")
            continue
        else:
            print("Invalid command, or shell command")
        #actually run the commands provided and print output
        output = run_c(u_i)
        print(output)
#__name == __main__ so it actually works, although i honestly dont understand this at all, it makes everything work like a charm
if __name__ == '__main__':
    main()