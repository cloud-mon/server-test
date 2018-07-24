import speedtest


def perform_test():
    s = speedtest.Speedtest()

    best_server = s.get_best_server()
    print('Best server: ')
    print(best_server['name'])

    print('Perform upload app:')
    result = s.upload()
    print('Done:' + str(result / 1024 / 1024) + ' MBit/s')
    print('Perform download app:')
    result = s.download()
    print('Done:' + str(result / 1024 / 1024) + ' MBit/s')

    print(s.results)
    return s.results
