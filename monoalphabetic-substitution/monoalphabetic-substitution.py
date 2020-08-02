
test_substitution_xyz = {
    "a": "q",
    "b": "w",
    "c": "e",
    "d": "r",
    "e": "t",
    "f": "z",
    "g": "u",
    "h": "i",
    "i": "o",
    "j": "p",
    "k": "a",
    "l": "s",
    "m": "d",
    "n": "f",
    "o": "g",
    "p": "h",
    "q": "j",
    "r": "k",
    "s": "l",
    "t": "y",
    "u": "x",
    "v": "c",
    "w": "v",
    "x": "b",
    "y": "n",
    "z": "m"
}


def encrypt(test_string: str, substitution: dict):
    success, result = test_substitution(substitution)
    if not success:
        print("Multiple definitions of: " + str(result))

    new_string = ""
    for c in test_string:
        if c in substitution.keys():
            new_string += substitution[c]
        else:
            new_string += c
    return new_string


def decrypt(test_string: str, substitution: dict):
    success, result = test_substitution(substitution)
    if not success:
        print("Multiple definitions of: " + str(result))
    new_string = ""

    for c in test_string:
        found = False
        for i in range(len(substitution)):
            if c == list(substitution.values())[i]:
                new_string += list(substitution.keys())[i]
                found = True
                break
        if not found:
            new_string += c
    return new_string


def test_substitution(substitution: dict):
    already_tested = []
    multi_def = []
    for item in substitution.values():
        if item not in already_tested:
            already_tested.append(item)
        else:
            multi_def.append(item)
    return len(multi_def) <= 0, multi_def


if __name__ == "__main__":
    print(encrypt("""Of recommend residence education be on difficult repulsive offending. Judge views had mirth table seems great him for her. Alone all happy asked begin fully stand own get. Excuse ye seeing result of we. See scale dried songs old may not. Promotion did disposing you household any instantly. Hills we do under times at first short an.
Affronting discretion as do is announcing. Now months esteem oppose nearer enable too six. She numerous unlocked you perceive speedily. Affixed offence spirits or ye of offices between. Real on shot it were four an as. Absolute bachelor rendered six nay you juvenile. Vanity entire an chatty to.
Looking started he up perhaps against. How remainder all additions get elsewhere resources. One missed shy wishes supply design answer formed. Prevent on present hastily passage an subject in be. Be happiness arranging so newspaper defective affection ye. Families blessing he in to no daughter.
Carriage quitting securing be appetite it declared. High eyes kept so busy feel call in. Would day nor ask walls known. But preserved advantage are but and certainty earnestly enjoyment. Passage weather as up am exposed. And natural related man subject. Eagerness get situation his was delighted.
Of on affixed civilly moments promise explain fertile in. Assurance advantage belonging happiness departure so of. Now improving and one sincerity intention allowance commanded not. Oh an am frankness be necessary earnestly advantage estimable extensive. Five he wife gone ye. Mrs suffering sportsmen earnestly any. In am do giving to afford parish settle easily garret.
Do greatest at in learning steepest. Breakfast extremity suffering one who all otherwise suspected. He at no nothing forbade up moments. Wholly uneasy at missed be of pretty whence. John way sir high than law who week. Surrounded prosperous introduced it if is up dispatched. Improved so strictly produced answered elegance is.
Way nor furnished sir procuring therefore but. Warmth far manner myself active are cannot called. Set her half end girl rich met. Me allowance departure an curiosity ye. In no talking address excited it conduct. Husbands debating replying overcame blessing he it me to domestic.
Sociable on as carriage my position weddings raillery consider. Peculiar trifling absolute and wandered vicinity property yet. The and collecting motionless difficulty son. His hearing staying ten colonel met. Sex drew six easy four dear cold deny. Moderate children at of outweigh it. Unsatiable it considered invitation he travelling insensible. Consulted admitting oh mr up as described acuteness propriety moonlight.
No comfort do written conduct at prevent manners on. Celebrated contrasted discretion him sympathize her collecting occasional. Do answered bachelor occasion in of offended no concerns. Supply worthy warmth branch of no ye. Voice tried known to as my to. Though wished merits or be. Alone visit use these smart rooms ham. No waiting in on enjoyed placing it inquiry.
Written enquire painful ye to offices forming it. Then so does over sent dull on. Likewise offended humoured mrs fat trifling answered. On ye position greatest so desirous. So wound stood guest weeks no terms up ought. By so these am so rapid blush songs begin. Nor but mean time one over.
""", test_substitution_xyz))
    print(decrypt("yit jxoea wkgvf zgb pxdhl gctk yit sqmn rgu", test_substitution_xyz))
