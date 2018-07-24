import api.cloudmon
import os
import sys
import tests.file_speedtest
import tests.network_speedtest


def main():
    print('Welcome!')
    print(sys.argv)
    if len(sys.argv) > 0:
        api_token = sys.argv[1]
    else:
        api_token = 'UNKNOWN'

    print(api_token)
    print('Now i will perform the tests.')
    print('First of all the network speed app')
    result = tests.network_speedtest.perform_test()
    print(result)

    speed = tests.file_speedtest.diskspeedmeasure(os.getcwd())
    print("Disk writing speed: %.2f Mbytes per second" % speed)
    if api_token != 'UNKNOWN':
        api.cloudmon.send_results_to_cloud_mon(api_token, 'network_upload', result.upload)
        api.cloudmon.send_results_to_cloud_mon(api_token, 'network_download', result.download)
        api.cloudmon.send_results_to_cloud_mon(api_token, 'disk_speed', speed)


if __name__ == "__main__":
    main()
