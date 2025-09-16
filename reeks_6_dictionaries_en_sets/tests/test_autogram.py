import pytest
from reeks_6_dictionaries_en_sets.autogram import letterfrequenties, letterposities

# --- Tests voor letterfrequenties ---

@pytest.mark.timeout(1)
def test_letterfrequenties_opgavevoorbeeld_1():
    assert letterfrequenties("Fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's") == {
        'u': 4, 'n': 4, 'e': 15, 'x': 3, 'w': 2, 's': 18, 'h': 6, 'r': 6, 'i': 8, 'v': 3, 'f': 7, 't': 8, 'o': 5, 'g': 4
    }

@pytest.mark.timeout(1)
def test_letterfrequenties_opgavevoorbeeld_2():
    assert letterfrequenties("Sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's") == {
        'h': 6, 'n': 5, 'e': 16, 'x': 4, 'w': 2, 's': 18, 'u': 3, 'r': 6, 'i': 9, 'v': 3, 'f': 5, 't': 8, 'o': 4, 'g': 3
    }

@pytest.mark.timeout(1)
def test_letterfrequenties_dit_pangram():
    assert letterfrequenties("Dit pangram bevat vijf a's, twee b's, twee c's, drie d's, zesenveertig e's, vijf f's, vier g's, twee h's, vijftien i's, vier j's, een k, twee l's, twee m's, zeventien n's, een o, twee p's, een q, zeven r's, vierentwintig s's, zestien t's, een u, elf v's, acht w's, een x, een y, en zes z's.") == {
        'z': 6, 'q': 1, 'x': 1, 's': 24, 'm': 2, 'w': 8, 'r': 7, 'd': 3, 'y': 1, 'f': 5, 'p': 2, 'j': 4, 'k': 1, 't': 16, 'o': 1, 'g': 4, 'i': 15, 'h': 2, 'n': 17, 'e': 46, 'v': 11, 'a': 5, 'u': 1, 'c': 2, 'b': 2, 'l': 2
    }

@pytest.mark.timeout(1)
def test_letterfrequenties_ezel():
    assert letterfrequenties("Alleen 'n ezel gelooft dat ik de moeite heb genomen na te tellen dat deze zin bestaat uit zestien a's, drie b's, vier c's, vijftien d's, negenenzeventig e's, zes f's, veertien g's, zes h's, vierendertig i's, vier j's, zeven k's, acht l's, vijf m's, achtendertig n's, zes o's, vier p's, een q, achttien r's, vijfendertig s's, drieendertig t's, drie u's, dertien v's, drie w's, een x, een y, tien z's, plus dertig komma's, vierentwintig afkappingstekens, twee aanhalingstekens en, niet te vergeten, een enkel !") == {
        'l': 10, 'q': 1, 'x': 1, 'z': 10, 'm': 5, 'w': 3, 'h': 6, 'r': 18, 'd': 15, 'y': 1, 'f': 6, 'p': 4, 'j': 4, 'k': 7, 't': 33, 'o': 6, 'g': 14, 'i': 34, 'u': 3, 'n': 38, 'e': 79, 'b': 3, 'c': 4, 'a': 16, 's': 35, 'v': 13
    }

@pytest.mark.timeout(1)
def test_letterfrequenties_minimaal():
    assert letterfrequenties('a') == {'a': 1}

@pytest.mark.timeout(1)
def test_letterfrequenties_alleen_nietletters():
    assert letterfrequenties(",.! 1234") == {}

@pytest.mark.timeout(1)
def test_letterfrequenties_case_insensitive():
    assert letterfrequenties('AaAaBb') == {'a': 4, 'b': 2}

