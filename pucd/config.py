_HOST = ''
_PORT = 8080
_PIDFILE = '/var/run/pucd.pid'
_DBNAME = '/usr/share/pucd/udp.db'
_SQL = 'INSERT INTO udp (ud, fm, dt) values (?,?, datetime(\'now\', \'localtime\'))'
