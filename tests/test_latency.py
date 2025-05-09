import time
import pytest
from src.utils.latency import measure_latency

def test_measure_latency():
    # A sample function to test latency measurement
    def sample_function():
        time.sleep(0.1)  # Simulate a delay

    latency = measure_latency(sample_function)
    assert latency >= 0.1, "Latency should be at least 0.1 seconds"
    assert latency < 0.2, "Latency should be less than 0.2 seconds"