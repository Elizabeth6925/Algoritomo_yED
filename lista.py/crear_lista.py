import math
import random

paises = [
    'Argentina', 'Brasil', 'Chile', 'Uruguay', 'Paraguay', 'Peru', 'Bolivia',
    'Colombia', 'Venezuela', 'Ecuador', 'Mexico', 'España', 'Francia', 'Italia',
    'Alemania', 'Portugal', 'Japon', 'China', 'India', 'Egipto', 'Canada',
    'EstadosUnidos', 'Rusia', 'Grecia', 'Turquia', 'Marruecos', 'Australia',
    'Noruega', 'Suecia', 'Finlandia',
]

nombres = [
    'Lucas', 'Martina', 'Sofia', 'Mateo', 'Valentina', 'Thiago', 'Emma',
    'Benjamin', 'Isabella', 'Santiago', 'Camila', 'Joaquin', 'Julieta',
    'Bautista', 'Mia', 'Agustin', 'Renata', 'Ignacio', 'Catalina', 'Tomas',
]

marvel = [
    'IronMan', 'CapitanAmerica', 'Thor', 'HulkMarvel', 'BlackWidow', 'Hawkeye',
    'SpiderMan', 'DoctorStrange', 'BlackPanther', 'CarolDanvers', 'ScottLang',
    'WandaMaximoff', 'Vision', 'Loki', 'Thanos', 'Groot', 'RocketRaccoon',
    'StarLord', 'Gamora', 'NickFury',
]

harry_potter = [
    'HarryPotter', 'HermioneGranger', 'RonWeasley', 'AlbusDumbledore',
    'SeverusSnape', 'DracoMalfoy', 'RubeusHagrid', 'MinervaMcGonagall',
    'LordVoldemort', 'SiriusBlack', 'LunaLovegood', 'NevilleLongbottom',
    'GinnyWeasley', 'FredWeasley', 'GeorgeWeasley', 'DobbyElfo',
]

disney_hadas = [
    'Campanita', 'Iridessa', 'Rosetta', 'Silvermist', 'Fawn', 'Vidia',
    'Zarina', 'Periwinkle', 'Nyx', 'Clank', 'Bobble', 'ReinaClarion',
    'Terence', 'FairyMary', 'FairyGary', 'MinistroDeLaPrimavera',
    'MinistroDelVerano', 'MinistraDelOtoño', 'MinistroDelInvierno',
    'LordMilori', 'Dewey', 'Gliss', 'Spike', 'Sled', 'Slush', 'LizzyGriffiths',
    'DrMartinGriffiths', 'JamesHook', 'Oppenheimer', 'Yang', 'Port', 'Starboard',
    'Smee', 'Chase', 'Scribble', 'Fury', 'Chloe', 'Glimmer', 'Rumble', 'Fern', 'Ivy',
    'Lilac', 'Zephyr', 'Flint', 'Stone', 'Viola', 'Cheese', 'Blaze', 'Gruff', 'Crocky', 'MrTwitches',
]

astronomia = [
    'Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano',
    'Neptuno', 'Pluton', 'Sol', 'Luna', 'Sirio', 'Betelgeuse', 'Rigel',
    'Antares', 'Vega', 'Polaris', 'Altair', 'Proxima Centauri', 'Alfa Centauri',
    'OsaMayor', 'OsaMenor', 'Orion', 'Casiopea', 'Escorpio', 'Sagitario',
    'Cassini', 'CruzDelSur', 'VíaLactea', 'Andromeda',
]

historia = [
    'PrimeraGuerraMundial', 'SegundaGuerraMundial', 'ElHolocausto',
    'RevoluciónFrancesa', 'RevoluciónRusa', 'RevoluciónIndustrial',
    'GuerraFria', 'CaidaDelMuroDeBerlin', 'ImperioRomano', 'EdadMedia',
    'Renacimiento', 'IndependenciaArgentina', 'DescubrimientoDeAmerica',
    'GuerraDeMalvinas', 'CrisisDel29', 'LlegadaALaLuna',
]

avatar_aang = [
    'Aang', 'Katara', 'Sokka', 'Toph', 'Zuko', 'Iroh', 'Azula', 'Suki',
    'Appa', 'Momo', 'Mai', 'TyLee', 'ReyOzai', 'ReyBumi', 'Yue', 'MaestroPakku',
    'Jet', 'Roku', 'Kyoshi', 'Kuruk', 'Zhao', 'Azulon', 'GeneralIroh',
    'GranSabioGyatso', 'Kanna', 'GuruPathik', 'JeongJeong', 'Piandao',
]

universo = paises + nombres + marvel + harry_potter + disney_hadas + astronomia + historia + avatar_aang


def crear_lista():
    return []


def tamanio_aleatorio():
    return round(math.exp(random.uniform(math.log(3), math.log(10_000_000))))


def elemento_aleatorio():
    return random.choice(universo)


def cargar_lista(lista, tamanio):
    for _ in range(tamanio):
        lista.append(elemento_aleatorio())
    return lista