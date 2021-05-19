from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
anon = AnonymousSurvey('В каком городе ты живешь?')

# Вывод вопроса и сохранение ответов.
anon.show_question()
print("Чтобы выйти, введите 'q' в любой момент.\n")
while True:
    response = input("Ответ: ")
    if response == 'q':
        break
    anon.store_response(response)

# Вывод результатов опроса.
print("\nСпасибо всем, кто принял участие в опросе!")
anon.show_results()
