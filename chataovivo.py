# Framework -> Conjunto de ferramentas para criação de sistemas
# Django, Flask, Flet, etc...

# Utilização do projeto Chat ao vivo = FLET
# pip install flet

# Título
# Botão de Iniciar o Chat
        # Popup
        # Bem vindo ao Chat
        # Escreva seu nome
    # Chat
        # ... entrou no chat
        # Mensagens do usuário
    # Campo para escrever a mensagem
    # Botão ENVIAR
    
import flet as ft

# Inserir data/hora
# # import datetime

def main(pagina):
    titulo = ft.Text("Chat ao vivo")
    
    nome_usuario = ft.TextField(label="Escreva seu nome")
    
    chat = ft.Column()
    
    
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    # Para que todas as pessoas no chat possam receber as mensagens
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    
    
    def enviar_mensagem(evento):
        # Colocar nome do usuario na mensagem
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        
        # Limpar o campo da mensagem
        campo_mensagem.value = ""
        pagina.update()
        
    
        
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", 
                                  on_submit=enviar_mensagem)
        
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        # Feche o chat
        popup.open = False
        
        # Tire o botão "Iniciar o chat" da tela
        pagina.remove(botao_iniciar)
        
        # Adicionar o chat
        pagina.add(chat)
        
        # Criar o campo de enviar mensagens
        linha_mensagem = ft.Row(                    # Utilizado ft.Row para colocar o botão ao lado
            [campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        
        # Botão de enviar mensagens  
        texto = f"{nome_usuario.value} entrou no chat"      
        pagina.pubsub.send_all(texto)
        pagina.update()
    
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem vindo ao chat"),
        content = nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)    # Função on_click recebe um evento por padrão
    
    # Enviar os códigos/botões/textos para a página web
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
    
    
#ft.app(main)                             # FORMATO APLICATIVO
ft.app(main, view=ft.WEB_BROWSER)         # FORMATO WEB
      