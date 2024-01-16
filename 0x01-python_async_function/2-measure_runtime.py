#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds for each call to wait_n.

    Returns:
        float: The average runtime of wait_n in seconds.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
