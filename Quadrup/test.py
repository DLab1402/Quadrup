import asyncio

async def my_coroutine():
    print("Start of the coroutine")
    await asyncio.sleep(2)
    print("End of the coroutine")

async def main():
    print("Before coroutine")

    # Run the coroutine in the background
    task = asyncio.create_task(my_coroutine())

    # Continue with other tasks while my_coroutine is running
    print("Doing other tasks...")

    # Wait for the background task to complete
    await task

    print("After coroutine")

# Run the event loop
asyncio.run(main())
