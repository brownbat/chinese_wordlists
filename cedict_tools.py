'''resources
https://en.wikibooks.org/wiki/Chinese_(Mandarin)/Table_of_Initial-Final_Combinations



'''

tests = [
    "bāba",
    "bā ba",
    "ni3",
    "fēng",
    "fēng1",
    "Tiān​'ān​mén",
    "Tiān'ānmén",
    "feng1 li4",
    "fēng​lì",
    "fēngjì",
    "gàng",
    "ma",
    "!ma",
    "ma-",
    "ma ",
    "xmnma ",
    "hello",
    "shuangr",
    "shuangr3",
    "shuangr9",
    "āiya!",
    "'ān​mén",
    "'ānmén",
    "ān​mén",
    "ānmén"
]


# just load the whole dictionary to memory
cedict = {}
location = ".//cedict_1_0_ts_utf-8_mdbg.txt"
with open(location, "rt") as cedict_file:
    for l in cedict_file.readlines():
        if l[0] == "#":
            pass
        else:
            trad_simp, pinyin_definition = l.split("[", 1)
            assert len(trad_simp.split()) == 2
            trad, simp = trad_simp.split()
            pinyin, definition = pinyin_definition.split("]", 1)
            definition = definition[2:-2]
            definition = definition.replace('|', '/')
            entry = [trad, simp, pinyin, definition]
            if trad not in cedict:
                cedict[trad] = entry
            else:
                if cedict[trad][1] != simp:
                    cedict[trad][1] += f"; {simp}"
                if pinyin not in cedict[trad][2]:
                    cedict[trad][2] += f"; {pinyin}"
                if definition not in cedict[trad][3]:
                    cedict[trad][3] += f"; {definition}"
            if simp not in cedict:
                cedict[simp] = entry

valid_pinyin_syllables = [
    "a", "ai", "an", "ang", "ao", "ba", "bai", "ban", "bang", "bao", "bei",
    "ben", "beng", "bi", "bian", "biao", "bie", "bin", "bing", "bo", "bu",
    "ca", "cai", "can", "cang", "cao", "ce", "cen", "ceng", "cha", "chai",
    "chan", "chang", "chao", "che", "chen", "cheng", "chi", "chong", "chou",
    "chu", "chua", "chuai", "chuan", "chuang", "chui", "chun", "chuo", "ci",
    "cong", "cou", "cu", "cuan", "cui", "cun", "cuo", "da", "dai", "dan",
    "dang", "dao", "de", "dei", "den", "deng", "di", "dia", "dian", "diao",
    "die", "ding", "diu", "dong", "dou", "du", "duan", "dui", "dun", "duo",
    "e", "ei", "en", "eng", "er", "fa", "fan", "fang", "fei", "fen", "feng",
    "fo", "fou", "fu", "ga", "gai", "gan", "gang", "gao", "ge", "gei", "gen",
    "geng", "gong", "gou", "gu", "gua", "guai", "guan", "guang", "gui",
    "gun", "guo", "ha", "hai", "han", "hang", "hao", "he", "hei", "hen",
    "heng", "hong", "hou", "hu", "hua", "huai", "huan", "huang", "hui",
    "hun", "huo", "ji", "jia", "jian", "jiang", "jiao", "jie", "jin", "jing",
    "jiong", "jiu", "ju", "juan", "jue", "jun", "ka", "kai", "kan", "kang",
    "kao", "ke", "ken", "keng", "kong", "kou", "ku", "kua", "kuai", "kuan",
    "kuang", "kui", "kun", "kuo", "la", "lai", "lan", "lang", "lao", "le",
    "lei", "leng", "li", "lia", "lian", "liang", "liao", "lie", "lin",
    "ling", "liu", "lo", "long", "lou", "lu", "luan", "lun", "luo", "lü",
    "lüe", "ma", "mai", "man", "mang", "mao", "me", "mei", "men", "meng",
    "mi", "mian", "miao", "mie", "min", "ming", "miu", "mo", "mou", "mu",
    "na", "nai", "nan", "nang", "nao", "ne", "nei", "nen", "neng", "ni",
    "nian", "niang", "niao", "nie", "nin", "ning", "niu", "nong", "nou",
    "nu", "nuan", "nun", "nuo", "nü", "nüe", "o", "ou", "pa", "pai", "pan",
    "pang", "pao", "pei", "pen", "peng", "pi", "pian", "piao", "pie", "pin",
    "ping", "po", "pou", "pu", "qi", "qia", "qian", "qiang", "qiao", "qie",
    "qin", "qing", "qiong", "qiu", "qu", "quan", "que", "qun", "ran", "rang",
    "rao", "re", "ren", "reng", "ri", "rong", "rou", "ru", "ruan", "rui",
    "run", "ruo", "sa", "sai", "san", "sang", "sao", "se", "sen", "seng",
    "sha", "shai", "shan", "shang", "shao", "she", "shen", "sheng", "shi",
    "shou", "shu", "shua", "shuai", "shuan", "shuang", "shui", "shun",
    "shuo", "si", "song", "sou", "su", "suan", "sui", "sun", "suo", "ta",
    "tai", "tan", "tang", "tao", "te", "teng", "ti", "tian", "tiao", "tie",
    "ting", "tong", "tou", "tu", "tuan", "tui", "tun", "tuo", "wa", "wai",
    "wan", "wang", "wei", "wen", "weng", "wo", "wu", "xi", "xia", "xian",
    "xiang", "xiao", "xie", "xin", "xing", "xiong", "xiu", "xu", "xuan",
    "xue", "xun", "ya", "yan", "yang", "yao", "ye", "yi", "yin", "ying",
    "yo", "yong", "you", "yu", "yuan", "yue", "yun", "za", "zai", "zan",
    "zang", "zao", "ze", "zei", "zen", "zeng", "zha", "zhai", "zhan",
    "zhang", "zhao", "zhe", "zhei", "zhen", "zheng", "zhi", "zhong", "zhou",
    "zhu", "zhua", "zhuai", "zhuan", "zhuang", "zhui", "zhun", "zhuo", "zi",
    "zong", "zou", "zu", "zuan", "zui", "zun", "zuo"
]

