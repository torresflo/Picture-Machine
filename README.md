![GitHub license](https://img.shields.io/github/license/torresflo/Picture-Machine.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/Picture-Machine.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/Picture-Machine.svg)

<p align="center">
  <h1 align="center">Picture Machine</h3>

  <p align="center">
    A little Python application to generate pictures from a text prompt.
    Based on <a href="https://github.com/CompVis/stable-diffusion">Stable Diffusion</a>.
    <br />
    <a href="https://github.com/torresflo/Picture-Machine/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites and dependencies](#prerequisites-and-dependencies)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Getting Started

### Prerequisites and dependencies

This repository is tested on Python 3.7+ and PyTorch LTS 1.8.2. It works only Nvidia graphics cards and CUDA should be installed.

You should install Picture Machine in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
First, create a virtual environment with the version of Python you're going to use and activate it.

Then, you will need to install PyTorch.
Please refer to [PyTorch installation page](https://pytorch.org/get-started/locally/#start-locally) regarding the specific install command for your platform.

When PyTorch is installed, 🤗 Transformers can be installed using pip as follows:

```bash
pip install transformers
```

You can refer to the repository of [🤗 Transformers](https://github.com/huggingface/transformers) for more information.

Then you will need to install diffusers using pip as follows:

```bash
pip install diffusers
```

Finally you will need to install PySide6, a port of QT for Python used for the graphic interface. It can be installed using pip as follows:

```bash
pip install pyside6
```

Optional but recommended, to have faster generation, you can also install scipy and ftfy:
```bash
pip install scipy ftfy
```

### Installation

Follow the instructions above then clone the repo (`git clone https:://github.com/torresflo/Picture-Machine.git`). You can now run `main.py`.

## Usage

The image generation and if it is possible or not will depends of your hardware.
This project has been tested on a Nvidia RTX 3070 with 8Gb of VRAM. With this hardware, it allows to generate images with a size of 512 x 512 pixels in around 10 seconds.

Enter your prompt and then press "generate" to generate an image. You can then click on the image to save it if you want to.

### Available parameters ###

<u>Image size (width and height):</u>

These are some recommendations to choose good image sizes:
- Make sure height and width are both multiples of 8.
- Going below 512 might result in lower quality images.
- Going over 512 in both directions will repeat image areas (global coherence is lost).
- The best way to create non-square images is to use 512 in one dimension, and a value larger than that in the other one.

<u>Iteration steps:</u>

You can change the number of inference steps using the this parameter. In general, results are better the more steps you use. Stable Diffusion, being one of the latest models, it works great with a relatively small number of steps (default is 50). If you want faster results you can use a smaller number here.

<u>Guidance scale:</u>

The last parameter is the guidance_scale. It is a way to increase the adherence to your prompt as well as overall sample quality. In simple terms, it forces the generation to better match with your prompt. Numbers like 7 or 8.5 give good results, if you use a very large number the images might look good, but will be less diverse.

### Screenshot ###

![Example image](https://github.com/torresflo/Picture-Machine/blob/main/examples/Example1.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
