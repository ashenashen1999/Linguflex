import sys
sys.path.insert(0, '..')
import pyaudio
import wave
import os

from linguflex_interfaces import TextToSpeechModule_IF
from linguflex_log import log, DEBUG_LEVEL_OFF, DEBUG_LEVEL_MIN, DEBUG_LEVEL_MID, DEBUG_LEVEL_MAX
from linguflex_config import cfg, set_section, get_section, configuration_parsing_error_message
from linguflex_message import LinguFlexMessage
from elevenlabs_texttospeech_helper import ConvertNumbersToText
from elevenlabs import set_api_key, generate, play
from elevenlabs.api import Voice, VoiceSettings

set_section('elevenlabs_texttospeech')

API_KEY_NOT_FOUND_ERROR_MESSAGE = 'Elevenlabs Speech API-Key not found. Please define the key in your linguflex config file or set the key in the environment variable LINGU_ELEVENLABS_SPEECH_KEY.'

# Import Elevenlabs Speech API-Key from either registry (LINGU_ELEVENLABS_SPEECH_KEY) or config file tts_elevenlabs/elevenlabs_speech_api_key
api_key = os.environ.get('LINGU_ELEVENLABS_SPEECH_KEY')
if api_key is None:
    try:
        api_key = cfg[get_section()]['elevenlabs_speech_api_key']
    except Exception as e:
        raise ValueError(configuration_parsing_error_message + ' ' + str(e))
if api_key is None:
    raise ValueError(API_KEY_NOT_FOUND_ERROR_MESSAGE)
set_api_key(api_key)

# Read module configuration
try:
    voice = cfg[get_section()].get('voice', 'Adam')
except Exception as e:
    raise ValueError(configuration_parsing_error_message + ' ' + str(e))

text_converter = ConvertNumbersToText()

class TextToSpeechModule_ElevenLabs(TextToSpeechModule_IF):
    def perform_text_to_speech(self, 
            message: LinguFlexMessage) -> None: 
        output_optimized = text_converter.optimiere(message.output_user)
        log(DEBUG_LEVEL_MAX, '  [tts_eleven] output [{}]'.format(output_optimized))

        voice = Voice(
            voice_id="z4z95FcLrYTsEFrmpOpI",
            name="Winkens 2",
            category="cloned",
            settings=VoiceSettings(stability=0.85, similarity_boost=0.85),
            # settings=VoiceSettings(stability=0.55, similarity_boost=0.55), # too much variety in output
        )

        audio = generate(
            text=output_optimized,
            voice=voice,
            model="eleven_multilingual_v1"
            )        
        
        play(audio)

    # def konvertiere_int_in_gesprochenen_text(zahl: int) -> str:
    #     einheiten = ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    #     zehner = ["", "zehn", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
    #     hunderter = ["", "einhundert", "zweihundert", "dreihundert", "vierhundert", "fünfhundert", "sechshundert", "siebenhundert", "achthundert", "neunhundert"]
    #     ausnahmen = {11: "elf", 12: "zwölf"}

    #     if zahl < 10:
    #         return einheiten[zahl]
    #     if zahl in ausnahmen:
    #         return ausnahmen[zahl]
    #     if zahl < 100:
    #         zehn = zahl // 10
    #         eins = zahl % 10
    #         if eins == 0:
    #             return zehner[zehn]
    #         else:
    #             return einheiten[eins] + "und" + zehner[zehn]
    #     if zahl < 1000:
    #         hundert = zahl // 100
    #         rest = zahl % 100
    #         if rest == 0:
    #             return hunderter[hundert]
    #         else:
    #             return hunderter[hundert] + konvertiere_int_in_gesprochenen_text(rest)
    #     if zahl < 10000:
    #         tausend = zahl // 1000
    #         rest = zahl % 1000
    #         if rest == 0:
    #             return einheiten[tausend] + "tausend"
    #         else:
    #             return einheiten[tausend] + "tausend" + konvertiere_int_in_gesprochenen_text(rest)

    #     return str(zahl)
    


#  voice_id='21m00Tcm4TlvDq8ikWAM', name='Rachel', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='AZnzlk1XvdvUeBnXmlld', name='Domi', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='EXAVITQu4vr4xnSDxMaL', name='Bella', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='ErXwobaYiN019PkySvjV', name='Antoni', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='MF3mGyEYCl7XYWbV9V6O', name='Elli', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='TxGEqnHWrfWFTfGW9XjX', name='Josh', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='VR6AewLTigWG4xSOukaG', name='Arnold', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='pNInz6obpgDQGcFmaJgB', name='Adam', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75
#  voice_id='yoZ06aMxZJJ28mfd3POQ', name='Sam', category='premade', settings=VoiceSettings(stability=0.75, similarity_boost=0.75