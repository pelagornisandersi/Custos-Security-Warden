import psutil


def get_top_processes(limit=10):

    processes = []

    for proc in psutil.process_iter(
        ['pid', 'name', 'cpu_percent']
    ):
        try:
            processes.append({
                "pid": proc.info["pid"],
                "name": proc.info["name"],
                "cpu": proc.info["cpu_percent"]
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            continue

    processes.sort(
        key=lambda x: x["cpu"],
        reverse=True
    )

    return processes[:limit]

def get_process_risk(proc):

    cpu = proc["cpu"]

    if cpu > 90:
        return "HIGH", "High CPU usage"

    elif cpu > 50:
        return "MEDIUM", "Moderate CPU usage"

    else:
        return "LOW", "Normal"        