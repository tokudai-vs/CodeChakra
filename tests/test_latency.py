import time
from src.utils.latency import measure_latency


def test_measure_latency():
    def sample_function():
        time.sleep(0.1)

    latency = measure_latency(sample_function)
    assert latency >= 0.1
    assert latency < 0.2
