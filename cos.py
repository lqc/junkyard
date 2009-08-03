import sys
port = open("cos.py", "r")

def rozpocznij_pomiar():

    #port = serial.Serial ("COM1", 19200, timeout=2)
    output1 = file("Pomiar.txt", "w")
    output2 = sys.stdout

    t = 0
    tab = []
    tab2 = []
    czas = int(raw_input('\nPodaj czas pomiaru w minutach: '))
    if czas <= t:
        print '\nCzas musi byc wiekszy niz zero!'
    elif czas > t:
        while czas > t:
            for i in range(10):
                line = port.readline()
                #tab.append(float(line[5:9]))
                #tab2.append(float(line[82:86]))
                #tab[t] = float(line[5:9])
                #tab2[t] = float(line[82:86])
                #print >> output2, time.strftime("%H:%M:%S -"), 'T1=', line[5:9],'  ', 'T2=', line[82:86]
                output2.flush()
            else:
                #print >> output1, time.strftime("%H:%M:%S -"), mean(tab), mean(tab2)
                output1.flush()
                t += 1
            print '\n'
        print 'Koniec pomiarow'

rozpocznij_pomiar()