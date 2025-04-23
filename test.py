from Treinamento.PreProcessamento.eliminadorRuido import tornar_texto_legivel_humano

texto = """De: admportonacional.to@portoconstrucao.com.br
    Para: ti@fscompany.com.br; atendimento@fabsolucoes.com.br; 
    Tarefa: [40848-Demissão de Colaborador - Indenizado/Término de Contrato|https://app.gclick.com.br/lfemail.do?em=1201&ev=40848&c=3&t=S]




    Olá







    Solicito a exclusão do seguinte usuário no sistema Point Service.




    Nome: Antonio Cabral PESSOA




    Peço que também seja excluido acesso em demais sistemas da empresa.







    Atenciosamente,
    |!https://s3.amazonaws.com/innubem-prod/gclick/empresa/1201/foto.jpg!| |h4. Ingred Alves da Mata Rocha
    \\| |




    *5 anexos*
    |
    | |!https://app.gclick.com.br/img/files/pdf.png!| |[FORMULÁRIO DE RESCISÃO - ANTONIO CABRAL PESSOA.pdf|https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143959%2FFORMUL%C3%81RIO%20DE%20RESCIS%C3%83O%20-%20ANTONIO%20CABRAL%20PESSOA.pdf&aid=143959]| |
    | |!https://app.gclick.com.br/img/files/arrowdown.png! <[https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143959%2FFORMUL%C3%81RIO%20DE%20RESCIS%C3%83O%20-%20ANTONIO%20CABRAL%20PESSOA.pdf&aid=143959]>| |
    | |!https://app.gclick.com.br/download.do?pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143957%2FAUTORIZA%C3%87%C3%83O.jpeg!| |[AUTORIZAÇÃO.jpeg|https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143957%2FAUTORIZA%C3%87%C3%83O.jpeg&aid=143957]| |
    | |!https://app.gclick.com.br/img/files/arrowdown.png! <[https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143957%2FAUTORIZA%C3%87%C3%83O.jpeg&aid=143957]>| |
    | |!https://app.gclick.com.br/img/files/pdf.png!| |[TERMO DE RECEBIMENTO DE CRACHÁ.pdf|https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143958%2FTERMO%20DE%20RECEBIMENTO%20DE%20CRACH%C3%81.pdf&aid=143958]| |
    | |!https://app.gclick.com.br/img/files/arrowdown.png! <[https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143958%2FTERMO%20DE%20RECEBIMENTO%20DE%20CRACH%C3%81.pdf&aid=143958]>| |
    | |!https://app.gclick.com.br/img/files/pdf.png!| |[FORMULÁRIO DE RESCISÃO - ANTONIO CABRAL PESSOA.pdf|https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143960%2FFORMUL%C3%81RIO%20DE%20RESCIS%C3%83O%20-%20ANTONIO%20CABRAL%20PESSOA.pdf&aid=143960]| |
    | |!https://app.gclick.com.br/img/files/arrowdown.png! <[https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=etapa143960%2FFORMUL%C3%81RIO%20DE%20RESCIS%C3%83O%20-%20ANTONIO%20CABRAL%20PESSOA.pdf&aid=143960]>| | 
    | |!https://app.gclick.com.br/img/files/pdf.png!| |[FORMULARIO DE RESCISAO - ANTONIO CABRAL PESSOA.pdf|https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=andam%2FFORMULARIO%20DE%20RESCISAO%20-%20ANTONIO%20CABRAL%20PESSOA.pdf]| |
    | |!https://app.gclick.com.br/img/files/arrowdown.png! <[https://app.gclick.com.br/open.do?email=atendimento%40fabsolucoes.com.br&cid=3&andamid=374504&ctipo=S&eveId=40848&cliente=19&innubem=false&empId=1201&arqNomeEmail=email2025-03-11-15-18-19.html&pasta=empresa/1201/csolic/3/40848/&arquivo=andam%2FFORMULARIO%20DE%20RESCISAO%20-%20ANTONIO%20CABRAL%20PESSOA.pdf]>| | 
    {color:white}#gccode#3:40848:374504:S:1201#{color}!https://284356hw.r.us-east-1.awstrack.me/I0/01000195866dd4dc-322ef4d8-b3c5-430f-a824-6c4aa82cd90a-000000/j3OJzCcXFPAtGBEl3c3UEtFvBWo=417!"""
print(tornar_texto_legivel_humano(texto))