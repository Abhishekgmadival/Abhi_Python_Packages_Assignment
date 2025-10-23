import statistics

def calculate_mean(data):
    if not data:
        return None
    return statistics.mean(data)

def calculate_median(data):
    if not data:
        return None
    return statistics.median(data)

def calculate_mode(data):
    if not data:
        return None
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        # If no unique mode, return None or list
        # We'll return the multimode result for clarity
        return statistics.multimode(data)
