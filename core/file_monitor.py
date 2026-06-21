import hashlib
import os


def file_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:

        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def build_baseline(folder):

    baseline = {}

    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            try:
                baseline[path] = file_hash(path)

            except Exception as e:
                print(f"Hashing failed: {path}")
                print(e)

    return baseline



def check_changes(folder, baseline):

    alerts = []

    current = build_baseline(folder)

    print("\nBASELINE:")
    for k, v in baseline.items():
        print(k)

    print("\nCURRENT:")
    for k, v in current.items():
        print(k)

    
    for file in current:

        if file not in baseline:

            alerts.append(
                (
                    "INFO",
                    f"File Created: {os.path.basename(file)}"
                )
            )

    
    for file in baseline:

        if file not in current:

            alerts.append(
                (
                    "WARNING",
                    f"File Deleted: {os.path.basename(file)}"
                )
            )

    
    for file in current:

        if file in baseline:

            if current[file] != baseline[file]:

                alerts.append(
                    (
                        "HIGH",
                        f"File Modified: {os.path.basename(file)}"
                    )
                )

    return alerts, current