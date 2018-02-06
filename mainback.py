# Recebe as strings, calcula o valor das letras, relaciona os números e imprime na tela a relação entre o nome e a
# personalidade descrita na numerologia.

print('{:=^100}'.format('   NUMEROLOGIC   '))

print('Numerologic 1.0 (Fev 05 2018, 21:12')

print('Digite "help", "credits" ou "license" para mais informações. Digite "exit" para sair.')

ripetilo = 0


def numerologic():

    a = int(nomo.count('a') * 1)
    b = int(nomo.count('b') * 2)
    c = int(nomo.count('c') * 3)
    d = int(nomo.count('d') * 4)
    e = int(nomo.count('e') * 5)
    f = int(nomo.count('f') * 6)
    g = int(nomo.count('g') * 7)
    h = int(nomo.count('h') * 8)
    i = int(nomo.count('i') * 9)
    j = int(nomo.count('j') * 1)
    k = int(nomo.count('k') * 2)
    l1 = int(nomo.count('l') * 3)
    m = int(nomo.count('m') * 4)
    n = int(nomo.count('n') * 5)
    o = int(nomo.count('o') * 6)
    p = int(nomo.count('p') * 7)
    q = int(nomo.count('q') * 8)
    r = int(nomo.count('r') * 9)
    s = int(nomo.count('s') * 1)
    t = int(nomo.count('t') * 2)
    u = int(nomo.count('u') * 3)
    v = int(nomo.count('v') * 4)
    w = int(nomo.count('w') * 5)
    x = int(nomo.count('x') * 6)
    y = int(nomo.count('y') * 7)
    z = int(nomo.count('z') * 8)

    totalo = int(a + b + c + d + e + f + g + h + i + j + k + l1 + m + n + o + p + q + r + s + t + u + v + w + x + y + z)

    if totalo == 11 or totalo == 22 or totalo < 10:
        redukto = int(totalo)
    else:
        while totalo > 9:
            unueco = totalo // 1 % 10
            deko = totalo // 10 % 10
            cento = totalo // 100 % 10
            totalo = unueco + deko + cento
            redukto = totalo

    return redukto


def rezolucio():

    if numerologic() == 1:
        nomo1()
    else:
        if numerologic() == 2:
            nomo2()
        else:
            if numerologic() == 3:
                nomo3()
            else:
                if numerologic() == 4:
                    nomo4()
                else:
                    if numerologic() == 5:
                        nomo5()
                    else:
                        if numerologic() == 6:
                            nomo6()
                        else:
                            if numerologic() == 7:
                                nomo7()
                            else:
                                if numerologic() == 8:
                                    nomo8()
                                else:
                                    if numerologic() == 9:
                                        nomo9()
                                    else:
                                        if numerologic() == 11:
                                            nomo11()
                                        else:
                                            nomo22()


