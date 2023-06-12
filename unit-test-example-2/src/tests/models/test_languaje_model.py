from src.models.LanguageModel import LanguageModel

lan = ["python", "js", "c++", "go", "c"]

def test_get_languages_not_none():
    languages = LanguageModel.get_languages()
    assert languages != None

def test_get_languages_has_elements():
    languages = LanguageModel.get_languages()
    assert len(languages) > 0

def test_get_languages_valids():
    languages = LanguageModel.get_languages()
    for languaje in languages:
        assert languaje in lan 