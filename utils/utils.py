import discord


async def parse_player_name(interaction: discord.Interaction, player_full_name: str):
    try:
        player_name, player_tag = player_full_name.split("#")
    except ValueError:
        if not interaction.response.is_done():
            await interaction.response.send_message("Wrong Format 'player_name#tag'。")
        else:
            await interaction.edit_original_response(content="Parsing data... Please wait.")
        return None, None
    if not interaction.response.is_done():
        await interaction.response.send_message("Parsing data... Please wait.")
    else:
        await interaction.edit_original_response(content="Parsing data... Please wait.")

    return player_name, player_tag
