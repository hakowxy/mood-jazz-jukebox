import pytest

from jukebox import LOCATIONS, MUSIC_DATA, recommend_music, vibe_label


@pytest.mark.parametrize("mood, location, expected", [
    (4, "commute", "jazz hiphop"),
    (5, "commute", "city pop"),
    (5, "work", "jazz hiphop"),
    (6, "study", "study focus"),
    (5, "park", "jazz hiphop"),
    (9, "park", "city pop"),
    (3, "home", "ambient jazz"),
    (7, "home", "jazz hiphop"),
])
def test_scene_rules(mood, location, expected):
    assert recommend_music(mood, location) == expected


def test_unknown_scene_falls_back_to_mood():
    assert recommend_music(9, "beach") == "city pop"
    assert recommend_music(6, "beach") == "jazz hiphop"
    assert recommend_music(2, "beach") == "ambient jazz"


def test_every_recommendation_has_tracks():
    for location in LOCATIONS:
        for mood in range(1, 11):
            assert MUSIC_DATA[recommend_music(mood, location)]


def test_vibe_labels():
    assert [vibe_label(m) for m in (1, 5, 8)] == ["cozy", "calm", "sparkly"]
