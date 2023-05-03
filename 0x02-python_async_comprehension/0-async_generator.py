#!/usr/bin/env python3
"""
Function for Async Generator
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that returns a randomn number between 1 - 10 after looping,
    each time 1s asynchronously waiting 1 second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
