"""
Creates a transcript of the text from an MP3 file.
"""
import sys
import argparse
import time
from rev_ai import apiclient

def get_file_name():
    parser = argparse.ArgumentParser(description='Get file name from cmd line')
    parser.add_argument('-f', '--file', required=True,
                        help='The name of the .mp3 file to convert to text')
    return parser.parse_args().file

if __name__ == "__main__":
    # Get the desired audio file from cmd line
    filename = get_file_name()
    if '.mp3' not in filename:
        print("Error: file type is not mp3")
        sys.exit()

    # Create client with given access token
    client = apiclient.RevAiAPIClient("028f4jLg6e4JCROQXE8vVZbkDlf_5oSfzH-HWyn1ehu6yOiTrVKtwtvLYnVzZZTAayHlalZFqD0zsKajkhYKjO7p8L37k")

    # Create a job to translate a given mp3 file
    job = client.submit_job_local_file(filename)

    # Check if the job is done transcribing
    while True:
        # Obtains details of a job in json format
        job_details = client.get_job_details(job.id)
        status = job_details.status.name

        print("Job Status : {}".format(status))

        # Checks if the job has been transcribed
        if status == "IN_PROGRESS":
            time.sleep(2)
            continue

        elif status == "FAILED":
            print("Job Failed : {}".format(job_details.failure_detail))
            break

        if status == "TRANSCRIBED":
            # Get the transcript text (job.id)
            transcript = client.get_transcript_text(job.id)
            # Write the transcript text to a file (named by job id)
            file_obj = open("./transcripts/text" + str(int(time.time())) + ".txt", "w+")
            file_obj.write(transcript)
            break
