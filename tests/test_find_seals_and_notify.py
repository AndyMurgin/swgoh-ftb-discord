from unittest.mock import Mock

from discord_bot.seals_finder import Hunter


def prepare_member(display_name: str):
    return Mock(display_name=display_name)


def prepare_context(channel_id, channel_members: list[str]):
    channel = Mock(
        id=channel_id,
        members=[prepare_member(display_name) for display_name in channel_members],
    )
    ctx = Mock(channel=channel)
    return ctx


# prepare
seals = ["PogrØᶆᶆist", "MINI Servant", "Lorem Ipsum"]
ctx = prepare_context(1144745341514698845, ["PogrØᶆᶆist (Андрей)"])

# act
grouped_members = Hunter.find_seal_members(seals, ctx)

# verify
assert grouped_members is not None, "Hunter should find and group seals"

auto_members = grouped_members.auto_found_members
assert auto_members is not None, "auto_found_members should not be None"
assert len(auto_members) == 1, "There should one item in auto_found_members"
assert (
    auto_members.get("PogrØᶆᶆist").display_name == "PogrØᶆᶆist (Андрей)"
), "PogrØᶆᶆist should be found in auto_found_members"

# TODO currently works only with the existing prod mongo - rework the test with proper mongo setup
mapped_members = grouped_members.mapped_accounts
assert mapped_members is not None, "mapped_accounts should not be None"
assert len(mapped_members) == 1, "There should one item in mapped_accounts"
assert (
    mapped_members.get("MINI Servant") is not None
), "MINI Servant should be found in mapped_accounts"

unrecognized = grouped_members.unrecognized
assert unrecognized is not None, "unrecognized should not be None"
assert len(unrecognized) == 1, "There should one item in unrecognized"
assert unrecognized[0] == "Lorem Ipsum", "Lorem Ipsum should be found in unrecognized"
