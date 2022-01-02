# Mdisk


## Install

- For [Package](https://github.com/heimanpictures/mdisk)

```bash
pip install mdisk
```

```bash
pip install git+https://github.com/HeimanPictures/Mdisk.git
```
---

## Usage

You can use this as python module or via terminal

### Use as python module
```python
from mdisk import Mdisk

d = Mdisk("YOUR_API_KEY")

# Upload video from direct links
d.upload("VIDEO_LINK")
```

### Use via terminal
set your Mdisk api key first
```bash
export MDISK_API=you_key_here
```
- Providesw link for mdisk
```bash
mdisk upload VIDEO_LINK
```

## Credits

- **[AkKiL](https://github.com/heimanpictures)**
