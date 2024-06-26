import environment


def show_key():
    key = environment.DISCORD_KEY
    print(f"'{key}', {type(key)}")
