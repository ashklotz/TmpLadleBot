import discord

from sqlalchemy import select
from sqlalchemy.orm import Session

import environment, enums
from models import Leaderboard, LeaderboardUser


async def create_leaderboard(
    interaction: discord.Interaction,
    leaderboard_name: str,
    positive_point_message: str = "[points] to [user]!",
    negative_point_message: str = "[points] deducted from [user]",
):
    with Session(environment.DB_ENGINE) as session:
        statement = select(Leaderboard).where(
            Leaderboard.guild_id == interaction.guild.id
        )
        leaderboard = session.scalar(statement)
        if leaderboard:
            await interaction.response.send_message(
                f"Leaderboard already exists title: {leaderboard.name}",
                ephemeral=True,
            )
        else:
            leaderboard = Leaderboard(
                guild_id=interaction.guild_id,
                name=leaderboard_name,
                positive_point_message=positive_point_message,
                negative_point_message=negative_point_message,
            )
            session.add(leaderboard)
            session.commit()
            await interaction.response.send_message(
                f"Leaderboard created with title: {leaderboard.name}"
            )


async def check_points(interaction: discord.Interaction, member: discord.Member):
    with Session(environment.DB_ENGINE) as session:
        statement = select(Leaderboard).where(
            Leaderboard.guild_id == interaction.guild_id
        )
        leaderboard = session.scalar(statement)

        statement = (
            select(LeaderboardUser)
            .where(LeaderboardUser.user_id == member.id)
            .where(LeaderboardUser.leaderboard_id == leaderboard.id)
        )
        leaderboard_user = session.scalar(statement)

        points = leaderboard_user.points if leaderboard_user else 0
        response_embed = discord.Embed(
            title=leaderboard.name,
            description=f"{member.mention} has {points} points",
        )
        await interaction.response.send_message(embed=response_embed)


async def top_points(interaction: discord.Interaction):
    MAX_USERS = 10
    with Session(environment.DB_ENGINE) as session:
        statement = select(Leaderboard).where(
            Leaderboard.guild_id == interaction.guild_id
        )
        leaderboard = session.scalar(statement)

        statement = (
            select(LeaderboardUser)
            .where(LeaderboardUser.leaderboard_id == leaderboard.id)
            .order_by(LeaderboardUser.points.desc())
            .limit(MAX_USERS)
        )
        leaderboard_users = session.scalars(statement)

        user_list = []
        for i, leaderboard_user in enumerate(leaderboard_users):
            member = await interaction.guild.fetch_member(leaderboard_user.user_id)
            user_list.append(
                f"#{i+1}. {member.mention} - {leaderboard_user.points} points"
            )

        await interaction.response.send_message(
            embed=discord.Embed(
                title=f"Top {MAX_USERS} {leaderboard.name}",
                description="\n".join(user_list),
            )
        )


async def add_points(
    interaction: discord.Interaction, member: discord.Member, points: int
):
    with Session(environment.DB_ENGINE) as session:
        statement = select(Leaderboard).where(
            Leaderboard.guild_id == interaction.guild_id
        )
        leaderboard = session.scalar(statement)
        if not leaderboard:
            await interaction.response.send_message(
                "Leaderboard does not exist for this guild yet", ephemeral=True
            )
            return

        statement = (
            select(LeaderboardUser)
            .where(LeaderboardUser.user_id == member.id)
            .where(LeaderboardUser.leaderboard_id == leaderboard.id)
        )
        leaderboard_user = session.scalar(statement)
        if leaderboard_user:
            leaderboard_user.points += points
        else:
            leaderboard_user = LeaderboardUser(
                user_id=member.id,
                leaderboard_id=leaderboard.id,
                points=points,
            )
        session.add(leaderboard_user)
        session.commit()
        response_message = (
            leaderboard.positive_point_message
            if points > 0
            else leaderboard.negative_point_message
        )
        response_message = response_message.replace("[user]", member.mention)
        response_message = response_message.replace("[points]", str(points))
        await interaction.response.send_message(response_message)


async def reset_points():
    pass


async def remove_leaderboard():
    pass
