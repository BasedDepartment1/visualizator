from dataclasses import dataclass


@dataclass
class Disk:
    name: str
    total: str
    used: str
    free: str
    percent: str

    def __str__(self):
        return f"Disk {self.name}\n" \
               f"Total space available (bytes): {self.total}\n" \
               f"Used space (bytes): {self.used}\n" \
               f"Free space (bytes): {self.free}\n" \
               f"Used, percent: {self.percent}"
