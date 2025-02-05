import asyncio
import os
from PIL import Image, ImageFilter
import time

async def process_image(image_path, output_folder):
    try:
        image = Image.open(image_path)
        image = image.filter(ImageFilter.BLUR)
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        image.save(output_path)
        print(f"Processada: {image_path}")
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")

async def process_images(input_folder, output_folder):
    tasks = []
    for image_name in os.listdir(input_folder):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, image_name)
            tasks.append(process_image(image_path, output_folder))
    await asyncio.gather(*tasks)

def main():
    input_folder = "input_images"
    output_folder = "output_images"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    start_time = time.perf_counter()
    asyncio.run(process_images(input_folder, output_folder))
    end_time = time.perf_counter()
    
    print(f"Tempo total de execução: {end_time - start_time:.4f} segundos")

if __name__ == "__main__":
    main()
