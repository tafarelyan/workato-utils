from datetime import datetime, timedelta

# Função para calcular a data da Páscoa (algoritmo de Meeus/Jones/Butcher)
def calcular_pascoa(ano):
    a = ano % 19
    b = ano // 100
    c = ano % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31
    dia = ((h + l - 7 * m + 114) % 31) + 1
    return datetime(ano, mes, dia)

# Função para calcular outros feriados móveis
def calcular_feriados_moveis(ano):
    pascoa = calcular_pascoa(ano)
    carnaval = pascoa - timedelta(days=47)
    corpus_christi = pascoa + timedelta(days=60)
    sexta_santa = pascoa - timedelta(days=2)
    return [carnaval, sexta_santa, pascoa, corpus_christi]

# Lista de feriados fixos do Brasil
def listar_feriados_fixos(ano):
    feriados_fixos = [
        '01/01',  # Confraternização Universal
        '21/04',  # Tiradentes
        '01/05',  # Dia do Trabalhador
        '07/09',  # Independência do Brasil
        '12/10',  # Nossa Senhora Aparecida
        '02/11',  # Finados
        '15/11',  # Proclamação da República
        '25/12',  # Natal
    ]
    # Convertendo feriados fixos para objetos datetime
    feriados = [datetime(ano, int(data.split('/')[1]), int(data.split('/')[0])) for data in feriados_fixos]
    return feriados

# Função para verificar se é dia útil
def eh_dia_util(data, feriados):
    # Verifica se é fim de semana
    if data.weekday() == 5:  # 5 = sábado, 6 = domingo
        return False, 'Sábado'
    if data.weekday() == 6:
        return False, 'Domingo'
    # Verifica se é feriado
    if data in feriados:
        return False, 'Feriado'
    return True, 'Dia útil'

# Função para calcular o número do dia útil até a data atual
def calcular_dia_util(ano, mes, dia, feriados):
    primeiro_dia = datetime(ano, mes, 1)
    dia_util_contador = 0
    dia_atual = primeiro_dia

    while dia_atual <= datetime(ano, mes, dia):
        eh_util, _ = eh_dia_util(dia_atual, feriados)
        if eh_util:
            dia_util_contador += 1
        dia_atual += timedelta(days=1)

    return dia_util_contador

# Função principal para mostrar qual é o dia útil de hoje
def main(input):
    # hoje = datetime.now()
    hoje = datetime(input['ano'], input['mes'], input['dia'])
    ano_atual = hoje.year
    mes_atual = hoje.month
    dia_atual = hoje.day

    # Obter lista de feriados
    feriados_fixos = listar_feriados_fixos(ano_atual)
    feriados_moveis = calcular_feriados_moveis(ano_atual)
    feriados_brasil = feriados_fixos + feriados_moveis

    # Calcular o número do dia útil até a data de hoje
    dia_util = calcular_dia_util(ano_atual, mes_atual, dia_atual, feriados_brasil)

    eh_util, observacao = eh_dia_util(hoje, feriados_brasil)

    if eh_util:
        return {
            'posicao_atual': dia_util,
        }
    else:
        return {
            'posicao_atual': observacao,
        }


if __name__ == '__main__':
    resultados = []
    for ano, mes in [(2024, 11), (2024, 12)] + [(2025, mes) for mes in range(1, 13)]:
        if mes == 12:
            ultimo_dia = (datetime(ano + 1, 1, 1) - timedelta(days=1)).day
        else:
            ultimo_dia = (datetime(ano, mes + 1, 1) - timedelta(days=1)).day

        for dia in range(15, min(25, ultimo_dia) + 1):
            entrada = {'ano': ano, 'mes': mes, 'dia': dia}
            resultado = main(entrada)
            resultados.append({
                'entrada': entrada,
                'resultado': resultado
            })
        resultados.append('------------------------------------------------------')

    # Exibir resultados
    for res in resultados:
        print(res)
