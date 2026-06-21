import os


SUSPICIOUS_NAMES = {
    "xmrig",
    "nc",
    "netcat",
    "ncat",
    "socat"
}

def get_process_risk(proc):

    cpu = proc["cpu"]

    if cpu > 90:
        return "HIGH", "High CPU usage"

    if cpu > 50:
        return "MEDIUM", "Moderate CPU usage"

    return "LOW", "Normal"