@pytest.mark.timeout(1)
def test_letterfrequenties_latijn():
    assert letterfrequenties('IN HAC SENTENTIA SUNT TREDECIM A, UNA B, QUATTUOR C, SEX D, UIGINTI E, UNA F, QUINQUE G, DUAE H, DUODEUIGINTI I, UNA L, SEX M, SEPTENDECIM N, SEPTEM O, QUATTUOR P, SEPTEM Q, SEX R, NOUEM S, UIGINTI UNA T, UIGINTI QUATTUOR U, QUATTUOR X, ET UNA Z.') == {
        'i': 18, 'h': 2, 'n': 17, 'e': 20, 'x': 4, 'g': 5, 'c': 4, 'a': 13, 'm': 6, 's': 9, 'u': 24, 'r': 6, 'd': 6, 'b': 1, 'f': 1, 'p': 4, 'q': 7, 'l': 1, 't': 21, 'o': 7, 'z': 1
    }

# --- Tests voor letterposities ---

@pytest.mark.timeout(1)
def test_letterposities_opgavevoorbeeld_1():
    assert letterposities("Fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")['e'] == {4, 5, 8, 14, 16, 43, 67, 83, 88, 89, 97, 121, 122, 141, 142}

@pytest.mark.timeout(1)
def test_letterposities_opgavevoorbeeld_2():
    assert letterposities("Sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")['f'] == {13, 18, 53, 63, 138}

@pytest.mark.timeout(1)
def test_letterposities_dit_pangram():
    assert letterposities("Dit pangram bevat vijf a's, twee b's, twee c's, drie d's, zesenveertig e's, vijf f's, vier g's, twee h's, vijftien i's, vier j's, een k, twee l's, twee m's, zeventien n's, een o, twee p's, een q, zeven r's, vierentwintig s's, zestien t's, een u, elf v's, acht w's, een x, een y, en zes z's.")['z'] == {226, 196, 58, 282, 157, 286}

@pytest.mark.timeout(1)
def test_letterposities_ezel():
    zin = "Alleen 'n ezel gelooft dat ik de moeite heb genomen na te tellen dat deze zin bestaat uit zestien a's, drie b's, vier c's, vijftien d's, negenenzeventig e's, zes f's, veertien g's, zes h's, vierendertig i's, vier j's, zeven k's, acht l's, vijf m's, achtendertig n's, zes o's, vier p's, een q, achttien r's, vijfendertig s's, drieendertig t's, drie u's, dertien v's, drie w's, een x, een y, tien z's, plus dertig komma's, vierentwintig afkappingstekens, twee aanhalingstekens en, niet te vergeten, een enkel !"
    assert letterposities(zin) == {'l': {1, 2, 234, 13, 463, 17, 401, 505, 60, 61}, 'p': {400, 281, 440, 439}, 'x': {380}, 's': {134, 264, 269, 397, 273, 403, 155, 283, 160, 418, 164, 304, 178, 183, 187, 444, 320, 322, 450, 205, 80, 467, 340, 215, 473, 92, 350, 226, 100, 363, 236, 110, 373, 246, 120}, 'm': {33, 48, 244, 414, 415}, 'q': {290}, 'h': {295, 40, 231, 461, 185, 251}, 'r': {193, 257, 355, 198, 326, 104, 424, 170, 489, 333, 302, 367, 211, 116, 407, 344, 315, 279}, 'i': {128, 259, 391, 277, 150, 409, 27, 36, 422, 298, 172, 429, 432, 308, 441, 317, 191, 327, 200, 75, 203, 335, 464, 209, 87, 345, 94, 480, 357, 105, 240, 368, 114, 124}, 'y': {387}, 'w': {371, 428, 454}, 'f': {162, 242, 436, 20, 310, 126}, 'z': {90, 71, 74, 11, 267, 395, 144, 181, 218, 158}, 'j': {241, 125, 309, 213}, 'k': {224, 437, 470, 503, 412, 28, 447}, 't': {258, 390, 21, 149, 408, 25, 37, 296, 297, 171, 427, 431, 55, 58, 316, 445, 67, 453, 199, 334, 81, 338, 84, 468, 88, 93, 482, 356, 484, 232, 492, 252, 127}, 'o': {34, 271, 47, 18, 19, 413}, 'g': {260, 201, 490, 139, 44, 15, 176, 336, 433, 466, 151, 410, 443, 318}, 'd': {65, 353, 196, 69, 132, 103, 325, 331, 366, 30, 405, 23, 313, 343, 255}, 'u': {402, 348, 86}, 'n': {385, 130, 5, 262, 8, 137, 393, 141, 143, 148, 288, 426, 300, 46, 174, 430, 50, 52, 312, 442, 63, 449, 195, 330, 76, 460, 465, 472, 476, 222, 479, 96, 359, 494, 499, 502, 378, 254}, 'e': {3, 4, 10, 12, 16, 31, 35, 38, 41, 45, 49, 56, 59, 62, 70, 72, 79, 91, 95, 106, 115, 129, 138, 140, 142, 145, 147, 153, 159, 168, 169, 173, 182, 192, 194, 197, 210, 219, 221, 253, 256, 268, 278, 286, 287, 299, 311, 314, 328, 329, 332, 346, 354, 358, 369, 376, 377, 383, 384, 392, 406, 423, 425, 446, 448, 455, 456, 469, 471, 475, 481, 485, 488, 491, 493, 497, 498, 501, 504}, 'v': {421, 167, 487, 361, 239, 208, 113, 146, 307, 276, 123, 220, 190}, 'a': {0, 416, 66, 98, 229, 293, 458, 459, 462, 82, 83, 435, 53, 438, 24, 249}, 'c': {294, 250, 118, 230}, 'b': {42, 108, 78}}

