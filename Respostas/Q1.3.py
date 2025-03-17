import asyncio
import os
import time
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

async def process_image(image_path, output_folder):
    try:
        image = Image.open(image_path).convert("RGBA")
        image = image.filter(ImageFilter.BLUR)
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        image.save(output_path)
    except:
        pass

async def process_images(input_folder, output_folder):
    tasks = []
    for image_name in os.listdir(input_folder):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, image_name)
            tasks.append(process_image(image_path, output_folder))
    await asyncio.gather(*tasks)

def measure_performance(input_folder, output_folder, num_threads_list):
    times = []
    for num_threads in num_threads_list:
        os.environ["PYTHONASYNCIODEBUG"] = str(num_threads)
        start_time = time.perf_counter()
        asyncio.run(process_images(input_folder, output_folder))
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times

def main():
    input_folder = "input_images"
    output_folder = "output_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    num_threads_list = [1, 2, 4, 8, 16]
    times = measure_performance(input_folder, output_folder, num_threads_list)

    plt.plot(num_threads_list, times, marker='o')
    plt.xlabel("Número de Threads")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Desempenho do Processamento de Imagens Assíncrono")
    plt.show()

if __name__ == "__main__":
    main()
