import os
import time
from subprocess import call


def install_fio():
    call(['apt', 'install', 'fio', '-y'])


def perform_test():
    fileName = "tmp_result.json"
    f = open(fileName, "w+")
    print(call(
        'fio --output-format=json --filesize=3g --ioengine=libaio --filename=fio_test_file --overwrite=1 --invalidate=0 --direct=1 --randrepeat=0 --iodepth=64 --size=4097152k --blocksize=4k --name=random_write --rw=randwrite --end_fsync=1 --name=random_read --stonewall --rw=randread --name=mixed_randrw --stonewall --rw=randrw --rwmixread=90 --rwmixwrite=10 --end_fsync=1', shell=True))
    tmp = f.read()
    print(tmp)
    os.remove(fileName)

    return tmp
