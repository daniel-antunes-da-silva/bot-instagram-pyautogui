Programa de automação para curtidas e comentários no instagram, utilizando o pyautogui.

Nesse script, o navegador é aberto automaticamente com a url do instagram, e em seguida ele verifica se está na tela de login ou não, através de um botão específico (verificado por print). Caso esteja na tela de login, ele vai fazer login com os dados pré-definidos no código, e caso os dados estejam incorretos, o programa vai identificar que não foi possível efetuar o login, gerando um alerta e interrompendo o loop.
Obs: Se o instagram já estiver logado, o programa identifica, e realiza as ações a partir disso.

Ao entrar no instagram, ele pesquisa e entra em um perfil fornecido pelo usuário, clica na primeira postagem e verifica se a postagem ainda não foi curtida. Caso não tenha sido, vai curtir e fazer um comentário aleatório de uma lista pré-definida. Caso já tenha sido, vai informar que já foi curtida. O programa pode ser configurado para fazer esse processo a cada 24h, sempre deixando curtidas e comentários na postagem mais recente, caso ainda não tenha sido feito.

Obs: por ser uma automação feita com pyautogui, precisa de algumas coordenadas na tela e identificação de imagens, e, por isso, funciona apenas no ambiente em que foi feito para funcionar. Isso quer dizer que não vai funcionar para qualquer um que tiver o código, pois precisaria de modificações. Caso queira, pode apenas utilizar o código como base, mas usando suas próprias coordenadas, imagens para detecção, etc.

Video de demonstração:
[pyautogui_instagram.mp4](pyautogui_instagram.mp4)