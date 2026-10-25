import asyncio, httpx, time, aiohttp


async def get_data(i: int, endpoint: str):
    start = time.time()
    print(f"Start runnning {endpoint}: {i}")
    url = f"http://127.0.0.1:8000/{endpoint}/{i}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:

            print(f"Finisher running {endpoint}: {i} in {time.time() - start:.2f}s")


async def main():
    # sync endpoint
    # start = time.time()
    # await asyncio.gather(
    #     *[get_data(i, "sync") for i in range(300)]
    # )
    # print(f"Finished running ALL in {time.time() - start:.2f}s")


    # async endpoint
    start = time.time()
    await asyncio.gather(
        *[get_data(i, "async") for i in range(300)]
    )
    print(f"Finished running ALL in {time.time() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
