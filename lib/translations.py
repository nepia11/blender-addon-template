# 通常の翻訳辞書があんまり見やすくなくて、記述量が多いので生成するようにしている
# translation_dictをimportするので同じ名前で手書きすればそっちでも使える
keys = [
    "word 1",
    "word 2",
]

jp = [
    "ワード 1",
    "ワード 2",
]

translation_dict = {
    "en_US": {("*", key): key for key in keys},
    "ja_JP": {("*", key): j for key, j in zip(keys, jp)}
}

# debug
# import pprint
# pprint.pprint(translation_dict)
