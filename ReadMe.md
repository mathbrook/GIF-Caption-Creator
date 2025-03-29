<p align=center><a href=http://ifunny.co><img src=https://raw.githubusercontent.com/UhhhAaron/iFunny-Captions/master/Documents/Pictures/Main/gifcaptioncreator.png width=675></a></p>

<p align=center><a href=http://python.org/downloads/release/python-3120><img src=https://img.shields.io/badge/Python-3.12.0-brightgreen?logo=python&logoColor=white&link=http://python.org/downloads/release/python-3120&style=for-the-badge></a>

<p align=center><a href=http://github.com/UhhhAaron/iFunny-Captions/releases/><img src=https://img.shields.io/github/v/release/UhhhAaron/iFunny-Captions?style=for-the-badge></a> <a href=http://github.com/UhhhAaron/iFunny-Captions/blob/master/License.txt><img src=https://img.shields.io/github/license/UhhhAaron/iFunny-Captions?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

### GIF-Caption-Creator is a tool designed to create GIF captions nearly identical to the "iFunny" caption style.

## Capabilities 
|  | iFunny App | `GIF-Caption-Creator` |
|:-:|:-:|:-:|
| PNG Captions | ✔️ | ✔️ |
| GIF Captions | ✔️ | ✔️ |
| MP4 Captions | ✔️ | ✔️ |
| Image optimization | ❌ | ✔️ |
| Custom Fonts | ❌ | ✔️ |
| Emoji support | ✔️ | ✔️ |
| Crop support | ✔️ | ❌ |
| Graphical User Interface | ✔️ | ❌ |
| Batch Processing | ❌ | ✔️ |
---
## Completed & Planned Features
- ✔️ PNG Captions
- ✔️ GIF Captions
- ✔️ Local file support
- ✔️ GIF size reduction
- ✔️ Custom fonts support
- ✔️ Transparent GIF support
- ✔️ Emoji support<sup>3</sup>
- ✔️ Automatic text wrap
- ❌ User-friendly GUI (4.0)
- ❌ Convenient setup process (4.0)

<sup>1</sup> - Please look at [Custom Fonts](http://github.com/UhhhAaron/GIF-Caption-Creator/wiki/Custom-Fonts) section in wiki.<br>
<sup>2</sup> - Problems with wrap height might occur.

## Requirements
Programs:
- [`Python >= 3.10`](http://www.python.org/downloads) 

Modules:
- [`Pillow >= 10.0`](http://github.com/python-pillow/Pillow) - Making images
- [`requests >= 2.13`](http://github.com/psf/requests) - URL fetching 
- [`emoji == 1.6.1`](http://github.com/carpedm20/emoji) - Text to emoji support (support for modern versions of this package soon)
- [`clipboard >= 0.0.4`](http://github.com/terryyin/clipboard) - Clipboard values handling 
- [`sty >= 0.0.4`](https://github.com/feluxe/sty) - Colored prints 
- [`colour >= 0.1.5`](https://github.com/vaab/colour) - Colored text values handling 
- [`unidecode`](http://github.com/avian2/unidecode) - [Text normalization](http://wikipedia.org/wiki/Text_normalization#Techniques) 
- [`distro >= 1.7`](https://github.com/python-distro/distro)<sup>1</sup> - Directory opening helper 
- [`pyshortcuts >= 1.8`](https://github.com/newville/pyshortcuts) - Shortcuts making 

Packages (bold links are **Windows** static executable binaries):
- [**`FFmpeg >= 4.2.0`**](http://videohelp.com/software/ffmpeg/old-versions) - Since `PIL.ImageSequence.Iterator` messes up the frames colors.
- [**`Gifsicle >= 1.92-2`**](http://eternallybored.org/misc/gifsicle/releases) - **Check after 64-bit if possible!** ([`Scale_Back`](http://github.com/kubinka0505/iFunny-Captions/wiki/Known-Issues-%F0%9F%93%9D%F0%9F%90%9B#4-scale_back-option-doesnt-work) option)
- [**`PNGQuant >= 2.14`**](http://pngquant.org/#download) *(optional)*
- [**`OxiPNG >= 5.0.1`**](https://github.com/shssoichiro/oxipng/releases) *(optional)*
- [`Python3-PIP`](http://packages.debian.org/sid/python3-pip)</a><sup>1</sup>
- [`Python3-TK`](http://packages.debian.org/sid/python3-tk)</a><sup>1</sup>

<sup>1</sup> - Required on Linux

The direct executable path for FFmpeg must be added to the "Path" Environment variable on Windows (for the time being).
---
## Linux Installation & Usage
`sudo apt-get install git python3-apt python3-pip python3-tk ffmpeg pngquant gifsicle`

**For non-Debian distros, use the equivalent package manager to install these dependencies.**
1. Clone the repository and move to its directory.
	```bash
	git clone http://github.com/UhhhAaron/GIF-Caption-Creator
	cd iFunny-Captions
	```
2. Install required modules	by inputting `pip install -r requirements.txt`
3. Allocate [the required files](http://github.com/UhhhAaron/GIF-Caption-Creator#requirements-) to `PATH` system environment variable.
4. Modify the parameters in the `Config.json` file. [Its documentation can be found here](http://github.com/UhhhAaron/GIF-Caption-Creator/wiki/Configuration-Documentation).
5. Open shell script file named `Run`. Supports positional arguments - type `python iFunny_Captions.pyw -h` for more.
6. Output should be in the `Images` folder.

## Support
This project was tested on:
| OS | Python Version |
|:-:|:-:|
Windows 10 | 3.12.0 

[**If there are problems, create an issue here.**](http://github.com/UhhhAaron/GIF-Caption-Creator/issues/new/choose)

---
### Supported GIF services

All GIF hosting sites are supported, as long as you have access to the raw URL for the GIF file you want to use.
---
### Comparisons

- | iFunny Android App | `GIF-Caption-Creator` |
  |:-:|:-:|
  | <img src=https://raw.githubusercontent.com/UhhhAaron/GIF-Caption-Creator/master/Documents/Pictures/Comparison_Graphics/1/iFunny.gif width=150> | <img src=https://raw.githubusercontent.com/UhhhAaron/GIF-Caption-Creator/master/Documents/Pictures/Comparison_Graphics/1/iFunny-Captions.gif width=150> 
  | <img src=https://raw.githubusercontent.com/UhhhAaron/GIF-Caption-Creator/master/Documents/Pictures/Comparison_Graphics/2/iFunny.gif width=150> | <img src=https://raw.githubusercontent.com/UhhhAaron/GIF-Caption-Creator/master/Documents/Pictures/Comparison_Graphics/2/iFunny-Captions.gif width=150> |
