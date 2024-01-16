#!/usr/bin/env python3
'''Task 3's module.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asynchronous task for wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asynchronous task that will execute the wait_random function.
    '''
    return asyncio.create_task(wait_random(max_delay))
