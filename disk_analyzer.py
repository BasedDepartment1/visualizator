import psutil
from disk import Disk


class DiskAnalyzer:
    @staticmethod
    def get_disk_space_info() -> list[Disk]:
        all_disk_partitions = [disk[0] for disk in
                               psutil.disk_partitions(True)]

        return [Disk(disk[0], *psutil.disk_usage(disk)) for disk in
                all_disk_partitions]
