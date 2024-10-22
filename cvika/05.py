def is_numeric(n:str)->bool:
    try:
        float(n)
        return True
    except ValueError:
        return False