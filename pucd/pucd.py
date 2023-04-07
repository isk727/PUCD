#!/usr/bin/env python3
import os
import sys
import sqlite3
from socket import socket, AF_INET, SOCK_DGRAM
from config import _DBNAME, _HOST, _PORT, _SQL, _PIDFILE

def main_unit():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((_HOST, _PORT))
    while True:
        msg, address = s.recvfrom(8192)
        writeCom(msg, address[0])

def daemonize():
    pid = os.fork()#ここでプロセスをforkする
    if pid > 0:#親プロセスの場合(pidは子プロセスのプロセスID)
        pid_file = open(_PIDFILE, 'w')
        pid_file.write(str(pid)+"\n")
        pid_file.close()
        sys.exit()
    if pid == 0:#子プロセスの場合
        main_unit()

def writeCom(msg, address):
#    dbname = 'udp.db'
    conn = sqlite3.connect(_DBNAME)
    cur = conn.cursor()
    data = [msg, address]
    cur.execute(_SQL, data)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    while True:
        daemonize()
