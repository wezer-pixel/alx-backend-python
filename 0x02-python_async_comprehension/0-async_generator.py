#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 random floating-point numbers between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.

    Raises:
        None

    Returns:
        None
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
