import socket
import time

startTime = time.time()

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    ip_addr = socket.gethostbyname(target)
    print('[*] IP Address found\n')
    print('[*] Starting scan on host: ', ip_addr)

    for i in range(1, 1235):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = s.connect_ex((ip_addr, i))
        #print('[*] Port scanning started')
        if(conn == 0):
            print('[*] Port %d: OPEN' % (i,))
            print(conn)
        s.close()
print('[*] Time Taken: ', time.time() - startTime)
