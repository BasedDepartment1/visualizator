import matplotlib.pyplot as plt
from disk_analyzer import DiskAnalyzer


class Visualizer:
    @staticmethod
    def visualize():
        labels = ["used", "free"]
        colors = ["gray", "white"]
        explode = [0.3, 0]
        all_disks = DiskAnalyzer.get_disk_space_info()
        for disk in all_disks:
            values = [disk.used, disk.free]
            plt.title(f"Disk {disk.name}, total: {disk.total} bytes",
                      fontdict={"fontsize": 16})
            plt.pie(values, labels=labels,
                    colors=colors, explode=explode,
                    shadow=True, autopct='%1.1f%%',
                    startangle=180, textprops={"fontsize": 16})

            plt.axis('equal')
            plt.show()
