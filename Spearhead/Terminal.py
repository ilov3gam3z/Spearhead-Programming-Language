import subprocess
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + "\\Y_frontend.py"
failedAsError = False
def run_c(c):
    try:
        #start terminal and get output
        output = subprocess.check_output(c, shell=True, stderr=subprocess.DEVNULL).decode()
        if output == '':
            print("Err0x1: Command NULL does not exist")
            global failedAsError
            failedAsError = True
            return ''
        if failedAsError != True:
            return output.decode()
    except subprocess.CalledProcessError as e:
        #incase i need to handle errors later
        return e.output.decode()
def main():
    while True:
        #get user input and check if it is "exit"
        print("Enter +h into command line for terminal guide")
        u_i = input("cmd< ")
        if u_i.lower() == "exit":
            break
        #get user input and check if it is "+help"
        elif u_i[:2] == "+h":
            print("Terminal instructions:")
            print("Press the enter key or enter \"exit\" into the command line to leave the terminal")
            print("Enter the command \"+r [replace with path of .spearhead file to be ran]\" to run a .spearhead file via the Spearhead Interpreter")
        #get user input and check if it is "+r" 
        elif u_i[:2] == "+r":
            try:
                r = subprocess.run(["python", dir_path, u_i], capture_output=True, text=True).stdout.strip("\n")
                print(r)
                if r == '':
                    print("Err1x1: Directory invalid")
            except FileNotFoundError as e:
                print("Err1x1: Directory invalid")
            continue
        else:
            print("Err0x2: Invalid command")
        #actually run the commands provided and print output
        output = run_c(u_i)
        print(output)
#__name == __main__ so it actually works, although i honestly dont understand this at all, it makes everything work like a charm
if __name__ == '__main__':
    main()