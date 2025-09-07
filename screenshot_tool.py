#!/usr/bin/env python3
"""
Screenshot tool using Playwright to capture https://peerpressure.social
"""
import asyncio
from playwright.async_api import async_playwright
import os

async def take_screenshot():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Set viewport size to capture header and hero section well
        await page.set_viewport_size({"width": 1200, "height": 800})
        
        try:
            print("Navigating to https://peerpressure.social...")
            await page.goto("https://peerpressure.social", wait_until="networkidle", timeout=30000)
            
            # Wait a bit more to ensure all elements are loaded
            await page.wait_for_timeout(2000)
            
            # Take screenshot focusing on header and hero section
            screenshot_path = "/Users/anneschuth/peerpressure/peerpressure-landing/peerpressure_screenshot.png"
            await page.screenshot(path=screenshot_path, full_page=False)
            
            print(f"Screenshot saved to: {screenshot_path}")
            
            # Also get page title and some basic info
            title = await page.title()
            print(f"Page title: {title}")
            
        except Exception as e:
            print(f"Error taking screenshot: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(take_screenshot())