@pytest.mark.timeout(1)
def test_letterposities_minimaal():
    assert letterposities("A") == {'a': {0}}

@pytest.mark.timeout(1)
def test_letterposities_alleen_nietletters():
    assert letterposities(",.! 1234") == {}

@pytest.mark.timeout(1)
def test_letterposities_case_insensitive():
    assert letterposities("AAa") == {'a': {0, 1, 2}}

@pytest.mark.timeout(1)
def test_letterposities_meerdere_letters():
    posities = letterposities("abcAbC")
    assert posities['a'] == {0, 3}
    assert posities['b'] == {1, 4}
    assert posities['c'] == {2, 5}

@pytest.mark.timeout(1)
def test_letterposities_latijn():
    zin = 'IN HAC SENTENTIA SUNT TREDECIM A, UNA B, QUATTUOR C, SEX D, UIGINTI E, UNA F, QUINQUE G, DUAE H, DUODEUIGINTI I, UNA L, SEX M, SEPTENDECIM N, SEPTEM O, QUATTUOR P, SEPTEM Q, SEX R, NOUEM S, UIGINTI UNA T, UIGINTI QUATTUOR U, QUATTUOR X, ET UNA Z.'
    assert letterposities(zin) =={'d': {97, 100, 133, 89, 25, 57}, 'h': {3, 94}, 'n': {64, 1, 194, 35, 132, 199, 72, 9, 106, 139, 12, 81, 209, 19, 241, 114, 181}, 'e': {128, 131, 134, 8, 11, 143, 146, 24, 26, 165, 168, 175, 54, 184, 68, 84, 92, 101, 237, 121}, 'x': {176, 122, 234, 55}, 'c': {50, 27, 5, 135}, 'a': {227, 4, 36, 200, 73, 43, 15, 242, 115, 215, 154, 91, 31}, 'm': {169, 137, 147, 185, 124, 29}, 's': {164, 7, 142, 174, 17, 53, 120, 187, 127}, 'u': {18, 153, 157, 34, 42, 46, 183, 60, 190, 198, 71, 205, 79, 83, 214, 90, 218, 222, 98, 226, 102, 230, 240, 113}, 'r': {232, 48, 178, 23, 220, 159}, 'i': {0, 193, 66, 196, 103, 136, 105, 108, 14, 206, 80, 208, 110, 211, 63, 28, 61, 191}, 'b': {38}, 'f': {75}, 'p': {144, 129, 161, 166}, 'q': {225, 41, 171, 78, 82, 213, 152}, 'l': {117}, 'z': {244}, 't': {130, 10, 13, 145, 20, 22, 155, 156, 167, 44, 45, 65, 195, 202, 210, 216, 217, 228, 229, 107, 238}, 'o': {99, 231, 47, 149, 182, 219, 158}, 'g': {192, 104, 207, 86, 62}}