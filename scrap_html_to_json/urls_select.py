"""
Исходные данные:
1. файл - старый список уникальных строк с url, этого файла может не быть.
2. файл - новые не уникальные строки с url.
3. подстрока для фильтра, которая должна входить в новые строки с url.

Последовательность применения функций к файлам:
1. leave_uniq_urls - из новых строк оставим только уникальные.
2. filter_urls - из новых уникальных строк оставим только те, в которые входит подстрока.
3. add_urls_to_uniq - добавим в файл с уникальными отфильтрованными строками новые строки.

Результат: файл с уникальными отфильтрованными строками с url.
"""


def leave_uniq_urls(file_not_uniq_lines='', file_uniq_lines=''):
    """
    Создаст новый файл с уникальными строками из исходного файла.
    :param file_not_uniq_lines: исходный файл с дублирующимися строками.
    :param file_uniq_lines: файл с уникальными строками из исходного файла.
    :return: новый файл с уникальными строками из исходного файла.
    """
    with open(file_not_uniq_lines, 'r') as a, \
            open(file_uniq_lines, 'w') as b:
        uniq_lines = list(set(map(lambda x: x.strip(), a.readlines())))
        uniq_lines.sort()

        for line in uniq_lines:
            if line == uniq_lines[-1]:
                b.write(line)
            else:
                b.write(line + '\n')


def filter_urls(file='', file_new='', filter_str=''):
    """
    Создаст новый файл со строками из исходного файла, которые содержат значение строки filter_str.
    :param file: исходный файл со строками.
    :param file_new: файл-результат со строками, содержащими значение filter_str.
    :param filter_str: строка, которая должна входить в строки исходного файла.
    :return: файл-результат со строками, содержащими значение filter_str.
    """
    with open(file, 'r') as a, \
            open(file_new, 'w') as b:
        lines = list(map(lambda x: x.strip(), a.readlines()))
        filtered_text = []

        for line in lines:
            if filter_str in line:
                filtered_text.append(line)
        filtered_text.sort()

        for i in range(len(filtered_text)):
            if i == len(filtered_text)-1:
                b.write(filtered_text[i])
            else:
                b.write(filtered_text[i] + '\n')


def add_urls_to_uniq(res_uniqlines_file='', newlines_file=''):
    """
    Добавит уникальные строки из newlines_file в файл res_uniqlines_file, если таких строк в нем еще нет.
    Если файл res_uniqlines_file не существует, то создаст его.
    :param newlines_file:
    :param res_uniqlines_file:
    :return: файл res_uniqlines_file, в который добавлены уникальные строки из файла newlines_file.
    """
    with open(res_uniqlines_file, 'a+') as a, \
            open(newlines_file, 'r') as b:
        # a+ Открывает файл для добавления и чтения. Указатель стоит в конце файла.
        # Создает файл с именем имя_файла, если такового не существует.
        a.seek(0)
        existing_lines = a.readlines()
        existing_lines = list(map(lambda x: x.strip(), existing_lines))
        new_lines = set(map(lambda x: x.strip(), b.readlines()))
        empty_file = True if len(existing_lines) == 0 else False

        new_uniq_lines = []
        for i in new_lines:
            if i not in existing_lines and len(i) != 0:
                new_uniq_lines.append(i)
        new_uniq_lines.sort()

        if not empty_file and len(new_uniq_lines) != 0:
            a.write('\n')

        for i in new_uniq_lines:
            if i == new_uniq_lines[-1]:
                a.write(i)
            else:
                a.write(i + '\n')


def get_updated_urls(
                    new_lines_file='urls_all_new.txt',
                    filter_str='',
                    res_uniq_url_file='urls_uniq_final.txt',
                    all_new_uniq_file='urls_all_new_uniq.txt',
                    all_new_filtered_file='urls_all_new_filtered.txt'
                    ):

    print('Начало работы.')

    leave_uniq_urls(file_not_uniq_lines=new_lines_file,
                    file_uniq_lines=all_new_uniq_file)

    filter_urls(file=all_new_uniq_file,
                file_new=all_new_filtered_file,
                filter_str=filter_str)

    add_urls_to_uniq(res_uniqlines_file=res_uniq_url_file,
                     newlines_file=all_new_filtered_file)

    print(f'Работа завершена.\nФайлы:\n{res_uniq_url_file}\n{all_new_uniq_file}\n{all_new_filtered_file}\n')
    return


# обработка urls, результат - файл.
get_updated_urls(new_lines_file='urls_all_new.txt',
                 filter_str='enter_your_filter_substring',
                 res_uniq_url_file='urls_uniq_final.txt',
                 )