vowels_with_tones = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"

initials = [
    "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x",
    "zh", "ch", "sh", "r", "z", "c", "s", "y"
    # y is not a traditional initial but helpful for text processing b/c
    # it is used in place of i at the beginning of syllables
    ]

finals = [
    # Group a Finals
    "a", "o", "e", "ai", "ei", "ao", "ou", "an", "en", "ang", "eng", "er",
    # Group i Finals
    "i", "ia", "io", "ie", "iai", "iao", "iu", "ian", "in", "iang", "ing",
    # Group u Finals
    "u", "ua", "uo", "uai", "ui", "uan", "un", "uang", "ong",
    # Group ü Finals
    "ü", "üe", "üan", "ün", "iong", "ue"
    # ue is not a traditional final but used in place of üe after j,q,x,y
]


def normalize_pinyin(accented_string, trim=False, leave_numbers=False):
    """Removes accents and reduces to lowercase, converts v to ü

    If trim set True, discards all nonstandard characters
    TODO: Optionally leave an initial capital alone
    """
    outstr = ""
    for l in accented_string.lower():
        if l in "āáǎà":
            outstr += "a"
        elif l in "ēéěè":
            outstr += "e"
        elif l in "īíǐì":
            outstr += "i"
        elif l in "ōóǒò":
            outstr += "o"
        elif l in "ūúǔù":
            outstr += "u"
        elif l in "ǖǘǚǜv":
            outstr += "ü"
        elif trim:
            test_str = "'" + "".join(initials) + "".join(finals)
            if leave_numbers:
                test_str += "012345"
            if l in test_str:
                outstr += l
        else:
            outstr += l
    return outstr


"""
test_function = normalize_pinyin
for t in tests:
    print(f"{t}: |{test_function(t)}|, trimmed: |"
          + f"{test_function(t, trim=True)}|")
exit()
"""


def is_valid_pinyin_syllable(syllable,
                             allow_numbered=True,
                             allow_toneless=True,
                             allow_erhua=True,
                             normalize=True):
    '''Returns true if syllable is valid pinyin.

    Currently checks against valid syllables list, with or without
    appended 'r' for erhua and/or number for numbered tones.
    '''
    if normalize:
        syllable = normalize_pinyin(syllable.lower())
    valid = False
    if syllable in valid_pinyin_syllables:
        valid = True
    elif (syllable[:-1] in valid_pinyin_syllables
          and syllable[-1] in ['0', '1', '2', '3', '4', '5', 'r']):
        valid = True
    elif (syllable[:-2] in valid_pinyin_syllables
          and syllable[-2:] in ['r0', 'r1', 'r2', 'r3', 'r4', 'r5']):
        valid = True
    return valid


