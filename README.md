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
- **Custom text source** — type from your own word list, code file, or any URL

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

### To type from a custom file or URL

```bash
# local file
python3 main.py --custom words_i_like.txt

# raw URL — type the typr source itself
python3 main.py --custom https://raw.githubusercontent.com/Sakura-sx/typr/main/main.py
```

You can also set the custom source interactively via the **Custom Text** menu option or **Settings → Custom Word File**. Both local paths and `http`/`https` URLs are supported. Line structure and indentation are preserved — press `Enter` when you reach a `↵` symbol.

## Roadmap

- [ ] Add a setting for the language.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

