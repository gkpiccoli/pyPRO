def time_favorito(**kwargs):
    for key in kwargs:
        print(f"{key} torce para o : {kwargs[key]}" )


time_favorito(Pedro="Grêmio", Matheus="Corinthians", Felipe="Internacional", Débora="Bahia")