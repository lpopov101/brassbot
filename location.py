from enum import Enum


class Location(Enum):
    # Cities
    STOKE_ON_TRENT = "stoke-on-trent"
    LEEK = "leek"
    BELPER = "belper"
    STONE = "stone"
    UTTOXETER = "uttoxeter"
    DERBY = "derby"
    STAFFORD = "stafford"
    BURTON_ON_TRENT = "burton-on-trent"
    CANNOCK = "cannock"
    COALBROOKDALE = "coalbrookdale"
    WOLVERHAMPTON = "wolverhampton"
    WALSALL = "walsall"
    TAMWORTH = "tamworth"
    DUDLEY = "dudley"
    BIRMINGHAM = "birmingham"
    NUNEATON = "nuneaton"
    COVENTRY = "coventry"
    KIDDERMINSTER = "kidderminster"
    WORCESTER = "worcester"
    REDDITCH = "redditch"
    # Farm breweries
    FARM1 = "farm1"
    FARM2 = "farm2"
    # Merchants
    WARRINGTON = "warrington"
    NOTTINGHAM = "nottingham"
    SHREWSBURY = "shrewsbury"
    GLOUCESTER = "gloucester"
    OXFORD = "oxford"


CITIES = [
    Location.STOKE_ON_TRENT,
    Location.LEEK,
    Location.BELPER,
    Location.STONE,
    Location.UTTOXETER,
    Location.DERBY,
    Location.STAFFORD,
    Location.BURTON_ON_TRENT,
    Location.CANNOCK,
    Location.COALBROOKDALE,
    Location.WOLVERHAMPTON,
    Location.WALSALL,
    Location.TAMWORTH,
    Location.DUDLEY,
    Location.BIRMINGHAM,
    Location.NUNEATON,
    Location.COVENTRY,
    Location.KIDDERMINSTER,
    Location.WORCESTER,
    Location.REDDITCH,
]

MERCHANTS = [
    Location.WARRINGTON,
    Location.NOTTINGHAM,
    Location.SHREWSBURY,
    Location.GLOUCESTER,
    Location.OXFORD,
]

FARM_BREWERIES = [
    Location.FARM1,
    Location.FARM2,
]
