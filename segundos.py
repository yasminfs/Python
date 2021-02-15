segundos_str = input ( "Por favor, entre com o número de segundos que deseja converter: " )
total_segs = int(segundos_str)
a = total_segs // 86400
x = total_segs % 86400
b = x // 3600
x = x % 3600
c = x // 60
d = x % 60

print(a,  " dias, ", b, "horas, ", c, "minutos e ", d, "segundos." )
