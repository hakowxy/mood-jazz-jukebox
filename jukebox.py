"""Music data and the recommendation rules, kept separate from the Streamlit UI so they can be tested."""

# YouTube embed URLs per genre
MUSIC_DATA = {
    "city pop": [
        "https://www.youtube.com/embed/TBLZSXwfjbE",
        "https://www.youtube.com/embed/p9dRg8yQ2DY",
        "https://www.youtube.com/embed/zXHS92Nirfo",
        "https://www.youtube.com/embed/2997s_xoioM",
    ],
    "jazz hiphop": [
        "https://www.youtube.com/embed/dtVwR4uMnfg",
        "https://www.youtube.com/embed/OIvGy0wM5_s",
        "https://www.youtube.com/embed/sunRCbqQ1CM",
        "https://www.youtube.com/embed/nIATxs_KREI",
    ],
    "study focus": [
        "https://www.youtube.com/embed/219beSEfbqA",
        "https://www.youtube.com/embed/_Q8Ih2SW-TE",
        "https://www.youtube.com/embed/jim9K1vBL0k",
        "https://www.youtube.com/embed/ZbyxjGE885I",
    ],
    "ambient jazz": [
        "https://www.youtube.com/embed/CfPxlb8-ZQ0",
        "https://www.youtube.com/embed/o26qoCYLdS8",
        "https://www.youtube.com/embed/MYPVQccHhAQ",
        "https://www.youtube.com/embed/FAdJjGl2xw0",
    ],
}

LOCATIONS = ["home", "commute", "work", "study", "park"]

# For each scene: (mood threshold, genre at or above it, genre below it)
SCENE_RULES = {
    "commute": (5, "city pop", "jazz hiphop"),
    "work": (6, "study focus", "jazz hiphop"),
    "study": (6, "study focus", "jazz hiphop"),
    "park": (6, "city pop", "jazz hiphop"),
    "home": (6, "jazz hiphop", "ambient jazz"),
}


def recommend_music(mood_score: int, location: str) -> str:
    """Pick a genre from a mood score (1 = cozy, 10 = sparkly) and where the listener is."""
    if location in SCENE_RULES:
        threshold, high, low = SCENE_RULES[location]
        return high if mood_score >= threshold else low
    # Unknown scene: fall back to mood alone
    if mood_score >= 8:
        return "city pop"
    if mood_score >= 5:
        return "jazz hiphop"
    return "ambient jazz"


def vibe_label(mood_score: int) -> str:
    if mood_score >= 8:
        return "sparkly"
    if mood_score >= 5:
        return "calm"
    return "cozy"
