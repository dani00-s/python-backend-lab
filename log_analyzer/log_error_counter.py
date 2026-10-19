import csv
import json
import os
from collections import Counter

LOG_FILE_PATH = "rufus.log"
OUTPUT_JSON_PATH = "error_summary.json"
OUTPUT_CSV_PATH = "error_summary.csv"

TARGET_ERRORS = [
    "404 Not Found",
    "500 Internal Server Error",
    "502 Bad Gateway",
    "TimeoutError",
    "ConnectionResetError",
    "Notice",
    "unknown Master Boot Record",
    "deactivated"
]

def count_errors_in_log(log_path,targets):
    counts = Counter({err: 0 for err in targets})

    if not os.path.exists(log_path):
        print(f"Errore: il file '{log_path} non esiste.")
        return counts
    with open(log_path,mode ='r', encoding="utf-8") as file:
        for line in file:
            for error in targets:
                if error in line:
                    counts[error] += line.count(error)
    return counts


def save_to_json(data,output_path):
    with open(output_path,mode="w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
    print(f"Riepilogo salvato con successo in JSON: {output_path}")

def save_to_csv(data,output_path):
    with open(output_path,mode="w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Errore","Conteggio"])
        for error,count in data.items():
            writer.writerow([error,count])
    print(f"Riepilogo salvato con successo in CSV: {output_path}")


if __name__ =="__main__":
    error_counts = count_errors_in_log(LOG_FILE_PATH,TARGET_ERRORS)

    save_to_json(error_counts,OUTPUT_JSON_PATH)
    save_to_csv(error_counts,OUTPUT_CSV_PATH)
