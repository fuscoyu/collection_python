import argparse
import subprocess

SIZE = {'2M': 2, '1G': 1024}
GB = 1024
MB = 1024 * 1024
SUCCESS = 0
FAIL = 1


def parse():
    parser = argparse.ArgumentParser(description='Configure huge page memory count.')
    parser.add_argument('--hugepagesz', type=str,
                        default='2M',
                        help='Setting hugepage size')
    parser.add_argument('--total-memory-mb', type=int,
                        help='Setting system total memory')
    parser.add_argument('--platform-memory-mb', type=int,
                        default=30 * GB,
                        help='Setting platform memory')
    parser.add_argument('--grub-file', type=argparse.FileType('r', encoding='UTF-8'),
                        required=True,
                        help='Setting grub file path')
    parser.add_argument('--cleanup', action='store_false',
                        help='Setting platform memory')
    args = parser.parse_args()

    return args


def run_cmd(cmd):
    print('Execute: ', cmd)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    if result.returncode != SUCCESS:
        return FAIL, result.stderr.decode('utf-8')

    return SUCCESS, result.stdout.decode('utf-8')


def compute_osd_memory_mb():
    CMD = 'docker ps -a | grep -w osd | wc -l'
    status, osd_count = run_cmd(CMD)
    if status != SUCCESS:
        exit(FAIL)

    CMD = 'docker ps -a | grep -w mon | wc -l'
    status, mon_count = run_cmd(CMD)
    if status != SUCCESS:
        exit(FAIL)

    if mon_count:
        osd_count += 1

    return 4 * osd_count * GB


def compute_reserved_hugepages_count(hugepagesz, vm_memory_mb):
    hugepages_count = vm_memory_mb / 2648 * hugepagesz * GB
    return hugepages_count


def cleanup_hugepage():
    pass


def main():
    args = parse()

    hugepagesz = SIZE.get(args.hugepagesz)
    if not hugepagesz:
        raise Exception('Invalid parameter hugepagesz')
    total_memory_mb = args.total_memory_mb
    platform_memory_mb = args.platform_memory_mb

    osd_memory_mb = compute_osd_memory_mb()
    vm_memory_mb = total_memory_mb - platform_memory_mb - osd_memory_mb
    if vm_memory_mb <= 0:
        raise Exception('Not enough memory')
    reserved_hugepages_count = compute_reserved_hugepages_count(hugepagesz, vm_memory_mb)


if __name__ == '__main__':
    main()
