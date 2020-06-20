import pyWars
#import local_pyWars as pyWars

def answer1(datasample):
    return datasample+5
def answer2(datasample):
    return 16**datasample
    
def a22(x):
    return x.split(",")[9]
    
def a23(x):
    return x.split(":")[1].split("$")[2]
    
def a24(x):
    x.append('Pywars rocks')
    return x
    
def total(x):
    total = 0
    for i in x:
        total = total + i
    return total 
    
def a29(xlist):
    answerstring = ""
    for hexchar in xlist:
        answerstring= answerstring + chr(int(hexchar,16))
    return answerstring
    
def a30(twolist):
    return sorted(set( twolist[0] + twolist[1] ))    
    
def a34(x):
    return x.get('python') + x.get('rocks')

def a45(x):
    file_name, line_num = x
    file_list = gzip.open(file_name, "rt").readlines()
    return file_list[line_num -1]

def a46(x):
    answer = []
    logpath = pathlib.Path.home() / "Public/log"
    for each_item in logpath.rglob("*"):
        if not each_item.is_file():
            continue
        file_content = each_item.read_bytes()
        if x.encode() in file_content:
            answer.append(str(each_item))   
    return sorted(answer)

def a56(x):
    logname, hostname = x
    fpath = pathlib.Path("/home/student/Public/log/dnslogs") / logname
    logfile = fpath.read_text()
    client_host_pairs = re.findall(r"client ([\d.]{7,15}).*?query: (\S+) IN", logfile)
    return sorted([ip for ip, host in client_host_pairs if host == hostname])
    
def a57(x):
    logfile, tgt_len = x
    file_content=pathlib.Path(r"/home/student/Public/log/dnslogs/"+logfile).read_text()
    all_host=re.findall(r"query: (.*?) IN" , file_content)
    answer =[]
    for each_host in all_host:
        if len(each_host) > tgt_len:
            answer.append(each_host)
    return len(answer)

def a67(x):
    rh = Registry("/home/student/Public/registry/SOFTWARE")
    rk = rh.open(r"Microsoft\Windows NT\CurrentVersion\Winlogon")
    return rk.value(x).value()
    
def a68(i):
    rh = Registry("/home/student/Public/registry/SOFTWARE")
    return list(map(lambda x:x.name(), rh.root().subkeys()))[i]
    
def a69(i):
    #find ssids 
    rh = Registry("/home/student/Public/registry/SOFTWARE")
    rk = rh.open(r"Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged")
    ssids = list(map(lambda x: x.value("FirstNetwork").value(),rk.subkeys()))
    return sorted([x for x in ssids if x.lower().startswith(i)])

def a70(i):
    rh = Registry(r"/home/student/Public/registry/NTUSER.DAT")
    rk = rh.open(i[5: ])
    return sum(map(lambda x: int(x.value()), rk.values()))

def main():
    print("#1", d.answer( 1, answer1(d.data(1))))
    print(d.score())

if __name__ == "__main__":
    d = pyWars.exercise()
    d.login("beer_me","beer")
    main()
    d.logout()
