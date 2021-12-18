(function(global){var Language = {};

Language.pluralFormFunction = function (n) {
		var mod10 = n % 10,
			mod100 = n % 100;

		if (mod10 === 1 && mod100 !== 11) {
			return 'one';
		}

		if (
			(mod10 >= 2 && mod10 <= 4) &&
			(mod100 < 12 || mod100 > 14 )
		) {
			return 'few';
		}

		return 'other';
	};


Language.bubble = Language.bubble || {};

Language.bubble.attention_grabber = {
	"message": "Уведомление-подсказка чата"
};


Language.chat = Language.chat || {};

Language.chat.Warning = {
	"message": "Предупреждение"
};
Language.chat.accept_call = {
	"message": "Принять"
};
Language.chat.active = {
	"message": "Активный"
};
Language.chat.agent_profile_image = {
	"message": "Изображение профиля оператора"
};
Language.chat.agent_ringing = {
	"message": "Входящий вызов"
};
Language.chat.all_conversations = {
	"message": "Посмотреть все разговоры"
};
Language.chat.call_end_details = {
	"message": "Начат в #startedOn и длился #duration",
	"vars": [
		"startedOn",
		"duration"
	]
};
Language.chat.call_error_load = {
	"message": "Невозможно загрузить данные звонка."
};
Language.chat.call_started_on = {
	"message": "Начат в #startedOn",
	"vars": [
		"startedOn"
	]
};
Language.chat.chatEnded = {
	"message": "Ваш чат завершен"
};
Language.chat.chat_icon = {
	"message": "Значок чата"
};
Language.chat.chat_qm = {
	"message": "Начать чат?"
};
Language.chat.chat_text = {
	"message": "Чат"
};
Language.chat.close_icon = {
	"message": "Значок \"Закрыть\""
};
Language.chat.completed_call = {
	"message": "Вызов завершен"
};
Language.chat.decline_call = {
	"message": "Отклонить"
};
Language.chat.defaultName = {
	"message": "Вы (изменить имя)"
};
Language.chat.departmentIsAway = {
	"message": "Отдел #strongStart #departmentName #strongEnd в данный момент недоступен.",
	"vars": [
		"departmentName",
		"strongStart",
		"strongEnd"
	]
};
Language.chat.departmentIsOffline = {
	"message": "Отдел #strongStart #departmentName #strongEnd в данный момент вне сети. Вас может обслужить другой отдел.",
	"vars": [
		"departmentName",
		"strongStart",
		"strongEnd"
	]
};
Language.chat.download = {
	"message": "Загрузить"
};
Language.chat.downloadFile = {
	"message": "Скачать файл"
};
Language.chat.dragDropText = {
	"message": "Перетащите файлы сюда для загрузки"
};
Language.chat.emoji_error_load = {
	"message": "Не удалось загрузить эмодзи"
};
Language.chat.error_title = {
	"message": "Ошибка"
};
Language.chat.failed = {
	"message": "Не удалось"
};
Language.chat.generalUploadError = {
	"message": "\"#fileName\", пожалуйста, попробуйте еще раз.",
	"vars": [
		"fileName"
	]
};
Language.chat.generalUploadErrorLabel = {
	"message": "Не удалось загрузить файл"
};
Language.chat.goToLatest = {
	"message": "Перейти к последнему"
};
Language.chat.hideButton = {
	"message": "Скрыть чат"
};
Language.chat.incoming_call_message = {
	"message": "Входящий вызов от #name",
	"vars": [
		"name"
	]
};
Language.chat.insert_emoji = {
	"message": "Вставить эмодзи"
};
Language.chat.justNow = {
	"message": "Сейчас"
};
Language.chat.limit2 = {
	"message": "Максимальный размер файла составляет 2 МБ для мобильных браузеров, пожалуйста, загрузите файл меньшего размера."
};
Language.chat.limit50 = {
	"message": "Максимальный размер файла составляет 50 МБ, пожалуйста, загрузите файл меньшего размера."
};
Language.chat.message_not_delivered = {
	"message": "Сообщение не доставлено, нажмите для повторной отправки."
};
Language.chat.message_too_long = {
	"message": "Сообщение не может превышать 5000 символов"
};
Language.chat.missed_agent = {
	"message": "Ваш звонок был пропущен"
};
Language.chat.missed_visitor = {
	"message": "Вы пропустили звонок"
};
Language.chat.missed_visitor_messagePreview = {
	"message": "Вы пропустили вызов от"
};
Language.chat.mobileName = {
	"message": "Вы"
};
Language.chat.newChat = {
	"message": "Начать новый чат"
};
Language.chat.newMessages = {
	"message": "Новые сообщения"
};
Language.chat.new_conversation = {
	"message": "Новый чат"
};
Language.chat.notificationTitle = {
	"message": "уведомление"
};
Language.chat.ongoing_call = {
	"message": "Текущий вызов"
};
Language.chat.past = {
	"message": "#time назад",
	"vars": [
		"time"
	]
};
Language.chat.pasted_image_title = {
	"message": "Изображение вставлено в #dateTime",
	"vars": [
		"dateTime"
	]
};
Language.chat.profile_prechat_text = {
	"message": "Заполните приведенную ниже форму, чтобы начать чат."
};
Language.chat.rejected_call = {
	"message": "Вы отклонили вызов"
};
Language.chat.remove_rate = {
	"message": "Вы удалили свою оценку этой беседы"
};
Language.chat.resend = {
	"message": "Отправить повторно"
};
Language.chat.retry = {
	"message": "Повторить."
};
Language.chat.say_something = {
	"message": "Написать ответ..."
};
Language.chat.screen_share_error = {
	"message": "Демонстрация экрана недоступна."
};
Language.chat.send_mail = {
	"message": "Отправить сообщение"
};
Language.chat.sent_file = {
	"message": "Отправил файл"
};
Language.chat.today_time = {
	"message": "Сегодня, #time",
	"vars": [
		"time"
	]
};
Language.chat.tryAgain = {
	"message": "Повторите попытку"
};
Language.chat.unanswered = {
	"message": "Неотвеченные"
};
Language.chat.uploading = {
	"message": "Загрузка..."
};
Language.chat.video_call_error = {
	"message": "Видео-вызов недоступен."
};
Language.chat.visitor_ringing = {
	"message": "Вызов..."
};
Language.chat.voice_call_error = {
	"message": "Голосовой вызов недоступен."
};
Language.chat.we_are_live = {
	"message": "Мы в сети и сейчас готовы приступить к чату с Вами. Скажите что-нибудь, чтобы начать чат."
};


Language.days = Language.days || {};

Language.days['0'] = {
	"message": "Воскресенье"
};
Language.days['1'] = {
	"message": "Понедельник"
};
Language.days['2'] = {
	"message": "Вторник"
};
Language.days['3'] = {
	"message": "Среда"
};
Language.days['4'] = {
	"message": "Четверг"
};
Language.days['5'] = {
	"message": "Пятница"
};
Language.days['6'] = {
	"message": "Суббота"
};


Language.form = Language.form || {};

Language.form.CancelButton = {
	"message": "Отменить"
};
Language.form.CloseButton = {
	"message": "Закрыть"
};
Language.form.DepartmentsErrorMessage = {
	"message": "Отдел обязателен."
};
Language.form.DepartmentsPlaceholder = {
	"message": "выберите отдел.."
};
Language.form.EmailErrorMessage = {
	"message": "Неверный адрес электронной почты"
};
Language.form.EmailPlaceholder = {
	"message": "Электронная почта"
};
Language.form.EmailTranscriptFormMessage = {
	"message": "Пожалуйста, заполните приведенную ниже форму, чтобы этот чат был отправлен на ваш электронный адрес."
};
Language.form.EmailTranscriptSuccess = {
	"message": "Запрашивает отправку протокола чата по эл.почте."
};
Language.form.EmailTranscriptTo = {
	"message": "Отправить переписку на"
};
Language.form.EndChatMessage = {
	"message": "Спасибо за общение с нами. Вы можете начать новый чат или ввести свой электронный адрес и отправить протокол данного чата в свой почтовый ящик."
};
Language.form.EndChatMessage2 = {
	"message": "Спасибо, что написали нам. Вы всегда можете начать новый сеанс чата."
};
Language.form.EndChatTitle = {
	"message": "Вы уверены, что хотите завершить этот чат?"
};
Language.form.MessagePlaceholder = {
	"message": "ваше сообщение.."
};
Language.form.NameErrorMessage = {
	"message": "Имя обязательно."
};
Language.form.NameFormMessage = {
	"message": "Пожалуйста, укажите свое имя, чтобы мы могли узнать Вас в следующий раз."
};
Language.form.OfflineFormMessage = {
	"message": "Пожалуйста, заполните приведенную ниже форму и мы с вами свяжемся в ближайшее время."
};
Language.form.OfflineMessageNotSent = {
	"message": "Ваше сообщение не было доставлено. Пожалуйста, повторите попытку."
};
Language.form.OfflineMessageSent = {
	"message": "Ваше сообщение успешно отправлено!"
};
Language.form.PhoneErrorMessage = {
	"message": "Неправильный номер телефона"
};
Language.form.PreChatFormMessage = {
	"message": "Пожалуйста, заполните приведенную ниже форму, чтобы начать чат со следующим свободным консультантом."
};
Language.form.PreChatFormMessageProfile = {
	"message": "Пожалуйста, заполните приведенную ниже форму, чтобы начать чат со мной."
};
Language.form.QuestionPlaceholder = {
	"message": "ваш запрос.."
};
Language.form.RequiredErrorMessage = {
	"message": "Это поле обязательно для заполнения"
};
Language.form.SaveButton = {
	"message": "Сохранить"
};
Language.form.SendButton = {
	"message": "Отправить"
};
Language.form.SendMessage = {
	"message": "Отправить сообщение"
};
Language.form.StartChatButton = {
	"message": "Начать чат"
};
Language.form.SubmitButton = {
	"message": "Отправить"
};
Language.form.SubmittedFrom = {
	"message": "Отправлено из"
};
Language.form.SubmittingProcess = {
	"message": "Отправляем"
};
Language.form.TranscriptMessage = {
	"message": "Вы можете ввести свой электронный адрес и отправить протокол данного чата в свой почтовый ящик."
};
Language.form.any = {
	"message": "Любой"
};
Language.form.chatEnded = {
	"message": "Ваш чат завершен"
};
Language.form.department = {
	"message": "Отдел"
};
Language.form.email = {
	"message": "Электронная почта"
};
Language.form.errorSaving = {
	"message": "Не удалось сохранить. Пожалуйста, попробуйте еще раз"
};
Language.form.message = {
	"message": "Сообщение"
};
Language.form.name = {
	"message": "Имя"
};
Language.form.sendAgain = {
	"message": "Отправить новое"
};
Language.form.visitButton = {
	"message": "Посетить tawk.to"
};


Language.home = Language.home || {};

Language.home.banner_image = {
	"message": "Изображение баннера"
};
Language.home.chat_button = {
	"message": "Новая беседа"
};
Language.home.chat_input = {
	"message": "Наберите текст здесь и нажмите \"Enter\"..."
};
Language.home.heading_main = {
	"message": "Привет! 👋"
};
Language.home.heading_sub = {
	"message": "Нужна помощь? Найдите ответы в нашем справочном центре или начните разговор:"
};
Language.home.kb_search = {
	"message": "Поиск ответов"
};
Language.home.logo_image = {
	"message": "Изображение логотипа"
};


Language.kb = Language.kb || {};

Language.kb.article_image = {
	"message": "Изображение статьи"
};
Language.kb.article_rating = {
	"message": "Эта статья была вам полезна?"
};
Language.kb.article_rating_count = {
	"message": "#totalLikes из #totalVotes эта статья понравилась",
	"vars": [
		"totalLikes",
		"totalVotes"
	]
};
Language.kb.author_profile_image = {
	"message": "Изображение профиля автора"
};
Language.kb.clear_search = {
	"message": "Очистить поиск"
};
Language.kb.downvote_rating_button = {
	"message": "Нет"
};
Language.kb.help_center = {
	"message": "Справочный центр"
};
Language.kb.negative_rating = {
	"message": "Негативные"
};
Language.kb.positive_rating = {
	"message": "Позитивные"
};
Language.kb.recent_searches = {
	"message": "Недавние поисковые запросы"
};
Language.kb.search_fail_description = {
	"message": "Пожалуйста, повторите попытку."
};
Language.kb.search_fail_title = {
	"message": "Ничего не найдено"
};
Language.kb.search_placeholder = {
	"message": "Поиск ответов"
};
Language.kb.search_results = {
	"message": "Результаты поиска"
};
Language.kb.show_all_results = {
	"message": "Показать все результаты (#num)",
	"vars": [
		"num"
	]
};
Language.kb.submit_search = {
	"message": "Отправить поисковый запрос"
};
Language.kb.upvote_rating_button = {
	"message": "Да"
};
Language.kb.view_full = {
	"message": "Посмотреть полностью"
};


Language.menu = Language.menu || {};

Language.menu.change_name = {
	"message": "Изменить имя"
};
Language.menu.email_transcript = {
	"message": "Отправить протокол"
};
Language.menu.end_chat_session = {
	"message": "Завершить сессию чата"
};
Language.menu.popout_widget = {
	"message": "Открыть виджет в окне"
};
Language.menu.sound_off = {
	"message": "Звук выключен"
};
Language.menu.sound_on = {
	"message": "Звук включен"
};


Language.months = Language.months || {};

Language.months['0'] = {
	"message": "Январь"
};
Language.months['1'] = {
	"message": "Февраль"
};
Language.months['10'] = {
	"message": "Ноябрь"
};
Language.months['11'] = {
	"message": "Декабрь"
};
Language.months['2'] = {
	"message": "Март"
};
Language.months['3'] = {
	"message": "Апрель"
};
Language.months['4'] = {
	"message": "Май"
};
Language.months['5'] = {
	"message": "Июнь"
};
Language.months['6'] = {
	"message": "Июль"
};
Language.months['7'] = {
	"message": "Август"
};
Language.months['8'] = {
	"message": "Сентябрь"
};
Language.months['9'] = {
	"message": "Октябрь"
};


Language.notifications = Language.notifications || {};

Language.notifications.dismiss_alert = {
	"message": "Закрыть оповещение"
};
Language.notifications.maximum_file_upload_warning = {
	"message": "Извините, передача файлов ограничена количеством в #limitFileNumber файлов. Пожалуйста, повторите для файла(-ов):",
	"vars": [
		"limitFileNumber"
	]
};
Language.notifications.maximum_size_upload_warning = {
	"message": "Извините, передача файлов ограничена размером в #limitFileSize за файл. Пожалуйста, создайте сжатый архив из файла(-ов) и повторите попытку.",
	"vars": [
		"limitFileSize"
	]
};
Language.notifications.reconnecting = {
	"message": "Повторное подключение"
};
Language.notifications.retry = {
	"message": "Повторите попытку"
};


Language.overlay = Language.overlay || {};

Language.overlay.cookiesOff = {
	"message": "Вы не можете использовать этот чат, так как в Вашем браузере отключены cookie. Пожалуйста, включите их и перезагрузите браузер."
};
Language.overlay.inactive = {
	"message": "Нажмите здесь, чтобы возобновить чат"
};
Language.overlay.maintenance = {
	"message": "Чат находится на обслуживании"
};
Language.overlay.tawkContent = {
	"message": "Этот виджет поддерживается tawk.to - бесплатным приложением для обмена сообщениями, которое позволяет отслеживать и вступать в общение с посетителями Вашего веб-сайта."
};


Language.rollover = Language.rollover || {};

Language.rollover.back = {
	"message": "Назад"
};
Language.rollover.chatMenu = {
	"message": "Меню"
};
Language.rollover.emailTranscriptOption = {
	"message": "Отправить протокол на электронную почту"
};
Language.rollover.end = {
	"message": "Завершить чат"
};
Language.rollover.knowledgeBase = {
	"message": "База знаний"
};
Language.rollover.maximize = {
	"message": "Развернуть"
};
Language.rollover.minimize = {
	"message": "Свернуть"
};
Language.rollover.negativeRating = {
	"message": "Оценить беседу на -1"
};
Language.rollover.popOut = {
	"message": "Открыть в новом окне"
};
Language.rollover.positiveRating = {
	"message": "Оценить беседу на +1"
};
Language.rollover.rateChat = {
	"message": "Оцените этот чат"
};
Language.rollover.resendMessage = {
	"message": "Переслать сообщение"
};
Language.rollover.resize = {
	"message": "Изменить размер"
};
Language.rollover.screenShare = {
	"message": "Демонстрация экрана"
};
Language.rollover.uploadFile = {
	"message": "Загрузить файл"
};
Language.rollover.videoCall = {
	"message": "Видео-вызов"
};
Language.rollover.voiceCall = {
	"message": "Голосовой вызов"
};


Language.routes = Language.routes || {};

Language.routes.all_agents = {
	"message": "Все операторы"
};
Language.routes.conversations = {
	"message": "Беседы"
};
Language.routes.load_more = {
	"message": "Загрузить ещё"
};


Language.status = Language.status || {};

Language.status.away = {
	"message": "Отсутствует"
};
Language.status.offline = {
	"message": "Оффлайн"
};
Language.status.online = {
	"message": "Онлайн"
};




Language.chat = Language.chat || {};

Language.chat.hours = {
	"pluralVars": [
		"num"
	],
	"message": {
		"one": "#num час",
		"few": "#num часа",
		"many": "#num часов",
		"other": "#num часов"
	}
};
Language.chat.messageQueuedText = {
	"pluralVars": [
		"t"
	],
	"message": {
		"one": "Приблизительное время ожидания составляет #strongStart #t минуту #strongEnd",
		"few": "Приблизительное время ожидания составляет #strongStart #t минуты #strongEnd",
		"many": "Приблизительное время ожидания составляет #strongStart #t минут #strongEnd",
		"other": "Приблизительное время ожидания составляет #strongStart #t минут #strongEnd"
	},
	"vars": [
		"strongStart",
		"strongEnd"
	]
};
Language.chat.minutes = {
	"pluralVars": [
		"num"
	],
	"message": {
		"one": "#num минута",
		"few": "#num минуты",
		"many": "#num минут",
		"other": "#num минут"
	}
};
Language.chat.newMessage = {
	"pluralVars": [
		"num"
	],
	"message": {
		"one": "#num новое сообщение",
		"few": "#num новых сообщения",
		"many": "#num новых сообщений",
		"other": "#num новых сообщений"
	}
};
Language.chat.seconds = {
	"pluralVars": [
		"num"
	],
	"message": {
		"one": "#num секунда",
		"few": "#num секунды",
		"many": "#num секунд",
		"other": "#num секунд"
	}
};


global.$_Tawk.language = Language;})(window);