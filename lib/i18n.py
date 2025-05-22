import yaml
from importlib.resources import read_binary


class Dictionary(object):
    """Provide dictionaries for i18n."""
    dictionary = {}

    def __init__(self, language):
        self.load(language)

    def load(self, language):
        """Load dictionary for given language."""
        content = ''
        try:
            content = open(f'i18n/{language}.yaml')
        except FileNotFoundError:
            try:
                content = read_binary('i18n', f'{language}.yaml')
            except FileNotFoundError:
                return
        _d = yaml.safe_load(content)
        self.dictionary = _d[language]


    def translate(self, message):
        """Translate message."""
        if type(message) == str:
            if message in self.dictionary:
                return self.dictionary[message]
            if message.lower() in self.dictionary:
                return self.dictionary[message.lower()].capitalize()
            # else
            return message
        else:
            return message
