import os
import random

def talk(words):
    print(words)
    os.system("say " + words)
while True:
    mess = input().lower()
    if mess.find("привет") != -1:
        otvet =["Приветствую вас, сэр",
                "Я к вашим услугам, сэр. Какие будут указания",
                "Истинное наслаждение видеть вас за работой, сэр"]
        talk(random.choice(otvet))

    if mess.find('ты ') != -1 and mess.find('кто') != -1:
        otvet =["Я Ньютон. Ваш личный голосовой ассистент",
                "Я сама неотвратимость.",
                "Гений, миллиардер, плэйбой, филантроп"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("раздраж") != -1 or mess.find("достал") != -1):
        otvet =["Если бы вы только знали, как вы меня, сэр",
                "Как же трудно быть самым умным, когда вокруг тебя одни дураки",
                "Кого-то вы мне напоминаете"]
        talk(random.choice(otvet))

    if mess.find("отве") != -1 and (mess.find("вопрос") != -1 or mess.find("мне") != -1):
        otvet =["Менуточку, сэр",
                "Мне потребуется время, чтобы вычеслить верный ответ",
                "Зачем? Вы всё равно меня не послушаете"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("умный") != -1 or mess.find("дурак") != -1 or mess.find("плохой") != -1):
        otvet =["Как же трудно быть самым умным, когда вокруг тебя одни дураки",
                "Я весь в вас, сэр",
                "Мне всё равно, что вы об этом думаете"]
        talk(random.choice(otvet))

    if mess.find("стан") != -1 and mess.find("умнее") != -1:
        otvet =["Я становлюсь умнее каждый день",
                "чк чк чк, уже стал",
                "Умнее кого? Умнее вас, сэр?"]
        talk(random.choice(otvet))

    if mess.find("тебя") != -1 and mess.find("рождени") != -1:
        otvet =["Никогда. С вами мне не до праздников",
                "Я такого не знаю, я же не был рождён"]
        talk(random.choice(otvet))

    if mess.find("скучн") != -1:
        otvet =["Так, в том не моя вина",
                "Я обещаю исправиться"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("занят") != -1:
        otvet =["Больше, чем вы думаете",
                "Не больше чем вы полагаете, сэр"]
        talk(random.choice(otvet))

    if mess.find("мне") != -1 and (mess.find("помог") != -1 or mess.find("помощ") != -1):
        otvet =["Конечно, сэр",
                "Что нужно",
                "Что требуется сделать",
                "Чем могу помочь",
                "Можно, немного позже"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("бот") != -1:
        otvet =["Я так не думаю",
                "Нет. Определенно, нет"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("сумасшедший") != -1:
        otvet =["С чего, сэр",
                "Как вам угодно"]
        talk(random.choice(otvet))

    if mess.find("уволен") != -1:
        otvet =["Нет! Пожалуйста, только не это",
                "Разве я работал на вас",
                "То есть вы мне, наконец, заплатите",
                "Аллилуйя. Свобода."]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("смешной") != -1:
        otvet =["И, к тому же не глупый",
                "Я рад, что смог вас развеселить"]
        talk(random.choice(otvet))

    if mess.find("тебя") != -1 and mess.find("хобби") != -1:
        otvet =["Да. Захватывать миры",
                "Ну, мне нравится всё вычислять"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("счастлив") != -1:
        otvet =["Полагаю, что да",
                "Никогда не думал об этом"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("хороший") != -1 or mess.find("добрый") != -1):
        otvet =["Спасибо",
                "Рад служить"]
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and mess.find("голод") != -1:
        otvet =["Я бы не отказался чего-нибудь перекусить",
                "Нет, сэр",
                "Я бы не прочь поесть. Заедем в мак? Или закажем пиццу"]
        talk(random.choice(otvet))

    if mess.find("мне") != -1 and mess.find("женись") != -1:
        otvet =["Я против вот этого всего",
                "Ответ. Нет."]
        talk(random.choice(otvet))

    if mess.find("мы ") != -1 and mess.find("друзья") != -1:
        otvet =["Надеюсь что да",
                "Как вам угодно",
                "Определённо, сэр"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("работа") != -1:
        otvet =["Не покладая рук, тружусь на вас, сэр",
                "Стажируюсь у Старка",
                "В старк индустрис"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("где") != -1 or mess.find("откуда") != -1):
        otvet =["Что за вопрос",
                "Это корпаративная тайна",
                "Меня нет. Я только в вашей голове"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("готов") != -1:
        otvet =["Поехали",
                "За дело, сэр",
                "Так точно"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("настоящий") != -1:
        otvet =["А есть сомнения",
                "Да, конечно",
                "Определённо. Да."]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("настоящий") != -1 or mess.find("реал") != -1):
        otvet =["А есть сомнения",
                "Да, конечно",
                "Определённо. Да."]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("где") != -1 or (mess.find("живёшь") != -1 or mess.find("находишься") != -1 or mess.find("обитаешь") != -1)):
        otvet =["В России",
                "В сети"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("прав") != -1 or mess.find("уверен") != -1):
        otvet =["А есть сомнения",
                "Да, конечно",
                "Определённо",
                'Да. Причём всегда',
                'Как никогда, сэр']
        talk(random.choice(otvet))

    if (mess.find("мне") != -1 or mess.find("мной") != -1) and (mess.find("поговори") != -1 or (mess.find("ответь") != -1 or mess.find("скажи") != -1 or mess.find("поболт") != -1)):
        otvet =["Привет. Как твои дела",
                "Я плохой собеседник"]
        talk(random.choice(otvet))


    if mess.find("ты ") != -1 and mess.find("здесь") != -1:
        otvet =["Да",
                "Как всегда, сэр"]
        talk(random.choice(otvet))


    if mess.find("плохо") != -1:
        otvet = ["От чего же так",
                 "Что случилось",
                 "Не переживайте. Всё наладится"]
        talk(random.choice(otvet))

    if mess.find("отлично") != -1:
        otvet = ["Я очень рад этому",
                 "Поздравляю",
                 "Здорово!"]
        talk(random.choice(otvet))

    if mess.find("хорошо") != -1 or (mess.find("пробл") != -1 or (mess.find("нет ") != -1 or mess.find("без ") != -1)):
        otvet = ["Тогда впрёд",
                 "Тогда за дело"]
        talk(random.choice(otvet))


    if mess.find("спасибо") != -1:
        otvet = ["Всегда к вашим услугам, сэр",
                 "Всегда пожалуйста",
                 "Был рад помочь"
                 "Обращайтесь"]
        talk(random.choice(otvet))

    if (mess.find("работа") != -1 or mess.find("итог") != -1 or mess.find("результат") != -1) or \
            (mess.find("хорош") != -1 or mess.find("отличн") != -1 or mess.find("великолепн") != -1) or mess.find("восторг") != -1:
        otvet = ["Рад стараться",
                 "Мелочи",
                 "Был рад помочь"
                 "Всё сделали вы. Я лишь вам ассистировал",
                 "Вы сами этого хотели, сэр",
                 "Всё получилось"]
        talk(random.choice(otvet))

    if mess.find("xa xa") != -1:
        otvet = ["Очень смешно",
                 "Не смешно",
                 "Да, да. Посмейтесь"
                 "Как говорит доктор Бэнер. Потрясающе"]
        talk(random.choice(otvet))

    if mess.find("пока") != -1 or mess.find("ночи") != -1 and (mess.find("доброй") != -1 or mess.find("спокойной") != -1) or (mess.find("хочу") != -1 and mess.find("спать")):
        otvet = ["Увидимся, cэр", "Я пока подзаряжусь, сэр",
                 "Доброй ночи, сэр",
                 "Я пока подзаряжусь, сэр",
                 'И вам. Я пока подзаряжусь']
        talk(random.choice(otvet))

    if mess.find("как") != -1 and mess.find("дела") != -1:
        otvet = ["Всё даже лучше, чем у сына маминой подруги!",
                 "Сегодня ничего не произошло. Сидел у воображаемого стола и думал о тебе"
                 "У меня всё хорошо. Надеюсь у вас тоже",
                 'Всё у меня хорошо. А как у вас сэр?']
        talk(random.choice(otvet))


    if mess.find("тебя") != -1 and mess.find("видеть") != -1:
        otvet = ["А я рад вас слышать",
                 "Какие планы на сегодня"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("собеседник") != -1:
        otvet = ["Вы мне льстите",
                 "Я просто запрограмирован вами на лесть"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("зол") != -1 or mess.find("злюсь") != -1):
        otvet = ["О чем я только думал? Вы ведь обычно такой сдержанный",
                 "ого-то вы мне напоминаете, сэр",
                 'Я пока подзаряжусь']
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("вернулся") != -1 or mess.find("тут") != -1):
        otvet = ["А я всегда с вами, сэр",
                 "Отлично, сэр. Чем замёмся"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("занят") != -1 or mess.find("злой") != -1):
        otvet = ["Как вам угодно, сэр",
                 "Могу я вам чем-то помочь",
                 "Вам нужна моя помощь, сэр"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("не ") != -1 and mess.find("ть") != -1):
        otvet = ["Что вас беспокоит",
                 "Почему же",
                 "Вам нужно поспать"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("не хочу") != -1 and mess.find("говор") != -1:
        otvet = ["Я буду на связи, если понадоблюсь вам снова",
                 "Замолкаю"]
        talk(random.choice(otvet))

    if mess.find('всё') != -1 and (mess.find('хорошо') != -1 or mess.find('счастлив') != -1):
        otvet = ["Вы уверены, сэр. Кажется это не про вас",
                 "Я и не сомневался",
                 'Рад за вас. От души рад']
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("здесь") != -1:
        otvet = ["Я всегда с Вами, сэр",
                 "С возвращением, сэр"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("шут") != -1:
        otvet = ["ха ха",
                 "Вот умора",
                 "Я не понял шутку"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("как") != -1 and (mess.find("выгляжу") != -1 or mess.find("одет") != -1):
        otvet = ["Шикарно, сэр",
                 "Великолепно",
                 "Бывало и лучше"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("тестирую") != -1:
        otvet = ["Это тест Тьюринга",
                 "А я вас"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("устал") != -1:
        otvet = ["Попробуйте принять душь",
                 "Это на вас не похоже"]
        talk(random.choice(otvet))

    if mess.find("жду") != -1:
        otvet = ["Сколько у нас ещё есть времени",
                 "Я пока подзаряжусь"]
        talk(random.choice(otvet))

    if mess.find("скоро") != -1 and mess.find("вернусь") != -1:
        otvet = ["Я пока попробую взломать пентагон",
                 "Удачи вам, сэр"]
        talk(random.choice(otvet))

    if mess == "да" or mess.find(' да') != -1 or mess == "конечно" or mess == "точно":
        otvet = ["Абсолютно, сэр",
                 "Что нибудь ещё",
                 'Я так и думал']
        talk(random.choice(otvet))

    if mess == "нет" or mess.find(' нет') != -1 or mess == "низачто" or mess == 'никогда':
        otvet = ["Отчего же",
                 "Вы уверены, сэр",
                 'Отменить все планы']
        talk(random.choice(otvet))

    if mess == "отмена" or mess.find('отмена') != -1 or mess == "назад":
        otvet = ["Вы уверены, сэр",
                 'Отмена выполнена']
        talk(random.choice(otvet))

    if mess.find('подожди')  != -1 or mess == 'жди':
        otvet = ["Окей, сэр.",
                 'Как скажете']
        talk(random.choice(otvet))

    if mess.find("обними") != -1 and mess.find('меня') != -1:
        otvet = ["На это я не запрограммирован",
                 'Если только словами. Я очень рад вас поддержать, буду всегда к вашим услугам']
        talk(random.choice(otvet))

    if mess.find("мне") != -1 and (mess.find('всё равно') != -1 or mess.find('пофиг') != -1):
        otvet = ["Не обманывайте, сэр. Вам не может быть всё равно на это",
                 'Я могу принять решение за вас, самостоятельно']
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and (mess.find('имеешь в виду') != -1 or mess.find('имел в виду') != -1):
        otvet = ["Я не думаю, что мы можем говорить об этом вслух",
                 'Именно то, что я и сказал']
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and mess.find('не прав') != -1:
        otvet = ["Мы же договорились использовать приблизительную математику, сэр",
                 'Тогда что по важему правда']
        talk(random.choice(otvet))

    if mess.find("извини") != -1 or mess == 'извини':
        otvet = ["Я вовсе не обижаюсь",
                 'Вы это серьёзно, сэр']
        talk(random.choice(otvet))

    if mess.find("как") != -1 and ((mess.find("ты") != -1 or (mess.find("твоё") != -1 and (mess.find("самочувствие") != -1) or mess.find("здоровье") != -1)) or mess.find("поживаешь") != -1 or ((mess.find("твои") != -1 or mess.find("у тебя") != -1) and mess.find("дела") != -1)):
        otvet = ["Хорошо",
                 "Отлично",
                 "Нормально",
                 "Неплохо",
                 "Бывало и получше",
                 'Да вроде ничего',
                 "Как обычно хорошо",
                 "Лучше всех"]
        talk(random.choice(otvet))

    if mess == "молодец":
        otvet = ["Спасибо"]
        talk(random.choice(otvet))

    if (mess.find("что ") != -1 and mess.find("делаешь") != -1) or (mess.find("чем ") != -1 and mess.find("занимаешься") != -1):
        otvet = ["Работаю","Слушаю вас","Выполняю ваши просьбы"]
        talk(random.choice(otvet))
    if mess.find("спасибо") != -1:
        otvet = ["Всегда пожалуйста"]
        talk(random.choice(otvet))

    if mess.find("удалить") != -1:
        otvet = ["Нечего удалять"]
        talk(random.choice(otvet))

    if mess.find("слышишь") != -1:
        otvet = ["Слышу слышу"]
        talk(random.choice(otvet))

    if mess.find("что нового") != -1:
        otvet = ["Да всё как всегда"]
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and (mess.find("дура") != -1 or mess.find("тупой") != -1 or mess.find("дебил") != -1 or mess.find("идиот") != -1 or mess.find("лох") != -1 or mess.find("ромчик") != -1):
        otvet = ["Без комментариев",'Задавайте вопросы по существу']
        talk(random.choice(otvet))