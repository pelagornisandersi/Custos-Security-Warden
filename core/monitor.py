import psutil


def get_cpu_usage():
    return psutil.cpu_percent()


def get_ram_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage("/").percent

