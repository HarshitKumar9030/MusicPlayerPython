def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{int(mins):02}:{int(secs):02}"
