from random import choice

name_length_text = [
    "Имя должно содержать хотя бы два слова.",
    "Пожалуйста, укажите полное имя, состоящее из двух или более слов.",
    "Убедитесь, что вы указали полное имя, состоящее хотя бы из двух слов.",
    "Полное имя должно содержать как минимум два слова.",
    "Введите полное имя, включая как имя, так и фамилию."
]

name_format_text = [
    "Полное имя должно состоять только из букв.",
    "Убедитесь, что имя содержит только буквы.",
    "Пожалуйста, используйте только буквы для указания имени.",
    "Полное имя не должно содержать цифры или символы.",
    "Укажите полное имя без специальных символов или цифр."
]

len_phone_text = [
    "Достаточная длина номера телефона - не менее 12 символов",
    "Убедитесь, что номер телефона состоит из 12 символов или больше",
    "Минимальная длина номера телефона - 12 символов, проверьте",
    "Необходимо ввести номер телефона, состоящий из не менее 12 символов",
    "Укажите номер телефона длиной не менее 12 символов",
    "Уточните номер телефона, должно быть не менее 12 символов",
    "Проверьте длину номера телефона - должно быть не меньше 12 символов",
    "Уведомление: номер телефона должен содержать не менее 12 символов",
    "Необходимо ввести номер телефона, длиной не менее 12 символов",
    "Внимание: допустимая длина номера телефона - 12 символов или больше",
]

format_phone_text = [
    "Укажите номер в формате международного набора цифр, пожалуйста!",
    "Пожалуйста, введите номер телефона в международном формате!",
    "Уточните номер, используя международный формат набора цифр!",
    "Внимательно запишите номер телефона, соблюдая международный формат!",
    "Необходимо указать номер в международном формате набора цифр!",
    "Просим вас предоставить номер телефона в соответствии с международным форматом!",
    "Уведомление: требуется указать номер в международном формате!",
    "Запишите номер телефона в формате международного набора цифр, пожалуйста!",
    "Укажите номер, соблюдая международный формат набора цифр!",
    "Необходимо ввести номер телефона в международно признанном формате!",
]

exception_phone_text = [
    "Пожалуйста, исключите символ '{0}' из телефонного номера!",
    "Убедитесь, что в номере отсутствует символ '{0}'!",
    "Не допускается использование символа '{0}' в телефонном номере!",
    "Проверьте номер на наличие символа '{0}', он не допустим!",
    "Обратите внимание, что символ '{0}' не может быть включен в номер!",
    "Телефонный номер не должен содержать символ '{0}', убедитесь в этом!",
    "Укажите номер без символа '{0}', это недопустимо!",
    "Внимание: символ '{0}' не разрешен в телефонном номере!",
    "Просим вас исключить символ '{0}' из указываемого номера телефона!",
    "Запишите номер без символа '{0}', это требование!",
]


def full_name_validation(full_name: str) -> dict:
    message_or_status = {
        'message': 'Пожалуйста, укажите полное имя.',
        'status': False
    }
    if not full_name or full_name.isspace() or len(full_name) < 2:
        return message_or_status
    
    full_name = full_name.strip()

    if len(full_name.split()) < 2:
        message_or_status['message'] = choice(name_length_text)
        return message_or_status

    if not all(word.isalpha() or word.isspace() for word in full_name):
        message_or_status['message'] = choice(name_format_text)
        return message_or_status

    message_or_status['status'] = True
    return message_or_status



def phone_validation(phone_number: str) -> dict:
    message_or_status = {
        'message': 'Пожалуйста, укажите правильный номер телефона.',
        'status': False
    }
    if not phone_number or phone_number.isspace() or phone_number.isalpha():
        return message_or_status

    phone_number = phone_number.replace(" ", "")
    
    if len(phone_number) != 12 :
        message_or_status['message'] = choice(len_phone_text)
        return message_or_status
    
    if not phone_number.startswith("+"):
        message_or_status["message"] = choice(format_phone_text)
        return message_or_status 
    
    numbers = '+0123456789'
    for i in phone_number:
        if i not in numbers:
            message_or_status["message"] = choice(exception_phone_text).format(i)
            return message_or_status
        
    message_or_status['status'] = True
    return message_or_status