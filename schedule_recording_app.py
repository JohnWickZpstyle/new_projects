import json
import argparse
import os
from datetime import datetime, date, timedelta

parser = argparse.ArgumentParser()
task_name = parser.add_argument('-n', '--task_name', nargs=1, help='Введите задание: ')
day_and_month_for_task = parser.add_argument('-d', '--day_and_month', nargs=1,
                                             help='Введите дату и месяц черезе точку: ')
args = parser.parse_args()



task_name_convert_to_json = str(f"{args.__dict__['task_name'][0]}.json")

day_and_month_split = args.__dict__['day_and_month'][0].split('.')

if task_name_convert_to_json in os.listdir("../program_recording_task_and_date"):
    print("This name of file are used")
else:
    try:
        convert_to_day_and_month = datetime.strptime(day_and_month_for_task, "%d.%m").strftime("%d.%m")

    except ValueError as value_error:

        if day_and_month_split[0] == "tomorrow":
            scheduled_to_tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")
            with open(task_name_convert_to_json, "w", encoding='utf8') as file:
                file.write(json.dumps({task_name: f"Scheduled to {scheduled_to_tomorrow}"},
                                      sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))

        elif day_and_month_split[0] == "day after tomorrow":
            scheduled_to_day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%d.%m")

            with open(task_name_convert_to_json, "w", encoding='utf8') as file:
                file.write(json.dumps({task_name: f"Scheduled to {scheduled_to_day_after_tomorrow}"},
                                      sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))
    else:
        with open(task_name_convert_to_json, "w", encoding='utf8') as file:
            file.write(json.dumps({task_name: f"Scheduled to {convert_to_day_and_month}"},
                                  sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))