from core.monitor import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage
)


def calculate_score():

    score = 100

    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()

    if cpu > 90:
        score -= 5

    if ram > 90:
        score -= 5

    if disk > 90:
        score -= 10

    return max(score, 0)