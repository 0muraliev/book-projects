favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Были упомянуты следующие языки:")
#  Чтобы получить список выбранных языков без повторений, можно воспользоваться множеством (set).
for language in set(favorite_languages.values()):
    print(language.title())


# ПРИМЕЧАНИЕ Множество можно построить прямо в фигурных скобках с разделением элементов запятыми:
languages = {'python', 'java', 'ruby', 'C', 'python'}
print(languages)
