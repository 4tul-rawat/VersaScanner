from zapv2 import ZAPv2
import time

# ZAP Proxy settings
zap_address = 'localhost'
zap_port = '8080'
zap_api_key = 'your_api_key'  # Change to your API key, if you have set one

# Target to scan
target_url = 'http://www.itsecgames.com/'  # Change to your target

# Initialize the ZAP API
zap = ZAPv2(apikey=zap_api_key, proxies={'http': f'http://{zap_address}:{zap_port}', 'https': f'http://{zap_address}:{zap_port}'})

# Start a new session
zap.core.new_session(name='newsession', overwrite=True)

# Spider the target
print(f'Spidering target {target_url}')
scan_id = zap.spider.scan(target_url)
time.sleep(2)

# Wait for the spider to finish
while int(zap.spider.status(scan_id)) < 100:
    print(f'Spider progress: {zap.spider.status(scan_id)}%')
    time.sleep(2)
print('Spider completed')

# Start the active scanner
print(f'Scanning target {target_url}')
scan_id = zap.ascan.scan(target_url)
while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan_id)}%')
    time.sleep(5)
print('Scan completed')

# Report the results
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
alerts = zap.core.alerts(baseurl=target_url)
for alert in alerts:
    print(f"Alert: {alert['alert']}, Risk: {alert['risk']}, URL: {alert['url']}")

# Optionally, save the session
# zap.core.save_session(name='mysession')

# Optionally, close ZAP
# zap.core.shutdown()
