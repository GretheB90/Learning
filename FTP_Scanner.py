import ftplib #helps our program to talk to FTP servers(file storage computers etc).

def anonLogin(hostname, timeout=5):
    try:
        ftp = ftplib.FTP(hostname) #Let me connect to the server at hostname
        ftp.connect(host=hostname, timeout=timeout)
        ftp.login('anonymous') #Let me try to log in with the name 'anonymous' — no password
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Succeded.')
        ftp.quit()
        return True
    except Exception as e:
        print(f"\n[!] {hostname} FTP Anonymous Login Failed. Reason: {e}")
        return False


if __name__ == '__main__':
    # Ask the user to enter a server address (instead of hardcoding)
    hostname = input("Enter the FTP server address (IP or domain): ").strip()
    
    if hostname:
        anonLogin(hostname)
    else:
        print("No hostname entered. Exiting.")

  #Try it like this:
#Enter the FTP server address (IP or domain): 85.221.11.10
#[+] 85.221.11.10 FTP Anonymous Login Succeeded.

#Or:

#Enter the FTP server address (IP or domain): fake-server.com
#[!] fake-server.com FTP Anonymous Login Failed. Reason: [Errno ...] ...
