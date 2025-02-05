import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt

async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Downloaded {url}: {len(content)} bytes")

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts"
    ]
    
    num_threads = [1, 2, 3, 4, 5]
    times = []
    
    for num in num_threads:
        start_time = time.perf_counter()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*(download_url(session, url) for url in urls[:num]))
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    
    plt.plot(num_threads, times)
    plt.xlabel('Número de Threads')
    plt.ylabel('Tempo (segundos)')
    plt.title('Número de Threads x Tempo de Download')
    plt.show()

    print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")
