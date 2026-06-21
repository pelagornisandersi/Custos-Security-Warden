active_alerts = {}


def raise_alert(alert_id):

    if alert_id in active_alerts:
        return False

    active_alerts[alert_id] = True
    return True


def clear_alert(alert_id):

    active_alerts.pop(alert_id, None)