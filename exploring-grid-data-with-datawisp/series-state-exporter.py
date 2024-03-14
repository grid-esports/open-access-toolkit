#!/usr/bin/env python3
import os
import sys
import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# set your GRID_API_KEY as an env var before running.
GRID_API_KEY = os.environ.get("GRID_API_KEY")
GRID_SSAPI_URL = "https://api-op.grid.gg/live-data-feed/series-state/graphql"

transport = AIOHTTPTransport(url=GRID_SSAPI_URL, headers={'X-API-KEY': GRID_API_KEY})
client = Client(transport=transport, fetch_schema_from_transport=True)

def writeToFile(filename, content):
    with open(filename, "w") as outfile:
        json.dump(content, outfile)

def getSeriesState(series_id):
    query = gql(
        """
        query GetCompleteSeriesState($seriesId: ID!) {
            seriesState(id: $seriesId) {
                __typename
                id
                title {
                    __typename
                    nameShortened
                }
                format
                started
                finished
                valid
                draftActions {
                    __typename
                    id
                    type
                    sequenceNumber
                    drafter {
                        id
                        type
                    }
                    draftable {
                        id
                        type
                        name
                    }
                }
                updatedAt
                ... GetCompleteSeriesState_SeriesTeamState
                ... GetCompleteSeriesState_SeriesGameState
            }
        }

        fragment GetCompleteSeriesState_SeriesTeamState on SeriesState {
            teams {
                __typename
                id
                name
                score
                won
                kills
                killAssistsReceived
                killAssistsGiven
                killAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    killAssistsReceived
                }
                weaponKills {
                    __typename
                    id
                    weaponName
                    count
                }
                teamkills
                teamkillAssistsReceived
                teamkillAssistsGiven
                teamkillAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    teamkillAssistsReceived
                }
                weaponTeamkills {
                    __typename
                    id
                    weaponName
                    count
                }
                selfkills
                deaths
                structuresDestroyed
                structuresCaptured
                objectives {
                    __typename
                    id
                    type
                    completionCount
                }
                ... GetCompleteSeriesState_SeriesTeamPlayerState
                ... on SeriesTeamStateCsgo {
                    headshots
                    teamHeadshots
                }
                ... on SeriesTeamStatePubg {
                    headshots
                    teamHeadshots
                }
                ... on SeriesTeamStateValorant {
                    headshots
                    teamHeadshots
                }
            }
        }

        fragment GetCompleteSeriesState_SeriesGameState on SeriesState {
            games {
                __typename
                id
                sequenceNumber
                ... GetCompleteSeriesState_SeriesGameMapState
                started
                finished
                paused
                clock {
                    __typename
                    id
                    type
                    ticking
                    ticksBackwards
                    currentSeconds
                }
                ... GetCompleteSeriesState_SeriesGameStructureState
                ... GetCompleteSeriesState_SeriesGameNonPlayerCharacterState
                ... GetCompleteSeriesState_SeriesGameTeamState
                draftActions {
                    __typename
                    id
                    type
                    sequenceNumber
                    drafter {
                        id
                        type
                    }
                    draftable {
                        id
                        type
                        name
                    }
                }
                ... GetCompleteSeriesState_SeriesGameSegmentState
            }
        }

        fragment GetCompleteSeriesState_SeriesTeamPlayerState on SeriesTeamState {
            players {
                __typename
                id
                name
                participationStatus
                kills
                killAssistsReceived
                killAssistsGiven
                killAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    killAssistsReceived
                }
                weaponKills {
                    __typename
                    id
                    weaponName
                    count
                }
                teamkills
                teamkillAssistsReceived
                teamkillAssistsGiven
                teamkillAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    teamkillAssistsReceived
                }
                weaponTeamkills {
                    __typename
                    id
                    weaponName
                    count
                }
                selfkills
                deaths
                structuresDestroyed
                structuresCaptured
                objectives {
                    __typename
                    id
                    type
                    completionCount
                }
                multikills {
                    __typename
                    id
                    numberOfKills
                    count
                }
                ... on SeriesPlayerStateCsgo {
                    headshots
                    teamHeadshots
                }
                ... on SeriesPlayerStatePubg {
                    headshots
                    teamHeadshots
                }
                ... on SeriesPlayerStateValorant {
                    headshots
                    teamHeadshots
                }
            }
        }
        fragment GetCompleteSeriesState_SeriesGameMapState on GameState {
            map {
                __typename
                name
                bounds {
                    __typename
                    min {
                        __typename
                        x
                        y
                    }
                    max {
                        __typename
                        x
                        y
                    }
                }
            }
        }
        fragment GetCompleteSeriesState_SeriesGameStructureState on GameState {
            structures {
                __typename
                id
                type
                side
                teamId
                maxHealth
                destroyed
                position {
                    x
                    y
                }
            }
        }
        fragment GetCompleteSeriesState_SeriesGameNonPlayerCharacterState on GameState {
            nonPlayerCharacters {
                __typename
                id
                type
                side
                respawnClock {
                    __typename
                    id
                    type
                    ticking
                    ticksBackwards
                    currentSeconds
                }
                position {
                    x
                    y
                }
                alive
            }
        }
        fragment GetCompleteSeriesState_SeriesGameTeamState on GameState {
            teams {
                __typename
                id
                name
                side
                won
                score
                money
                loadoutValue
                netWorth
                kills
                killAssistsReceived
                killAssistsGiven
                killAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    killAssistsReceived
                }
                weaponKills {
                    __typename
                    id
                    weaponName
                    count
                }
                teamkills
                teamkillAssistsReceived
                teamkillAssistsGiven
                teamkillAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    teamkillAssistsReceived
                }
                weaponTeamkills {
                    __typename
                    id
                    weaponName
                    count
                }
                selfkills
                deaths
                structuresDestroyed
                structuresCaptured
                ... GetCompleteSeriesState_SeriesGameTeamPlayerState
                objectives {
                    __typename
                    id
                    type
                    completionCount
                }
                ... on GameTeamStateCsgo {
                    damageDealt
                    damageTaken
                    selfdamageDealt
                    selfdamageTaken
                    teamdamageDealt
                    teamdamageTaken
                    headshots
                    teamHeadshots
                }
                ... on GameTeamStateDota {
                    experiencePoints
                }
                ... on GameTeamStateLol {
                    experiencePoints
                }
                ... on GameTeamStatePubg {
                    headshots
                    teamHeadshots
                }
                ... on GameTeamStateValorant {
                    headshots
                    teamHeadshots
                }
            }
        }
        fragment GetCompleteSeriesState_SeriesGameSegmentState on GameState {
            segments {
                __typename
                id
                type
                sequenceNumber
                started
                finished
                ... GetCompleteSeriesState_SeriesGameSegmentTeamState
            }
        }
        fragment GetCompleteSeriesState_SeriesGameTeamPlayerState on GameTeamState {
            players {
                __typename
                id
                name
                character {
                    __typename
                    id
                    name
                }
                participationStatus
                money
                loadoutValue
                netWorth
                kills
                killAssistsReceived
                killAssistsGiven
                killAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    killAssistsReceived
                }
                weaponKills {
                    __typename
                    id
                    weaponName
                    count
                }
                teamkills
                teamkillAssistsReceived
                teamkillAssistsGiven
                teamkillAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    teamkillAssistsReceived
                }
                weaponTeamkills {
                    __typename
                    id
                    weaponName
                    count
                }
                selfkills
                deaths
                structuresDestroyed
                structuresCaptured
                inventory {
                    items {
                        __typename
                        id
                        equipped
                        stashed
                    }
                }
                objectives {
                    __typename
                    id
                    type
                    completionCount
                }
                position {
                    x
                    y
                }
                multikills {
                    __typename
                    id
                    numberOfKills
                    count
                }
                abilities {
                    __typename
                    id
                    name
                    ready
                }
                ... on GamePlayerStateCsgo {
                    alive
                    currentArmor
                    currentHealth
                    damageDealt
                    damageTaken
                    maxHealth
                    selfdamageDealt
                    selfdamageTaken
                    teamdamageDealt
                    teamdamageTaken
                    headshots
                    teamHeadshots
                }
                ... on GamePlayerStateDota {
                    alive
                    currentHealth
                    experiencePoints
                    maxHealth
                }
                ... on GamePlayerStateLol {
                    alive
                    currentHealth
                    experiencePoints
                    maxHealth
                }
                ... on GamePlayerStatePubg {
                    alive
                    currentHealth
                    maxHealth
                    headshots
                    teamHeadshots
                }
                ... on GamePlayerStateValorant {
                    alive
                    currentArmor
                    currentHealth
                    maxHealth
                    headshots
                    teamHeadshots
                }
            }
        }
        fragment GetCompleteSeriesState_SeriesGameSegmentTeamState on SegmentState {
            teams {
                __typename
                id
                name
                side
                won
                kills
                killAssistsReceived
                killAssistsGiven
                killAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    killAssistsReceived
                }
                weaponKills {
                    __typename
                    id
                    weaponName
                    count
                }
                teamkills
                teamkillAssistsReceived
                teamkillAssistsGiven
                teamkillAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    teamkillAssistsReceived
                }
                weaponTeamkills {
                    __typename
                    id
                    weaponName
                    count
                }
                selfkills
                deaths
                objectives {
                    __typename
                    id
                    type
                    completionCount
                }
                ... GetCompleteSeriesState_SeriesGameSegmentTeamPlayerState
                ... on SegmentTeamStateCsgo {
                    damageDealt
                    damageTaken
                    selfdamageDealt
                    selfdamageTaken
                    teamdamageDealt
                    teamdamageTaken
                    winType
                    headshots
                    teamHeadshots
                }
                ... on SegmentTeamStateValorant {
                    winType
                    headshots
                    teamHeadshots
                }
            }
        }
        fragment GetCompleteSeriesState_SeriesGameSegmentTeamPlayerState on SegmentTeamState {
            players {
                __typename
                id
                name
                kills
                killAssistsReceived
                killAssistsGiven
                killAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    killAssistsReceived
                }
                weaponKills {
                    __typename
                    id
                    weaponName
                    count
                }
                teamkills
                teamkillAssistsReceived
                teamkillAssistsGiven
                teamkillAssistsReceivedFromPlayer {
                    __typename
                    id
                    playerId
                    teamkillAssistsReceived
                }
                weaponTeamkills {
                    __typename
                    id
                    weaponName
                    count
                }
                selfkills
                deaths
                objectives {
                    __typename
                    id
                    type
                    completionCount
                }
                ... on SegmentPlayerStateCsgo {
                    headshots
                    teamHeadshots
                    alive
                    currentArmor
                    currentHealth
                    damageDealt
                    damageTaken
                    maxHealth
                    selfdamageDealt
                    selfdamageTaken
                    teamdamageDealt
                    teamdamageTaken
                }
                ... on SegmentPlayerStateValorant {
                    alive
                    currentArmor
                    currentHealth
                    maxHealth
                    headshots
                    teamHeadshots
                }
            }
        }
    """
    )

    params = {"seriesId": series_id}

    try:
        result = client.execute(query, variable_values=params)
        return result
    except Exception as error:
        print(error)
        sys.exit(2)

    return result

def cleanseSeriesStateData(ssapi_data):
    if ('seriesState' not in ssapi_data):
        print(f'Query response does not appear to be valid.')
        return
    
    return ssapi_data['seriesState']

def main(argv):
    series_id = 0
    try:
        series_id = int(argv[1])
    except:
        print("series-state-exporter [series-id]")
        sys.exit(2)

    ssapi_data = getSeriesState(series_id)
    formatted_data = cleanseSeriesStateData(ssapi_data)
    output_filename = f'{series_id}_series_state.json'
    writeToFile(output_filename, formatted_data)
    print(f'Series State for {series_id} has been written to file: {output_filename}')


if __name__ == "__main__":
   main(sys.argv)

