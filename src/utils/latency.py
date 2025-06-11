def measure_latency(func):
    """Execute *func* and return the time it took in seconds."""
    import time
    start_time = time.time()
    func()
    end_time = time.time()
    latency = end_time - start_time
    print(f"Latency for {func.__name__}: {latency:.4f} seconds")
    return latency


def analyze_latency(data):
    """Return average latency from a sequence of values."""
    return {"average_latency": sum(data) / len(data) if data else 0}
