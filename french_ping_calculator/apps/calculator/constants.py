SCORE_TABLE = {
    (0, 25): {
        'normal_victory': 6,
        'normal_defeat': -5,
        'anormal_victory': 6,
        'anormal_defeat': -5,
    },
    (25, 50): {
        'normal_victory': 5.5,
        'normal_defeat': -4.5,
        'anormal_victory': 7,
        'anormal_defeat': -6,
    },
    (50, 100): {
        'normal_victory': 5,
        'normal_defeat': -4,
        'anormal_victory': 8,
        'anormal_defeat': -7,
    },
    (100, 150): {
        'normal_victory': 4,
        'normal_defeat': -3,
        'anormal_victory': 10,
        'anormal_defeat': -8,
    },
    (150, 200): {
        'normal_victory': 3,
        'normal_defeat': -2,
        'anormal_victory': 13,
        'anormal_defeat': -10,
    },
    (200, 300): {
        'normal_victory': 2,
        'normal_defeat': -1,
        'anormal_victory': 17,
        'anormal_defeat': -12.5,
    },
    (300, 400): {
        'normal_victory': 1,
        'normal_defeat': -0.5,
        'anormal_victory': 22,
        'anormal_defeat': -16,
    },
    (400, 500): {
        'normal_victory': 0.5,
        'normal_defeat': 0,
        'anormal_victory': 28,
        'anormal_defeat': -20,
    },
    (500, 4000): {
        'normal_victory': 0,
        'normal_defeat': 0,
        'anormal_victory': 40,
        'anormal_defeat': -29,
    },
}
