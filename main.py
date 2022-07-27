from disk_analyzer import DiskAnalyzer

if __name__ == "__main__":
    all_disks = DiskAnalyzer.get_disk_space_info()
    for disk in all_disks:
        print(disk)
