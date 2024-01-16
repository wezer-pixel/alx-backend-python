#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The maximum delay for each execution of wait_random.

    Returns:
        List[float]: A sorted list of the wait times for each execution of wait_random.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
