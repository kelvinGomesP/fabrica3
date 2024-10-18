def format_date(date_string):
    # Função auxiliar para formatar datas
    from datetime import datetime
    return datetime.strptime(date_string, "%Y-%m-%d")
