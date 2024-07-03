import random
import discord


async def rock_paper_scissors(interaction: discord.Interaction, choice: str):
    print(f"{interaction.user.display_name} played rock-paper-scissors")
    choice = choice.lower()
    if choice not in {"rock", "paper", "scissors"}:
        await interaction.response.send_message(
            f"{choice} isn't an option, quick tryna cheat!", ephemeral=True
        )
    rps_dict = {
        "rock": ["scissors", "rock", "paper"],
        "paper": ["rock", "paper", "scissors"],
        "scissors": ["paper", "scissors", "rock"],
    }
    choice_list: list = rps_dict[choice]
    ladel_choice_index = random.randint(0, 2)
    match ladel_choice_index:
        case 0:
            response = (
                f"I chose {choice_list[ladel_choice_index]}, I lost to your {choice}!"
            )
        case 1:
            response = f"We both chose {choice}, its a tie!"
        case 2:
            response = (
                f"I chose {choice_list[ladel_choice_index]}, I beat your {choice}!"
            )
    await interaction.response.send_message(response)
