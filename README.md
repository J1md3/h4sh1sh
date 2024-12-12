              ██╗  ██╗██╗  ██╗███████╗██╗  ██╗ ██╗███████╗██╗  ██╗
              ██║  ██║██║  ██║██╔════╝██║  ██║███║██╔════╝██║  ██║
              ███████║███████║███████╗███████║╚██║███████╗███████║
              ██╔══██║╚════██║╚════██║██╔══██║ ██║╚════██║██╔══██║
              ██║  ██║     ██║███████║██║  ██║ ██║███████║██║  ██║
              ╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═╝╚══════╝╚═╝  ╚═╝
                                ...',;;:cccccccc:;,..
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
              
              
## Image Hash Modifier

A Python tool that modifies an image to create a hash that matches a specified prefix.

 This project utilizes various hashing algorithms and provides a colorful command-line interface.

## Features

- Modify images randomly until a hash with a specified prefix is generated.
- Supports multiple hashing algorithms.

## Requirements

- Python 3.x
- Required libraries:
  - `Pillow` (for image processing)
  - `NumPy` (for numerical operations)

You can install the required libraries using pip:

```bash
pip install pillow numpy

```



✨ Usage: ✨

    python3 hashish.py <hash_algorithm> <hex_prefix> <original_image> <output_image>

🌟 Hash Algorithms Supported:
    - sha256
    - sha512
    - md5
    - sha1
    - blake2b
    - blake2s

🎉 Example:
    python3 hashish.py sha256 0x24 original.jpg altered.jpg

Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

Acknowledgments

Made with ❤️ by j1md3!

