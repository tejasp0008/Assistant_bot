```markdown
# Toru Voice Assistant

Toru is a Python-based voice assistant that can perform various tasks using voice commands. It utilizes speech recognition and text-to-speech technology to interact with users in natural language.

## Features

- **Wikipedia Search**: Search for information on Wikipedia by simply asking Toru.
- **Web Browsing**: Open websites like Google, YouTube, and Stack Overflow with voice commands.
- **Play YouTube Videos**: Play YouTube videos based on your search query.
- **Toss a Coin**: Have Toru toss a coin and tell you the result.
- **Tell Jokes**: Toru can lighten the mood by telling jokes.
- **Get Time and Date**: Ask Toru for the current time and date.

## Requirements

- Python 3.x
- pyttsx3: `pip install pyttsx3`
- SpeechRecognition: `pip install SpeechRecognition`
- wikipedia: `pip install wikipedia`

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/tejasp0008/toru.git
```

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Run the Toru Voice Assistant:

```bash
python toru.py
```

4. Once Toru is running, simply say "Toru" followed by your command to interact with the voice assistant.

## How it Works

Toru uses the SpeechRecognition library to listen for voice commands. When a command is recognized, it processes the command and performs the corresponding action. Text-to-speech technology is used to provide responses and information to the user.

## Contributing

Contributions are welcome! If you have any ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```