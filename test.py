import re

# Defining a regex pattern to match only the specified Chinese character ranges
chinese_check = re.compile(
            r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF"  # Arabic
            r"\u4E00-\u9FFF\u3400-\u4DBF\U00020000-\U0002A6DF\U0002A700-\U0002EBEF\U00030000-\U000323AF"  # Chinese
            r"\uFA0E\uFA0F\uFA11\uFA13\uFA14\uFA1F\uFA21\uFA23\uFA24\uFA27\uFA28\uFA29"  # Chinese rare characters
            r"\u3006\u3007"  # Ideographic number zero, ideograph (general)
            r"\u3040-\u309F\u30A0-\u30FF"  # Japanese Hiragana and Katakana
            r"\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F"  # Korean
            r"\u0E00-\u0E7F"  # Thai
            r"\u1EA0-\u1EF9"  # Vietnamese, focus on letters with diacritics
            r"\u0900-\u097F"  # Devanagari (Hindi, Sanskrit, and others)
            r"\u0B80-\u0BFF"  # Tamil
            r"\u0980-\u09FF"  # Bengali
            r"]+"
        )

# Testing with the character 'a'
test_char = "qwertzuiopü+*~asdfghjklöä''<>|yxcvbnm,.-;:_QWERTZUIOPÜASDFGHJKLÖÄYXCVBNM^^!§$%&/()=?´´12345678900?\\}][{µ€"
while match := chinese_check.search(test_char):
    test_char = test_char.replace(match.group(), "")
    print("Replace")

print(test_char)

result = "Match found: {}".format(match.group()) if match else "No match found for 'a'."

print(result)
