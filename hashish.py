import hashlib
from PIL import Image
import numpy as np
import sys
import random
import time
import threading

# ANSI escape codes for coloring
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BLACK = "\033[90m"
WHITE = "\033[97m"

# Logo 
logo = f"""
{MAGENTA}              ██╗  ██╗██╗  ██╗███████╗██╗  ██╗ ██╗███████╗██╗  ██╗
{CYAN}              ██║  ██║██║  ██║██╔════╝██║  ██║███║██╔════╝██║  ██║
{GREEN}              ███████║███████║███████╗███████║╚██║███████╗███████║
{YELLOW}              ██╔══██║╚════██║╚════██║██╔══██║ ██║╚════██║██╔══██║
{BLUE}              ██║  ██║     ██║███████║██║  ██║ ██║███████║██║  ██║
{RED}              ╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═╝╚══════╝╚═╝  ╚═╝
{RED}                                ...',;;:cccccccc:;,..
                            ..,;:cccc::::ccccclloooolc;'.
                         .',;:::;;;;:loodxk0kkxxkxxdocccc;;'..
                       .,;;;,,;:coxldKNWWWMMMMWNNWWNNKkdolcccc:,.
                    .',;;,',;lxo:...dXWMMMMMMMMNkloOXNNNX0koc:coo;.
                 ..,;:;,,,:ldl'   .kWMMMWXXNWMMMMXd..':d0XWWN0d:;lkd,
               ..,;;,,'':loc.     lKMMMNl. .c0KNWNK:  ..';lx00X0l,cxo,.
             ..''....'cooc.       c0NMMX;   .l0XWN0;       ,ddx00occl:.
           ..'..  .':odc.         .x0KKKkolcld000xc.       .cxxxkkdl:,..
         ..''..   ;dxolc;'         .lxx000kkxx00kc.      .;looolllol:'..
        ..'..    .':lloolc:,..       'lxkkkkk0kd,   ..':clc:::;,,;:;,'..
        ......   ....',;;;:ccc::;;,''',:loddol:,,;:clllolc:;;,'........
            .     ....'''',,,;;:cccccclllloooollllccc:c:::;,'..
                    .......'',,,,,,,,;;::::ccccc::::;;;,,''...
                      ...............''',,,;;;,,''''''......
                           ............................       
{BLACK}               
            {MAGENTA} Don't worry, the tool will be even better, be patient!{RESET}
"""

# README message with colorful enhancements
readme_message = f"""
{logo}


{CYAN}{BLACK}This tool modifies an image to create a hash that matches a specified prefix.{RESET}

{YELLOW}✨ Usage: ✨
    {GREEN}python3 hashish.py <hash_algorithm> <hex_prefix> <original_image> <output_image>{RESET}

{BLUE}🌟 Hash Algorithms Supported:
    - {RED}sha256
    - {RED}sha512
    - {RED}md5
    - {RED}sha1
    - {RED}blake2b
    - {RED}blake2s{RESET}

{MAGENTA}🎉 Example:
    {GREEN}python3 hashish.py sha256 0x24 original.jpg altered.jpg{RESET}

{CYAN}Made with ❤️ by j1md3!{RESET}
"""

def display_readme():
    print(readme_message)

def calculate_hash(file_path, algorithm):
    hasher = algorithm()
    with open(file_path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def modify_image(image_path, hex_prefix, algorithm, output_path):
    # Calculate and display the original hash
    original_hash = calculate_hash(image_path, algorithm)
    print(f"{CYAN}Original Hash: {original_hash}{RESET}")

    # Load the image
    img = Image.open(image_path)
    img_data = np.array(img)

    iteration_count = 0
    spinning_cursor = ['|', '/', '-', '\\']  # Cursor animation
    progress_bar_length = 30  # Length of the progress bar

    start_time = time.time()  # Start timing

    def display_progress():
        while True:
            for cursor in spinning_cursor:
                # Calculate progress percentage
                progress = (iteration_count % 1000) / 1000
                bar_length = int(progress_bar_length * progress)
                bar = '#' * bar_length + '-' * (progress_bar_length - bar_length)
                print(f'\r{YELLOW}Iteration: {iteration_count} {cursor} | Progress: [{bar}] {RESET}', end='', flush=True)
                time.sleep(0.1)

    # Start the progress display in a separate thread
    progress_thread = threading.Thread(target=display_progress)
    progress_thread.daemon = True
    progress_thread.start()

    while True:  # Run indefinitely until a match is found
        # Randomly modify pixel values
        for _ in range(10):  # Modify 10 pixels per iteration
            random_x = random.randint(0, img_data.shape[0] - 1)
            random_y = random.randint(0, img_data.shape[1] - 1)
            img_data[random_x, random_y] = (img_data[random_x, random_y] + random.randint(1, 10)) % 256  # Random change

        # Save the modified image
        modified_img = Image.fromarray(img_data)
        modified_img.save(output_path)

        # Calculate the hash
        hash_value = calculate_hash(output_path, algorithm)

        # Check if hash starts with the desired prefix
        if hash_value.startswith(hex_prefix):
            elapsed_time = time.time() - start_time  # Calculate elapsed time
            print(f'\r{YELLOW}Iteration: {iteration_count} {GREEN}Hash matched: {RED}{hash_value}!{RESET}')
            print(f"{GREEN}Success! {BLACK}The desired hash prefix was found in {elapsed_time:.2f} seconds.{RESET}")
            return

        iteration_count += 1

if __name__ == "__main__":
    display_readme()  # Display the README message

    if len(sys.argv) != 5:
        print("Usage: python3 hashish.py <hash_algorithm> <hex_prefix> <original_image> <output_image>")
        sys.exit(1)

    # Mapping user-friendly names to hashlib algorithms
    algorithms = {
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'blake2b': hashlib.blake2b,
        'blake2s': hashlib.blake2s,
    }

    hash_algorithm = sys.argv[1]
    if hash_algorithm not in algorithms:
        print(f"Unsupported algorithm. Choose from: {', '.join(algorithms.keys())}")
        sys.exit(1)

    hex_prefix = sys.argv[2][2:]  # Remove '0x'
    original_image = sys.argv[3]
    output_image = sys.argv[4]

    modify_image(original_image, hex_prefix, algorithms[hash_algorithm], output_image)