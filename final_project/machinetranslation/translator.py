"""
This module handles the establishment of a session to the Watson Language Translator, as well as
some shortcut functions for languages we expect to use.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def get_translator_instance():
    """
    This function handles establishing an instance of the Translator Service.
    It takes in apikey and url and returns an instance.
    """
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
        )
    language_translator.set_service_url(url)
    return language_translator


def englishToFrench(translator_instance, englishText):
    """
    This function takes an English language string and returns a French translation.
    """
    if englishText == '' or englishText is None:
        return None
    result = translator_instance.translate(text=englishText, model_id="en-fr").get_result()
    return result['translations'][0]['translation']


def frenchToEnglish(translator_instance, frenchText):
    """
    This function takes a French language string and returns an English translation.
    """
    if frenchText == '' or frenchText is None:
        return None
    result = translator_instance.translate(text=frenchText, model_id="fr-en").get_result()
    return result['translations'][0]['translation']


if __name__ == "__main__":
    translator = get_translator_instance()
    print(englishToFrench(translator, "Hello"))