def nomo1():

    print('\n{:^100}'.format('Número 1 – Guia os outros e os representa'.upper()))
    print(
        '''\nPara a Numerologia, o número 1 é o número que significa início, recomeços, novos ciclos, é um número'''
        '''\núnico e absoluto. Ele está ligado diretamente à energia da criatividade, originalidade e poder.'''
        '''\nDe energia masculina, o 1 tem ímpeto, força e assertividade típicas dos homens. Tem como'''
        '''\ncaracterísticas marcantes a liderança, a ambição, a coragem, autoconfiança e a independência.'''
        '''\nRepresenta a unidade de Deus, a Trindade, o Pai, o poder supremo.'''
        '''\n '''
    )
    print('{:^100}'.format('LADO POSITIVO:'))
    print('\nSão líderes por natureza, ambiociosos e resilientes. Destacam-se pela sua resiliência.\n')
    print('{:^100}'.format('LADO NEGATIVO:'))
    print('\nFacilmente caem no autoritarismo. Podem mostrar-se egoístas e cínicos.\n')
    print('{:^100}'.format('PALAVRAS-CHAVE PARA AUTOCONHECIMENTO:'))
    print('\nInício, Individualidade, Conquista, Coragem, Iniciativa.\n')
    print('{:^100}'.format('DICAS PARA SER FELIZ:'))
    print('\nNão se deixe levar pelo egoísmo. Estimule a partilha. Verá o poder da dávida.\n')
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nSão pessoas muito positivas, estão sempre pensando pelo lado bom. São ousados, criativos, autoconfiantes'''
        '''\ne pioneiros em tudo que fazem. Não desistem nunca, são muito obstinados e corajosos. Ambiciosos, buscam'''
        '''\na sua independência financeira e emocional sempre. São líderes natos, prezam pela sua individualidade e'''
        '''\ngostam de comandar.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nO seu excesso de autoconfiança e seu gosto por comandar podem gerar características de prepotência,'''
        '''\negocentrismo e autoritarismo. Têm aversão ao fracasso, e quando isso acontece pode se tornar até'''
        '''\nagressivo, ou se render à solidão. É muito orgulho e um tanto inflexível quanto aos seus pontos de'''
        '''\nvista. Apesar de ser muito ativo, tem também um forte lado preguiçoso.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 1 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nGostam de comandar no relacionamento, geralmente tomam a frente das decisões. São muito dedicados no'''
        '''\namor e nos relacionamentos, o romance é muito importante para eles. Mas como tendem a ser egoístas, têm'''
        '''\nde aprender a controlar para deixar que o parceiro também se manifeste neste relacionamento. Estão'''
        '''\nsempre dispostos a experimentar coisas novas, viver aventuras, muita emoção e diversão. Os parceiros'''
        '''\nprecisam ser bastante pacientes pois eles se aborrecem facilmente, ficam emburrados, mas depois passa e'''
        '''\no bom humor volta.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 1:'))
    print(
        '''\nSeu espírito de liderança pode ser estimulado e domado em esportes e jogos com os amigos, não apenas no'''
        '''\ntrabalho. Saber gerir esse espírito aliado à diversão e descontração vai fazer com que você consiga'''
        '''\ncontrolá-lo com maior facilidade. É importante também valorizar cada vitória, já que o fracasso o'''
        '''\natormenta. No amor, não tente impor suas ideias, tente sempre argumentar e ouvir o seu parceiro, a'''
        '''\nopinião dele deve ser sempre tão importante quando a sua. Evite o autoritarismo e o egoísmo.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATÍVEL COM:'))
    print('\nAltamente compatível com 2 e 6.')
    print('Incompatível com 8 e 1.')
    print('Pode ser feliz e desenvolver bons laços com 5 e 7.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-1/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo2():

    print('\n{:^100}'.format('Número 2 – Colabora e facilita'.upper()))
    print(
        '''\nO número 2 representa a dualidade, os pólos positivos e negativos que entram em equilíbrio e buscam a'''
        '''\nharmonia. A energia deste número é essencialmente positiva, passiva e de complementação. Representa a'''
        '''\nmãe, que gera, nutre e acolhe. É o número da sensibilidade, intuição, da ponderação e do conhecimento.'''
        '''\nAtravés do seu poder conciliador e pacificador, consegue equilibrar forças opostos. Representa a busca'''
        '''\ndo equilíbrio espiritual do homem.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nSão pessoas extremamente pacientes, atenciosas e solidárias. Trata a tudo e a todos com a diplomacia,'''
        '''\namabilidade e espírito de colaboração que lhe são característicos. São pessoas muito receptivas,'''
        '''\nmodestas companheiras.'''
        '''\n'''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nA dualidade característica deste número traz muita indecisão e insegurança aos nativos do número 2 na'''
        '''\nnumerologia. A submissão, timidez e passividade também são características frequentes.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 2 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nSão excelentes parceiros amorosos. São compreensivos, carinhosos e adora encher o seu parceiro de'''
        '''\ncarinhos e mimos. É um tanto recatado quando o assunto é sexo devido à sua timidez, tem medo de se'''
        '''\naventurar no amor. Tem dificuldade em se relacionar com as pessoas de início, mas depois se solta e se'''
        '''\ntorna muito sociável e amável.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 2:'))
    print(
        '''\nÉ preciso não ter medo de expressar seus sentimentos nem esconder suas emoções. Evite a dependência'''
        '''\nemocional das outras pessoas, busque a sua completude sozinho para que os outros sejam seus companheiros'''
        '''\ne não a sua essência. Desenvolva seu espírito cooperativo e sociável.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATÍVEL COM:'))
    print('\nAltamente compatível com o 2, 4, 6, 3 e 5.')
    print('Incompatível com 7, 1, 8 e 9.')
    print(
        '''\nFonte: wemystic.com.br/significado-do-numero-2/'''
        '''\n       linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo3():

    print('\n{:^100}'.format('Número 3 – Diverte e alegra'.upper()))
    print(
        '''\nO número 3 é o algarismo que representa a comunicação. Ele estimula a expansão da criatividade, a'''
        '''\nsociabilidade entre as pessoas e o movimento. Está relacionado com o mundo exterior e com a expressão do'''
        '''\nhomem dentro da sociedade, por isso é tão ligado à comunicação e à interação social. Dentro do'''
        '''\nsignificado religioso, significa o Espírito Santo e a sabedoria da alma humana.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nQuem tem a influência do número 3 tem muito otimismo e bom gosto. São os reis da comunicação,'''
        '''\ncomunicam-se muito bem e com qualquer pessoa. São pessoas muito sociáveis e cordiais com todos ao seu'''
        '''\nredor. São talentosos pois têm muita criatividade e entusiasmo pelas artes e cultura. '''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nO número 3 também provoca nas pessoas o exibicionismo, a vontade de aparecer, a supercialidade e a'''
        '''\nostentação. Como gosta muito de se comunicar, pode acabar falando demais e ganhar um espírito'''
        '''\nfofoqueiro, daqueles que até aumenta a fofoca com uma mentirinha. Certa imaturidade e dispersão também'''
        '''\nsã comuns.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 3 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nOs nativos do número 3 no amor são divertidos e estão sempre dispostos a agradar o seu parceiro,'''
        '''\nencarando novidades com entusiasmo. Eles, no entanto, gostam de ter o seu espaço privado para ficar'''
        '''\nsozinho de vez em quando e ter contato com amigos e familiares para se sentir completo. Quando alguém é'''
        '''\nmuito ciumento ou tenta o prender, eles ficam infelizes, inquietos e acabam pulando fora. Em um'''
        '''\nrelacionamento equilibrado eles são românticos, sedutores, alegres, sociáveis e transmitem muita'''
        '''\nconfiança para o seu parceiro. '''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 3:'))
    print(
        '''\nTodos sabem que você é talentoso, não é preciso ficar exibindo a suas habilidades o tempo todo pois isso'''
        '''\npode irritar. Cuidado também com as suas críticas, muitas vezes isso pode inibir as pessoas ao seu'''
        '''\nredor, que passam a ter sempre medo das suas opiniões. Não reprima a sua criatividade e o seu jeito de'''
        '''\nser, apenas pense duas vezes antes de falar algo para alguém que você não gostaria de ouvir. '''
        '''\n '''
    )
    print('{:^100}'.format('COMPATÍVEL COM:'))
    print('\nAltamente compatível com o 3, 1, 5 e 9.')
    print('Incompatível com 2, 4, 6, 7 e 8.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-3/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo4():

    print('\n{:^100}'.format('Número 4 – Responsabiliza e cumpre metas'.upper()))
    print(
        '''\nO número 4 representa segurança e estabilidade pois é a base da pirâmide, firme e estável. É um símbolo'''
        '''\nde racionalidade, ordem, organização e de tudo que é concreto. A estabilidade e segurança deste número'''
        '''\ntraz também fidelidade e conservadorismo ao seus nativos. A confiança que uma pessoa do número 4'''
        '''\nrepresenta é inabalável. É um número perfeito, que representa a concretização de objetivos, incentiva o'''
        '''\nsenso prático e a disciplina, dá força de vontade e força o poder próprio.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nSão pessoas muito leais, organizadas, disciplinas e estáveis. Resolvem tudo com base na calma, trabalho'''
        '''\ne cautela. São tradicionais, e dedicam sua vida aos outros com muito amor, confiança e honestidade. Sua'''
        '''\nfranqueza é símbolo da sua verdade. São trabalhadores dedicados.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nSão excessivamente rígidos consigo mesmo e com as pessoas ao seu redor, tendendo a ser demasiado crítico'''
        '''\ncom os outros e magoar as pessoas. Ao mesmo tempo, são inseguros e precisam da opinião alheia sobre tudo'''
        '''\no que vai fazer. Entretanto, é ao mesmo tempo cabeça dura, e tem dificuldade em ser flexível. Apega-se'''
        '''\nmuito fácil ao passado, não deixa o passado ir embora. É um bocado avarento e conformista.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 4 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nSão extremamente perfeccionistas no amor, querem ser os parceiros perfeitos, e para isso gostam de'''
        '''\nseguir fórmulas tradicionais e não inovar muito. São muito constantes, estáveis e confiáveis quando'''
        '''\nestão em um relacionamento, mas também não suportam viver em uma relação estagnada. Se tiver algum'''
        '''\nproblema atrapalhando a harmonia do casal, eles querem conversar logo e resolver.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 4:'))
    print(
        '''\nNão se deixe oprimir pelas suas responsabilidades, principalmente em relação ao seu trabalho. Tenha'''
        '''\ncuidado para não viver pelas suas responsabilidades e obrigações ao invés de guiá-las através da sua'''
        '''\nnecessidade. Diante de conflito com outras pessoas, converse, não discuta. Não perca a cabeça, nem todo'''
        '''\nmundo tem uma mente tão tradicional e conservadora quanto você, e tudo bem se as pessoas pensam'''
        '''\ndiferente, isso é saudável, não tente convencê-las do contrário. Evite prometer coisas que você não tem'''
        '''\ncerteza se pode cumprir pois essa promessa irá te atormentar até que você consiga cumpri-la. '''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nAltamente compatível com o 2, 6 e 7.')
    print('Incompatível com 3 e 5.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-4/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo5():

    print('\n{:^100}'.format('Número 5 – Rompe as regras e as questiona'.upper()))
    print(
        '''\nO Número 5 é o algarismo que representa a estrela de 5 pontas, o Pentagrama, a representação do Homem'''
        '''\ndiante do Universo. O pentagrama tem o significado de evolução, de liberdade, do sentimento de aventura'''
        '''\nque leva ao crescimento pessoal e do universo. O número 5 representa também as viagens internas e'''
        '''\nexternas, a versatilidade em pessoa. É um número de movimento, da velocidade, da agitação que acaba com'''
        '''\nqualquer estabilidade e limitação que venha pela frente. É um número trangressor, simbolo da evolução.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nQuem é nativo do número 5 tem características empreendedoras e aventureiras. São pessoas muito versáteis'''
        '''\ne que adoram a sua liberdade. São sensuais e inteligentes, com a curiosidade e a vontade de mudança à'''
        '''\nflor da pele.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nO senso de aventura em excesso gera irresponsabilidade, falta de objetivos na vida, inquietação e'''
        '''\ninfidelidade em seus relacionamentos. São muitos ímpetos que surgem ao mesmo tempo, e isso gera'''
        '''\nansiedade, instabilidade e impulsividade.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 5 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nSão pessoas extremamente sensuais e atraentes, possuem magnetismo pessoal que faz com que tenham'''
        '''\ndiversos pretendentes. Sua sexualidade é intensa, quase agressiva, cheia de energia. Quando está em um'''
        '''\nrelacionamento costuma se entregar de cabeça, desde que não cortem com a sua liberdade. Tem tendência a'''
        '''\nquerer ter mais de um parceiro ao mesmo tempo ou de fugir à infidelidade.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 5:'))
    print(
        '''\nEstimule o seu lado aventureiro e curioso mas não deixe que este ímpeto te torne irresponsável e'''
        '''\ninconsequente. Algumas tarefas de rotina são muito chatas mas precisam ser feitas, não adianta'''
        '''\npestanejar. O melhor é resolvê-las e ficar livre delas. Aceite as mudanças e não tente fazer uso'''
        '''\ninadequado da liberdade pessoal que deseja ter.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nAltamente compatível com o 5 e 3.')
    print('Incompatível com 9, 1 e 4.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-5/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo6():

    print('\n{:^100}'.format('Número 6 – Mantém as tradições e a família'.upper()))
    print(
        '''\nNa Numerologia, o número 6 é o algarismo do equilíbrio e da harmonia. É um número conciliador,'''
        '''\nrelacionado diretamente com a justiça, verdade e honestidade. Ele representa a harmonia e organização do'''
        '''\nlar e da família, mas também tem estreitas ligações com as manifestações artísticas. O 6 representa o'''
        '''\namor, a fidelidade, honestidade, solidariedade, tolerância e inteligência.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nQuem é nativo do número 6 é uma pessoa generosa, conciliadora e muito estável. São pessoas muito'''
        '''\ncompanheiras, que se preocupam com o seu lar, com sua família e com seus amigos. Tem um senso de justiça'''
        '''\ne honestidade apuradas. São muito equilibrados e procuram a harmonia em todas as relações.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nSão pessoas um tanto acomodadas com a sua vida, e isso costuma gerar problemas de relacionamento. Gostam'''
        '''\nde se fazer de vítima e têm espírito de mártir. São excessivamente ciumentos, guardam mágoas e rancores'''
        '''\nantigos e têm muita dificuldade em aceitar a realidade.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 6  NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nNo sexo, eles aparentam ser pessoas quietas e passivas mas na verdade fazem de tudo para dar prazer ao'''
        '''\nseu parceiro. São dominadores e possessivos, por isso muitas vezes sente-se inseguro em relação aos'''
        '''\nsentimentos. São muito ciumentos. Como conciliadores, eles sempre buscam a paz e a harmonia no'''
        '''\nrelacionamento, tentando sempre resolver as diferenças com calma e muita conversa. São apegados ao lar e'''
        '''\nà família, acha importante o contato constante.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 6:'))
    print(
        '''\nVocê precisa aceitar as coisas como elas são, tem coisas que não vale a pena ser teimoso. Valorize a sua'''
        '''\nsolidariedade e incentive os outros a serem como você. Mas cuidado para não impor sua vontade aos'''
        '''\ndemais. Controle o seu ciúme, ele só irá prejudicar sua relação com as demais pessoas.'''
        '''\n'''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nAltamente compatível com o 2 e 6.')
    print('Incompatível com 7 e 9.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-6/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo7():

    print('\n{:^100}'.format('Número 7 – Analisa de maneira científica e busca os detalhes'.upper()))
    print(
        '''\nO número 7 é o algarismo que representa a espiritualidade. O 7 é um numero muito marcante na,'''
        '''\nnumerologia é o número da perfeição, que integra o mundo, é o símbolo da totalidade do Universo em'''
        '''\ntransformação. 7 são os dias da semana, as cores do arco-iris, as maravilhas do mundo. Está ligado à'''
        '''\nintrospecção, ao ocultismo, à pesquisa da espiritualidade, à reflexão que leva à sabedoria. A busca por'''
        '''\naquilo que não se vê, a meditação, o descanso, a busca da paz interior. É o número que aproxima o homem'''
        '''\nde Deus.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nQuem é nativo do número 7 na numerologia tem por característica a tranquilidade, a intuição apurada,'''
        '''\nsabedoria e introspecção. São pessoas meticulosas, lógicas, donos de grande perfeccionismo e'''
        '''\nautocontrole. Gostam de se aprofundar em tudo o que fazem, investigar tudo pois querem ter conhecimentos'''
        '''\nsobre todas as coisas.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nPodem se tornar pessoas melancólicas e solitárias. São desligados, não estabelecem objetivos e acabam se'''
        '''\nperdendo e esquecendo o sentido da vida. São excessivamente críticos e autocríticos. Exigem demais de si'''
        '''\nmesmo, acaba se excluindo de grupos de amigos e familiares.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 7 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nO amor na vida dos nativos do número 7 é algo difícil de definir e compreender. Eles têm desinteresse'''
        '''\npelas coisas materiais, por isso não se liga a presentes e datas. Sua preocupação com o muito espiritual'''
        '''\né muito forte, o que o torna um companheiro excêntrico. São muito intuitivos e por isso precisam ter'''
        '''\nmomentos solitários em sua vida, mas eles sentem falta de ter um companheiro e por isso precisam'''
        '''\nbalancear os momentos sozinhos e momentos com companhia. Eles atingem níveis extremos de intimidade com'''
        '''\nos seus parceiros, se jogamde cabeça, mas são propensos a confiar demais e a sofrer decepções amorosas'''
        '''\npor causa disso.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 7:'))
    print(
        '''\nVocê precisa respeitar a sua necessidade de ficar só, mas não a estimule, todo mundo precisa de'''
        '''\ncompanhia e você não é diferente. Tente entender o seu próprio mundo, desvendar os seus próprios'''
        '''\nsegredos e refletir o que há dentro de si, assim será mais fácil entender as suas atitudes e lidar com'''
        '''\nas atitudes alheias.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nAltamente compatível com o 7, 4 e 9.')
    print('Incompatível com 6 e 2.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-7/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo8():

    print('\n{:^100}'.format('Número 8 – Faz justiça e promove a prosperidade'.upper()))
    print(
        '''\nO número 8 representa na Numerologia a vitória, a prosperidade e a superação. Este algarismo representa'''
        '''\npessoas que sabem gerir bem o seu dinheiro e o seu poder. São responsáveis, adoradores de bens materiais'''
        '''\ne do reconhecimento do seu poder. Seu caminho mostra como ele se dedicou e se transformou para chegar'''
        '''\naté o topo da montanha para adquirir seu prestigio movido à pura ambição. É símbolo da luta, dos'''
        '''\nenfrentamentos, da guerra pessoal, mas sempre dotados de muita justiça, honestidade, senso ético e'''
        '''\nmoral. O 8 simboliza também o renascimento, a renovação, a regeneração e a vitória pessoal através do'''
        '''\nenriquecimento.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nQuem nasce sobre a influência do número 8, vem ao mundo com espírito de liderança, de eficiência e uma'''
        '''\npessoa que luta pelo poder e pelo prestígio. São muito ligados ao sucesso e à riqueza, mas tudo com'''
        '''\nmuita justiça e honestidade. São perseverantes e não se deixam abater pelas dificuldades. São muito'''
        '''\nautoconfiantes, verdadeiros e compreensivos.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nSão demasiado ambiciosos, com sede pelo poder e isso gera um materialismo desenfreado. Em busca dos seus'''
        '''\nobjetivos materiais eles se tornam arrogantes, intolerantes e autoritários. Sua teimosia e impaciência'''
        '''\ngeram discórdias.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 8 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nSua sexualidade é tão intensa que chega a ser agressiva. Adora desafios e tem tendência a se envolver em'''
        '''\nrelacionamentos complicados. Quando se envolvem são bastante responsáveis e passam segurança no'''
        '''\nrelacionamento. No entanto, o seu parceiro não deve se envolver nos seus assuntos de negócios, pois eles'''
        '''\nse tornam intolerantes, frios e arrogantes.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 8:'))
    print(
        '''\nControle a sua arrogância e autoritarismo, isso irá magoar as pessoas e elas irão se afastar de você,'''
        '''\npreze sempre pela diplomacia. Use o seu dinheiro e o seu poder de forma correta, pautado na justiça e'''
        '''\nhonestidade.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nAltamente compatível com o 2, 6 e 3.')
    print('Incompatível com 8 e 1.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-8/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo9():

    print('\n{:^100}'.format('Número 9 – Ultrapassa e expande os limites'.upper()))
    print(
        '''\nO número 9 simboliza o fim de um ciclo e começo de outro. É um algarismo associado ao altruísmo, à'''
        '''\ngenerosidade, à fraternidade e à espiritualidade. Seu significado é de compreensão, realização,'''
        '''\nuniversalidade e compaixão. O símbolo de realização é o mais alto que um ser humano pode alcançar,'''
        '''\ndepois de ultrapassar o seu ego ele é capaz de amor universal e incondicional. A sua espiritualidade é'''
        '''\nelevada e por isso ele possui muita sabedoria. É considerado o número auge, em plenitude, na totalidade'''
        '''\ndo ser.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nSão pessoas únicas, capazes de sentir o amor universal, algo raro e difícil. São muito tolerantes,'''
        '''\npacientes e generosos. Possuem uma forte espiritualidade e fé, nada é capaz de abalar sua crença. Tem'''
        '''\nrespeito e carinho por tudo e por todos.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nSua fé inabalável gera brecha para o fanatismo religioso, para pessoas que querem pregar a sua'''
        '''\nreligiosidade o tempo todo e isso incomoda a muitas pessoas. Eles acabam solitários e se sentindo'''
        '''\nfracassados. Fazem sacrifícios desnecessários e depois se arrependem de não ter aproveitado a vida.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 9 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nQuando os nativos do número 9 se apaixonam, eles se tornam grandes amantes, dóceis e dedicados. O número'''
        '''\n9 é o número das pessoas prestativas e bem dispostas. Sua simpatia e disposição fazem com que eles'''
        '''\npossam ser dominados facilmente. Eles gostam de demonstração de amor, e estão sempre fazendo os seus'''
        '''\nparceiros se sentirem amadas. Ele assume os problemas do parceiro para si e quer enfrentá-los juntos.'''
        '''\nQuando infeliz o número nove pode recorrer a táticas de abuso emocional e intimidação.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 9:'))
    print(
        '''\nA confiança é peça chave para as pessoas do número 9.  A sua fé e confiança faz com que se confie demais'''
        '''\nnas pessoas e se decepcione. É preciso dosar a confiança para não ser passado para trás ou ficar muito'''
        '''\ntriste quando alguém diz que não confia em você. Você tem o dom de desenvolver o amor universal, a'''
        '''\ncompreensão e a compaixão nas pessoas, use desse dom!'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nAltamente compatível com o 9, 7 e 4.')
    print('Incompatível com 1 e 5.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-9/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo11():

    print('\n{:^100}'.format('Número 11 – Não se encaixa em nenhum grupo específico'.upper()))
    print(
        '''\nO número 11 é um número mestre, um número perfeito que representa o idealismo do homem na busca pela sua'''
        '''\nprópria espiritualidade e pelo contato com Deus. Este número tem um forte magnetismo aos ideais humanos'''
        '''\ne quem nasce sobre essa influência tem a intuição e a sensibilidade muito aguçadas. Este número é'''
        '''\nvoltado para as pessoas que buscam o bem da humanidade, que têm ideias avançadas e elevadas para'''
        '''\nevolução do Homem.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nSão pessoas idealistas, que seguem a sua intuição e o seu coração o tempo todo. Possuem paciência'''
        '''\ninigualável, sabedoria nata e poderes extra sensoriais. São voltados para os assuntos místicos e possuem'''
        '''\nsenso humanitário acentuado, gostam de trazer o bem para todos ao seu redor e é reconhecido pela sua'''
        '''\nsimpatia.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nSuas características de espiritualidade e elevação quando não são bem geridas podem dar brecha para a'''
        '''\nexistência do fanatismo, charlatanismo, pragmatismo e cinismo. Há pessoas do número 11 que ficam'''
        '''\ndesorientadas com sua sensibilidade e intuição, passam a se sentir superiores aos demais, são'''
        '''\ndesonestas, preguiçosas e mesquinhas.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 11 DO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nO onze é um dos números mais românticos de toda a numerologia. Eles idealizam o relacionamento, só veem'''
        '''\no lado bom do seu parceiro e são extremamente atenciosos. Procuram em seus parceiros um companheiro para'''
        '''\na vida e tentam fazê-los feliz de toda maneira. Costumam ser muito tolerantes em suas diferenças e'''
        '''\naceitam as ideias e opiniões, mesmo que sejam divergentes.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 11:'))
    print(
        '''\nLeve a sua intuição à sério, ela é muito poderosa e será sempre pertinente avaliá-las antes de tomar'''
        '''\ndecisões. Saiba também diferenciar intuição de vontade. São coisas bem diferentes.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nCompatível com o 2, 4, 6, 3 e 5.')
    print('Incompatível com 7, 1, 8 e 9.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-11/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def nomo22():

    print('\n{:^100}'.format('Número 22 – Tenta realizar o impossível'.upper()))
    print(
        '''O número 22 é um número mestre que representa o mundo material, o mundo concreto. Ele está relacionado a'''
        '''\ntudo que envolve a construção, o trabalho, o poder e também o otimismo. O número 11 simboliza a '''
        '''\ntransformação dos desejos e necessidades humanas em realidade, com o seu espírito empreendedor,'''
        '''\nperspicácia e raciocínio lógico afiado.'''
        '''\n'''
    )
    print('{:^100}'.format('CARACTERÍSTICAS POSITIVAS:'))
    print(
        '''\nSão pessoas muito generosas, mão aberta, daqueles que não medem esforços para ajudar quem ele pode. É'''
        '''\ndono de um raciocínio invejável, muito sagaz e com espírito empreendedor sabe transformar sonhos em'''
        '''\nrealidade. É otimista e muito leal.'''
        '''\n '''
    )
    print('{:^100}'.format('CARACTERÍSTICAS NEGATIVAS:'))
    print(
        '''\nSão pessoas que têm tendências opostas: ou se tornam vaidosos em excesso, ou sofrem de um complexo de'''
        '''\ninferioridade de se achar mais feio e pior do que todos ao seu redor. Falta determinação para concluir'''
        '''\nos seus projetos e detestam que as pessoas apontem esse defeito, reage com cinismo.'''
        '''\n '''
    )
    print('{:^100}'.format('NÚMERO 22 NO AMOR E NOS RELACIONAMENTOS:'))
    print(
        '''\nNo amor, os nativos do número 22 da numerologia são pessoas de extremo, é tudo ou nada. Não se entregam'''
        '''\nparcialmente, ou gostam demais da pessoa, ou não se envolvem de jeito nenhum. É preciso ter cuidado com'''
        '''\nesse lado extremista, pois uma pessoa que é para ele o amor de sua vida pode se tornar o seu pior'''
        '''\ninimigo caso o relacionamento não dê certo.'''
        '''\n '''
    )
    print('{:^100}'.format('DICAS PARA PESSOAS NATIVAS DO NÚMERO 22:'))
    print(
        '''\nA dica é: liberte-se, se entregue, não podere tanto. Tente ver os outros com suas individualidades, não'''
        '''\ncomo um espelho de si mesmo, as pessoas são diferentes de você, isso é natural e saudável.'''
        '''\n '''
    )
    print('{:^100}'.format('COMPATIBILIDADE COM:'))
    print('\nCompatível com o 2, 6, 7 e 11.')
    print('Incompatível com 3 e 5.')
    print(
        '''\nFontes: wemystic.com.br/significado-do-numero-22/'''
        '''\n        linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
    )


def numerologicint():

    a = int(nomo.count('a') * 1)
    e = int(nomo.count('e') * 5)
    i = int(nomo.count('i') * 9)
    o = int(nomo.count('o') * 6)
    u = int(nomo.count('u') * 3)

    totalo = int(a + e + i + o + u)

    if totalo == 11 or totalo == 22 or totalo < 10:
        redukto = int(totalo)
    else:
        while totalo > 9:
            unueco = totalo // 1 % 10
            deko = totalo // 10 % 10
            cento = totalo // 100 % 10
            totalo = unueco + deko + cento
            redukto = totalo

    return redukto


def rezolucioint():

    if numerologicint() == 1:
        nomoint1()
    else:
        if numerologicint() == 2:
            nomoint2()
        else:
            if numerologicint() == 3:
                nomoint3()
            else:
                if numerologicint() == 4:
                    nomoint4()
                else:
                    if numerologicint() == 5:
                        nomoint5()
                    else:
                        if numerologicint() == 6:
                            nomoint6()
                        else:
                            if numerologicint() == 7:
                                nomoint7()
                            else:
                                if numerologicint() == 8:
                                    nomoint8()
                                else:
                                    if numerologicint() == 9:
                                        nomoint9()
                                    else:
                                        if numerologicint() == 11:
                                            nomoint11()
                                        else:
                                            nomoint22()


def nomoint1():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 1 – Independente, individualista, tende a comandar as relações.'.upper()))
    print(
        '''\nVocê é uma pessoa que carrega dentro de si uma urgência em ser independente, dirigir a sua própria vida,'''
        '''\nandar com as próprias pernas e viver conforme aquilo que acredita. Tem um espírito de liderança muito'''
        '''\nforte, gosta de assumir compromissos ousados, sente-se impulsionado a reger. Conduz as pessoas com'''
        '''\ncoragem e confiança, tem boa autoconfiança e acredita que o seu julgamento se sobressai frente às demais'''
        '''\npessoais. Analisa muito antes de tomar uma decisão, e quando toma, normalmente não volta atrás. É uma'''
        '''\npessoa inteligente e esperta, detesta a rotina ou qualquer outra coisa que o prenda, que limite a sua'''
        '''\nliberdade e independência. Tem tendência a ser muito individualista e um autoritário.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint2():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 2 – Dependente, sensível, tende a ser conduzido e a se adaptar'.upper()))
    print(
        '''\nSe o seu número da alma é o número 2, a busca pela paz e pela harmonia devem ser uma prioridade em sua'''
        '''\nvida. São pessoas diplomáticas, atenciosas e gentis. Uma característica marcante das pessoas do número 2'''
        '''\né: a sensibilidade. São extremamente sensíveis, emocionais e preocupam-se muito com os sentimentos dos'''
        '''\noutros. Evita ferir os outros a todo custo, à ponto de submeter-se às vontades alheias. Gosta de'''
        '''\ntrabalhar em equipe, tem mais talento para ser liderado do que para ser líder. Outra característica'''
        '''\nforte: a indecisão. São muito indecisos pela carência de confiança, é preciso trabalhar a autoconfiança'''
        '''\ne domar a timidez para equilibrar as emoções e tomar decisões sábias. Normalmente, têm um excelente'''
        '''\ngosto musical e dom para compreender sobre música e outras artes.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint3():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 3 – Alegre, criativo e de temperamento infantil para bem e mal'.upper()))
    print(
        '''\nAs pessoas do número de motivação 3 são pessoas muito queridas, que gostam de estar sempre rodeados por'''
        '''\naquele que ama, compartilhar a felicidade, o amor e boas energias. Tem talento nato para diversas áreas,'''
        '''\nespecialmente para escrita, canto e poesia. Consegue canalizar os seus sentimentos de forma artística e'''
        '''\ncriativa de forma incrível. É uma pessoa muito confiável em todos os quesitos. São namoradores, adoram'''
        '''\nnamorar, e são muito fieis ao sentimento e ao parceiro, mesmo que os namoros não sejam longos. Adora'''
        '''\nreceber atenção e dar atenção aos outros. É bem responsável com seus compromissos e deveres, sabe que'''
        '''\ndeve usar a sua imaginação e inspiração para trabalhar bem e auxiliar os outros, e gosta de fazer disso'''
        '''\na sua filosofia de vida. Procura a felicidade e a encontra ao deixar os outros felizes.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint4():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 4 – Confiável, previsível; busca relações estáveis e sólidas, mantém '
                             'tradições'.upper()))
    print(
        '''\nQuem possui o número de motivação na casa número 4 gosta de estabilidade, segurança e organização. São'''
        '''\npessoas muito determinadas, qualidade que deverá lhe trazer sucesso profissional. Gosta de tudo muito'''
        '''\nbem organizado e estabelecido, por isso mudanças repentinas e de última hora o incomodam. Gostam da'''
        '''\nrotina pois ela o traz segurança. É um perfeccionista, sistemático, que adora analisar com cuidado e'''
        '''\nlógica qualquer questão, sempre atento aos detalhes. Seu ideal é ser seguro, firme e estável como uma'''
        '''\nrocha. É uma pessoa muito fiel e caseira, com a família e com os subordinados no trabalho pode ser'''
        '''\ndemasiado rígido e disciplinador. A honestidade é uma grande virtude sua.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint5():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 5 – Sensual, imprevisível, busca novidade e aventura, reage às tradições'.upper()))
    print(
        '''\nQuem tem o número de motivação 5 tem em sua alma o desejo de liberdade. Adora novas experiências,'''
        '''\nmudanças, a excitação do novo, corres riscos, aprender coisas novas. É uma pessoa extremamente flexível'''
        '''\ne se adapta bem em qualquer situação. Adora a adrenalina do desconhecido, ama conhecer lugares novos,'''
        '''\nespecialmente se eles forem exóticos e distantes. As viagens são um desejo constante de sua alma, por'''
        '''\nconsiderá-las educativas e ampliadoras de horizontes. É uma pessoa com mente afiada, pensamento rápido e'''
        '''\naptidão nata para as palavras. Um excelente comunicador e uma pessoa com uma imaginação muito fértil.'''
        '''\nGosta da variedade, evita o “mais do mesmo”, seguir caminhos seguros, gosta de sair da zona de conforto.'''
        '''\nÉ um entusiasta, intuitivo e sensual. Atividades rotineiras o deixam aborrecido e entediado, detesta'''
        '''\nqualquer tipo de mesquinharia.'''
        '''\n'''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint6():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 6 – Valoriza a família, emotivo, ciumento, apaixonado e parcial'.upper()))
    print(
        '''\nQuem tem o número da alma 6 é alguém que preza muito pela harmonia familiar. Adora a companhia da sua'''
        '''\nfamília, dar conforto (e se possível luxo) a eles. Ver a sua família feliz é algo que te dá muita'''
        '''\nmotivação. Tem um desejo muito forte em ajudar os outros, e costuma até colocar as necessidades daquele'''
        '''\nque você ama em prioridade. É uma pessoa muito leal e honesta, não gosta de julgar os outros. Muito'''
        '''\natencioso, gosta de ouvir a todos, dar conselhos, pois é muito compreensivo e afetuoso. É preciso evitar'''
        '''\nque o seu cuidado com a família e com as outras pessoas seja tão grande que não os deixe ter opinião'''
        '''\nprópria, que eles expressem ideais de vida diferentes do seu. O seu desejo de proteção é tão grande que'''
        '''\nas vezes os sufoca e faz com que eles não consigam ter independência em relação à você.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint7():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 7 – Valoriza o intelecto, racional, precisa de certo isolamento, busca o '
                             'espiritual'.upper()))
    print(
        '''\nAs pessoas de alma são muito tranquilas e reservadas, apreciam o estudo, o conhecimento e são'''
        '''\nnaturalmente calados e introspectivos. São sensíveis, refinados e normalmente muito intuitivos.'''
        '''\nAmbientes barulhentos e discussões o deixam muito irritado, gosta de espaços pacíficos e calmos. Por ser'''
        '''\numa pessoa muito reservada, não tem urgência em estabelecer um relacionamento amoroso, gosta de estar'''
        '''\nsozinho e pode permanecer solteiro por toda a vida sem se incomodar com isso. Evita relacionamentos que'''
        '''\nconduzam o casamento pois gosta de preservar a sua individualidade. Aprecia a filosofia, a'''
        '''\nintelectualidade e a ordem mística mais elevada da humanidade. Possui natureza calma, e apesar de não'''
        '''\ngostar de demonstrar os seus sentimentos, são bastante emotivos.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint8():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 8 – Pragmático, justo, objetivo, parece dominar, mas é ultra-sensível'.upper()))
    print(
        '''\nAs pessoas de alma 8 são movidas pela ambição. Sonham grande, querem ter sucesso financeiro, riqueza,'''
        '''\nconforto e poder pessoal. Sonha em ser uma pessoa respeitada e busca por isso com muita determinação.'''
        '''\nQuer se destacar na multidão, ser lembrado pelos seus feitos. Tem faro apurado para os negócios e grande'''
        '''\nespírito de liderança. É muito apegado aos detalhes e detesta a rotina. Apesar de sua ambição material'''
        '''\nser muito grande, é ligado também às questões espirituais e busca o equilíbrio entre os dois planos.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint9():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 9 – Energia extrema, ânsia, precisa de movimento e grandiosidade'.upper()))
    print(
        '''\nA palavra chave das pessoas de motivação número 9 é a intuição. São extremamente sensíveis,'''
        '''\nimaginativos e conseguem pensar e compreender conceitos abstratos e invisíveis com facilidade. São'''
        '''\ncompassivos e generosos, gentis e clementes. Precisam receber muito amor e dar muito amor, sua'''
        '''\nfelicidade se baseia nesta troca. Possui consciência expansiva e dedicada à evolução da humanidade.'''
        '''\nDeseja o entendimento universal, quer servir o mundo e atrair a bondade para o planeta. Sua maior'''
        '''\nsatisfação é saber que foi útil para o avanço da humanidade, nem que seja só um pouquinho.Esforça-se'''
        '''\nmuito para fazer do mundo um local melhor para se viver. É um perfeccionista nato, até demais. Deseja'''
        '''\nter recursos para aliviar imediatamente o sofrimento de outra pessoa, quer seja econômico, físico ou'''
        '''\npsicológico.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint11():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 11 – Voltado ao transcendental, precisa se sentir compreendido, o que é '
                             'raro'.upper()))
    print(
        '''\nAs pessoas do número de motivação 11 são pessoas altamente espiritualizadas (e isso não tem relação com'''
        '''\na religião). São idealistas, pacificadores, gostam de ajudar sem esperar nada em troca. Procura'''
        '''\nestabelecer a paz e a harmonia onde quer que vá. É uma “alma velha”, que está neste caminho espiritual'''
        '''\nhá muito tempo e tem grande conhecimento acumulado. Por isso, veio ao mundo para oferecer a luz, possui'''
        '''\nintuição muito elevada e sensibilidade extrema. Possui coragem incrível para enfrentar qualquer'''
        '''\nsituação, pois sua alma já viveu de tudo um pouco. Aprecia coisas refinadas e sofisticadas.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def nomoint22():

    print('\n{:^100}'.format('NÚMERO DE MOTIVAÇÃO:'))
    print(
        '''\nO número de motivação representa, como diz o próprio nome, a vida interna da pessoa, seu lado afetivo,'''
        '''\nseu comportamento dentro de casa, com a família, com amigos íntimos e o tipo de personalidade que'''
        '''\ndemonstra na vida amorosa. É aquele aspecto da pessoa que só quem a conhece na intimidade tem acesso.'''
    )
    print('\n{:^100}'.format('Número 22 – Voltado à realização do impossível, emocionalmente delicado apesar de'
                             'resistente'.upper()))
    print(
        '''\nO número de motivação 22 é aquele que possui maior vibração entre todos os outros. São pessoas elevadas'''
        '''\ne evoluídas. Possuem como ninguém: paciência, diplomacia, cooperação, otimismo e sabedoria para lidar'''
        '''\ncom as coisas materiais. Busca um motivo nobre para estar na terra, para canalizar todo o poder que'''
        '''\npossui. Tem desejo por poder material e para isso tem grande capacidade administrativa, mas seu desejo'''
        '''\nnão é egoista, quer modificar o mundo para dar melhores condições materiais a todos. Tem fortes'''
        '''\nhabilidades diplomáticas e organizacionais e por isso sabem lidar muito bem com projetos e assuntos'''
        '''\ndifíceis e/ou delicados. Quando encontra alguém ou algum obstáculo que o afasta de seu objetivo nobre,'''
        '''\npode ser tornar grosseiro.'''
        '''\n'''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-de-expressao-motivacao-e-personalidade/'''
        '''\n       wemystic.com.br/artigos/numerologia-da-alma-descubra-o-seu-numero-de-motivacao/'''
    )


def numerologicext():

    b = int(nomo.count('b') * 2)
    c = int(nomo.count('c') * 3)
    d = int(nomo.count('d') * 4)
    f = int(nomo.count('f') * 6)
    g = int(nomo.count('g') * 7)
    h = int(nomo.count('h') * 8)
    j = int(nomo.count('j') * 1)
    k = int(nomo.count('k') * 2)
    l1 = int(nomo.count('l') * 3)
    m = int(nomo.count('m') * 4)
    n = int(nomo.count('n') * 5)
    p = int(nomo.count('p') * 7)
    q = int(nomo.count('q') * 8)
    r = int(nomo.count('r') * 9)
    s = int(nomo.count('s') * 1)
    t = int(nomo.count('t') * 2)
    v = int(nomo.count('v') * 4)
    w = int(nomo.count('w') * 5)
    x = int(nomo.count('x') * 6)
    y = int(nomo.count('y') * 7)
    z = int(nomo.count('z') * 8)

    totalo = int(b + c + d + f + g + h + j + k + l1 + m + n + p + q + r + s + t + v + w + x + y + z)

    if totalo == 11 or totalo == 22 or totalo < 10:
        redukto = int(totalo)
    else:
        while totalo > 9:
            unueco = totalo // 1 % 10
            deko = totalo // 10 % 10
            cento = totalo // 100 % 10
            totalo = unueco + deko + cento
            redukto = totalo

    return redukto


def rezolucioext():

    if numerologicext() == 1:
        nomoext1()
    else:
        if numerologicext() == 2:
            nomoext2()
        else:
            if numerologicext() == 3:
                nomoext3()
            else:
                if numerologicext() == 4:
                    nomoext4()
                else:
                    if numerologicext() == 5:
                        nomoext5()
                    else:
                        if numerologicext() == 6:
                            nomoext6()
                        else:
                            if numerologicext() == 7:
                                nomoext7()
                            else:
                                if numerologicext() == 8:
                                    nomoext8()
                                else:
                                    if numerologicext() == 9:
                                        nomoext9()
                                    else:
                                        if numerologicext() == 11:
                                            nomoext11()
                                        else:
                                            nomoext22()


def nomoext1():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 1 – Arrogante, pose de líder, o que direciona'.upper()))
    print(
        '''\nVocê transmite a imagem de liderança, dinamismo e independência.'''
        '''\nSua autoconfiança indica a capacidade de enfrentar as dificuldades e transpor os obstáculos que surgirem'''
        '''\nem seu caminho com certa facilidade. As pessoas vão procurá-la para tocar projetos e empreendimentos'''
        '''\nonde suas qualidades sejam essenciais.'''
        '''\nOs outros acreditam em sua capacidade para assumir e tomar conta com eficiência de qualquer situação.'''
        '''\nEssa forma original de enfrentar os problemas causa bastante admiração nas pessoas que estão à sua'''
        '''\nvolta.'''
        '''\nPara aproveitar o lado positivo do seu número, é necessário que a mente esteja concentrada em um'''
        '''\nobjetivo único: conseguir um resultado satisfatório em um curto espaço de tempo.'''
        '''\nAja com bastante equilíbrio para ganhar a confiança e o apoio de seus comandados.'''
        '''\nAssim, será uma líder e empreendedora de sucesso.'''
        '''\n '''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext2():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 2 – Discreto, reflete o ambiente em que se encontra'.upper()))
    print(
        '''\nTransmite uma imagem de pessoa prestativa e não costuma causar transtornos nos relacionamentos em casa'''
        '''\nou no trabalho.'''
        '''\nAs pessoas a vêem como liberal e simpática. Os que estão ao seu redor são atraídos por suas qualidades'''
        '''\ninspiradoras.'''
        '''\nNão gosta de ocupar cargo de liderança e ser o centro das atenções.'''
        '''\nPrefere agir nos bastidores, mas nem por isso deixa de ser brilhante.'''
        '''\nCostuma preocupar-se com a maneira com que os outros a vêem e isso, às vezes, pode prejudicar um pouco o'''
        '''\nseu rendimento.'''
        '''\nNão é mandona e consegue colocar suas idéias sem demostrar autoritarismo.'''
        '''\nA persuasão é uma qualidade marcante.'''
        '''\nTem a capacidade de dizer sempre a coisa certa no momento certo, deixando as pessoas sempre à vontade.'''
        '''\nColabora para um melhor entendimento entre os diversos grupos com os quais se relaciona, já que é'''
        '''\ncondescendente.'''
        '''\nTem um espírito de cooperação que é apreciado pelos colegas.'''
        '''\n'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext3():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 3 – Comunicativo e simpático, às vezes um tanto exibido'.upper()))
    print(
        '''\nVocê transborda em alegria, afeto e otimismo.'''
        '''\nEstas qualidades acabam projetando a imagem de uma pessoa muito popular no seu círculo de amizades.'''
        '''\nNão perde um agito por nada, principalmente aqueles em que pode demonstrar o seu talento artístico, a'''
        '''\nsua imaginação e a sua criatividade.'''
        '''\nUma festinha é sempre bem-vinda para você.'''
        '''\nTem espírito comunicativo e um charme especial, que parece usar para conseguir o que quer.'''
        '''\nTransmite descontração e um ótimo senso de humor.'''
        '''\nParece sempre jovem, não importa a idade que tenha.'''
        '''\nToda essa animação contagia seus colegas, que acabam apreciando sua companhia.'''
        '''\nTem uma mente fértil em idéias e está sempre aberta para novos conceitos, o que é muito bom,'''
        '''\nprincipalmente nos negócios.'''
        '''\nMesmo nas situações mais complicadas, consegue vislumbrar um lado positivo, contagiando, inclusive, as'''
        '''\npessoas que estão à sua volta.'''
        '''\nIsso acaba aumentando a produtividade e abrindo as portas para você.'''
        '''\nProcura, ainda, tirar lições das situações menos favoráveis.'''
        '''\n '''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext4():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 4 – Transmite confiança e seriedade à primeira vista'.upper()))
    print(
        '''\nA aparência é de alguém em quem se pode confiar e que é muito produtiva.'''
        '''\nNão admite superficialidade, desonestidade e covardia.'''
        '''\nÉ vista como uma pessoa muito eficiente e que norteia seus atos tendo como diretriz a prudência.'''
        '''\nO senso organizacional contribui para uma impressão ainda mais positiva a seu respeito.'''
        '''\nNão se deixa envolver facilmente, principalmente se as propostas se mostrarem levianas e sedutoras'''
        '''\ndemais.'''
        '''\nNinguém a faz de boba.'''
        '''\nAparenta estabilidade, como se tivesse seu caminho delineado.'''
        '''\nÉ bastante pontual e procura cumprir todos os compromissos assumidos, o que contribui para uma reputação'''
        '''\nde ser leal e responsável, você sempre termina o que começa.'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext5():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 5 – Rebelde, irônico, atraente, provocativo'.upper()))
    print(
        '''\nVocê aparenta ser uma pessoa curiosa e impaciente.'''
        '''\nEstá metida em um monte de coisas ao mesmo tempo, principalmente quando o assunto é negócio. O espírito'''
        '''\naventureiro da adolescência se transforma em dinamismo quando atinge a fase adulta.'''
        '''\nAs pessoas a acham excitante e, muitas vezes, imprevisível.'''
        '''\nNão gosta da rotina, por isso, procura sempre inovar e fazer coisas diferentes.'''
        '''\nA versatilidade acaba sendo uma qualidade em evidência.'''
        '''\nAceita assumir os riscos de uma situação mais complexa.'''
        '''\nSente necessidade de manter as coisas funcionando e as pessoas pensando.'''
        '''\nAtrai os que estão à sua volta com o seu magnetismo, a sua vitalidade e o seu senso prático.'''
        '''\nNão vive do passado e nem fica criando expectativas com relação ao futuro.'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext6():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 6 – Familiaridade e hospitalidade'.upper()))
    print(
        '''\nDesde criança, transmite uma imagem de afetuosidade, beleza, harmonia e serenidade.'''
        '''\nDá a impressão de que é um porto seguro no mar das tormentas da vida.'''
        '''\nDemonstra um espírito bondoso e está sempre pronta a ajudar quem necessita da sua atenção e de seus'''
        '''\nconselhos.'''
        '''\nOdeia a mentira e a injustiça, portanto, mantém uma constante luta para buscar a verdade e a justiça.'''
        '''\nNão aceita a companhia de pessoas que não agem de acordo com as suas convicções.'''
        '''\nSeu comportamento está acima de qualquer suspeita.'''
        '''\nAs pessoas a vêem como um exemplo de honestidade e confiabilidade.'''
        '''\nÉ equilibrada, procurando agir sempre com imparcialidade. Graças a esse estilo de vida, dificilmente'''
        '''tira conclusões precipitadas sobre os outros.'''
        '''Dá valor ao lar e à família.'''
        '''No casamento, é super dedicada.'''
        '''Também é uma excelente anfitriã.'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext7():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 7 – Frio e distante, transmite inteligência'.upper()))
    print(
        '''\nDemonstra, desde a infância, uma vocação para desenvolver trabalhos intelectuais.'''
        '''\nPor outro lado, não é muito atraída por atividades desgastantes fisicamente.'''
        '''\nNa fase adulta, parece manter a vida sob controle.'''
        '''\nPassa a impressão de ser uma pessoa inteligente, com intuição aguçada.'''
        '''\nValoriza o lado espiritual.'''
        '''\nDeus tem uma importância significativa na sua vida.'''
        '''\nParece ser solitária, absorvida pelos pensamentos íntimos.'''
        '''\nVeste-se com um toque de classe e tem uma aparência distinta e refinada.'''
        '''\nNão gosta de intimidades e muito menos de brincadeiras fora de hora.'''
        '''\nA vida pessoal é mantida em sigilo.'''
        '''\nGanhar sua confiança não é fácil, já que não costuma contar seus segredos para qualquer um.'''
        '''\nÉ atraída por atividades excêntricas que exijam concentração.'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext8():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 8 – Senso de justiça e objetividade que transparece logo'.upper()))
    print(
        '''\nÉ uma pessoa prestativa e trabalhadora.'''
        '''\nCuida com muito carinho das suas coisas.'''
        '''\nDesde criança, dá valor ao dinheiro e não sai gastando por aí desordenadamente.'''
        '''\nGosta de projetos ambiciosos, que ofereçam a possibilidade de atingir rapidamente a independência'''
        '''\nprofissional e financeira.'''
        '''\nEstá sempre pronta para entrar de cabeça em toda a atividade que se propõe a participar, seja'''
        '''\nprofissional ou assistencial.'''
        '''\nEm ocasiões de calamidade, é a primeira a oferecer ajuda.'''
        '''\nVive muito ocupada, mas se alguém precisar de um favor, está sempre pronta para ajudar.'''
        '''\nAparenta ser bem-sucedida e se preocupa em causar boa impressão logo de cara.'''
        '''\nApesar de usar bem o dinheiro, não economiza quando o assunto é qualidade.'''
        '''\nNada de artigos baratos ou de liquidações.'''
        '''\nFaz questão de andar sempre na moda, de preferência com roupas e acessórios de marcas famosas.'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext9():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 9 – Ansioso e impaciente, mas se dá bem com todo tipo de pessoa'.upper()))
    print(
        '''\nVive preocupada com o próximo.'''
        '''\nNo jardim da infância, já dividia seu lanche com os colegas e costumava doar os brinquedos ou as roupas'''
        '''\nque não usava mais para os necessitados.'''
        '''\nGeralmente, está ligada a profissões onde pode ajudar os outros, como medicina, enfermagem ou'''
        '''\nassistência'''
        '''\nsocial.'''
        '''\nParece ter uma energia interminável quando participa de programas assistenciais.'''
        '''\nTambém gosta de atividades rentáveis para que tenha condições de construir um mundo melhor.'''
        '''\nAparenta ter um talento especial e um desejo ímpar de ajudar os outros.'''
        '''\nEstá à vontade em todos os ambientes.'''
        '''\nEm hipótese alguma faz isso com segundas intenções ou em troca de certos favorecimentos.'''
        '''\nOutra qualidade positiva: não tem nenhum tipo de preconceito, seja ele racial, religioso ou sexual.'''
    )
    print('\nFonte: linhadasaguas.com.br/numero-da-personalidade')


def nomoext11():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 11 – Ar de mistério e parece inatingível ou incompreensível'.upper()))
    print(
        '''\nVocê parece ser uma pessoa amável e despretensioso. Externa suavidade e calor, e as e seguro. Elas se'''
        '''\nsentem atraídas para você, pessoas vêem em você um Porto tranquilo, pois, entre outras razões, sua'''
        '''\naparência é acolhedora e sensível. Suas roupas são limpas e bem cuidadas. Deveria usar roupas'''
        '''\nconfortáveis, leves e despojadas. Evite as lisas e inexpressivas. Faça um esforço para ter uma'''
        '''\naparência um pouco mais ousada e excitante, o que permitirá um equilíbrio.'''
        '''\n '''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-da-personalidade'''
        '''\n       numerologianasuaessencia.blogspot.com.br/2010/10/estudo-das-consoantes-no-nome'''
    )


def nomoext22():

    print('\n{:^100}'.format('NÚMERO DA PERSONALIDADE:'))
    print(
        '''\nO número da personalidade reflete a personalidade pública, a maneira como a pessoa se comporta fora de'''
        '''\ncasa, ou seja, na sociedade, no trabalho, na escola, nas festas. É a primeira impressão que a pessoa'''
        '''\ncausa, aquilo que os outros vêem no indivíduo ao ter contato social pela primeira vez, ou ainda aquilo'''
        '''\nque se ouve falar da pessoa, a marca que ela deixa no imaginário de quem a observa de longe.'''
    )
    print('\n{:^100}'.format('Número 22 – Alguém pronto para as mais difíceis empreitadas'))
    print(
        '''\nVocê irradia segurança e consistência. As pessoas confiam em você e se sentem seguras com seu'''
        '''\njulgamento. Aos olhos do próximo, você é a pedra fundamental de um negócio e todos confiam que fará seu'''
        '''\ntrabalho de modo eficiente e hábil. Força e respeitabilidade são características suas. Tende a'''
        '''\nvestir-se de maneira prática, preocupando-se principalmente com convenções, durabilidade e preço.'''
        '''\nApresenta-se como alguém que valoriza a correção, o controle e a precisão.'''
    )
    print(
        '''Fonte: linhadasaguas.com.br/numero-da-personalidade'''
        '''\n       numerologianasuaessencia.blogspot.com.br/2010/10/estudo-das-consoantes-no-nome'''
    )


while ripetilo == 0:
    nomo = str(input('\nNome completo [sem acentuação]: ')).lower().strip()
    if nomo == 'license':
        print('NUMEROLOGIC is under GPLv3.')
    else:
        if nomo == 'credits':
            print("Tauan Queiroz. \nContact: tauan3@gmail.com \nI'm sorry for anything.")
        else:
            if nomo == 'help':
                print('Digite seu nome sem acentuação para ler seu significado numerológico ou digite '
                      '"exit" para sair.')
            else:
                if nomo == 'exit':
                    ripetilo = 1
                else:
                    if numerologic() == 0:
                        print('Por favor, digite um nome sem acentuações ou encerre o programa.')
                    else:
                        print('O número referente ao seu nome é: {}.'.format(numerologic()))
                        rezolucio()
                        rezolucioint()
                        rezolucioext()
