from unittest import result
import paramiko
import time

host = '217.21.77.137'
user = 'u108653975'
password = 'GioSer159A7!'
port = 65002


if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username=user, password=password)

    stdin, stdout, stderr = client.exec_command('cd public_html/public_html; ls')
    time.sleep(1)

    result = stdout.read().decode()

    print(result)