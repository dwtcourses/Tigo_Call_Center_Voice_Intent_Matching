# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "speech_transcribe_enhanced_model")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-speech

# sample-metadata
#   title: Using Enhanced Models (Local File)
#   description: Transcribe a short audio file using an enhanced model
#   usage: python3 samples/v1/speech_transcribe_enhanced_model.py [--local_file_path "resources/hello.wav"]

# [START speech_transcribe_enhanced_model]
from google.cloud import speech_v1
import io


def sample_recognize(local_file_path,file_name):
    print("""Passing voice clip "{}" to Google voice to text API.......""".format(file_name))
    """
    Transcribe a short audio file using an enhanced model
    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """
    text = ''
    client = speech_v1.SpeechClient()

    # local_file_path = 'resources/hello.wav'

    # The enhanced model to use, e.g. phone_call
    model = "phone_call"

    # Use an enhanced model for speech recognition (when set to true).
    # Project must be eligible for requesting enhanced models.
    # Enhanced speech models require that you opt-in to data logging.
    use_enhanced = True

    # The language of the supplied audio
    language_code = "en-US"
    config = {
        "model": model,
        "use_enhanced": use_enhanced,
        "language_code": language_code,
        "audio_channel_count": 2,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        text = text +  alternative.transcript + '\n'

    return text
# [END speech_transcribe_enhanced_model]


#def main():
    #audio_path = "Data/Dual_Channel/Service_Failure/Recording (29)-2.wav"
#    audio_path = "C:/Users/Anushan Temp/Desktop/Recordings/Recharge_Issue_01.wav"
#    text = sample_recognize(audio_path)
#    print(text)

#if __name__ == "__main__":
#    main()