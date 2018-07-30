import os
import time
import json
from subprocess import call


def install_fio():
    call(['apt', 'install', 'fio', '-y'])


def perform_test(volume=False):
    file_name = "tmp_result.json"
    try:
        os.remove(file_name)
    except OSError:
        pass

    file = 'fio_test_file'
    path = ''
    filesize = "3"
    if volume:
        file = '/mnt/test-volume/' + file
        path = '/mnt/test-volume/'
        filesize = "1"

    print(call(
        'fio --output-format=json --filesize='+filesize+'g --ioengine=libaio --filename=' + file + ' --overwrite=1 --invalidate=0 --direct=1 --randrepeat=0 --iodepth=64 --size=4097152k --blocksize=4k --name=random_write --rw=randwrite --end_fsync=1 --name=random_read --stonewall --rw=randread --name=mixed_randrw --stonewall --rw=randrw --rwmixread=90 --rwmixwrite=10 --end_fsync=1 >> ' + file_name,
        shell=True))
    f = open(path + file_name, "r+")
    data = json.load(f)
    result = {
        'random_write': data['jobs'][0]['write']['iops'],
        'random_read': data['jobs'][1]['read']['iops'],
        'mixed_rand_read': data['jobs'][2]['read']['iops'],
        'mixed_rand_write': data['jobs'][2]['write']['iops']
    }
    return result
