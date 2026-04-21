import re
from collections import Counter

class BlogPostTitleSuggester:
    def __init__(self, text):
        self.text = text

    def suggest_title(self):
        # Kelimalarini ajratib olamiz
        words = re.findall(r'\b\w+\b', self.text.lower())

        # Eng ko'p ishlatilgan so'zlarni topamiz
        word_counts = Counter(words)

        # Eng ko'p ishlatilgan so'zni chiqarib olamiz
        most_common_word = word_counts.most_common(1)[0]

        # Blog post title sini taklif qilamiz
        title = f"{most_common_word[0]}: {self.text}"

        return title

# Misol uchun foydalanish
text = "Bu blog postda biz blog postlar uchun mavzularni taklif qilamiz. Blog postlar uchun mavzularni taklif qilishning eng yaxshi yo'li haqida gapirib boramiz."
suggester = BlogPostTitleSuggester(text)
print(suggester.suggest_title())
