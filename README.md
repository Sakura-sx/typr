# typr

![typr](https://github.com/Sakura-sx/typr/blob/main/image.png?raw=true)

TUI typing test with a word selection algorithm inspired by [keybr](https://keybr.com/)

## Features
 - Word selection algorithm to optimize your typing speed inspired by [keybr](https://keybr.com/) weighted by:
    - Accuracy with the letter
    - Frequency of the letter in the English language
    - Speed at which you type the letter
- A cool TUI with curses
- Stores your data in a JSON file

## Installation
### Windows

```bash
git clone https://github.com/Sakura-sx/typr.git
cd typr
pip install -r requirements.txt
python3 main.py
```

### Linux

```bash
git clone https://github.com/Sakura-sx/typr.git
cd typr
python3 main.py
```

## Usage

### Running it normally
```bash
python3 main.py
```

### To forgive errors
```bash
python3 main.py --forgive-errors
```

### To set the time limit
```bash
python3 main.py --time 60
```

### To set the words limit
```bash
python3 main.py --words 100
```

### To run it forever
```bash
python3 main.py --forever
```

### Running with Docker
#### Using pre-built image (recommended)
```bash
# Run the latest version
docker run -it --rm ghcr.io/imperatormarsa/typr

# Run with custom options
docker run -it --rm ghcr.io/imperatormarsa/typr python3 main.py --time 60 --forgive-errors
```

#### Building from source
```bash
# Build the Docker image
docker build -t typr .

# Run the container
docker run -it --rm typr
```

## Roadmap
- [ ] Add a setting for the wordlist.
- [ ] Add a setting for the language.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
