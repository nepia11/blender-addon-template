# 通常の翻訳辞書があんまり見やすくなくて、記述量が多いので生成するようにしている
keys = [
    "word 1",
    "word 2",
    "my operator",
]

jp = [
    "ワード 1",
    "ワード 2",
    "マイオペレータ"
]


def get_dict():
    translation_dict = {
        "en_US": {("*", key): key for key in keys},
        "ja_JP": {("*", key): j for key, j in zip(keys, jp)}
    }
    return translation_dict

# debug
# import pprint
# pprint.pprint(translation_dict)
