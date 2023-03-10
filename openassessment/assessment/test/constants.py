"""
Constants used as test data.
"""

STUDENT_ITEM = {
    'student_id': '๐ฝ๐ฎ๐ผ๐ฝ ๐ผ๐ฝ๐พ๐ญ๐ฎ๐ท๐ฝ',
    'item_id': '๐๐๐๐ ๐๐๐๐',
    'course_id': 'ีัเธฃี ฯเนเธขะณเธฃั',
    'item_type': 'openassessment'
}

ANSWER = {'text': 'แบรซแนกแบ รคแนแนกแบรซแน'}

RUBRIC_OPTIONS = [
    {
        "order_num": 0,
        "name": "๐๐๐๐",
        "explanation": "๐ป๐๐๐ ๐๐๐!",
        "points": 0,
    },
    {
        "order_num": 1,
        "name": "๐ฐ๐ธ๐ธ๐ญ",
        "explanation": "๏ปญัปัปษ ๏ปัปเน!",
        "points": 1,
    },
    {
        "order_num": 2,
        "name": "ัฯยขัโโัฮทั",
        "explanation": "ไน๏พcไน๏พ๏พไนๅ๏ฝฒ ๏พoไน!",
        "points": 2,
    },
]

RUBRIC = {
    'prompts': [{"description": "ะะพัะ-โััะบ; ะพั, ะะั ะฉะะฐlั"}],
    'criteria': [
        {
            "order_num": 0,
            "name": "vรธศผศบฦแตพลศบษษ",
            "prompt": "ฤฆรธw vศบษษจษฤ ษจs ลงฤงษ vรธศผศบฦแตพลศบษษ?",
            "options": RUBRIC_OPTIONS
        },
        {
            "order_num": 1,
            "name": "๏ปญษผเธเนเนเธษผ",
            "prompt": "๐ณ๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐?",
            "options": RUBRIC_OPTIONS
        }
    ]
}

RUBRIC_POSSIBLE_POINTS = sum(
    max(
        option["points"] for option in criterion["options"]
    ) for criterion in RUBRIC["criteria"]
)

# Used to generate OPTIONS_SELECTED_DICT. Indices refer to RUBRIC_OPTIONS.
OPTIONS_SELECTED_CHOICES = {
    "none": [0, 0],
    "few": [0, 1],
    "most": [1, 2],
    "all": [2, 2],
}

OPTIONS_SELECTED_DICT = {
    # This dict is constructed from OPTIONS_SELECTED_CHOICES.
    # 'key' is expected to be a string, such as 'none', 'all', etc.
    # 'value' is a list, indicating the indices of the RUBRIC_OPTIONS selections that pertain to that key
    key: {
        "options": {
            RUBRIC["criteria"][i]["name"]: RUBRIC_OPTIONS[j]["name"] for i, j in enumerate(value)
        },
        "expected_points": sum(
            RUBRIC_OPTIONS[i]["points"] for i in value
        )
    } for key, value in OPTIONS_SELECTED_CHOICES.items()
}

EXAMPLES = [
    {
        'answer': (
            "๐ฟ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐"
            " ๐๐๐๐ ๐ ๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐ ๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐ ๐๐๐๐, ๐๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐"
            " ๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐, ๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐ ๐๐ ๐๐ ๐๐๐๐๐๐'๐ ๐๐๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐."
        ),
        'options_selected': {
            "vรธศผศบฦแตพลศบษษ": "๐ฐ๐ธ๐ธ๐ญ",
            "๏ปญษผเธเนเนเธษผ": "๐๐๐๐",
        }
    },
    {
        'answer': "Tลแน-hรฉรกvำณ แบรกล thรฉ ลhรญแน รกล รก dรญลลรฉลฤบรฉลล ลtรบdรฉลt แบรญth รกฤบฤบ รลรญลtลtฤบรฉ รญล hรญล hรฉรกd.",
        'options_selected': {
            "vรธศผศบฦแตพลศบษษ": "๐๐๐๐",
            "๏ปญษผเธเนเนเธษผ": "ัฯยขัโโัฮทั",
        }
    },
]
