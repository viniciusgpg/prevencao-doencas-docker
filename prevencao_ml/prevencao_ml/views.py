from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, '../templates/index.html')


def getPredictions(peso, altura, imc, sistolica, diastolica, usa_medicamentos,
       cirurgia, diabetes, depressao, dor_cronica, hipertensao,
       cancer, outra_doenca, freq_medico, freq_exame, fuma,
       parou_fumar, bebe, qtd_bebida, usa_droga, atv_fisica,
       hora_atv_fisica, alimentacao_saudavel, ansiedade, estresse):
    import pickle
    model = pickle.load((open("prevencao.sav", "rb")))
    prediction = model.predict([[peso, altura, imc, sistolica, diastolica, usa_medicamentos,
       cirurgia, diabetes, depressao, dor_cronica, hipertensao,
       cancer, outra_doenca, freq_medico, freq_exame, fuma,
       parou_fumar, bebe, qtd_bebida, usa_droga, atv_fisica,
       hora_atv_fisica, alimentacao_saudavel, ansiedade, estresse]])
    
    mensagem = ""
    c_doenca = 1 if diabetes or depressao or dor_cronica or hipertensao or cancer or outra_doenca else 0

    if imc >= 30 and not atv_fisica:
        mensagem += 'Você possui um IMC superior a 30 e não faz atividade fisica. Uma boa prática seria começar a se \
            exercitar durante a semana. Entre em contato com nossos instrutores para iniciar seu treino.\n'
        
    if fuma:
        mensagem += 'Fumar apenas prejudica sua saúde. Você poderia procurar ajuda para largar esse hábito! Entre em contato \
            com nossos profissionais.\n'

    if depressao:
        mensagem += 'Depressão é uma doença que atinge cerca de 6% da população brasileira. Entre em contato com nossos \
            profissionais e agende uma consulta.\n'

    if qtd_bebida > 2:
        mensagem += 'É preciso ter cuidado com o abuso do álcool. O alcoolismo é uma doença que atinge cerca de \
            10% da população brasileira. Entre em contato com nossos profissionais e receba dicas de como maneirar \
                no bebida.\n' 

    if estresse > 5 or ansiedade > 5 and not atv_fisica:
        mensagem += 'Realizar atividade fisica diminui a ansiedade e o estresse. Pratique exercicios! Veja o nosso \
            catalogo de profissionais especializados para montar o treino ideal para você.\n'

    if not c_doenca and imc < 30 and not fuma and ansiedade < 6 and estresse < 6 and qtd_bebida < 2 and not usa_droga and atv_fisica:
        mensagem = 'Você possui um perfil saúdavel. Para continuar assim e se manter motivado, faço acompanhamento com nossos \
            profissionais!\n'

    if prediction == 1:
        return ["Resultado: Grupo A", mensagem]
    elif prediction == 2:
        return ["Resultado: Grupo B", mensagem]
    elif prediction == 3:
        return ["Resultado: Grupo C", mensagem]
    elif prediction == 4:
        return ["Resultado: Grupo D", mensagem]
    else:
        return "error"
        

def result(request):
    peso = float(request.GET['peso'])
    altura = int(request.GET['altura'])
    sistolica = int(request.GET['sistolica'])
    diastolica = int(request.GET['diastolica'])
    usa_medicamentos = int(request.GET['usa_medicamentos'])
    cirurgia = int(request.GET['cirurgia'])
    diabetes = int(request.GET['diabetes'])
    depressao = int(request.GET['depressao'])
    dor_cronica = int(request.GET['dor_cronica'])
    hipertensao = int(request.GET['hipertensao'])
    cancer = int(request.GET['cancer'])
    outra_doenca = int(request.GET['outra_doenca'])
    freq_medico = int(request.GET['freq_medico'])
    freq_exame = int(request.GET['freq_exame'])
    fuma = int(request.GET['fuma'])
    parou_fumar = int(request.GET['parou_fumar'])
    bebe = int(request.GET['bebe'])
    qtd_bebida = int(request.GET['qtd_bebida'])
    usa_droga = int(request.GET['usa_droga'])
    atv_fisica = int(request.GET['atv_fisica'])
    hora_atv_fisica = int(request.GET['hora_atv_fisica'])
    alimentacao_saudavel = int(request.GET['alimentacao_saudavel'])
    ansiedade = int(request.GET['ansiedade'])
    estresse = int(request.GET['estresse'])

    altura = altura/100 if altura > 100 else altura
    peso = peso / 10 if peso > 200 else peso
    imc = peso / (altura * altura)

    estresse = 10 if estresse > 10 else estresse
    ansiedade = 10 if ansiedade > 10 else ansiedade

    result = getPredictions(peso, altura, imc, sistolica, diastolica, usa_medicamentos,
                            cirurgia, diabetes, depressao, dor_cronica, hipertensao,
                            cancer, outra_doenca, freq_medico, freq_exame,
                            fuma, parou_fumar, bebe, qtd_bebida, usa_droga, atv_fisica,
                            hora_atv_fisica, alimentacao_saudavel, ansiedade, estresse)

    return render(request, 'result.html', {'result':result[0], 'message':result[1]})
