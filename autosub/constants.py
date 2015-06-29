SPEECH_CUTOFF_SECONDS = 1.5
MAX_TIMEOUT = 9999999

FFMPEG_CONVERT_COMMAND = "ffmpeg -y -i {source_path} -ac {channels} -ar {rate} -loglevel error {destination_path}"
FFMPEG_SPLIT_COMMAND = "ffmpeg -y -i {source_path} -ss {start} -t {duration} -loglevel error {destination_path}"

GOOGLE_SPEECH_API_KEY = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
GOOGLE_SPEECH_API_URL = "http://www.google.com/speech-api/v2/recognize?client=chromium&lang={lang}&key={key}"

SOURCE_LANGUAGES = {
    'af': 'Afrikaans',
    'eu': 'Basque',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ar-EG': 'Arabic (Egypt)',
    'ar-JO': 'Arabic (Jordan)',
    'ar-KW': 'Arabic (Kuwait)',
    'ar-LB': 'Arabic (Lebanon)',
    'ar-QA': 'Arabic (Qatar)',
    'ar-AE': 'Arabic (UAE)',
    'ar-MA': 'Arabic (Morocco)',
    'ar-IQ': 'Arabic (Iraq)',
    'ar-DZ': 'Arabic (Algeria)',
    'ar-BH': 'Arabic (Bahrain)',
    'ar-LY': 'Arabic (Lybia)',
    'ar-OM': 'Arabic (Oman)',
    'ar-SA': 'Arabic (Saudi Arabia)',
    'ar-TN': 'Arabic (Tunisia)',
    'ar-YE': 'Arabic (Yemen)',
    'cs': 'Czech',
    'nl-NL': 'Dutch',
    'en-AU': 'English (Australia)',
    'en-CA': 'English (Canada)',
    'en-IN': 'English (India)',
    'en-NZ': 'English (New Zealand)',
    'en-ZA': 'English (South Africa)',
    'en-GB': 'English(UK)',
    'en-US': 'English(US)',
    'fi': 'Finnish',
    'fr-FR': 'French',
    'gl': 'Galician',
    'de-DE': 'German',
    'he': 'Hebrew',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'it-IT': 'Italian',
    'id': 'Indonesian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'la': 'Latin',
    'zh-CN': 'Mandarin Chinese',
    'zh-TW': 'Traditional Taiwan',
    'zh-CN': 'Simplified China',
    'zh-HK': 'Simplified Hong Kong',
    'zh-yue': 'Yue Chinese (Traditional Hong Kong)',
    'ms-MY': 'Malaysian',
    'no-NO': 'Norwegian',
    'pl': 'Polish',
    'xx-piglatin': 'Pig Latin',
    'pt-PT': 'Portuguese',
    'pt-BR': 'Portuguese (brasil)',
    'ro-RO': 'Romanian',
    'ru': 'Russian',
    'sr-SP': 'Serbian',
    'sk': 'Slovak',
    'es-AR': 'Spanish (Argentina)',
    'es-BO': 'Spanish (Bolivia)',
    'es-CL': 'Spanish (Chile)',
    'es-CO': 'Spanish (Colombia)',
    'es-CR': 'Spanish (Costa Rica)',
    'es-DO': 'Spanish (Dominican Republic)',
    'es-EC': 'Spanish (Ecuador)',
    'es-SV': 'Spanish (El Salvador)',
    'es-GT': 'Spanish (Guatemala)',
    'es-HN': 'Spanish (Honduras)',
    'es-MX': 'Spanish (Mexico)',
    'es-NI': 'Spanish (Nicaragua)',
    'es-PA': 'Spanish (Panama)',
    'es-PY': 'Spanish (Paraguay)',
    'es-PE': 'Spanish (Peru)',
    'es-PR': 'Spanish (Puerto Rico)',
    'es-ES': 'Spanish (Spain)',
    'es-US': 'Spanish (US)',
    'es-UY': 'Spanish (Uruguay)',
    'es-VE': 'Spanish (Venezuela)',
    'sv-SE': 'Swedish',
    'tr': 'Turkish',
    'zu': 'Zulu',
}

DESTINATION_LANGUAGES = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'az': 'Azerbaijani',
    'be': 'Belarusian',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'eo': 'Esperanto',
    'es': 'Spanish',
    'et': 'Estonian',
    'eu': 'Basque',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'ga': 'Irish',
    'gl': 'Galician',
    'gu': 'Gujarati',
    'ha': 'Hausa',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hr': 'Croatian',
    'ht': 'Haitian Creole',
    'hu': 'Hungarian',
    'hy': 'Armenian',
    'id': 'Indonesian',
    'ig': 'Igbo',
    'is': 'Icelandic',
    'it': 'Italian',
    'iw': 'Hebrew',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'ka': 'Georgian',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'kn': 'Kannada',
    'ko': 'Korean',
    'la': 'Latin',
    'lo': 'Lao',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mg': 'Malagasy',
    'mi': 'Maori',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mn': 'Mongolian',
    'mr': 'Marathi',
    'ms': 'Malay',
    'mt': 'Maltese',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'ny': 'Chichewa',
    'pa': 'Punjabi',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'sq': 'Albanian',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'su': 'Sundanese',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'tg': 'Tajik',
    'th': 'Thai',
    'tl': 'Filipino',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zh': 'Chinese',
    'zh-CN': 'Chinese (Simplified)',
    'zh-TW': 'Chinese (Traditional)',
    'zu': 'Zulu',
}