"""
test_function = is_valid_pinyin_syllable
for t in tests:
    print(f'''{t}: {test_function(t)}, no normalize:''' +
          f'''{test_function(t, normalize=False)}''')
exit()
"""


def number_pinyin(syllable):
    '''Convert accented pinyin syllable to numbered pinyin.

    Currently discards extra junk characters, punctuation, spaces.
    TODO: Optionally keep and correctly place other characters.
    '''

    outstr = ""
    tone = 5
    for letter in syllable:
        if letter.lower() in vowels_with_tones:
            vowels_index = vowels_with_tones.find(letter.lower())
            new_vowel = "aeiouü"[vowels_index // 4]
            outstr += new_vowel
            tone = vowels_index % 4 + 1
        else:
            outstr += letter
    outstr = normalize_pinyin(outstr)
    assert is_valid_pinyin_syllable(outstr), (
        f"""outstr "{outstr}" not valid pinyin""")
    outstr += str(tone)
    return outstr


"""
test_function = number_pinyin
for t in tests:
    if is_valid_pinyin_syllable(t):
        print(f"{t}: {test_function(t)}")
exit()
"""


def first_pinyin_syllable(syllables_string, trim=True):
    """Returns first syllable of valid accented pinyin

    longest pinyin syllable might be: shuangr3"""

    if trim:
        tmp_syl_str = syllables_string
        while (tmp_syl_str[0].lower() not in "".join(initials) +
               "".join(finals) + "".join(vowels_with_tones)):
            tmp_syl_str = tmp_syl_str[1:]
        syllables_string = tmp_syl_str

    outstr = None
    for syl_len in range(8, 0, -1):
        test_str = syllables_string[:syl_len]
        if is_valid_pinyin_syllable(test_str):
            outstr = test_str
            break
    return outstr


"""
test_function = first_pinyin_syllable
for t in tests:
    print(f'''{t}: |{test_function(t)}|, notrim: |{test_function(t,
          trim=False)}|''')
exit()
"""


def rest_of_string(syllables_string):
    start_index = syllables_string.find(first_pinyin_syllable(syllables_string))
    str_len = len(first_pinyin_syllable(syllables_string))
    index = start_index + str_len
    return syllables_string[index:]


"""
test_function = rest_of_string
for t in tests:
    print(f"{t}: |{test_function(t)}|")
exit()
"""


def is_valid_numbered_pinyin(syllable, strict=False):
    valid = is_valid_pinyin_syllable(syllable, normalize=False)
    if strict:
        valid = valid and syllable[-1] in "12345"
    return valid


"""
test_function = is_valid_numbered_pinyin
for t in tests:
    print(f"{t}: {test_function(t)}, strict:" +
          f"{test_function(t, strict=True)}")
exit()
"""


def accent_pinyin_syllable(syllable):
    '''Converts numbered pinyin syllable to accented

    e.g., 'xia3' to 'xiǎ'

    Rules:
    1. accent a or e
    2. accent o in ou
    3. in all other cases, accent the final vowel'''

    vowels_with_tones = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    syllable = syllable.lower().strip()
    if syllable[-1] in "1234":
        tone = int(syllable[-1])
    elif syllable[-1] in "05":
        tone = 5
        syllable = syllable[:-1]
    else:
        # unaccented syllable
        tone = 5

    if "a" in syllable:
        index = syllable.find("a")
    elif "e" in syllable:
        index = syllable.find("e")
    elif "ou" in syllable:
        index = syllable.find("ou")
    elif syllable[-2] in "nr":
        index = len(syllable) - 3
    elif syllable[-2] == "g":
        index = len(syllable) - 4
    else:
        index = len(syllable) - 2

    if str(tone) in "1234":
        tone_index = "aeiouü".find(syllable[index]) * 4 + tone - 1
        new_vowel = vowels_with_tones[tone_index]
        syllable = syllable[:index] + new_vowel + syllable[index+1:-1]
    return syllable


"""
test_function = accent_pinyin_syllable
for t in tests:
    if is_valid_numbered_pinyin(t):
        print(f"{t}: |{test_function(t)}|")
exit()
"""


def longest_initial_valid_pinyin_syllable(syllables_string):
    final_idx = None
    for idx in range(7, 0, -1):
        test_str = normalize_pinyin(syllables_string[:idx])
        if test_str in valid_pinyin_syllables:
            final_idx = idx
            break
    syllable = None
    if final_idx:
        syllable = syllables_string[:final_idx]
        if len(syllables_string) > final_idx:
            if syllables_string[final_idx] == "r":
                syllable += "r"
                final_idx += 1
        if len(syllables_string) > final_idx:
            if syllables_string[final_idx] in "012345":
                final_idx += 1
                syllable = syllables_string[:final_idx]        
    return syllable


"""
test_function = longest_initial_valid_pinyin_syllable
for t in tests:
    print(f"{t}: |{test_function(t)}|")
exit()
"""


def first_valid_pinyin_syllable(syllables_string):
    """Aggressively drops initial characters until it finds valid pinyin

    """
    first = None
    for idx in range(len(syllables_string)):
        tmp = longest_initial_valid_pinyin_syllable(syllables_string[idx:])
        if tmp:
            first = tmp
            break
    return first


"""
test_function = first_valid_pinyin_syllable
for t in tests:
    print(f"{t}: |{test_function(t)}|")
exit()
"""


def first_valid_pinyin_index(syllables_string):
    """Aggressively drops initial characters until it finds valid pinyin

    """
    first = None
    start_idx = None
    for idx in range(len(syllables_string)):
        tmp = longest_initial_valid_pinyin_syllable(syllables_string[idx:])
        if tmp:
            first = tmp
            start_idx = idx
            break
    if first:
        final_idx = start_idx + len(first)
        if len(syllables_string) > final_idx:
            if syllables_string[final_idx] == "r":
                final_idx += 1
        if len(syllables_string) > final_idx:
            if syllables_string[final_idx] in "012345":
                final_idx += 1
        return [start_idx, final_idx]
    else:
        return None


"""
test_function = first_valid_pinyin_index
for t in tests:
    print(f"{t}: |{test_function(t)}|")
exit()
"""


def split_pinyin_syllables(syllables):
    """
    Split string into list of substrings that are valid pinyin or not
    TODO: Currently hopelessly broken
    """
    idxs = first_valid_pinyin_index(syllables)
    while idxs[-1] < len(syllables):
        print(syllables[idxs[-1]])
        input()
        tmp_idxs = first_valid_pinyin_index(syllables[idxs[-1]])
        if tmp_idxs:
            idxs.extend([_ + idxs[-1] for _ in tmp_idxs])
        else:
            idxs.append(len(syllables))
    return idxs

"""
tests = [
    "Tiān​'ān​mén",
    "Tiān'ānmén",
    "'ān​mén",
    "'ānmén",
    "ān​mén",
    "ānmén"
]


test_function = split_pinyin_syllables
for t in tests:
    print(f"{t}: |{test_function(t)}|")
exit()


def accent_pinyin_syllables(syllables):
    outstr = ""
    for s in split_pinyin_syllables(syllables):
        if is_valid_pinyin(s):
            outstr += accent_pinyin_syllable(s)
        elif s in ",; ":
            outstr += s
        else:
            print(syllables)
            print(split_pinyin_syllables(syllables))
            print(f"{s} is not valid pinyin, cannot accent it")
            assert False
    outstr.strip()
    return outstr


test_function = accent_pinyin_syllables
for t in tests:
    print(f"{t}: |{test_function(t)}|")
exit()
"""

cases = """倒
安靜
安排
爸爸""".split()

for c in cases:
    trad, simp, pinyin, definition = cedict[c]
    if trad != simp:
        print(f"{simp} ({trad})|{pinyin}|{definition}")
    else:
        print(f"{trad}|{pinyin}|{definition}")

""" # restore if accent_pinyin_syllables() fixed
    if trad != simp:
        print(f"{simp} ({trad})|{accent_pinyin_syllables(pinyin)}|{definition}")
    else:
        print(f"{trad}|{accent_pinyin_syllables(pinyin)}|{definition}")
"""