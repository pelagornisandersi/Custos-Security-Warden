import psutil


def get_connections(limit=20):

    connections = []
    

    for conn in psutil.net_connections(kind="inet"):

        try:

            if not conn.raddr:
                continue

            pid = conn.pid

            if pid is None:
                continue

            process = psutil.Process(pid)

            connections.append({
                "process": process.name(),
                "pid": pid,
                "remote_ip": conn.raddr.ip,
                "remote_port": conn.raddr.port
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            continue

    return connections[:limit]