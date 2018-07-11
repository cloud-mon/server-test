import app.tests.network_speedtest, app.api.cloudmon, app.tests.file_speedtest, os

print('Welcome!')
print('Now i will perform the tests.')
print('First of all the network speed app')
result = app.tests.network_speedtest.perform_test()
print(result)
#app.api.cloudmon.send_results_to_cloud_mon("1234abc", 'network_upload', result.upload)
#app.api.cloudmon.send_results_to_cloud_mon("1234abc", 'network_download', result.download)

speed = app.tests.file_speedtest.diskspeedmeasure(os.getcwd())
print("Disk writing speed: %.2f Mbytes per second" % speed)