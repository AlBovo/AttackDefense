import nmap

#this aint it chief, va migliorato -R

nm = nmap.PortScanner()

for i in range(1, 88):
    ip_address = f'10.60.{i}.1'
    print(f"Scanning {ip_address}...")
    nm.scan(ip_address, '22-5000')

    for host in nm.all_hosts():
        print(f'Host : {host} ({nm[host].hostname()})')
        print(f'State : {nm[host].state()}')
        for proto in nm[host].all_protocols():
            print(f'----------')
            print(f'Protocol : {proto}')

            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print(f'port : {port}\tstate : {nm[host][proto][port]["state"]}')
