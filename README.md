# HackMIT2019
HackMIT 2019: Hack for a Reason

## Social Q's
#### For answering your socializing questions
Our project is meant to help autistic people, among others, who struggle to understand social cues.

Emotional intelligence is essential in the modern world, but it can be hard to develop if it does not come naturally. Feedback about social performance is often cryptic or nonexistent, as it can be difficult to genuinely discuss one's feelings with others. That's where **Social Q's** can help -- Social Q's uses a Muse to detect brainwaves during a conversation. When aligned with the text from the conversation (translated using the asynchronous Rev.ai SDK) in a clear visual labeled with timestamps, users are provided with quantitative data with which to gauge social situations.

## How it Works
Using the legacy Muse SDK, data is read from the Muse and processed with MuseIO. The data is stored in a .csv, which is compressed to a more concise version.

When the headband is placed on the head, an audio recording is simultaneously started. After the conversation, the audio recording is then stopped and processed with Rev.ai to obtain the conversation transcript.

After the conversation transcript is obtained, the timestamps from both files are aligned to match text with the conversation partner's brainwaves.

## Usage
Open two separate terminal windows.
In the first terminal, run the following command:
```
./muse-io --osc osc.tcp://localhost:5000 --device call
```
In the second terminal, run:
```
./muse-player -l 5000 -C /tmp/out.csv
```

Start recording the conversation once the conversation partner wears the Muse. After the conversation is over, remove the Muse at the same time that the audio recording is ended.

If your recorded file is an mp4, convert it to mp3. This can be done by installing the ffmpeg package (it is available with Brew) and running the following command:
```
ffmpeg -i <input.mp4> <destination.mp3>
```
Then, run compressor.py:
```
python3 compressor.py
```
Run the audio_to_text.py script and pass in the file path to the mp3 file.
```
python3 audio_to_text.py -f <file_path>
```
Run the gen_visuals.py script to view a graph of the data.
```
python3 gen_visuals.py
```
