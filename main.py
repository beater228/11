# Погода для Любимой



from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM("c60c5864ff1ac807578b5e2aef43f1dc")


place = input( "Милая, куда собираешься ехать?: " )
mrg = owm.weather_manager()
obs = mrg.weather_at_place(place)
w = obs.weather
config_dict = get_default_config()
config_dict['language'] = 'ru'

# температура
t = w.temperature( "celsius" )
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

# ветер
wind = w.wind()['speed']

# влажность
humi = w.humidity

# облачность
cloud = w.clouds

# статус
st = w.status

# детальный
det = w.detailed_status

# время
ti = w.reference_time('iso')

#давление
pr = w.pressure['press']

# видимость
vd = w.visibility_distance



print(f'Зайка,в городе {place} температура {t1}℃ , скорость ветра {wind}м/сек \n Влажность достигает {humi}%, облачность составляет {cloud}%, давление {pr}мм рт. столба' )

if det == ( 'clear sky' ):
    print( "Ясно, улыбнись!)" )
elif det == 'clouds':
    print( "Облачно, милая" )
elif det == 'few clouds':
    print( "Облачно, заюш" )
elif det == 'scattered clouds':
    print( "Облачно, сладкая" )
elif det == 'broken clouds':
    print( "Облачно, но ты все равно улыбнись!)" )
elif det == 'shower rain':
    print( "Ожидается ливень, возьми зонт!" )
elif det == 'rain':
    print( "Будет дождик, зайка, возьми зонт!" )
elif det == 'thunderstorm':
    print( "Будет гроза, смотри мне если не возьмешь зонт!" )
elif det == 'snow':
    print( "Снег пойти должен, осторожнее будь!" )
elif det == 'mist':
    print( "Туманно, внимательнее будь сладкая!" )



print (f"Замерено в {ti}")     
