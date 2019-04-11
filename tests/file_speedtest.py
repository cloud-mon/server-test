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
    filesize = "3"
    if volume:
        file = '/mnt/test_volume/' + file
        path = '/mnt/test_volume/'
        file_name = path + "tmp_result.json"
        filesize = "10"

    command = 'fio --output-format=json --filesize=' + filesize + 'g --ioengine=libaio --filename=' + file + ' --overwrite=1 --invalidate=0 --direct=1 --randrepeat=0 --iodepth=64 --size=4097152k --blocksize=4k --name=random_write --rw=randwrite --end_fsync=1 --name=random_read --stonewall --rw=randread --name=mixed_randrw --stonewall --rw=randrw --rwmixread=90 --rwmixwrite=10 --end_fsync=1 --runtime=600>> ' + file_name,
    print(command)
    call(command,
         shell=True)
    f = open(file_name, "r+")
    data = json.load(f)
    result = {
        'random_write': data['jobs'][0]['write']['iops'],
        'random_read': data['jobs'][1]['read']['iops'],
        'mixed_rand_read': data['jobs'][2]['read']['iops'],
        'mixed_rand_write': data['jobs'][2]['write']['iops']
    }
    return result
