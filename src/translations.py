keys = [
    "tranlation 1",
    "tranlation 2",
]

jp = [
    "翻訳 1",
    "翻訳 2",
]

translation_dict = {
    "en_US": {("*", key): key for key in keys},
    "ja_JP": {("*", key): j for key, j in zip(keys, jp)}
}

# debug
# import pprint
# pprint.pprint(translation_dict)
