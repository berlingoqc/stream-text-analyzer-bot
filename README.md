# STREAM TEXT DETECTION BOT

This is a twitch bot to detect text from stream and send it to chat

Use to get stream information from twitch

[streamlink](https://streamlink.github.io/api_guide.html#examples)

I use this as a base to extract text from the image

[Python tesseract opencv](https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/)

## Dependencies

You need to install tesseract-ocr and the data for the english language.

## Usage

To test you can stream a file in loop to twitch with the script provides.

```
./stream_demo.sh <TWITCH_KEY> <FILE_TO_STREAM>
```

```
# Extract text from image and send them to the chat
python main.py <TWITCH_CHANNEL> <BOT_NAME> <OAUTH_TOKEN>
```
