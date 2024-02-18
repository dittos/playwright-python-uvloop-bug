import asyncio
import uvloop
from playwright.sync_api import sync_playwright

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

with sync_playwright() as p:
    print("got it:", p)
