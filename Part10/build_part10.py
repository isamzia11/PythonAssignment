# Name Isam Zia Roll no: TRN-2026-00346 


from pathlib import Path


def create_sample_log(path):
    with open(path, "w", encoding="utf-8") as file:
        for number in range(1, 51):
            if number % 10 == 0:
                file.write(f"Line {number}: ERROR detected\n")
            else:
                file.write(f"Line {number}: INFO normal\n")


def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


log_path = Path("logs.txt")

create_sample_log(log_path)

error_count = 0

for error_line in only_errors(read_lines(log_path)):
    print(error_line.strip())
    error_count += 1

print("Total ERROR lines:", error_count)
