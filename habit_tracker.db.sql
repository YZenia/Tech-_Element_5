--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Пт апр 19 13:00:52 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: habit_progress
CREATE TABLE IF NOT EXISTS habit_progress (id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER, progress_date DATE, FOREIGN KEY (habit_id) REFERENCES habits (id));
INSERT INTO habit_progress (id, habit_id, progress_date) VALUES (1, 5, '2024-04-19');
INSERT INTO habit_progress (id, habit_id, progress_date) VALUES (2, 2, '2024-04-19');
INSERT INTO habit_progress (id, habit_id, progress_date) VALUES (3, 7, '2024-04-19');

-- Таблица: habits
CREATE TABLE IF NOT EXISTS habits (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, user_id INTEGER, habit_name TEXT, habit_description TEXT, habit_goal TEXT, habit_frequency TEXT, FOREIGN KEY (user_id) REFERENCES users (id));
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (1, 1, 'Регулярные упражнения', 'Это может быть ходьба, бег, йога или любой другой вид спорта.', 'Поддерживайте физическую активность, чтобы улучшить здоровье, настроение и общее самочувствие.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (2, 2, 'Постоянное обучение', 'Постоянно обучайтесь новому, читайте книги, изучайте языки или развивайте новые навыки', 'Это стимулирует ваш мозг и помогает оставаться умственно активным.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (3, 3, 'Медитация или время на размышления', 'Уделяйте время тишине, медитации или просто спокойствию', 'Уменьшить стресс и улучшить ментальное здоровье', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (4, 1, 'Достаточный сон', 'Стремитесь спать 7-8 часов каждую ночью', 'Качественный сонвлияеет на наше настроение,продуктивность и общее здоровье', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (5, 1, 'Здоровое питание', 'Придерживайтесь сбалансированного рациона, включающего фрукты, овощи, белки и зерновые. Избегайте переедания и фастфуда', 'Улучшить здоровье,настроение и общее самочувствие', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (7, 3, 'Постоянное обучение', 'Постоянно обучайтесь новому, читайте книги, изучайте языки или развивайте новые навыки', 'Это стимулирует ваш мозг и помогает оставаться умственно активным.', 'Ужедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (8, NULL, ' Табакокурение ??', 'Привычка вдыхать ядовитый дым табака.', 'Улучшение здоровья и качества жизни', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (9, NULL, ' Злоупотребление алкоголем ??', 'Использование спиртного как психологического костыля.', 'Ограничение потребления алкого', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (10, NULL, ' Употребление наркотиков ??', 'Поиск психологического покоя в наркотиках.', 'Прекращение употребления наркотиков', 'Ужедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (11, NULL, ' Нездоровое питание ??', 'Использование еды как эмоциональной защиты.', 'Установление здорового рациона питания', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (12, NULL, ' Малоподвижный образ жизни ???', 'Прибежище от стресса в бездействии.', 'Увеличение физической активности', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (13, NULL, ' Чрезмерное использование цифровых устройств ??', 'Уход от проблем в виртуальный мир.', 'Ограничение времени, проведенного перед экраном', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (14, NULL, ' Прокрастинация ?', 'Уход от реальности в мир "потом".', 'Повышение производительности и эффективности', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (15, NULL, ' Недостаток сна ??', 'Избегание обработки эмоций во сне.', 'Обеспечение достаточного и качественного сна', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (16, NULL, ' Чрезмерное потребление кофеина ?', 'Замена отдыха на возбуждающий напиток.', 'Ограничение потребления кофеина', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (17, NULL, ' Агрессивное поведение ??', 'Использование агрессии как защиты.', 'Управление эмоциями и поведением', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (18, NULL, ' Избыточная критичность к себе и другим ??', 'Постоянное оценивание и сравнение с окружающим.', 'Принятие и положительное отношение к себе', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (19, NULL, ' Игнорирование личной гигиены ??', 'Уход от заботы о себе в погоне за идеалом.', 'Улучшение здоровья и самочувствия', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (20, NULL, ' Обман ??', 'Использование лжи как защитного механизма.', 'Построение доверительных отношений', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (21, NULL, ' Чрезмерное употребление сахара ??', 'Замена недостающего удовольствия на сладкое.', 'Ограничение потребления сахара', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (22, NULL, ' Нежелание принимать помощь или советы ??', 'Страх открыться и показать свою слабость.', 'Открытость и готовность к улучшению', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (23, NULL, ' Изоляция ??', 'Поиск убежища от общества и его оценок.', 'Установление социальных связей', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (24, NULL, ' Чрезмерное ношение высоких каблуков ??', 'Привычка маскировать боли за красоту.', 'Забота о здоровье стоп и ног', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (25, NULL, ' Игнорирование проблем со здоровьем ??', 'Страх признать себя слабым или больным.', 'Уход за собой и своим здоровьем', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (26, NULL, ' Перфекционизм ??', 'Стремление к идеалу в каждом действии.', 'Принятие недостатков и достижение гибкости', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (27, NULL, ' Зависимость от мнений других ??', 'Отказ от собственной самооценки.', 'Развитие собственной самооценки', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (28, NULL, ' Чрезмерная зависимость от кредитов и займов ??', 'Использование денег как психологической опоры.', 'Управление финансовым положением', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (29, NULL, 'Чрезмерное времяпрепровождение перед телевизором ??', 'Поиск убежища в мире фиктивных историй.', 'Ограничение времени перед экраном', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (31, NULL, ' Избыточный шопинг или потребительство ???', 'Поиск удовлетворения в материальных вещах.', 'Управление финансами и потребностями', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (32, NULL, 'Избегание ответвенности', 'Страх не справиться с возложенными обязанностями.', 'Принятие ответственности за свои действия', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (33, NULL, ' Чрезмерное употребление соли ??', 'Использование соли как попытка дозировать стресс.', 'Ограничение потребления соли', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (34, NULL, 'Игнорирование проблем с психическим здоровьем ??', 'Страх показать свою уязвимость.', 'Обращение за помощью и поддержка', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (35, NULL, 'Склонность к сплетням и осуждению других', 'Поиск удовлетворения в чужих проблемах.', 'Повышение уважения и понимания к окружающим', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (36, NULL, 'Игнорирование социальных норм и правил', 'Отказ от взаимодействия с обществом.', 'Уважение и соблюдение социальных норм', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (37, NULL, 'Злоупотребление слуховыми устройствами', 'Поиск поглощения в мире звуков.', 'Защита слуха и предотвращение повреждений', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (38, NULL, 'Регулярные физические упражнения ????>?', 'Активное движение для здоровья и энергии.', 'Улучшение физической формы и общего самочувствия.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (39, NULL, 'Здоровое питание ??', 'Питание, богатое питательными веществами и витаминами.', 'Поддержание здорового образа жизни и оптимального веса.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (40, NULL, 'Достаточный сон ??', 'Полноценный отдых для восстановления организма.', 'Обеспечение хорошего психоэмоционального и физического состояния.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (41, NULL, 'Питье достаточного количества воды ??', 'Употребление достаточного объема воды для гидратации.', 'Поддержание здорового обмена веществ и функционирования организма.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (42, NULL, 'Чтение книг ??', 'Интеллектуальное развитие и отдых от повседневности', 'Развитие креативности, воображения и когнитивных навыков.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (43, NULL, 'Медитация или йога ??', 'Практика умиротворения и сброса стресса.', 'Улучшение психического здоровья и снятие напряжения.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (44, NULL, 'Планирование своего времени ??', 'Эффективное распределение времени для достижения целей.', 'Повышение производительности и организация повседневной жизни.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (45, NULL, 'Ходьба на свежем воздухе ??', 'Физическая активность и насыщение кислородом.', 'Улучшение здоровья и настроения, снижение стресса.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (46, NULL, 'Умение говорить "нет" ??', 'Умение отказаться от ненужных обязательств и стресса.', 'Установление границ, сохранение энергии и здоровья.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (47, NULL, 'Регулярные медицинские осмотры ??', 'Поддержание здоровья и своевременное выявление проблем.', 'Профилактика заболеваний и раннее выявление здоровотрепящих проблем.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (50, NULL, 'Сохранение чистоты и порядка ??', 'Создание комфортной и уютной обстановки в доме.', 'Улучшение физического и психологического благополучия.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (51, NULL, 'Умеренное потребление алкоголя ??', 'Умеренное употребление алкогольных напитков для удовольствия.', 'Поддержание здорового образа жизни и социальных отношений.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (52, NULL, 'Сохранение позитивного настроения ??', 'Оптимистическое мышление и радостное настроение.', 'Улучшение эмоционального состояния и отношений с окружающими.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (53, NULL, 'Участие в волонтерских проектах ??', 'Помощь и поддержка другим, создание позитивного влияния.', 'Удовлетворение от сотрудничества и укрепление связей с сообществом.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (54, NULL, 'Практика благодарности ??', 'Осознанное признание благодарности и признательности.', 'Повышение уровня счастья и улучшение психического состояния.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (55, NULL, 'Отказ от курения ??', 'Прекращение потребления табачных изделий.', 'Улучшение здоровья и снижение риска развития различных заболеваний.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (56, NULL, 'Правильное дыхание ???', 'Сознательное управление дыханием для уменьшения стресса.', 'Повышение эффективности дыхательной системы и снижение уровня стресса', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (57, NULL, 'Обучение новым навыкам ??', 'Постоянное обогащение себя новыми знаниями и навыками.', 'Развитие личности, расширение кругозора и повышение самооценки.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (58, NULL, 'Поддержание социальных связей ??', 'Участие в общественной жизни и поддержание отношений', 'Повышение эмоциональной поддержки и ощущения принадлежности.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (59, NULL, 'Забота о своем психическом здоровье ??', 'Сознательное уход за психическим состоянием и эмоциями.', 'Укрепление психологической стойкости и адаптивных ресурсов.', 'Ежедневно');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (60, NULL, 'Регулярное обновление целей ??', 'Постоянное стремление к самосовершенствованию и росту.', 'Поддержание мотивации и ощущения направленности в жизни.', 'Ежедневно');

-- Таблица: users
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL);
INSERT INTO users (id, username) VALUES (1, 'Олег');
INSERT INTO users (id, username) VALUES (2, 'Карина');
INSERT INTO users (id, username) VALUES (3, 'Ольга');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
