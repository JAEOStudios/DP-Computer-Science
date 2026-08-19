# A1-StorageSpeeds.py
# Lesson A1-3 - Secondary Storage, Compression & SaaS
# Vibecoded slop to give an example of how much the reading time differs between medium
#
# One question, asked of six devices: how long does it take to read a file?
# Transfer rates are typical consumer figures, rounded for teaching.

FILE_SIZES_GB = [0.005, 1, 4, 50]

DEVICES = [
    # name,                        MB/s,  moving parts?
    ("Registers / cache / RAM", 20000, "n/a - not storage"),
    ("Internal SSD (NVMe)", 3500, "no"),
    ("Internal SSD (SATA)", 550, "no"),
    ("Internal HDD (7200 rpm)", 120, "yes"),
    ("eMMC (phone / cheap tablet)", 250, "no"),
    ("USB 3 flash drive", 90, "no"),
    ("External HDD over USB 3", 110, "yes"),
    ("DVD drive (16x)", 22, "yes"),
]


def seconds_to_read(size_gb, rate_mb_per_s):
    megabytes = size_gb * 1000
    return megabytes / rate_mb_per_s


def friendly(seconds):
    if seconds < 1:
        return "{:.1f} ms".format(seconds * 1000)
    if seconds < 90:
        return "{:.1f} s".format(seconds)
    if seconds < 5400:
        return "{:.1f} min".format(seconds / 60)
    return "{:.1f} hours".format(seconds / 3600)


def main():
    print("TIME TO READ A FILE, BY DEVICE")
    print("(RAM is in the table only to show the stark difference.)")
    for size in FILE_SIZES_GB:
        label = "{:.0f} MB".format(size * 1000) if size < 1 else "{:.0f} GB".format(size)
        print()
        print("=" * 68)
        print("FILE SIZE: " + label)
        print("=" * 68)
        print("{:<30}{:>10}{:>14}{:>20}".format("device", "MB/s", "time", "moving parts"))
        for name, rate, moving in DEVICES:
            print("{:<30}{:>10}{:>14}{:>20}".format(
                name, rate, friendly(seconds_to_read(size, rate)), moving))

    print()
    print("-" * 68)
    hdd = seconds_to_read(4, 120)
    nvme = seconds_to_read(4, 3500)
    print("Same 4 GB file: HDD {}, NVMe SSD {}.".format(friendly(hdd), friendly(nvme)))
    print("That is {:.1f}x, and the only difference is whether something spins.".format(hdd / nvme))
    print("-" * 68)


if __name__ == "__main__":
    main()