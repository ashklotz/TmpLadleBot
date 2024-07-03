import discord, random, re


async def roll_dice(interaction: discord.Interaction, dice: str):
    if not re.match(r"\d*d\d+", dice):
        await interaction.response.send_message(
            "I don't know how to roll that as dice", ephemeral=True
        )
    print(f"{interaction.user.display_name} rolled {dice}")

    dice_vars = dice.split("d")
    loops = int(dice_vars[0] if dice_vars[0] else 1)
    dice_results = []
    for i in range(0, loops):
        dice_results.append(random.randint(1, int(dice_vars[1])))

    response = f"rolled {dice}\n"
    if len(dice_results) == 1:
        response += dice_results[0]
    else:
        response += (
            f"{' + '.join([str(r) for r in dice_results])} = {sum(dice_results)}"
        )

    await interaction.response.send_message(response)
