# Asynchronous Python Tasks

This repository contains Python modules implementing various asynchronous tasks using the `asyncio` library. Each task is designed to demonstrate different aspects of asynchronous programming in Python.

## Task 0: Basic Async Syntax

File: `0-basic_async_syntax.py`

This module provides a basic asynchronous function named `wait_random`. It asynchronously waits for a random number of seconds, with the maximum delay specified as an argument.

## Task 1: Concurrent Coroutines

File: `1-concurrent_coroutines.py`

In this module, there is an asynchronous function `wait_n` that executes the `wait_random` function multiple times concurrently using `asyncio.gather`. It returns a sorted list of the wait times for each execution.

## Task 2: Measure Time

File: `2-measure_time.py`

The `measure_time` function in this module calculates the average runtime of the `wait_n` function over multiple calls. It takes the number of calls (`n`) and the maximum delay as parameters.

## Task 3: Creating an Async Task

File: `3-tasks.py`

The `task_wait_random` function creates an asynchronous task for the `wait_random` function using `asyncio.create_task`. This task can be scheduled for execution in an event loop.

## Task 4: Executing Tasks Concurrently

File: `4-executing_tasks.py`

The `task_wait_n` function in this module executes the `task_wait_random` function multiple times concurrently using `asyncio.gather`. It returns a sorted list of the wait times for each task.

## How to Run

To run any of the tasks, execute the corresponding Python file using the Python 3 interpreter:

```bash
python3 <filename>.py
