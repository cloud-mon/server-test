import app.tests.network_speedtest, app.api.cloudmon

print('Welcome!')
print('Now i will perform the tests.')
print('First of all the network speed app')
result = app.tests.network_speedtest.perform_test()
print(result)
app.api.cloudmon.send_results_to_cloud_mon("1234abc", 'network_upload', result.upload)
app.api.cloudmon.send_results_to_cloud_mon("1234abc", 'network_download', result.download)
