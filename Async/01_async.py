import asyncio

async def brew(name):
    print(f"Brewing: {name}")
    await asyncio.sleep(3)
    print(f"Finished: {name}")

async def main():
    await asyncio.gather(       #.gather() helps calling multiple times and it doon't  get blocked.
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai"),
    )


asyncio.run(main())