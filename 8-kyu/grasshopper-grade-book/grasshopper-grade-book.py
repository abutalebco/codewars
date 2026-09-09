def get_grade(s1, s2, s3):
    # Code here
    s = (s1 + s2 + s3) / 3
    if s >= 90 and s <= 100:
        return "A"
    elif s >= 80 and s < 90:
        return "B"
    elif s >= 70 and s < 80:
        return "C"
    elif s >= 60 and s < 70:
        return "D"
    elif s >= 0 and s < 60:
        return "F"
    