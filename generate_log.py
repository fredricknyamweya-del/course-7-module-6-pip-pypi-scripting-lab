from datetime import datetime


def generate_log(data):
    """
    Generates a timestamped log file from a list of entries.
    Returns the created filename.
    Raises ValueError if input is not a list.
    """

    if not isinstance(data, list):
        raise ValueError("Input must be a list of strings.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename
