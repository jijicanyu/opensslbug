import ssl,socket,sys
 
SSL_VERSION={
    'SSLv2':ssl.PROTOCOL_SSLv2,
    'SSLv3':ssl.PROTOCOL_SSLv3,
    'SSLv23':ssl.PROTOCOL_SSLv23,
    'TLSv1':ssl.PROTOCOL_TLSv1,
}
 
def check_ssl_version(version):
    try:
        https = ssl.SSLSocket(socket.socket(),ssl_version=SSL_VERSION.get(version))
        c = https.connect((ip,port))
        print version + ' Supported'
        return True
    except Exception as e:
        return False
 
USAGE = '==========\nKPoodle - SSL version and poodle attack vulnerability detect tool\n==========\nUsage: python kpoodle.py target port(default:443)\n\nby kingx'
try:
    ip = sys.argv[1]
except:
    print USAGE
    sys.exit()
try:
    port = int(sys.argv[2])
except:
    port = 443
 
try:
    print 'Connecting...'
    s = socket.socket().connect((ip,port))
except Exception as e:
    print e
    print 'Can not connect to the target!'
    sys.exit()
 
try:
    print 'Checking...'
    ssl3 = check_ssl_version('SSLv3')
    ssl2 = check_ssl_version('SSLv2')
    ssl23 = check_ssl_version('SSLv23')
    tls = check_ssl_version('TLSv1')
    if ssl3:
        print '\nSSLv3 Poodle Vulnerable!'
    else:
        print '\nNo SSLv3 Support!'
except Exception as e:
    print e
