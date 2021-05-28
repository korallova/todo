import sys
import datetime
from datetime import date
import todo_functions as f
today = str(date.today())
if len(sys.argv) == 1:
    f.cap()
    with open('todo.txt', 'r') as todo:
        text = todo.readlines()
        for line in text:
            if 'x ' in line:
                text.remove(line)
        f.print_requested(text)
elif len(sys.argv) == 2:
    f.cap()
    if 'all' in sys.argv[1]:
        with open('todo.txt', 'r') as todo:
            text = todo.readlines()
            f.print_requested(text)
    else:
        print("Недостаточно аргументов командной строки")
else:
    try:
        if 'add' in sys.argv[1]:
            f.cap()
            with open('todo.txt', 'a') as todo:
                todo.write(today + " " + " ".join(sys.argv[2:]) + "\n")
            with open('todo.txt', 'r') as todo:
                text = todo.readlines()
                i = len(text)
                f.print_changes(text, i, ' - ДОБАВЛЕНО')
        elif 'remove' in sys.argv[1]:
            i = int(sys.argv[2])
            with open('todo.txt', 'r') as todo:
                text = todo.readlines()
                for index, value in enumerate(text, 1):
                    print(("{}: {}".format(i, text[i - 1])).replace("\n", ""))
                    choice = input(f"Хотите удалить задачу {i}? (y/n): ").lower()
                    if choice == 'n':
                        print("Задача не удалена")
                        f.cap()
                        f.print_requested(text)
                        break
                    if choice == 'y':
                        print("Задача удалена")
                        f.cap()
                        text.remove(text[i - 1])
                        with open('todo.txt', 'w') as todo:
                            for line in text:
                                todo.write(line)
                        f.print_requested(text)
                        break
        elif 'edit' in sys.argv[1]:
            f.cap()
            if len(sys.argv) == 3:
                print("Отсутствует новое описание задачи!")
            else:
                i = int(sys.argv[2])
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    if 'due:' in text[i - 1]:
                        a = text[i - 1].index('due:')
                        edit = text[i - 1].replace(text[i - 1][11:a - 1], ' '.join(sys.argv[3:]))
                        text.insert(i - 1, edit)
                        text.remove(text[i])
                        with open('todo.txt', 'w') as todo:
                            for line in text:
                                todo.write(line)
                        f.print_changes(text, i, ' - ИЗМЕНЕНО')
                    else:
                        edit = text[i - 1].replace(text[i - 1][11:], ' '.join(sys.argv[3:]))
                        text.insert(i - 1, edit)
                        text.remove(text[i])
                        with open('todo.txt', 'w') as todo:
                            for line in text:
                                todo.write(line)
                        f.print_changes(text, i, ' - ИЗМЕНЕНО')
        elif 'due' in sys.argv[1]:
            answer = []
            if 'between' in sys.argv[2]:
                start = sys.argv[3].split('-')
                end = sys.argv[4].split('-')
                start_date = datetime.date(int(start[0]), int(start[1]), int(start[2]))
                end_date = datetime.date(int(end[0]), int(end[1]), int(end[2]))
                f.cap('<due between ' + sys.argv[3] + ' - ' + sys.argv[4] + '>')
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    for line in text:
                        if 'x ' not in line:
                            if 'due:' in line:
                                b = line.index('due:')
                                due = line[b + 4:].split('-')
                                due_date = datetime.date(int(due[0]), int(due[1]), int(due[2]))
                                if start_date <= due_date <= end_date:
                                    answer.append(line)
                    f.print_requested(answer)
            elif 'before' in sys.argv[2]:
                before = sys.argv[3].split('-')
                before_date = datetime.date(int(before[0]), int(before[1]), int(before[2]))
                f.cap('<due before ' + sys.argv[3] + '>')
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    for line in text:
                        if 'x ' not in line:
                            if 'due:' in line:
                                b = line.index('due:')
                                due = line[b + 4:].split('-')
                                due_date = datetime.date(int(due[0]), int(due[1]), int(due[2]))
                                if due_date <= before_date:
                                    answer.append(line)
                    f.print_requested(answer)
            elif 'after' in sys.argv[2]:
                after = sys.argv[3].split('-')
                after_date = datetime.date(int(after[0]), int(after[1]), int(after[2]))
                f.cap('<due after ' + sys.argv[3] + '>')
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    for line in text:
                        if 'x ' not in line:
                            if 'due:' in line:
                                b = line.index('due:')
                                due = line[b + 4:].split('-')
                                due_date = datetime.date(int(due[0]), int(due[1]), int(due[2]))
                                if after_date <= due_date:
                                    answer.append(line)
                    f.print_requested(answer)
            else:
                f.cap()
                i = int(sys.argv[2])
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    if 'due:' in text[i - 1]:
                        a = text[i - 1].index('due:')
                        due = text[i - 1].replace(text[i - 1][a + 4:], ''.join(sys.argv[3:]) + '\n')
                        text.insert(i - 1, due)
                        text.remove(text[i])
                        with open('todo.txt', 'w') as todo:
                            for line in text:
                                todo.write(line)
                        f.print_changes(text, i, ' - ИЗМЕНЕН СРОК')
                    else:
                        due = text[i - 1].replace('\n', '') + ' due:' + ''.join(sys.argv[3:]) + '\n'
                        text.insert(i - 1, due)
                        text.remove(text[i])
                        with open('todo.txt', 'w') as todo:
                            for line in text:
                                todo.write(line)
                        f.print_changes(text, i, ' - ИЗМЕНЕН СРОК')
        elif 'done' in sys.argv[1]:
            if len(sys.argv) > 2:
                f.cap()
                i = int(sys.argv[2])
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    done = 'x ' + text[i - 1]
                    text.remove(text[i - 1])
                    text.append(done)
                    with open('todo.txt', 'w') as todo:
                        for line in text:
                            todo.write(line)
                    n = len(text)
                    f.print_changes(text, n, ' - ЗАВЕРШЕНО')
        elif 'undo' in sys.argv[1]:
            f.cap()
            i = int(sys.argv[2])
            with open('todo.txt', 'r') as todo:
                text = todo.readlines()
                undo = text[i - 1].replace('x ', '')
                text.insert(i - 1, undo)
                text.remove(text[i])
                with open('todo.txt', 'w') as todo:
                    for line in text:
                        todo.write(line)
                f.print_changes(text, i, ' - ВОССТАНОВЛЕНО')
        elif 'search' in sys.argv[1]:
            answer = []
            f.cap('<' + sys.argv[2] + '>')
            with open('todo.txt', 'r') as todo:
                text = todo.readlines()
                for line in text:
                    if sys.argv[2] in line:
                        answer.append(line)
            f.print_requested(answer)
        elif 'created' in sys.argv[1]:
            answer = []
            if 'between' in sys.argv[2]:
                start = sys.argv[3].split('-')
                end = sys.argv[4].split('-')
                start_date = datetime.date(int(start[0]), int(start[1]), int(start[2]))
                end_date = datetime.date(int(end[0]), int(end[1]), int(end[2]))
                f.cap('<created between' + sys.argv[3] + ' - ' + sys.argv[4] + '>')
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    for line in text:
                        if 'x ' not in line:
                            created = line[:10].split('-')
                            created_date = datetime.date(int(created[0]), int(created[1]), int(created[2]))
                            if start_date <= created_date <= end_date:
                                answer.append(line)
                    f.print_requested(answer)
            elif 'before' in sys.argv[2]:
                before = sys.argv[3].split('-')
                before_date = datetime.date(int(before[0]), int(before[1]), int(before[2]))
                f.cap('<created before ' + sys.argv[3] + '>')
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    for line in text:
                        if 'x ' not in line:
                            created = line[:10].split('-')
                            created_date = datetime.date(int(created[0]), int(created[1]), int(created[2]))
                            if created_date <= before_date:
                                answer.append(line)
                    f.print_requested(answer)
            elif 'after' in sys.argv[2]:
                after = sys.argv[3].split('-')
                after_date = datetime.date(int(after[0]), int(after[1]), int(after[2]))
                f.cap('<created after ' + sys.argv[3] + '>')
                with open('todo.txt', 'r') as todo:
                    text = todo.readlines()
                    for line in text:
                        if 'x ' not in line:
                            created = line[:10].split('-')
                            created_date = datetime.date(int(created[0]), int(created[1]), int(created[2]))
                            if after_date <= created_date:
                                answer.append(line)
                    f.print_requested(answer)
    except:
        print("Ошибка при вводе! Проверьте список задач, ввод аргументов и повторите попытку!")
